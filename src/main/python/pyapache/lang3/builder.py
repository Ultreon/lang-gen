from __future__ import annotations
from overload import overload


 
from builtins import str
import org.apache.commons.lang3.builder.DiffResult as __DiffResult
__DiffResult = __DiffResult
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class DiffResult(__Iterable, Iterable):
    """org.apache.commons.lang3.builder.DiffResult"""
 
    @staticmethod
    def __wrap(java_value: __DiffResult) -> 'DiffResult':
        return DiffResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DiffResult):
        """
        Dynamic initializer for DiffResult.
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
    def getDiffs(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.builder.Diff<?>> org.apache.commons.lang3.builder.DiffResult.getDiffs()"""
        return 'List'.__wrap(super(DiffResult, self).getDiffs())

    @overload
    def toString(self, arg0: 'ToStringStyle') -> str:
        """public java.lang.String org.apache.commons.lang3.builder.DiffResult.toString(org.apache.commons.lang3.builder.ToStringStyle)"""
        return str.__wrap(super(__DiffResult, self).toString(arg0))

    @overload
    def getNumberOfDiffs(self) -> int:
        """public int org.apache.commons.lang3.builder.DiffResult.getNumberOfDiffs()"""
        return int.__wrap(super(DiffResult, self).getNumberOfDiffs())

    @overload
    def getToStringStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.DiffResult.getToStringStyle()"""
        return 'ToStringStyle'.__wrap(super(DiffResult, self).getToStringStyle())

    @overload
    def getRight(self) -> object:
        """public T org.apache.commons.lang3.builder.DiffResult.getRight()"""
        return object.__wrap(super(DiffResult, self).getRight())

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
        """public java.lang.String org.apache.commons.lang3.builder.DiffResult.toString()"""
        return str.__wrap(super(DiffResult, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.commons.lang3.builder.Diff<?>> org.apache.commons.lang3.builder.DiffResult.iterator()"""
        return 'Iterator'.__wrap(super(DiffResult, self).iterator())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getLeft(self) -> object:
        """public T org.apache.commons.lang3.builder.DiffResult.getLeft()"""
        return object.__wrap(super(DiffResult, self).getLeft())

 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffResult
from builtins import str
import org.apache.commons.lang3.builder.DiffResult as __DiffResult
__DiffResult = __DiffResult
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class DiffResult(__Iterable, Iterable):
    """org.apache.commons.lang3.builder.DiffResult"""
 
    @staticmethod
    def __wrap(java_value: __DiffResult) -> 'DiffResult':
        return DiffResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DiffResult):
        """
        Dynamic initializer for DiffResult.
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
    def getDiffs(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.builder.Diff<?>> org.apache.commons.lang3.builder.DiffResult.getDiffs()"""
        return 'List'.__wrap(super(DiffResult, self).getDiffs())

    @overload
    def toString(self, arg0: 'ToStringStyle') -> str:
        """public java.lang.String org.apache.commons.lang3.builder.DiffResult.toString(org.apache.commons.lang3.builder.ToStringStyle)"""
        return str.__wrap(super(__DiffResult, self).toString(arg0))

    @overload
    def getNumberOfDiffs(self) -> int:
        """public int org.apache.commons.lang3.builder.DiffResult.getNumberOfDiffs()"""
        return int.__wrap(super(DiffResult, self).getNumberOfDiffs())

    @overload
    def getToStringStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.DiffResult.getToStringStyle()"""
        return 'ToStringStyle'.__wrap(super(DiffResult, self).getToStringStyle())

    @overload
    def getRight(self) -> object:
        """public T org.apache.commons.lang3.builder.DiffResult.getRight()"""
        return object.__wrap(super(DiffResult, self).getRight())

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
        """public java.lang.String org.apache.commons.lang3.builder.DiffResult.toString()"""
        return str.__wrap(super(DiffResult, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.commons.lang3.builder.Diff<?>> org.apache.commons.lang3.builder.DiffResult.iterator()"""
        return 'Iterator'.__wrap(super(DiffResult, self).iterator())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getLeft(self) -> object:
        """public T org.apache.commons.lang3.builder.DiffResult.getLeft()"""
        return object.__wrap(super(DiffResult, self).getLeft())

 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffResult 
 
 
# CLASS: org.apache.commons.lang3.builder.Diff
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.lang3.tuple.Pair as __Pair
__Pair = __Pair
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyapache.lang3 import tuple
except ImportError:
    tuple = __import_once__("pyapache.lang3.tuple")

