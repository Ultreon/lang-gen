from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bag.SynchronizedBag as _SynchronizedBag
_SynchronizedBag = _SynchronizedBag
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import org.apache.commons.collections4.collection.SynchronizedCollection as _SynchronizedCollection
_SynchronizedCollection = _SynchronizedCollection
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SynchronizedBag():
    """org.apache.commons.collections4.bag.SynchronizedBag"""
 
    @staticmethod
    def _wrap(java_value: _SynchronizedBag) -> 'SynchronizedBag':
        return SynchronizedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronizedBag):
        """
        Dynamic initializer for SynchronizedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronizedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronizedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object]._wrap(super(collection.SynchronizedCollection, self).toArray())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_SynchronizedBag, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.add(E,int)"""
        return bool._wrap(super(_SynchronizedBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.SynchronizedCollection.clear()"""
        super(collection.SynchronizedCollection, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).contains(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).retainAll(arg0))

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'SynchronizedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedBag<E> org.apache.commons.collections4.bag.SynchronizedBag.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return SynchronizedBag._wrap(_SynchronizedBag.synchronizedBag(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).remove(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeIf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.isEmpty()"""
        return bool._wrap(super(collection.SynchronizedCollection, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).add(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object]._wrap(super(_collection.SynchronizedCollection, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.SynchronizedCollection.iterator()"""
        return 'Iterator'._wrap(super(collection.SynchronizedCollection, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).containsAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.SynchronizedBag.uniqueSet()"""
        return 'Set'._wrap(super(SynchronizedBag, self).uniqueSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedBag, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.hashCode()"""
        return int._wrap(super(SynchronizedBag, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int._wrap(super(collection.SynchronizedCollection, self).size())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_SynchronizedBag, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str._wrap(super(collection.SynchronizedCollection, self).toString())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).addAll(arg0))

    @staticmethod
    @overload
    def synchronizedCollection(arg0: 'Collection') -> 'collection.SynchronizedCollection':
        """public static <T> org.apache.commons.collections4.collection.SynchronizedCollection<T> org.apache.commons.collections4.collection.SynchronizedCollection.synchronizedCollection(java.util.Collection<T>)"""
        return collection.SynchronizedCollection._wrap(_SynchronizedCollection.synchronizedCollection(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.bag.SynchronizedBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bag.SynchronizedBag as _SynchronizedBag
_SynchronizedBag = _SynchronizedBag
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import org.apache.commons.collections4.collection.SynchronizedCollection as _SynchronizedCollection
_SynchronizedCollection = _SynchronizedCollection
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SynchronizedBag():
    """org.apache.commons.collections4.bag.SynchronizedBag"""
 
    @staticmethod
    def _wrap(java_value: _SynchronizedBag) -> 'SynchronizedBag':
        return SynchronizedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronizedBag):
        """
        Dynamic initializer for SynchronizedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronizedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronizedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object]._wrap(super(collection.SynchronizedCollection, self).toArray())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_SynchronizedBag, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.add(E,int)"""
        return bool._wrap(super(_SynchronizedBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.SynchronizedCollection.clear()"""
        super(collection.SynchronizedCollection, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).contains(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).retainAll(arg0))

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'SynchronizedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedBag<E> org.apache.commons.collections4.bag.SynchronizedBag.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return SynchronizedBag._wrap(_SynchronizedBag.synchronizedBag(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).remove(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeIf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.isEmpty()"""
        return bool._wrap(super(collection.SynchronizedCollection, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).add(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object]._wrap(super(_collection.SynchronizedCollection, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.SynchronizedCollection.iterator()"""
        return 'Iterator'._wrap(super(collection.SynchronizedCollection, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).containsAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.SynchronizedBag.uniqueSet()"""
        return 'Set'._wrap(super(SynchronizedBag, self).uniqueSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedBag, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.hashCode()"""
        return int._wrap(super(SynchronizedBag, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int._wrap(super(collection.SynchronizedCollection, self).size())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_SynchronizedBag, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str._wrap(super(collection.SynchronizedCollection, self).toString())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).addAll(arg0))

    @staticmethod
    @overload
    def synchronizedCollection(arg0: 'Collection') -> 'collection.SynchronizedCollection':
        """public static <T> org.apache.commons.collections4.collection.SynchronizedCollection<T> org.apache.commons.collections4.collection.SynchronizedCollection.synchronizedCollection(java.util.Collection<T>)"""
        return collection.SynchronizedCollection._wrap(_SynchronizedCollection.synchronizedCollection(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.bag.SynchronizedBag 
 
 
# CLASS: org.apache.commons.collections4.bag.UnmodifiableBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.AbstractBagDecorator as _AbstractBagDecorator
_AbstractBagDecorator = _AbstractBagDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import org.apache.commons.collections4.bag.UnmodifiableBag as _UnmodifiableBag
_UnmodifiableBag = _UnmodifiableBag
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableBag():
    """org.apache.commons.collections4.bag.UnmodifiableBag"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableBag) -> 'UnmodifiableBag':
        return UnmodifiableBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableBag):
        """
        Dynamic initializer for UnmodifiableBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableBag, self).addAll(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractBagDecorator, self).getCount(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.UnmodifiableBag.clear()"""
        super(UnmodifiableBag, self).clear()

    @staticmethod
    @overload
    def unmodifiableBag(arg0: 'Bag') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.UnmodifiableBag.unmodifiableBag(org.apache.commons.collections4.Bag<? extends E>)"""
        return collections4.Bag._wrap(_UnmodifiableBag.unmodifiableBag(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableBag, self).removeIf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int._wrap(super(AbstractBagDecorator, self).hashCode())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.UnmodifiableBag.uniqueSet()"""
        return 'Set'._wrap(super(UnmodifiableBag, self).uniqueSet())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.add(E,int)"""
        return bool._wrap(super(_UnmodifiableBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.UnmodifiableBag.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableBag, self).iterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableBag, self).remove(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractBagDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableBag, self).removeAll(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_UnmodifiableBag, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.add(E)"""
        return bool._wrap(super(_UnmodifiableBag, self).add(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableBag, self).retainAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractSortedBagDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.AbstractBagDecorator as _AbstractBagDecorator
_AbstractBagDecorator = _AbstractBagDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bag.AbstractSortedBagDecorator as _AbstractSortedBagDecorator
_AbstractSortedBagDecorator = _AbstractSortedBagDecorator
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSortedBagDecorator():
    """org.apache.commons.collections4.bag.AbstractSortedBagDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSortedBagDecorator) -> 'AbstractSortedBagDecorator':
        return AbstractSortedBagDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSortedBagDecorator):
        """
        Dynamic initializer for AbstractSortedBagDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSortedBagDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSortedBagDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractBagDecorator, self).getCount(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'._wrap(super(AbstractBagDecorator, self).uniqueSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.add(E,int)"""
        return bool._wrap(super(_AbstractBagDecorator, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractBagDecorator, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int._wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.last()"""
        return object._wrap(super(AbstractSortedBagDecorator, self).last())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.AbstractSortedBagDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBagDecorator, self).comparator())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractBagDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.first()"""
        return object._wrap(super(AbstractSortedBagDecorator, self).first())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.TreeBag
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.bag.TreeBag as _TreeBag
_TreeBag = _TreeBag
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import org.apache.commons.collections4.bag.AbstractMapBag as _AbstractMapBag
_AbstractMapBag = _AbstractMapBag
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TreeBag():
    """org.apache.commons.collections4.bag.TreeBag"""
 
    @staticmethod
    def _wrap(java_value: _TreeBag) -> 'TreeBag':
        return TreeBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeBag):
        """
        Dynamic initializer for TreeBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractMapBag, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bag.TreeBag()"""
        val = _TreeBag()
        self.__wrapper = val

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).retainAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractMapBag.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMapBag, self).uniqueSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.TreeBag.last()"""
        return object._wrap(super(TreeBag, self).last())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).remove(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).removeAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bag.AbstractMapBag.toString()"""
        return str._wrap(super(AbstractMapBag, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.AbstractMapBag.clear()"""
        super(AbstractMapBag, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).equals(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.TreeBag.comparator()"""
        return 'Comparator'._wrap(super(TreeBag, self).comparator())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.bag.AbstractMapBag.toArray(T[])"""
        return List[object]._wrap(super(_AbstractMapBag, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.hashCode()"""
        return int._wrap(super(AbstractMapBag, self).hashCode())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.bag.TreeBag(java.util.Collection<? extends E>)"""
        val = _TreeBag(arg0)
        self.__wrapper = val

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.TreeBag.first()"""
        return object._wrap(super(TreeBag, self).first())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.AbstractMapBag.iterator()"""
        return 'Iterator'._wrap(super(AbstractMapBag, self).iterator())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMapBag, self).getCount(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E,int)"""
        return bool._wrap(super(_AbstractMapBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.bag.AbstractMapBag.toArray()"""
        return List[object]._wrap(super(AbstractMapBag, self).toArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.isEmpty()"""
        return bool._wrap(super(AbstractMapBag, self).isEmpty())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bag.TreeBag()"""
        val = _TreeBag()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).contains(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.TreeBag.add(E)"""
        return bool._wrap(super(_TreeBag, self).add(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.size()"""
        return int._wrap(super(AbstractMapBag, self).size())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractMapBag, self).addAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.bag.TreeBag(java.util.Comparator<? super E>)"""
        val = _TreeBag(arg0)
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.bag.SynchronizedSortedBag
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.bag.SynchronizedSortedBag as _SynchronizedSortedBag
_SynchronizedSortedBag = _SynchronizedSortedBag
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bag.SynchronizedBag as _SynchronizedBag
_SynchronizedBag = _SynchronizedBag
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import org.apache.commons.collections4.collection.SynchronizedCollection as _SynchronizedCollection
_SynchronizedCollection = _SynchronizedCollection
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SynchronizedSortedBag():
    """org.apache.commons.collections4.bag.SynchronizedSortedBag"""
 
    @staticmethod
    def _wrap(java_value: _SynchronizedSortedBag) -> 'SynchronizedSortedBag':
        return SynchronizedSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronizedSortedBag):
        """
        Dynamic initializer for SynchronizedSortedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronizedSortedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronizedSortedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def last(self) -> object:
        """public synchronized E org.apache.commons.collections4.bag.SynchronizedSortedBag.last()"""
        return object._wrap(super(SynchronizedSortedBag, self).last())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object]._wrap(super(collection.SynchronizedCollection, self).toArray())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_SynchronizedBag, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.add(E,int)"""
        return bool._wrap(super(_SynchronizedBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.SynchronizedCollection.clear()"""
        super(collection.SynchronizedCollection, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).contains(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).retainAll(arg0))

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'SynchronizedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedBag<E> org.apache.commons.collections4.bag.SynchronizedBag.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return SynchronizedBag._wrap(_SynchronizedBag.synchronizedBag(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).remove(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeIf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.isEmpty()"""
        return bool._wrap(super(collection.SynchronizedCollection, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).add(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object]._wrap(super(_collection.SynchronizedCollection, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.SynchronizedCollection.iterator()"""
        return 'Iterator'._wrap(super(collection.SynchronizedCollection, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).containsAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.SynchronizedBag.uniqueSet()"""
        return 'Set'._wrap(super(SynchronizedBag, self).uniqueSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedBag, self).equals(arg0))

    @override
    @overload
    def first(self) -> object:
        """public synchronized E org.apache.commons.collections4.bag.SynchronizedSortedBag.first()"""
        return object._wrap(super(SynchronizedSortedBag, self).first())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public synchronized java.util.Comparator<? super E> org.apache.commons.collections4.bag.SynchronizedSortedBag.comparator()"""
        return 'Comparator'._wrap(super(SynchronizedSortedBag, self).comparator())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.hashCode()"""
        return int._wrap(super(SynchronizedBag, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int._wrap(super(collection.SynchronizedCollection, self).size())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_SynchronizedBag, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def synchronizedSortedBag(arg0: 'SortedBag') -> 'SynchronizedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedSortedBag<E> org.apache.commons.collections4.bag.SynchronizedSortedBag.synchronizedSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return SynchronizedSortedBag._wrap(_SynchronizedSortedBag.synchronizedSortedBag(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str._wrap(super(collection.SynchronizedCollection, self).toString())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).addAll(arg0))

    @staticmethod
    @overload
    def synchronizedCollection(arg0: 'Collection') -> 'collection.SynchronizedCollection':
        """public static <T> org.apache.commons.collections4.collection.SynchronizedCollection<T> org.apache.commons.collections4.collection.SynchronizedCollection.synchronizedCollection(java.util.Collection<T>)"""
        return collection.SynchronizedCollection._wrap(_SynchronizedCollection.synchronizedCollection(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bag.CollectionBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.AbstractBagDecorator as _AbstractBagDecorator
_AbstractBagDecorator = _AbstractBagDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.bag.CollectionBag as _CollectionBag
_CollectionBag = _CollectionBag
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CollectionBag():
    """org.apache.commons.collections4.bag.CollectionBag"""
 
    @staticmethod
    def _wrap(java_value: _CollectionBag) -> 'CollectionBag':
        return CollectionBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectionBag):
        """
        Dynamic initializer for CollectionBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectionBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectionBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CollectionBag, self).retainAll(arg0))

    @overload
    def __init__(self, arg0: 'Bag'):
        """public org.apache.commons.collections4.bag.CollectionBag(org.apache.commons.collections4.Bag<E>)"""
        val = _CollectionBag(arg0)
        self.__wrapper = val

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractBagDecorator, self).getCount(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.add(E)"""
        return bool._wrap(super(_CollectionBag, self).add(arg0))

    @staticmethod
    @overload
    def collectionBag(arg0: 'Bag') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.CollectionBag.collectionBag(org.apache.commons.collections4.Bag<E>)"""
        return collections4.Bag._wrap(_CollectionBag.collectionBag(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'._wrap(super(AbstractBagDecorator, self).uniqueSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractBagDecorator, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.remove(java.lang.Object)"""
        return bool._wrap(super(_CollectionBag, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int._wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.add(E,int)"""
        return bool._wrap(super(_CollectionBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractBagDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_CollectionBag, self).addAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CollectionBag, self).removeAll(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CollectionBag, self).containsAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractMapBag$MutableInteger
import org.apache.commons.collections4.bag.AbstractMapBag as _AbstractMapBag_MutableInteger
_MutableInteger = _AbstractMapBag_MutableInteger.MutableInteger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableInteger():
    """org.apache.commons.collections4.bag.AbstractMapBag.MutableInteger"""
 
    @staticmethod
    def _wrap(java_value: _MutableInteger) -> 'MutableInteger':
        return MutableInteger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableInteger):
        """
        Dynamic initializer for MutableInteger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableInteger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableInteger__wrapper":
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag$MutableInteger.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableInteger, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag$MutableInteger.hashCode()"""
        return int._wrap(super(MutableInteger, self).hashCode())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString()) 
 
 
# CLASS: org.apache.commons.collections4.bag.PredicatedSortedBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection
_PredicatedCollection = _PredicatedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

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
import org.apache.commons.collections4.bag.PredicatedSortedBag as _PredicatedSortedBag
_PredicatedSortedBag = _PredicatedSortedBag
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection_Builder
_Builder = _PredicatedCollection_Builder.Builder
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.bag.PredicatedBag as _PredicatedBag
_PredicatedBag = _PredicatedBag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedSortedBag():
    """org.apache.commons.collections4.bag.PredicatedSortedBag"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedSortedBag) -> 'PredicatedSortedBag':
        return PredicatedSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedSortedBag):
        """
        Dynamic initializer for PredicatedSortedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedSortedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedSortedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def predicatedBag(arg0: 'Bag', arg1: 'Predicate') -> 'PredicatedBag':
        """public static <E> org.apache.commons.collections4.bag.PredicatedBag<E> org.apache.commons.collections4.bag.PredicatedBag.predicatedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedBag._wrap(_PredicatedBag.predicatedBag(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def predicatedSortedBag(arg0: 'SortedBag', arg1: 'Predicate') -> 'PredicatedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.PredicatedSortedBag<E> org.apache.commons.collections4.bag.PredicatedSortedBag.predicatedSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSortedBag._wrap(_PredicatedSortedBag.predicatedSortedBag(arg0, arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.hashCode()"""
        return int._wrap(super(PredicatedBag, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_PredicatedBag, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedBag, self).equals(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.PredicatedBag.uniqueSet()"""
        return 'Set'._wrap(super(PredicatedBag, self).uniqueSet())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.PredicatedSortedBag.comparator()"""
        return 'Comparator'._wrap(super(PredicatedSortedBag, self).comparator())

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.notNullBuilder())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.add(E,int)"""
        return bool._wrap(super(_PredicatedBag, self).add(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection._wrap(_PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.PredicatedSortedBag.last()"""
        return object._wrap(super(PredicatedSortedBag, self).last())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.PredicatedSortedBag.first()"""
        return object._wrap(super(PredicatedSortedBag, self).first())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.builder(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_PredicatedBag, self).getCount(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.HashBag
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
import org.apache.commons.collections4.bag.AbstractMapBag as _AbstractMapBag
_AbstractMapBag = _AbstractMapBag
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.bag.HashBag as _HashBag
_HashBag = _HashBag
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashBag():
    """org.apache.commons.collections4.bag.HashBag"""
 
    @staticmethod
    def _wrap(java_value: _HashBag) -> 'HashBag':
        return HashBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashBag):
        """
        Dynamic initializer for HashBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractMapBag, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.bag.HashBag(java.util.Collection<? extends E>)"""
        val = _HashBag(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bag.HashBag()"""
        val = _HashBag()
        self.__wrapper = val

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).retainAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractMapBag.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMapBag, self).uniqueSet())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E)"""
        return bool._wrap(super(_AbstractMapBag, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).remove(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).removeAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bag.AbstractMapBag.toString()"""
        return str._wrap(super(AbstractMapBag, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.AbstractMapBag.clear()"""
        super(AbstractMapBag, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.bag.AbstractMapBag.toArray(T[])"""
        return List[object]._wrap(super(_AbstractMapBag, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.hashCode()"""
        return int._wrap(super(AbstractMapBag, self).hashCode())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.AbstractMapBag.iterator()"""
        return 'Iterator'._wrap(super(AbstractMapBag, self).iterator())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMapBag, self).getCount(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bag.HashBag()"""
        val = _HashBag()
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E,int)"""
        return bool._wrap(super(_AbstractMapBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.bag.AbstractMapBag.toArray()"""
        return List[object]._wrap(super(AbstractMapBag, self).toArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.isEmpty()"""
        return bool._wrap(super(AbstractMapBag, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.size()"""
        return int._wrap(super(AbstractMapBag, self).size())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractMapBag, self).addAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bag.CollectionSortedBag
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.bag.CollectionSortedBag as _CollectionSortedBag
_CollectionSortedBag = _CollectionSortedBag
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.AbstractBagDecorator as _AbstractBagDecorator
_AbstractBagDecorator = _AbstractBagDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bag.AbstractSortedBagDecorator as _AbstractSortedBagDecorator
_AbstractSortedBagDecorator = _AbstractSortedBagDecorator
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.SortedBag as _SortedBag
_SortedBag = _SortedBag
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CollectionSortedBag():
    """org.apache.commons.collections4.bag.CollectionSortedBag"""
 
    @staticmethod
    def _wrap(java_value: _CollectionSortedBag) -> 'CollectionSortedBag':
        return CollectionSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectionSortedBag):
        """
        Dynamic initializer for CollectionSortedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectionSortedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectionSortedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_CollectionSortedBag, self).addAll(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractBagDecorator, self).getCount(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.add(E)"""
        return bool._wrap(super(_CollectionSortedBag, self).add(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'._wrap(super(AbstractBagDecorator, self).uniqueSet())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CollectionSortedBag, self).retainAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def collectionSortedBag(arg0: 'SortedBag') -> 'collections4.SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.bag.CollectionSortedBag.collectionSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return collections4.SortedBag._wrap(_CollectionSortedBag.collectionSortedBag(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'SortedBag'):
        """public org.apache.commons.collections4.bag.CollectionSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        val = _CollectionSortedBag(arg0)
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractBagDecorator, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CollectionSortedBag, self).removeAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int._wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CollectionSortedBag, self).containsAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.last()"""
        return object._wrap(super(AbstractSortedBagDecorator, self).last())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.add(E,int)"""
        return bool._wrap(super(_CollectionSortedBag, self).add(arg0, _int.valueOf(arg1)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.remove(java.lang.Object)"""
        return bool._wrap(super(_CollectionSortedBag, self).remove(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.AbstractSortedBagDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBagDecorator, self).comparator())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractBagDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.first()"""
        return object._wrap(super(AbstractSortedBagDecorator, self).first()) 
 
 
# CLASS: org.apache.commons.collections4.bag.TransformedBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.bag.TransformedBag as _TransformedBag
_TransformedBag = _TransformedBag
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedBag():
    """org.apache.commons.collections4.bag.TransformedBag"""
 
    @staticmethod
    def _wrap(java_value: _TransformedBag) -> 'TransformedBag':
        return TransformedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedBag):
        """
        Dynamic initializer for TransformedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.add(E,int)"""
        return bool._wrap(super(_TransformedBag, self).add(arg0, _int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_TransformedBag, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.TransformedBag.uniqueSet()"""
        return 'Set'._wrap(super(TransformedBag, self).uniqueSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformedBag, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.TransformedCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.hashCode()"""
        return int._wrap(super(TransformedBag, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def transformedBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag._wrap(_TransformedBag.transformedBag(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformingCollection(arg0, arg1))

    @staticmethod
    @overload
    def transformingBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformingBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag._wrap(_TransformedBag.transformingBag(arg0, arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_TransformedBag, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.UnmodifiableSortedBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.AbstractBagDecorator as _AbstractBagDecorator
_AbstractBagDecorator = _AbstractBagDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bag.AbstractSortedBagDecorator as _AbstractSortedBagDecorator
_AbstractSortedBagDecorator = _AbstractSortedBagDecorator
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.SortedBag as _SortedBag
_SortedBag = _SortedBag
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import org.apache.commons.collections4.bag.UnmodifiableSortedBag as _UnmodifiableSortedBag
_UnmodifiableSortedBag = _UnmodifiableSortedBag
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableSortedBag():
    """org.apache.commons.collections4.bag.UnmodifiableSortedBag"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableSortedBag) -> 'UnmodifiableSortedBag':
        return UnmodifiableSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableSortedBag):
        """
        Dynamic initializer for UnmodifiableSortedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableSortedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableSortedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractBagDecorator, self).getCount(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.add(E,int)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.UnmodifiableSortedBag.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableSortedBag, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.add(E)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).add(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).addAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.UnmodifiableSortedBag.uniqueSet()"""
        return 'Set'._wrap(super(UnmodifiableSortedBag, self).uniqueSet())

    @staticmethod
    @overload
    def unmodifiableSortedBag(arg0: 'SortedBag') -> 'collections4.SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.bag.UnmodifiableSortedBag.unmodifiableSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return collections4.SortedBag._wrap(_UnmodifiableSortedBag.unmodifiableSortedBag(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int._wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.last()"""
        return object._wrap(super(AbstractSortedBagDecorator, self).last())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.AbstractSortedBagDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBagDecorator, self).comparator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractBagDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.UnmodifiableSortedBag.clear()"""
        super(UnmodifiableSortedBag, self).clear()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).retainAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.first()"""
        return object._wrap(super(AbstractSortedBagDecorator, self).first())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableSortedBag, self).removeAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractMapBag
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
import org.apache.commons.collections4.bag.AbstractMapBag as _AbstractMapBag
_AbstractMapBag = _AbstractMapBag
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMapBag():
    """org.apache.commons.collections4.bag.AbstractMapBag"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMapBag) -> 'AbstractMapBag':
        return AbstractMapBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMapBag):
        """
        Dynamic initializer for AbstractMapBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMapBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMapBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractMapBag, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).retainAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractMapBag.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMapBag, self).uniqueSet())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E)"""
        return bool._wrap(super(_AbstractMapBag, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).remove(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMapBag, self).removeAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bag.AbstractMapBag.toString()"""
        return str._wrap(super(AbstractMapBag, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.AbstractMapBag.clear()"""
        super(AbstractMapBag, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.bag.AbstractMapBag.toArray(T[])"""
        return List[object]._wrap(super(_AbstractMapBag, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.hashCode()"""
        return int._wrap(super(AbstractMapBag, self).hashCode())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.AbstractMapBag.iterator()"""
        return 'Iterator'._wrap(super(AbstractMapBag, self).iterator())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMapBag, self).getCount(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E,int)"""
        return bool._wrap(super(_AbstractMapBag, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.bag.AbstractMapBag.toArray()"""
        return List[object]._wrap(super(AbstractMapBag, self).toArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.isEmpty()"""
        return bool._wrap(super(AbstractMapBag, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapBag, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.size()"""
        return int._wrap(super(AbstractMapBag, self).size())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractMapBag, self).addAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bag.TransformedSortedBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import org.apache.commons.collections4.bag.TransformedSortedBag as _TransformedSortedBag
_TransformedSortedBag = _TransformedSortedBag
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.bag.TransformedBag as _TransformedBag
_TransformedBag = _TransformedBag
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedSortedBag():
    """org.apache.commons.collections4.bag.TransformedSortedBag"""
 
    @staticmethod
    def _wrap(java_value: _TransformedSortedBag) -> 'TransformedSortedBag':
        return TransformedSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedSortedBag):
        """
        Dynamic initializer for TransformedSortedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedSortedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedSortedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.add(E,int)"""
        return bool._wrap(super(_TransformedBag, self).add(arg0, _int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_TransformedBag, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.TransformedBag.uniqueSet()"""
        return 'Set'._wrap(super(TransformedBag, self).uniqueSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformedBag, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def transformedSortedBag(arg0: 'SortedBag', arg1: 'Transformer') -> 'TransformedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.TransformedSortedBag<E> org.apache.commons.collections4.bag.TransformedSortedBag.transformedSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedBag._wrap(_TransformedSortedBag.transformedSortedBag(arg0, arg1))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.TransformedSortedBag.first()"""
        return object._wrap(super(TransformedSortedBag, self).first())

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.TransformedCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.hashCode()"""
        return int._wrap(super(TransformedBag, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def transformedBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag._wrap(_TransformedBag.transformedBag(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.TransformedSortedBag.last()"""
        return object._wrap(super(TransformedSortedBag, self).last())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.TransformedSortedBag.comparator()"""
        return 'Comparator'._wrap(super(TransformedSortedBag, self).comparator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformingCollection(arg0, arg1))

    @staticmethod
    @overload
    def transformingBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformingBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag._wrap(_TransformedBag.transformingBag(arg0, arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @staticmethod
    @overload
    def transformingSortedBag(arg0: 'SortedBag', arg1: 'Transformer') -> 'TransformedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.TransformedSortedBag<E> org.apache.commons.collections4.bag.TransformedSortedBag.transformingSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedBag._wrap(_TransformedSortedBag.transformingSortedBag(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_TransformedBag, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.PredicatedBag
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection
_PredicatedCollection = _PredicatedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection_Builder
_Builder = _PredicatedCollection_Builder.Builder
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.bag.PredicatedBag as _PredicatedBag
_PredicatedBag = _PredicatedBag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedBag():
    """org.apache.commons.collections4.bag.PredicatedBag"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedBag) -> 'PredicatedBag':
        return PredicatedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedBag):
        """
        Dynamic initializer for PredicatedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def predicatedBag(arg0: 'Bag', arg1: 'Predicate') -> 'PredicatedBag':
        """public static <E> org.apache.commons.collections4.bag.PredicatedBag<E> org.apache.commons.collections4.bag.PredicatedBag.predicatedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedBag._wrap(_PredicatedBag.predicatedBag(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.hashCode()"""
        return int._wrap(super(PredicatedBag, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.remove(java.lang.Object,int)"""
        return bool._wrap(super(_PredicatedBag, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedBag, self).equals(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.PredicatedBag.uniqueSet()"""
        return 'Set'._wrap(super(PredicatedBag, self).uniqueSet())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.notNullBuilder())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.add(E,int)"""
        return bool._wrap(super(_PredicatedBag, self).add(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection._wrap(_PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.builder(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.getCount(java.lang.Object)"""
        return int._wrap(super(_PredicatedBag, self).getCount(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractBagDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.AbstractBagDecorator as _AbstractBagDecorator
_AbstractBagDecorator = _AbstractBagDecorator
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractBagDecorator():
    """org.apache.commons.collections4.bag.AbstractBagDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractBagDecorator) -> 'AbstractBagDecorator':
        return AbstractBagDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractBagDecorator):
        """
        Dynamic initializer for AbstractBagDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractBagDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractBagDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractBagDecorator, self).getCount(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'._wrap(super(AbstractBagDecorator, self).uniqueSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.add(E,int)"""
        return bool._wrap(super(_AbstractBagDecorator, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool._wrap(super(_AbstractBagDecorator, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int._wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractBagDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))