from builtins import type
import org.apache.commons.lang3.builder.Diff as __Diff
__Diff = __Diff
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
from builtins import object
from abc import abstractmethod, ABC
from typing import List
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Diff(ABC, lang3.__Pair, tuple.Pair):
    """org.apache.commons.lang3.builder.Diff"""
 
    @staticmethod
    def __wrap(java_value: __Diff) -> 'Diff':
        return Diff(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Diff):
        """
        Dynamic initializer for Diff.
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
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type org.apache.commons.lang3.builder.Diff.getType()"""
        return 'Type'.__wrap(super(Diff, self).getType())

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object.__wrap(super(tuple.Pair, self).getKey())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int.__wrap(super(__tuple.Pair, self).compareTo(arg0))

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object.__wrap(super(__tuple.Pair, self).apply(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool.__wrap(super(__tuple.Pair, self).equals(arg0))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'tuple.Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return tuple.Pair.__wrap(__Pair.ofNonNull(arg0, arg1))

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(__tuple.Pair, self).accept(arg0)

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Pair.getRight()"""
        pass

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
    def setValue(self, arg0: object) -> object:
        """public final T org.apache.commons.lang3.builder.Diff.setValue(T)"""
        return object.__wrap(super(__Diff, self).setValue(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int.__wrap(super(tuple.Pair, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getLeft(self, ):
        """public abstract L org.apache.commons.lang3.tuple.Pair.getLeft()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String org.apache.commons.lang3.builder.Diff.toString()"""
        return str.__wrap(super(Diff, self).toString())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str.__wrap(super(__tuple.Pair, self).toString(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'tuple.Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return tuple.Pair.__wrap(__Pair.of(arg0, arg1))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object.__wrap(super(tuple.Pair, self).getValue())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'tuple.Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return tuple.Pair.__wrap(__Pair.of(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def emptyArray() -> List['tuple.Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[tuple.Pair].__wrap(__Pair.emptyArray())

    @overload
    def getFieldName(self) -> str:
        """public final java.lang.String org.apache.commons.lang3.builder.Diff.getFieldName()"""
        return str.__wrap(super(Diff, self).getFieldName()) 
 
 
# CLASS: org.apache.commons.lang3.builder.EqualsExclude
import org.apache.commons.lang3.builder.EqualsExclude as __EqualsExclude
__EqualsExclude = __EqualsExclude
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
 
class EqualsExclude(ABC, __Annotation, Annotation):
    """org.apache.commons.lang3.builder.EqualsExclude"""
 
    @staticmethod
    def __wrap(java_value: __EqualsExclude) -> 'EqualsExclude':
        return EqualsExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EqualsExclude):
        """
        Dynamic initializer for EqualsExclude.
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
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.Diffable
import org.apache.commons.lang3.builder.Diffable as __Diffable
__Diffable = __Diffable
from abc import abstractmethod, ABC
 
class Diffable(ABC):
    """org.apache.commons.lang3.builder.Diffable"""
 
    @staticmethod
    def __wrap(java_value: __Diffable) -> 'Diffable':
        return Diffable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Diffable):
        """
        Dynamic initializer for Diffable.
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
    def diff(self, arg0: object):
        """public abstract org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.Diffable.diff(T)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.EqualsBuilder
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import java.util.Collection as Collection
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
import org.apache.commons.lang3.builder.EqualsBuilder as __EqualsBuilder
__EqualsBuilder = __EqualsBuilder
from builtins import bool
from builtins import int
import java.util.List as List
 
class EqualsBuilder(__Builder, Builder):
    """org.apache.commons.lang3.builder.EqualsBuilder"""
 
    @staticmethod
    def __wrap(java_value: __EqualsBuilder) -> 'EqualsBuilder':
        return EqualsBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EqualsBuilder):
        """
        Dynamic initializer for EqualsBuilder.
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
    def append(self, arg0: float, arg1: float) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(float,float)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setReflectUpToClass(self, arg0: 'Class') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setReflectUpToClass(java.lang.Class<?>)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).setReflectUpToClass(arg0))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, *arg2: str) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,java.lang.String...)"""
        return bool.__wrap(__EqualsBuilder.reflectionEquals(arg0, arg1, arg2))

    @override
    @overload
    def build(self) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.lang3.builder.EqualsBuilder.build()"""
        return 'Boolean'.__wrap(super(EqualsBuilder, self).build())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: 'long', arg1: 'long') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(long[],long[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @overload
    def reflectionAppend(self, arg0: object, arg1: object) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.reflectionAppend(java.lang.Object,java.lang.Object)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).reflectionAppend(arg0, arg1))

    @overload
    def setTestRecursive(self, arg0: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setTestRecursive(boolean)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).setTestRecursive(__boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(byte,byte)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__byte.valueOf(arg0), __byte.valueOf(arg1)))

    @overload
    def appendSuper(self, arg0: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.appendSuper(boolean)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).appendSuper(__boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: str) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(char,char)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def setExcludeFields(self, *arg0: str) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setExcludeFields(java.lang.String...)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).setExcludeFields(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.EqualsBuilder()"""
        val = __EqualsBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: 'float', arg1: 'float') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(float[],float[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: bool, arg3: 'Class', *arg4: str) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,boolean,java.lang.Class<?>,java.lang.String...)"""
        return bool.__wrap(__EqualsBuilder.reflectionEquals(arg0, arg1, __boolean.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(int,int)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def append(self, arg0: bytes, arg1: bytes) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(byte[],byte[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(bytes, bytes))

    @overload
    def append(self, arg0: 'char', arg1: 'char') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(char[],char[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.EqualsBuilder()"""
        val = __EqualsBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: bool, arg1: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(boolean,boolean)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__boolean.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def append(self, arg0: 'boolean', arg1: 'boolean') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(boolean[],boolean[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def append(self, arg0: object, arg1: object) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(java.lang.Object,java.lang.Object)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: float, arg1: float) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(double,double)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: 'Collection') -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,java.util.Collection<java.lang.String>)"""
        return bool.__wrap(__EqualsBuilder.reflectionEquals(arg0, arg1, arg2))

    @overload
    def setTestTransients(self, arg0: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setTestTransients(boolean)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).setTestTransients(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: 'int', arg1: 'int') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(int[],int[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setBypassReflectionClasses(self, arg0: 'List') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setBypassReflectionClasses(java.util.List<java.lang.Class<?>>)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).setBypassReflectionClasses(arg0))

    @overload
    def append(self, arg0: 'double', arg1: 'double') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(double[],double[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: bool, arg3: 'Class', arg4: bool, *arg5: str) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,boolean,java.lang.Class<?>,boolean,java.lang.String...)"""
        return bool.__wrap(__EqualsBuilder.reflectionEquals(arg0, arg1, __boolean.valueOf(arg2), arg3, __boolean.valueOf(arg4), arg5))

    @overload
    def append(self, arg0: 'short', arg1: 'short') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(short[],short[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(short,short)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__short.valueOf(arg0), __short.valueOf(arg1)))

    @overload
    def reset(self):
        """public void org.apache.commons.lang3.builder.EqualsBuilder.reset()"""
        super(EqualsBuilder, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: 'Object', arg1: 'Object') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(java.lang.Object[],java.lang.Object[])"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: bool) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,boolean)"""
        return bool.__wrap(__EqualsBuilder.reflectionEquals(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(long,long)"""
        return 'EqualsBuilder'.__wrap(super(__EqualsBuilder, self).append(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def isEquals(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.EqualsBuilder.isEquals()"""
        return bool.__wrap(super(EqualsBuilder, self).isEquals()) 
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringSummary
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.apache.commons.lang3.builder.ToStringSummary as __ToStringSummary
__ToStringSummary = __ToStringSummary
from abc import abstractmethod, ABC
 
class ToStringSummary(ABC, __Annotation, Annotation):
    """org.apache.commons.lang3.builder.ToStringSummary"""
 
    @staticmethod
    def __wrap(java_value: __ToStringSummary) -> 'ToStringSummary':
        return ToStringSummary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToStringSummary):
        """
        Dynamic initializer for ToStringSummary.
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
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringStyle
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class ToStringStyle(ABC, __Serializable, Serializable):
    """org.apache.commons.lang3.builder.ToStringStyle"""
 
    @staticmethod
    def __wrap(java_value: __ToStringStyle) -> 'ToStringStyle':
        return ToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToStringStyle):
        """
        Dynamic initializer for ToStringStyle.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(__ToStringStyle, self).append(arg0, arg1, __short.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(__ToStringStyle, self).append(arg0, arg1, __int.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, bytes, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(__ToStringStyle, self).append(arg0, arg1, __double.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(__ToStringStyle, self).append(arg0, arg1, __byte.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendEnd(arg0, arg1)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendToString(arg0, arg1)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendSuper(arg0, arg1)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(__ToStringStyle, self).append(arg0, arg1, __long.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map.__wrap(__ToStringStyle.getRegistry())

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(__ToStringStyle, self).append(arg0, arg1, __char.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(__ToStringStyle, self).append(arg0, arg1, __float.valueOf(arg2)) 
 
 
# CLASS: org.apache.commons.lang3.builder.CompareToBuilder
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import transform as __transform
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.util.Collection as Collection
from builtins import object
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.builder.CompareToBuilder as __CompareToBuilder
__CompareToBuilder = __CompareToBuilder
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CompareToBuilder(__Builder, Builder):
    """org.apache.commons.lang3.builder.CompareToBuilder"""
 
    @staticmethod
    def __wrap(java_value: __CompareToBuilder) -> 'CompareToBuilder':
        return CompareToBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CompareToBuilder):
        """
        Dynamic initializer for CompareToBuilder.
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
    def append(self, arg0: float, arg1: float) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(double,double)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def append(self, arg0: 'char', arg1: 'char') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(char[],char[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: bytes, arg1: bytes) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(byte[],byte[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(bytes, bytes))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, arg2: bool) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,boolean)"""
        return int.__wrap(__CompareToBuilder.reflectionCompare(arg0, arg1, __boolean.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: object, arg1: object) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object,java.lang.Object)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: 'short', arg1: 'short') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(short[],short[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, *arg2: str) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,java.lang.String...)"""
        return int.__wrap(__CompareToBuilder.reflectionCompare(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: str) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(char,char)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(byte,byte)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__byte.valueOf(arg0), __byte.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.CompareToBuilder()"""
        val = __CompareToBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: 'long', arg1: 'long') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(long[],long[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'boolean', arg1: 'boolean') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(boolean[],boolean[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(short,short)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__short.valueOf(arg0), __short.valueOf(arg1)))

    @overload
    def append(self, arg0: 'Object', arg1: 'Object') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object[],java.lang.Object[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: bool, arg1: bool) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(boolean,boolean)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__boolean.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def build(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.builder.CompareToBuilder.build()"""
        return __transform(super(CompareToBuilder, self).build()).'Integer'Value()

    @overload
    def append(self, arg0: float, arg1: float) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(float,float)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.CompareToBuilder()"""
        val = __CompareToBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: 'Object', arg1: 'Object', arg2: 'Comparator') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object[],java.lang.Object[],java.util.Comparator<?>)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(long,long)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(int,int)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def appendSuper(self, arg0: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.appendSuper(int)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).appendSuper(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: 'double', arg1: 'double') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(double[],double[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'float', arg1: 'float') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(float[],float[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object)"""
        return int.__wrap(__CompareToBuilder.reflectionCompare(arg0, arg1))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, arg2: bool, arg3: 'Class', *arg4: str) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,boolean,java.lang.Class<?>,java.lang.String...)"""
        return int.__wrap(__CompareToBuilder.reflectionCompare(arg0, arg1, __boolean.valueOf(arg2), arg3, arg4))

    @overload
    def toComparison(self) -> int:
        """public int org.apache.commons.lang3.builder.CompareToBuilder.toComparison()"""
        return int.__wrap(super(CompareToBuilder, self).toComparison())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: object, arg1: object, arg2: 'Comparator') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object,java.lang.Object,java.util.Comparator<?>)"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: 'int', arg1: 'int') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(int[],int[])"""
        return 'CompareToBuilder'.__wrap(super(__CompareToBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, arg2: 'Collection') -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,java.util.Collection<java.lang.String>)"""
        return int.__wrap(__CompareToBuilder.reflectionCompare(arg0, arg1, arg2)) 
 
 
# CLASS: org.apache.commons.lang3.builder.HashCodeBuilder
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.util.Collection as Collection
from builtins import object
import org.apache.commons.lang3.builder.HashCodeBuilder as __HashCodeBuilder
__HashCodeBuilder = __HashCodeBuilder
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashCodeBuilder(__Builder, Builder):
    """org.apache.commons.lang3.builder.HashCodeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __HashCodeBuilder) -> 'HashCodeBuilder':
        return HashCodeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashCodeBuilder):
        """
        Dynamic initializer for HashCodeBuilder.
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
    def append(self, arg0: bool) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(boolean)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.HashCodeBuilder()"""
        val = __HashCodeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: 'int') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(int[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'short') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(short[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.HashCodeBuilder()"""
        val = __HashCodeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def reflectionHashCode(arg0: int, arg1: int, arg2: object, arg3: bool, arg4: 'Class', *arg5: str) -> int:
        """public static <T> int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(int,int,T,boolean,java.lang.Class<? super T>,java.lang.String...)"""
        return int.__wrap(__HashCodeBuilder.reflectionHashCode(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4, arg5))

    @overload
    def append(self, arg0: 'char') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(char[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toHashCode(self) -> int:
        """public int org.apache.commons.lang3.builder.HashCodeBuilder.toHashCode()"""
        return int.__wrap(super(HashCodeBuilder, self).toHashCode())

    @overload
    def append(self, arg0: 'Object') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(java.lang.Object[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @overload
    def appendSuper(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.appendSuper(int)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).appendSuper(__int.valueOf(arg0)))

    @overload
    def append(self, arg0: bytes) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(byte[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(bytes))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: object, *arg1: str) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(java.lang.Object,java.lang.String...)"""
        return int.__wrap(__HashCodeBuilder.reflectionHashCode(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: 'float') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(float[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'boolean') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(boolean[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: float) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(double)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__double.valueOf(arg0)))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(byte)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__byte.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.builder.HashCodeBuilder.hashCode()"""
        return int.__wrap(super(HashCodeBuilder, self).hashCode())

    @overload
    def append(self, arg0: object) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(java.lang.Object)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: int, arg1: int, arg2: object) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(int,int,java.lang.Object)"""
        return int.__wrap(__HashCodeBuilder.reflectionHashCode(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.lang3.builder.HashCodeBuilder(int,int)"""
        val = __HashCodeBuilder(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: float) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(float)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: object, arg1: 'Collection') -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(java.lang.Object,java.util.Collection<java.lang.String>)"""
        return int.__wrap(__HashCodeBuilder.reflectionHashCode(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(short)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__short.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: 'double') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(double[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(int)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__int.valueOf(arg0)))

    @overload
    def append(self, arg0: 'long') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(long[])"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(arg0))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: int, arg1: int, arg2: object, arg3: bool) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(int,int,java.lang.Object,boolean)"""
        return int.__wrap(__HashCodeBuilder.reflectionHashCode(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __boolean.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.builder.HashCodeBuilder.equals(java.lang.Object)"""
        return bool.__wrap(super(__HashCodeBuilder, self).equals(arg0))

    @override
    @overload
    def build(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.builder.HashCodeBuilder.build()"""
        return __transform(super(HashCodeBuilder, self).build()).'Integer'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: str) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(char)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__char.valueOf(arg0)))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(long)"""
        return 'HashCodeBuilder'.__wrap(super(__HashCodeBuilder, self).append(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: object, arg1: bool) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(java.lang.Object,boolean)"""
        return int.__wrap(__HashCodeBuilder.reflectionHashCode(arg0, __boolean.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffExclude
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.apache.commons.lang3.builder.DiffExclude as __DiffExclude
__DiffExclude = __DiffExclude
from abc import abstractmethod, ABC
 
class DiffExclude(ABC, __Annotation, Annotation):
    """org.apache.commons.lang3.builder.DiffExclude"""
 
    @staticmethod
    def __wrap(java_value: __DiffExclude) -> 'DiffExclude':
        return DiffExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DiffExclude):
        """
        Dynamic initializer for DiffExclude.
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
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.HashCodeExclude
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.apache.commons.lang3.builder.HashCodeExclude as __HashCodeExclude
__HashCodeExclude = __HashCodeExclude
from abc import abstractmethod, ABC
 
class HashCodeExclude(ABC, __Annotation, Annotation):
    """org.apache.commons.lang3.builder.HashCodeExclude"""
 
    @staticmethod
    def __wrap(java_value: __HashCodeExclude) -> 'HashCodeExclude':
        return HashCodeExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashCodeExclude):
        """
        Dynamic initializer for HashCodeExclude.
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
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.RecursiveToStringStyle
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.builder.RecursiveToStringStyle as __RecursiveToStringStyle
__RecursiveToStringStyle = __RecursiveToStringStyle
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class RecursiveToStringStyle(__ToStringStyle, ToStringStyle):
    """org.apache.commons.lang3.builder.RecursiveToStringStyle"""
 
    @staticmethod
    def __wrap(java_value: __RecursiveToStringStyle) -> 'RecursiveToStringStyle':
        return RecursiveToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecursiveToStringStyle):
        """
        Dynamic initializer for RecursiveToStringStyle.
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
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(__ToStringStyle, self).append(arg0, arg1, __char.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(__ToStringStyle, self).append(arg0, arg1, __short.valueOf(arg2))

    @override
    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendToString(arg0, arg1)

    @override
    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendEnd(arg0, arg1)

    @override
    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(__ToStringStyle, self).append(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendDetail(self, arg0: 'StringBuffer', arg1: str, arg2: object):
        """public void org.apache.commons.lang3.builder.RecursiveToStringStyle.appendDetail(java.lang.StringBuffer,java.lang.String,java.lang.Object)"""
        super(__RecursiveToStringStyle, self).appendDetail(arg0, arg1, arg2)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, bytes, arg3)

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
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendSuper(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(__ToStringStyle, self).append(arg0, arg1, __double.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.RecursiveToStringStyle()"""
        val = __RecursiveToStringStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.RecursiveToStringStyle()"""
        val = __RecursiveToStringStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

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
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(__ToStringStyle, self).append(arg0, arg1, __byte.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(__ToStringStyle, self).append(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map.__wrap(__ToStringStyle.getRegistry())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(__ToStringStyle, self).append(arg0, arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3) 
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringBuilder
import org.apache.commons.lang3.builder.ToStringBuilder as __ToStringBuilder
__ToStringBuilder = __ToStringBuilder
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.StringBuffer as StringBuffer
from builtins import float
from builtins import object
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ToStringBuilder(__Builder, Builder):
    """org.apache.commons.lang3.builder.ToStringBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ToStringBuilder) -> 'ToStringBuilder':
        return ToStringBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToStringBuilder):
        """
        Dynamic initializer for ToStringBuilder.
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
    def append(self, arg0: str, arg1: object, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object,boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def setDefaultStyle(arg0: 'ToStringStyle'):
        """public static void org.apache.commons.lang3.builder.ToStringBuilder.setDefaultStyle(org.apache.commons.lang3.builder.ToStringStyle)"""
        __ToStringBuilder.setDefaultStyle(arg0)

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __short.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(bytes))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__byte.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,java.lang.Class<? super T>)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0, arg1, __boolean.valueOf(arg2), arg3))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __long.valueOf(arg1)))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def getStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.builder.ToStringBuilder.getStringBuffer()"""
        return 'StringBuffer'.__wrap(super(ToStringBuilder, self).getStringBuffer())

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def appendToString(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendToString(java.lang.String)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).appendToString(arg0))

    @overload
    def append(self, arg0: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __byte.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def appendSuper(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendSuper(java.lang.String)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).appendSuper(arg0))

    @overload
    def append(self, arg0: str, arg1: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__float.valueOf(arg0)))

    @overload
    def append(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def getObject(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.builder.ToStringBuilder.getObject()"""
        return object.__wrap(super(ToStringBuilder, self).getObject())

    @overload
    def append(self, arg0: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__long.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, bytes, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0, arg1))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__double.valueOf(arg0)))

    @overload
    def appendAsObjectToString(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendAsObjectToString(java.lang.Object)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).appendAsObjectToString(arg0))

    @overload
    def append(self, arg0: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __int.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def getStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getStyle()"""
        return 'ToStringStyle'.__wrap(super(ToStringBuilder, self).getStyle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def append(self, arg0: str, arg1: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__short.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @staticmethod
    @overload
    def getDefaultStyle() -> 'ToStringStyle':
        """public static org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getDefaultStyle()"""
        return ToStringStyle.__wrap(__ToStringBuilder.getDefaultStyle())

    @overload
    def append(self, arg0: str, arg1: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __boolean.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.build()"""
        return str.__wrap(super(ToStringBuilder, self).build())

    @staticmethod
    @overload
    def reflectionToString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.ToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = __ToStringBuilder(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.builder.ToStringBuilder(java.lang.Object)"""
        val = __ToStringBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __char.valueOf(arg1)))

    @overload
    def append(self, arg0: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.toString()"""
        return str.__wrap(super(ToStringBuilder, self).toString())

    @overload
    def append(self, arg0: str, arg1: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, bytes))

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __float.valueOf(arg1)))

    @overload
    def append(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__char.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

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
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer'):
        """public org.apache.commons.lang3.builder.ToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer)"""
        val = __ToStringBuilder(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __double.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.builder.ReflectionToStringBuilder
import org.apache.commons.lang3.builder.ToStringBuilder as __ToStringBuilder
__ToStringBuilder = __ToStringBuilder
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Collection as Collection
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
from builtins import object
import org.apache.commons.lang3.builder.ReflectionToStringBuilder as __ReflectionToStringBuilder
__ReflectionToStringBuilder = __ReflectionToStringBuilder
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class ReflectionToStringBuilder(__ToStringBuilder, ToStringBuilder):
    """org.apache.commons.lang3.builder.ReflectionToStringBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionToStringBuilder) -> 'ReflectionToStringBuilder':
        return ReflectionToStringBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionToStringBuilder):
        """
        Dynamic initializer for ReflectionToStringBuilder.
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
    def isAppendTransients(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.ReflectionToStringBuilder.isAppendTransients()"""
        return bool.__wrap(super(ReflectionToStringBuilder, self).isAppendTransients())

    @overload
    def getExcludeFieldNames(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.builder.ReflectionToStringBuilder.getExcludeFieldNames()"""
        return List[str].__wrap(super(ReflectionToStringBuilder, self).getExcludeFieldNames())

    @overload
    def append(self, arg0: str, arg1: object, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object,boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def setDefaultStyle(arg0: 'ToStringStyle'):
        """public static void org.apache.commons.lang3.builder.ToStringBuilder.setDefaultStyle(org.apache.commons.lang3.builder.ToStringStyle)"""
        __ToStringBuilder.setDefaultStyle(arg0)

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer', arg3: 'Class', arg4: bool, arg5: bool):
        """public <T> org.apache.commons.lang3.builder.ReflectionToStringBuilder(T,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer,java.lang.Class<? super T>,boolean,boolean)"""
        val = __ReflectionToStringBuilder(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4), __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getUpToClass(self) -> 'type.Class':
        """public java.lang.Class<?> org.apache.commons.lang3.builder.ReflectionToStringBuilder.getUpToClass()"""
        return 'type.Class'.__wrap(super(ReflectionToStringBuilder, self).getUpToClass())

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __short.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def setUpToClass(self, arg0: 'Class'):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setUpToClass(java.lang.Class<?>)"""
        super(__ReflectionToStringBuilder, self).setUpToClass(arg0)

    @overload
    def append(self, arg0: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(bytes))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__byte.valueOf(arg0)))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder(java.lang.Object)"""
        val = __ReflectionToStringBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,java.lang.Class<? super T>)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0, arg1, __boolean.valueOf(arg2), arg3))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def toStringExclude(arg0: object, arg1: 'Collection') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringExclude(java.lang.Object,java.util.Collection<java.lang.String>)"""
        return str.__wrap(__ReflectionToStringBuilder.toStringExclude(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        return str.__wrap(__ReflectionToStringBuilder.toString(arg0, arg1))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def appendToString(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendToString(java.lang.String)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).appendToString(arg0))

    @overload
    def append(self, arg0: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def isExcludeNullValues(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.ReflectionToStringBuilder.isExcludeNullValues()"""
        return bool.__wrap(super(ReflectionToStringBuilder, self).isExcludeNullValues())

    @overload
    def setIncludeFieldNames(self, *arg0: str) -> 'ReflectionToStringBuilder':
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder org.apache.commons.lang3.builder.ReflectionToStringBuilder.setIncludeFieldNames(java.lang.String...)"""
        return 'ReflectionToStringBuilder'.__wrap(super(__ReflectionToStringBuilder, self).setIncludeFieldNames(arg0))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __byte.valueOf(arg1)))

    @override
    @overload
    def getStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.builder.ToStringBuilder.getStringBuffer()"""
        return 'StringBuffer'.__wrap(super(ToStringBuilder, self).getStringBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def appendSuper(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendSuper(java.lang.String)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).appendSuper(arg0))

    @overload
    def append(self, arg0: str, arg1: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__float.valueOf(arg0)))

    @overload
    def append(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.builder.ToStringBuilder.getObject()"""
        return object.__wrap(super(ToStringBuilder, self).getObject())

    @overload
    def append(self, arg0: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__long.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, bytes, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        return str.__wrap(__ReflectionToStringBuilder.toString(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def isAppendStatics(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.ReflectionToStringBuilder.isAppendStatics()"""
        return bool.__wrap(super(ReflectionToStringBuilder, self).isAppendStatics())

    @overload
    def setAppendStatics(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setAppendStatics(boolean)"""
        super(__ReflectionToStringBuilder, self).setAppendStatics(__boolean.valueOf(arg0))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__double.valueOf(arg0)))

    @overload
    def appendAsObjectToString(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendAsObjectToString(java.lang.Object)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).appendAsObjectToString(arg0))

    @staticmethod
    @overload
    def toStringExclude(arg0: object, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringExclude(java.lang.Object,java.lang.String...)"""
        return str.__wrap(__ReflectionToStringBuilder.toStringExclude(arg0, arg1))

    @overload
    def append(self, arg0: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __int.valueOf(arg1)))

    @overload
    def getIncludeFieldNames(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.builder.ReflectionToStringBuilder.getIncludeFieldNames()"""
        return List[str].__wrap(super(ReflectionToStringBuilder, self).getIncludeFieldNames())

    @staticmethod
    @overload
    def toStringInclude(arg0: object, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringInclude(java.lang.Object,java.lang.String...)"""
        return str.__wrap(__ReflectionToStringBuilder.toStringInclude(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer'):
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer)"""
        val = __ReflectionToStringBuilder(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def toString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object)"""
        return str.__wrap(__ReflectionToStringBuilder.toString(arg0))

    @overload
    def append(self, arg0: str, arg1: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__short.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @staticmethod
    @overload
    def getDefaultStyle() -> 'ToStringStyle':
        """public static org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getDefaultStyle()"""
        return ToStringStyle.__wrap(__ToStringBuilder.getDefaultStyle())

    @overload
    def append(self, arg0: str, arg1: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __boolean.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer', arg3: 'Class', arg4: bool, arg5: bool, arg6: bool):
        """public <T> org.apache.commons.lang3.builder.ReflectionToStringBuilder(T,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer,java.lang.Class<? super T>,boolean,boolean,boolean)"""
        val = __ReflectionToStringBuilder(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4), __boolean.valueOf(arg5), __boolean.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.build()"""
        return str.__wrap(super(ToStringBuilder, self).build())

    @staticmethod
    @overload
    def reflectionToString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object)"""
        return str.__wrap(__ToStringBuilder.reflectionToString(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = __ReflectionToStringBuilder(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __char.valueOf(arg1)))

    @overload
    def append(self, arg0: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString()"""
        return str.__wrap(super(ReflectionToStringBuilder, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: bool, arg4: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,boolean,java.lang.Class<? super T>)"""
        return str.__wrap(__ReflectionToStringBuilder.toString(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3), arg4))

    @overload
    def append(self, arg0: str, arg1: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, bytes))

    @overload
    def setAppendTransients(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setAppendTransients(boolean)"""
        super(__ReflectionToStringBuilder, self).setAppendTransients(__boolean.valueOf(arg0))

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean,boolean)"""
        return str.__wrap(__ReflectionToStringBuilder.toString(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: bool, arg4: bool, arg5: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,boolean,boolean,java.lang.Class<? super T>)"""
        return str.__wrap(__ReflectionToStringBuilder.toString(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4), arg5))

    @overload
    def append(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(__char.valueOf(arg0)))

    @overload
    def setExcludeNullValues(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setExcludeNullValues(boolean)"""
        super(__ReflectionToStringBuilder, self).setExcludeNullValues(__boolean.valueOf(arg0))

    @overload
    def append(self, arg0: str, arg1: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setExcludeFieldNames(self, *arg0: str) -> 'ReflectionToStringBuilder':
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder org.apache.commons.lang3.builder.ReflectionToStringBuilder.setExcludeFieldNames(java.lang.String...)"""
        return 'ReflectionToStringBuilder'.__wrap(super(__ReflectionToStringBuilder, self).setExcludeFieldNames(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, __double.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[],boolean)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def reflectionAppendArray(self, arg0: object) -> 'ReflectionToStringBuilder':
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder org.apache.commons.lang3.builder.ReflectionToStringBuilder.reflectionAppendArray(java.lang.Object)"""
        return 'ReflectionToStringBuilder'.__wrap(super(__ReflectionToStringBuilder, self).reflectionAppendArray(arg0))

    @overload
    def append(self, arg0: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0))

    @staticmethod
    @overload
    def toStringInclude(arg0: object, arg1: 'Collection') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringInclude(java.lang.Object,java.util.Collection<java.lang.String>)"""
        return str.__wrap(__ReflectionToStringBuilder.toStringInclude(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[])"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object)"""
        return 'ToStringBuilder'.__wrap(super(__ToStringBuilder, self).append(arg0, arg1))

    @override
    @overload
    def getStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getStyle()"""
        return 'ToStringStyle'.__wrap(super(ToStringBuilder, self).getStyle()) 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffBuilder
from builtins import str
import java.lang.Character as __char
import org.apache.commons.lang3.builder.DiffResult as __DiffResult
__DiffResult = __DiffResult
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import org.apache.commons.lang3.builder.DiffBuilder as __DiffBuilder
__DiffBuilder = __DiffBuilder
from builtins import int
 
class DiffBuilder(__Builder, Builder):
    """org.apache.commons.lang3.builder.DiffBuilder"""
 
    @staticmethod
    def __wrap(java_value: __DiffBuilder) -> 'DiffBuilder':
        return DiffBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DiffBuilder):
        """
        Dynamic initializer for DiffBuilder.
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
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,long,long)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __long.valueOf(arg1), __long.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: 'float') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,float[],float[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def append(self, arg0: str, arg1: float, arg2: float) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,float,float)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bytes) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,byte[],byte[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, bytes, bytes))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: 'char') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,char[],char[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: 'DiffResult') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,org.apache.commons.lang3.builder.DiffResult<T>)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: 'double') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,double[],double[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: 'short') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,short[],short[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,short,short)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __short.valueOf(arg1), __short.valueOf(arg2)))

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
    def append(self, arg0: str, arg1: str, arg2: str) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,char,char)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __char.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: 'boolean') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,boolean[],boolean[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: 'Object') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,java.lang.Object[],java.lang.Object[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle', arg3: bool):
        """public org.apache.commons.lang3.builder.DiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        val = __DiffBuilder(arg0, arg1, arg2, __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: bool, arg2: bool) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,boolean,boolean)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: float, arg2: float) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,double,double)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: 'int') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,int[],int[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: str, arg1: object, arg2: object) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,byte,byte)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __byte.valueOf(arg1), __byte.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: 'long') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,long[],long[])"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def build(self) -> 'DiffResult':
        """public org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.DiffBuilder.build()"""
        return 'DiffResult'.__wrap(super(DiffBuilder, self).build())

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,int,int)"""
        return 'DiffBuilder'.__wrap(super(__DiffBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.DiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = __DiffBuilder(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.builder.StandardToStringStyle
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import org.apache.commons.lang3.builder.StandardToStringStyle as __StandardToStringStyle
__StandardToStringStyle = __StandardToStringStyle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class StandardToStringStyle(__ToStringStyle, ToStringStyle):
    """org.apache.commons.lang3.builder.StandardToStringStyle"""
 
    @staticmethod
    def __wrap(java_value: __StandardToStringStyle) -> 'StandardToStringStyle':
        return StandardToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StandardToStringStyle):
        """
        Dynamic initializer for StandardToStringStyle.
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
    def getArrayStart(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getArrayStart()"""
        return str.__wrap(super(StandardToStringStyle, self).getArrayStart())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.StandardToStringStyle()"""
        val = __StandardToStringStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(__ToStringStyle, self).append(arg0, arg1, __char.valueOf(arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.StandardToStringStyle()"""
        val = __StandardToStringStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getArrayEnd(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getArrayEnd()"""
        return str.__wrap(super(StandardToStringStyle, self).getArrayEnd())

    @overload
    def isUseIdentityHashCode(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseIdentityHashCode()"""
        return bool.__wrap(super(StandardToStringStyle, self).isUseIdentityHashCode())

    @overload
    def getSizeStartText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSizeStartText()"""
        return str.__wrap(super(StandardToStringStyle, self).getSizeStartText())

    @override
    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(__ToStringStyle, self).append(arg0, arg1, __float.valueOf(arg2))

    @overload
    def isFieldSeparatorAtStart(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isFieldSeparatorAtStart()"""
        return bool.__wrap(super(StandardToStringStyle, self).isFieldSeparatorAtStart())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setArrayContentDetail(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArrayContentDetail(boolean)"""
        super(__StandardToStringStyle, self).setArrayContentDetail(__boolean.valueOf(arg0))

    @overload
    def isFieldSeparatorAtEnd(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isFieldSeparatorAtEnd()"""
        return bool.__wrap(super(StandardToStringStyle, self).isFieldSeparatorAtEnd())

    @override
    @overload
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendSuper(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def getSummaryObjectEndText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSummaryObjectEndText()"""
        return str.__wrap(super(StandardToStringStyle, self).getSummaryObjectEndText())

    @overload
    def getArraySeparator(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getArraySeparator()"""
        return str.__wrap(super(StandardToStringStyle, self).getArraySeparator())

    @overload
    def setContentEnd(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setContentEnd(java.lang.String)"""
        super(__StandardToStringStyle, self).setContentEnd(arg0)

    @overload
    def setFieldSeparatorAtStart(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldSeparatorAtStart(boolean)"""
        super(__StandardToStringStyle, self).setFieldSeparatorAtStart(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getContentEnd(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getContentEnd()"""
        return str.__wrap(super(StandardToStringStyle, self).getContentEnd())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isUseClassName(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseClassName()"""
        return bool.__wrap(super(StandardToStringStyle, self).isUseClassName())

    @overload
    def isDefaultFullDetail(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isDefaultFullDetail()"""
        return bool.__wrap(super(StandardToStringStyle, self).isDefaultFullDetail())

    @overload
    def setSizeStartText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSizeStartText(java.lang.String)"""
        super(__StandardToStringStyle, self).setSizeStartText(arg0)

    @overload
    def getNullText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getNullText()"""
        return str.__wrap(super(StandardToStringStyle, self).getNullText())

    @overload
    def setSizeEndText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSizeEndText(java.lang.String)"""
        super(__StandardToStringStyle, self).setSizeEndText(arg0)

    @overload
    def getFieldNameValueSeparator(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getFieldNameValueSeparator()"""
        return str.__wrap(super(StandardToStringStyle, self).getFieldNameValueSeparator())

    @overload
    def setArrayEnd(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArrayEnd(java.lang.String)"""
        super(__StandardToStringStyle, self).setArrayEnd(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def getSummaryObjectStartText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSummaryObjectStartText()"""
        return str.__wrap(super(StandardToStringStyle, self).getSummaryObjectStartText())

    @overload
    def isArrayContentDetail(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isArrayContentDetail()"""
        return bool.__wrap(super(StandardToStringStyle, self).isArrayContentDetail())

    @overload
    def getFieldSeparator(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getFieldSeparator()"""
        return str.__wrap(super(StandardToStringStyle, self).getFieldSeparator())

    @overload
    def setNullText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setNullText(java.lang.String)"""
        super(__StandardToStringStyle, self).setNullText(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(__ToStringStyle, self).append(arg0, arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isUseShortClassName(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseShortClassName()"""
        return bool.__wrap(super(StandardToStringStyle, self).isUseShortClassName())

    @overload
    def setArraySeparator(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArraySeparator(java.lang.String)"""
        super(__StandardToStringStyle, self).setArraySeparator(arg0)

    @overload
    def setUseFieldNames(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseFieldNames(boolean)"""
        super(__StandardToStringStyle, self).setUseFieldNames(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setSummaryObjectStartText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSummaryObjectStartText(java.lang.String)"""
        super(__StandardToStringStyle, self).setSummaryObjectStartText(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(__ToStringStyle, self).append(arg0, arg1, __short.valueOf(arg2))

    @override
    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendToString(arg0, arg1)

    @override
    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendEnd(arg0, arg1)

    @overload
    def setDefaultFullDetail(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setDefaultFullDetail(boolean)"""
        super(__StandardToStringStyle, self).setDefaultFullDetail(__boolean.valueOf(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def setContentStart(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setContentStart(java.lang.String)"""
        super(__StandardToStringStyle, self).setContentStart(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def setFieldSeparator(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldSeparator(java.lang.String)"""
        super(__StandardToStringStyle, self).setFieldSeparator(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, bytes, arg3)

    @overload
    def setFieldNameValueSeparator(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldNameValueSeparator(java.lang.String)"""
        super(__StandardToStringStyle, self).setFieldNameValueSeparator(arg0)

    @overload
    def getContentStart(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getContentStart()"""
        return str.__wrap(super(StandardToStringStyle, self).getContentStart())

    @overload
    def setUseClassName(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseClassName(boolean)"""
        super(__StandardToStringStyle, self).setUseClassName(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(__ToStringStyle, self).append(arg0, arg1, __double.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def setSummaryObjectEndText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSummaryObjectEndText(java.lang.String)"""
        super(__StandardToStringStyle, self).setSummaryObjectEndText(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def setUseShortClassName(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseShortClassName(boolean)"""
        super(__StandardToStringStyle, self).setUseShortClassName(__boolean.valueOf(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def getSizeEndText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSizeEndText()"""
        return str.__wrap(super(StandardToStringStyle, self).getSizeEndText())

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
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(__ToStringStyle, self).append(arg0, arg1, __byte.valueOf(arg2))

    @overload
    def setArrayStart(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArrayStart(java.lang.String)"""
        super(__StandardToStringStyle, self).setArrayStart(arg0)

    @overload
    def setFieldSeparatorAtEnd(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldSeparatorAtEnd(boolean)"""
        super(__StandardToStringStyle, self).setFieldSeparatorAtEnd(__boolean.valueOf(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(__ToStringStyle, self).append(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map.__wrap(__ToStringStyle.getRegistry())

    @overload
    def isUseFieldNames(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseFieldNames()"""
        return bool.__wrap(super(StandardToStringStyle, self).isUseFieldNames())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def setUseIdentityHashCode(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseIdentityHashCode(boolean)"""
        super(__StandardToStringStyle, self).setUseIdentityHashCode(__boolean.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringExclude
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.apache.commons.lang3.builder.ToStringExclude as __ToStringExclude
__ToStringExclude = __ToStringExclude
from abc import abstractmethod, ABC
 
class ToStringExclude(ABC, __Annotation, Annotation):
    """org.apache.commons.lang3.builder.ToStringExclude"""
 
    @staticmethod
    def __wrap(java_value: __ToStringExclude) -> 'ToStringExclude':
        return ToStringExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToStringExclude):
        """
        Dynamic initializer for ToStringExclude.
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
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.ReflectionDiffBuilder
from builtins import str
import org.apache.commons.lang3.builder.DiffResult as __DiffResult
__DiffResult = __DiffResult
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.builder.ReflectionDiffBuilder as __ReflectionDiffBuilder
__ReflectionDiffBuilder = __ReflectionDiffBuilder
from typing import List
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
 
class ReflectionDiffBuilder(__Builder, Builder):
    """org.apache.commons.lang3.builder.ReflectionDiffBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionDiffBuilder) -> 'ReflectionDiffBuilder':
        return ReflectionDiffBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionDiffBuilder):
        """
        Dynamic initializer for ReflectionDiffBuilder.
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
    def getExcludeFieldNames(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.builder.ReflectionDiffBuilder.getExcludeFieldNames()"""
        return List[str].__wrap(super(ReflectionDiffBuilder, self).getExcludeFieldNames())

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

    @override
    @overload
    def build(self) -> 'DiffResult':
        """public org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.ReflectionDiffBuilder.build()"""
        return 'DiffResult'.__wrap(super(ReflectionDiffBuilder, self).build())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setExcludeFieldNames(self, *arg0: str) -> 'ReflectionDiffBuilder':
        """public org.apache.commons.lang3.builder.ReflectionDiffBuilder<T> org.apache.commons.lang3.builder.ReflectionDiffBuilder.setExcludeFieldNames(java.lang.String...)"""
        return 'ReflectionDiffBuilder'.__wrap(super(__ReflectionDiffBuilder, self).setExcludeFieldNames(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.ReflectionDiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = __ReflectionDiffBuilder(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.lang3.builder.ToStringStyle as __ToStringStyle
__ToStringStyle = __ToStringStyle
import org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle as __MultilineRecursiveToStringStyle
__MultilineRecursiveToStringStyle = __MultilineRecursiveToStringStyle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class MultilineRecursiveToStringStyle(__RecursiveToStringStyle, RecursiveToStringStyle):
    """org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle"""
 
    @staticmethod
    def __wrap(java_value: __MultilineRecursiveToStringStyle) -> 'MultilineRecursiveToStringStyle':
        return MultilineRecursiveToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultilineRecursiveToStringStyle):
        """
        Dynamic initializer for MultilineRecursiveToStringStyle.
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
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(__ToStringStyle, self).append(arg0, arg1, __char.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(__ToStringStyle, self).append(arg0, arg1, __short.valueOf(arg2))

    @override
    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendToString(arg0, arg1)

    @override
    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendEnd(arg0, arg1)

    @override
    @overload
    def appendDetail(self, arg0: 'StringBuffer', arg1: str, arg2: object):
        """public void org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle.appendDetail(java.lang.StringBuffer,java.lang.String,java.lang.Object)"""
        super(__MultilineRecursiveToStringStyle, self).appendDetail(arg0, arg1, arg2)

    @override
    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(__ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(__ToStringStyle, self).append(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle()"""
        val = __MultilineRecursiveToStringStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, bytes, arg3)

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
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(__ToStringStyle, self).appendSuper(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(__ToStringStyle, self).append(arg0, arg1, __double.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle()"""
        val = __MultilineRecursiveToStringStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

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
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(__ToStringStyle, self).append(arg0, arg1, __byte.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(__ToStringStyle, self).append(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map.__wrap(__ToStringStyle.getRegistry())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(__ToStringStyle, self).append(arg0, arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(__ToStringStyle, self).append(arg0, arg1, arg2, arg3) 
 
 
# CLASS: org.apache.commons.lang3.builder.Builder
import org.apache.commons.lang3.builder.Builder as __Builder
__Builder = __Builder
from abc import abstractmethod, ABC
 
class Builder(ABC):
    """org.apache.commons.lang3.builder.Builder"""
 
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
 
    @abstractmethod
    def build(self, ):
        """public abstract T org.apache.commons.lang3.builder.Builder.build()"""
        pass