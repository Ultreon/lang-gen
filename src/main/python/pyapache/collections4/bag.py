from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.bag.UnmodifiableBag as __UnmodifiableBag
__UnmodifiableBag = __UnmodifiableBag
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableBag(__AbstractBagDecorator, AbstractBagDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.bag.UnmodifiableBag"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableBag) -> 'UnmodifiableBag':
        return UnmodifiableBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableBag):
        """
        Dynamic initializer for UnmodifiableBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).removeIf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.add(E)"""
        return bool.__wrap(super(__UnmodifiableBag, self).add(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.UnmodifiableBag.clear()"""
        super(UnmodifiableBag, self).clear()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableBag, self).remove(arg0))

    @staticmethod
    @overload
    def unmodifiableBag(arg0: 'Bag') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.UnmodifiableBag.unmodifiableBag(org.apache.commons.collections4.Bag<? extends E>)"""
        return collections4.Bag.__wrap(__UnmodifiableBag.unmodifiableBag(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.add(E,int)"""
        return bool.__wrap(super(__UnmodifiableBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__UnmodifiableBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.UnmodifiableBag.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableBag, self).iterator())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.UnmodifiableBag.uniqueSet()"""
        return 'Set'.__wrap(super(UnmodifiableBag, self).uniqueSet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).removeAll(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.bag.UnmodifiableBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.bag.UnmodifiableBag as __UnmodifiableBag
__UnmodifiableBag = __UnmodifiableBag
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableBag(__AbstractBagDecorator, AbstractBagDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.bag.UnmodifiableBag"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableBag) -> 'UnmodifiableBag':
        return UnmodifiableBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableBag):
        """
        Dynamic initializer for UnmodifiableBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).removeIf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.add(E)"""
        return bool.__wrap(super(__UnmodifiableBag, self).add(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.UnmodifiableBag.clear()"""
        super(UnmodifiableBag, self).clear()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableBag, self).remove(arg0))

    @staticmethod
    @overload
    def unmodifiableBag(arg0: 'Bag') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.UnmodifiableBag.unmodifiableBag(org.apache.commons.collections4.Bag<? extends E>)"""
        return collections4.Bag.__wrap(__UnmodifiableBag.unmodifiableBag(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.add(E,int)"""
        return bool.__wrap(super(__UnmodifiableBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__UnmodifiableBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.UnmodifiableBag.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableBag, self).iterator())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.UnmodifiableBag.uniqueSet()"""
        return 'Set'.__wrap(super(UnmodifiableBag, self).uniqueSet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableBag, self).removeAll(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.bag.UnmodifiableBag 
 
 
# CLASS: org.apache.commons.collections4.bag.TransformedSortedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bag.TransformedSortedBag as __TransformedSortedBag
__TransformedSortedBag = __TransformedSortedBag
from builtins import bool
import org.apache.commons.collections4.collection.TransformedCollection as __TransformedCollection
__TransformedCollection = __TransformedCollection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import org.apache.commons.collections4.bag.TransformedBag as __TransformedBag
__TransformedBag = __TransformedBag
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TransformedSortedBag(__TransformedBag, TransformedBag, pyapache.__SortedBag, collections4.SortedBag):
    """org.apache.commons.collections4.bag.TransformedSortedBag"""
 
    @staticmethod
    def __wrap(java_value: __TransformedSortedBag) -> 'TransformedSortedBag':
        return TransformedSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedSortedBag):
        """
        Dynamic initializer for TransformedSortedBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).addAll(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.TransformedSortedBag.comparator()"""
        return 'Comparator'.__wrap(super(TransformedSortedBag, self).comparator())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.TransformedSortedBag.first()"""
        return object.__wrap(super(TransformedSortedBag, self).first())

    @staticmethod
    @overload
    def transformedSortedBag(arg0: 'SortedBag', arg1: 'Transformer') -> 'TransformedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.TransformedSortedBag<E> org.apache.commons.collections4.bag.TransformedSortedBag.transformedSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedBag.__wrap(__TransformedSortedBag.transformedSortedBag(arg0, arg1))

    @staticmethod
    @overload
    def transformedBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag.__wrap(__TransformedBag.transformedBag(arg0, arg1))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.add(E,int)"""
        return bool.__wrap(super(__TransformedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__TransformedBag, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.TransformedBag.uniqueSet()"""
        return 'Set'.__wrap(super(TransformedBag, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__TransformedBag, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def transformingBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformingBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag.__wrap(__TransformedBag.transformingBag(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformedBag, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.TransformedSortedBag.last()"""
        return object.__wrap(super(TransformedSortedBag, self).last())

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def transformingSortedBag(arg0: 'SortedBag', arg1: 'Transformer') -> 'TransformedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.TransformedSortedBag<E> org.apache.commons.collections4.bag.TransformedSortedBag.transformingSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedBag.__wrap(__TransformedSortedBag.transformingSortedBag(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformingCollection(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.hashCode()"""
        return int.__wrap(super(TransformedBag, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.bag.PredicatedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection_Builder
__Builder = __PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bag.PredicatedBag as __PredicatedBag
__PredicatedBag = __PredicatedBag
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection
__PredicatedCollection = __PredicatedCollection
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class PredicatedBag(collections4.__PredicatedCollection, collection.PredicatedCollection, pyapache.__Bag, collections4.Bag):
    """org.apache.commons.collections4.bag.PredicatedBag"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedBag) -> 'PredicatedBag':
        return PredicatedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedBag):
        """
        Dynamic initializer for PredicatedBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__PredicatedBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__PredicatedBag, self).getCount(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.add(E,int)"""
        return bool.__wrap(super(__PredicatedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder.__wrap(__PredicatedCollection.builder(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder.__wrap(__PredicatedCollection.notNullBuilder())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.PredicatedBag.uniqueSet()"""
        return 'Set'.__wrap(super(PredicatedBag, self).uniqueSet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def predicatedBag(arg0: 'Bag', arg1: 'Predicate') -> 'PredicatedBag':
        """public static <E> org.apache.commons.collections4.bag.PredicatedBag<E> org.apache.commons.collections4.bag.PredicatedBag.predicatedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedBag.__wrap(__PredicatedBag.predicatedBag(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).addAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedBag, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.hashCode()"""
        return int.__wrap(super(PredicatedBag, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection.__wrap(__PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractBagDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class AbstractBagDecorator(ABC, collections4.__AbstractCollectionDecorator, collection.AbstractCollectionDecorator, pyapache.__Bag, collections4.Bag):
    """org.apache.commons.collections4.bag.AbstractBagDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractBagDecorator) -> 'AbstractBagDecorator':
        return AbstractBagDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractBagDecorator):
        """
        Dynamic initializer for AbstractBagDecorator.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.add(E,int)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractBagDecorator, self).uniqueSet()) 
 
 
# CLASS: org.apache.commons.collections4.bag.HashBag
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bag.AbstractMapBag as __AbstractMapBag
__AbstractMapBag = __AbstractMapBag
from builtins import bool
import org.apache.commons.collections4.bag.HashBag as __HashBag
__HashBag = __HashBag
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class HashBag(__AbstractMapBag, AbstractMapBag, __Serializable, Serializable):
    """org.apache.commons.collections4.bag.HashBag"""
 
    @staticmethod
    def __wrap(java_value: __HashBag) -> 'HashBag':
        return HashBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashBag):
        """
        Dynamic initializer for HashBag.
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
    def size(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.size()"""
        return int.__wrap(super(AbstractMapBag, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).removeAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.AbstractMapBag.iterator()"""
        return 'Iterator'.__wrap(super(AbstractMapBag, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bag.HashBag()"""
        val = __HashBag()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractMapBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).remove(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E)"""
        return bool.__wrap(super(__AbstractMapBag, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.bag.AbstractMapBag.toArray(T[])"""
        return List[object].__wrap(super(__AbstractMapBag, self).toArray(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.AbstractMapBag.clear()"""
        super(AbstractMapBag, self).clear()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).retainAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).contains(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E,int)"""
        return bool.__wrap(super(__AbstractMapBag, self).add(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bag.HashBag()"""
        val = __HashBag()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractMapBag, self).addAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.isEmpty()"""
        return bool.__wrap(super(AbstractMapBag, self).isEmpty())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractMapBag.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMapBag, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMapBag, self).getCount(arg0))

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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.bag.AbstractMapBag.toArray()"""
        return List[object].__wrap(super(AbstractMapBag, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.hashCode()"""
        return int.__wrap(super(AbstractMapBag, self).hashCode())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bag.AbstractMapBag.toString()"""
        return str.__wrap(super(AbstractMapBag, self).toString())

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.bag.HashBag(java.util.Collection<? extends E>)"""
        val = __HashBag(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.bag.CollectionSortedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import org.apache.commons.collections4.SortedBag as __SortedBag
__SortedBag = __SortedBag
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.bag.CollectionSortedBag as __CollectionSortedBag
__CollectionSortedBag = __CollectionSortedBag
import java.lang.Integer as __int
import org.apache.commons.collections4.bag.AbstractSortedBagDecorator as __AbstractSortedBagDecorator
__AbstractSortedBagDecorator = __AbstractSortedBagDecorator
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class CollectionSortedBag(__AbstractSortedBagDecorator, AbstractSortedBagDecorator):
    """org.apache.commons.collections4.bag.CollectionSortedBag"""
 
    @staticmethod
    def __wrap(java_value: __CollectionSortedBag) -> 'CollectionSortedBag':
        return CollectionSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectionSortedBag):
        """
        Dynamic initializer for CollectionSortedBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CollectionSortedBag, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def __init__(self, arg0: 'SortedBag'):
        """public org.apache.commons.collections4.bag.CollectionSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        val = __CollectionSortedBag(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.AbstractSortedBagDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBagDecorator, self).comparator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.add(E,int)"""
        return bool.__wrap(super(__CollectionSortedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__CollectionSortedBag, self).remove(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CollectionSortedBag, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__CollectionSortedBag, self).addAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.first()"""
        return object.__wrap(super(AbstractSortedBagDecorator, self).first())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.last()"""
        return object.__wrap(super(AbstractSortedBagDecorator, self).last())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

    @staticmethod
    @overload
    def collectionSortedBag(arg0: 'SortedBag') -> 'collections4.SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.bag.CollectionSortedBag.collectionSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return collections4.SortedBag.__wrap(__CollectionSortedBag.collectionSortedBag(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CollectionSortedBag, self).retainAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionSortedBag.add(E)"""
        return bool.__wrap(super(__CollectionSortedBag, self).add(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractBagDecorator, self).uniqueSet()) 
 
 
# CLASS: org.apache.commons.collections4.bag.SynchronizedSortedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.SynchronizedSortedBag as __SynchronizedSortedBag
__SynchronizedSortedBag = __SynchronizedSortedBag
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.collection.SynchronizedCollection as __SynchronizedCollection
__SynchronizedCollection = __SynchronizedCollection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.bag.SynchronizedBag as __SynchronizedBag
__SynchronizedBag = __SynchronizedBag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SynchronizedSortedBag(__SynchronizedBag, SynchronizedBag, pyapache.__SortedBag, collections4.SortedBag):
    """org.apache.commons.collections4.bag.SynchronizedSortedBag"""
 
    @staticmethod
    def __wrap(java_value: __SynchronizedSortedBag) -> 'SynchronizedSortedBag':
        return SynchronizedSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SynchronizedSortedBag):
        """
        Dynamic initializer for SynchronizedSortedBag.
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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str.__wrap(super(collection.SynchronizedCollection, self).toString())

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'SynchronizedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedBag<E> org.apache.commons.collections4.bag.SynchronizedBag.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return SynchronizedBag.__wrap(__SynchronizedBag.synchronizedBag(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.SynchronizedCollection.clear()"""
        super(collection.SynchronizedCollection, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).containsAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object].__wrap(super(collection.SynchronizedCollection, self).toArray())

    @override
    @overload
    def last(self) -> object:
        """public synchronized E org.apache.commons.collections4.bag.SynchronizedSortedBag.last()"""
        return object.__wrap(super(SynchronizedSortedBag, self).last())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).remove(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).retainAll(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.SynchronizedCollection.iterator()"""
        return 'Iterator'.__wrap(super(collection.SynchronizedCollection, self).iterator())

    @staticmethod
    @overload
    def synchronizedSortedBag(arg0: 'SortedBag') -> 'SynchronizedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedSortedBag<E> org.apache.commons.collections4.bag.SynchronizedSortedBag.synchronizedSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return SynchronizedSortedBag.__wrap(__SynchronizedSortedBag.synchronizedSortedBag(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.SynchronizedBag.uniqueSet()"""
        return 'Set'.__wrap(super(SynchronizedBag, self).uniqueSet())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).removeIf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__SynchronizedBag, self).getCount(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__SynchronizedBag, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object].__wrap(super(__collection.SynchronizedCollection, self).toArray(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def first(self) -> object:
        """public synchronized E org.apache.commons.collections4.bag.SynchronizedSortedBag.first()"""
        return object.__wrap(super(SynchronizedSortedBag, self).first())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public synchronized java.util.Comparator<? super E> org.apache.commons.collections4.bag.SynchronizedSortedBag.comparator()"""
        return 'Comparator'.__wrap(super(SynchronizedSortedBag, self).comparator())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.add(E,int)"""
        return bool.__wrap(super(__SynchronizedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int.__wrap(super(collection.SynchronizedCollection, self).size())

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
    def synchronizedCollection(arg0: 'Collection') -> 'collection.SynchronizedCollection':
        """public static <T> org.apache.commons.collections4.collection.SynchronizedCollection<T> org.apache.commons.collections4.collection.SynchronizedCollection.synchronizedCollection(java.util.Collection<T>)"""
        return collection.SynchronizedCollection.__wrap(__SynchronizedCollection.synchronizedCollection(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.hashCode()"""
        return int.__wrap(super(SynchronizedBag, self).hashCode())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).addAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__SynchronizedBag, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.isEmpty()"""
        return bool.__wrap(super(collection.SynchronizedCollection, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractMapBag
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bag.AbstractMapBag as __AbstractMapBag
__AbstractMapBag = __AbstractMapBag
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class AbstractMapBag(ABC, pyapache.__Bag, collections4.Bag):
    """org.apache.commons.collections4.bag.AbstractMapBag"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMapBag) -> 'AbstractMapBag':
        return AbstractMapBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMapBag):
        """
        Dynamic initializer for AbstractMapBag.
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
    def size(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.size()"""
        return int.__wrap(super(AbstractMapBag, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).removeAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.AbstractMapBag.iterator()"""
        return 'Iterator'.__wrap(super(AbstractMapBag, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractMapBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).remove(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E)"""
        return bool.__wrap(super(__AbstractMapBag, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.bag.AbstractMapBag.toArray(T[])"""
        return List[object].__wrap(super(__AbstractMapBag, self).toArray(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.AbstractMapBag.clear()"""
        super(AbstractMapBag, self).clear()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).retainAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).contains(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E,int)"""
        return bool.__wrap(super(__AbstractMapBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractMapBag, self).addAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.isEmpty()"""
        return bool.__wrap(super(AbstractMapBag, self).isEmpty())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractMapBag.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMapBag, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMapBag, self).getCount(arg0))

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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.bag.AbstractMapBag.toArray()"""
        return List[object].__wrap(super(AbstractMapBag, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.hashCode()"""
        return int.__wrap(super(AbstractMapBag, self).hashCode())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bag.AbstractMapBag.toString()"""
        return str.__wrap(super(AbstractMapBag, self).toString()) 
 
 
# CLASS: org.apache.commons.collections4.bag.CollectionBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bag.CollectionBag as __CollectionBag
__CollectionBag = __CollectionBag
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class CollectionBag(__AbstractBagDecorator, AbstractBagDecorator):
    """org.apache.commons.collections4.bag.CollectionBag"""
 
    @staticmethod
    def __wrap(java_value: __CollectionBag) -> 'CollectionBag':
        return CollectionBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectionBag):
        """
        Dynamic initializer for CollectionBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @staticmethod
    @overload
    def collectionBag(arg0: 'Bag') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.CollectionBag.collectionBag(org.apache.commons.collections4.Bag<E>)"""
        return collections4.Bag.__wrap(__CollectionBag.collectionBag(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def __init__(self, arg0: 'Bag'):
        """public org.apache.commons.collections4.bag.CollectionBag(org.apache.commons.collections4.Bag<E>)"""
        val = __CollectionBag(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__CollectionBag, self).addAll(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CollectionBag, self).retainAll(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CollectionBag, self).removeAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.add(E)"""
        return bool.__wrap(super(__CollectionBag, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CollectionBag, self).containsAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__CollectionBag, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.CollectionBag.add(E,int)"""
        return bool.__wrap(super(__CollectionBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractBagDecorator, self).uniqueSet()) 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractSortedBagDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import org.apache.commons.collections4.bag.AbstractSortedBagDecorator as __AbstractSortedBagDecorator
__AbstractSortedBagDecorator = __AbstractSortedBagDecorator
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class AbstractSortedBagDecorator(ABC, __AbstractBagDecorator, AbstractBagDecorator, pyapache.__SortedBag, collections4.SortedBag):
    """org.apache.commons.collections4.bag.AbstractSortedBagDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSortedBagDecorator) -> 'AbstractSortedBagDecorator':
        return AbstractSortedBagDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSortedBagDecorator):
        """
        Dynamic initializer for AbstractSortedBagDecorator.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.AbstractSortedBagDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBagDecorator, self).comparator())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.add(E,int)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.first()"""
        return object.__wrap(super(AbstractSortedBagDecorator, self).first())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.last()"""
        return object.__wrap(super(AbstractSortedBagDecorator, self).last())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractBagDecorator.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractBagDecorator, self).uniqueSet()) 
 
 
# CLASS: org.apache.commons.collections4.bag.AbstractMapBag$MutableInteger
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.apache.commons.collections4.bag.AbstractMapBag as __AbstractMapBag_MutableInteger
__MutableInteger = __AbstractMapBag_MutableInteger.MutableInteger
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutableInteger():
    """org.apache.commons.collections4.bag.AbstractMapBag.MutableInteger"""
 
    @staticmethod
    def __wrap(java_value: __MutableInteger) -> 'MutableInteger':
        return MutableInteger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableInteger):
        """
        Dynamic initializer for MutableInteger.
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
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag$MutableInteger.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableInteger, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag$MutableInteger.hashCode()"""
        return int.__wrap(super(MutableInteger, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.bag.TreeBag
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bag.AbstractMapBag as __AbstractMapBag
__AbstractMapBag = __AbstractMapBag
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import org.apache.commons.collections4.bag.TreeBag as __TreeBag
__TreeBag = __TreeBag
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TreeBag(__AbstractMapBag, AbstractMapBag, pyapache.__SortedBag, collections4.SortedBag, __Serializable, Serializable):
    """org.apache.commons.collections4.bag.TreeBag"""
 
    @staticmethod
    def __wrap(java_value: __TreeBag) -> 'TreeBag':
        return TreeBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeBag):
        """
        Dynamic initializer for TreeBag.
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
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.bag.TreeBag(java.util.Collection<? extends E>)"""
        val = __TreeBag(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.size()"""
        return int.__wrap(super(AbstractMapBag, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).removeAll(arg0))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.TreeBag.first()"""
        return object.__wrap(super(TreeBag, self).first())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.AbstractMapBag.iterator()"""
        return 'Iterator'.__wrap(super(AbstractMapBag, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.TreeBag.add(E)"""
        return bool.__wrap(super(__TreeBag, self).add(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__AbstractMapBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).remove(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.bag.AbstractMapBag.toArray(T[])"""
        return List[object].__wrap(super(__AbstractMapBag, self).toArray(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.bag.TreeBag(java.util.Comparator<? super E>)"""
        val = __TreeBag(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bag.AbstractMapBag.clear()"""
        super(AbstractMapBag, self).clear()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMapBag, self).retainAll(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.TreeBag.comparator()"""
        return 'Comparator'.__wrap(super(TreeBag, self).comparator())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapBag, self).contains(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.add(E,int)"""
        return bool.__wrap(super(__AbstractMapBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractMapBag, self).addAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.TreeBag.last()"""
        return object.__wrap(super(TreeBag, self).last())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractMapBag.isEmpty()"""
        return bool.__wrap(super(AbstractMapBag, self).isEmpty())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.AbstractMapBag.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMapBag, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMapBag, self).getCount(arg0))

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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.bag.AbstractMapBag.toArray()"""
        return List[object].__wrap(super(AbstractMapBag, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractMapBag.hashCode()"""
        return int.__wrap(super(AbstractMapBag, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bag.TreeBag()"""
        val = __TreeBag()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bag.TreeBag()"""
        val = __TreeBag()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bag.AbstractMapBag.toString()"""
        return str.__wrap(super(AbstractMapBag, self).toString()) 
 
 
# CLASS: org.apache.commons.collections4.bag.UnmodifiableSortedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import org.apache.commons.collections4.bag.UnmodifiableSortedBag as __UnmodifiableSortedBag
__UnmodifiableSortedBag = __UnmodifiableSortedBag
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.bag.AbstractBagDecorator as __AbstractBagDecorator
__AbstractBagDecorator = __AbstractBagDecorator
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import org.apache.commons.collections4.SortedBag as __SortedBag
__SortedBag = __SortedBag
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import org.apache.commons.collections4.bag.AbstractSortedBagDecorator as __AbstractSortedBagDecorator
__AbstractSortedBagDecorator = __AbstractSortedBagDecorator
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableSortedBag(__AbstractSortedBagDecorator, AbstractSortedBagDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.bag.UnmodifiableSortedBag"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableSortedBag) -> 'UnmodifiableSortedBag':
        return UnmodifiableSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableSortedBag):
        """
        Dynamic initializer for UnmodifiableSortedBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).removeAll(arg0))

    @staticmethod
    @overload
    def unmodifiableSortedBag(arg0: 'SortedBag') -> 'collections4.SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.bag.UnmodifiableSortedBag.unmodifiableSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return collections4.SortedBag.__wrap(__UnmodifiableSortedBag.unmodifiableSortedBag(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.UnmodifiableSortedBag.uniqueSet()"""
        return 'Set'.__wrap(super(UnmodifiableSortedBag, self).uniqueSet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.AbstractSortedBagDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBagDecorator, self).comparator())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.add(E)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).add(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).addAll(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).remove(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractBagDecorator, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.add(E,int)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.first()"""
        return object.__wrap(super(AbstractSortedBagDecorator, self).first())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).retainAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.AbstractBagDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractBagDecorator, self).equals(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.AbstractSortedBagDecorator.last()"""
        return object.__wrap(super(AbstractSortedBagDecorator, self).last())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.AbstractBagDecorator.hashCode()"""
        return int.__wrap(super(AbstractBagDecorator, self).hashCode())

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
    def clear(self):
        """public void org.apache.commons.collections4.bag.UnmodifiableSortedBag.clear()"""
        super(UnmodifiableSortedBag, self).clear()

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.bag.UnmodifiableSortedBag.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableSortedBag, self).iterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bag.UnmodifiableSortedBag.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableSortedBag, self).removeIf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bag.SynchronizedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.collection.SynchronizedCollection as __SynchronizedCollection
__SynchronizedCollection = __SynchronizedCollection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.bag.SynchronizedBag as __SynchronizedBag
__SynchronizedBag = __SynchronizedBag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SynchronizedBag(collections4.__SynchronizedCollection, collection.SynchronizedCollection, pyapache.__Bag, collections4.Bag):
    """org.apache.commons.collections4.bag.SynchronizedBag"""
 
    @staticmethod
    def __wrap(java_value: __SynchronizedBag) -> 'SynchronizedBag':
        return SynchronizedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SynchronizedBag):
        """
        Dynamic initializer for SynchronizedBag.
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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str.__wrap(super(collection.SynchronizedCollection, self).toString())

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'SynchronizedBag':
        """public static <E> org.apache.commons.collections4.bag.SynchronizedBag<E> org.apache.commons.collections4.bag.SynchronizedBag.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return SynchronizedBag.__wrap(__SynchronizedBag.synchronizedBag(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.SynchronizedCollection.clear()"""
        super(collection.SynchronizedCollection, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).containsAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object].__wrap(super(collection.SynchronizedCollection, self).toArray())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).remove(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).retainAll(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.SynchronizedCollection.iterator()"""
        return 'Iterator'.__wrap(super(collection.SynchronizedCollection, self).iterator())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.SynchronizedBag.uniqueSet()"""
        return 'Set'.__wrap(super(SynchronizedBag, self).uniqueSet())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).removeIf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__SynchronizedBag, self).getCount(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__SynchronizedBag, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object].__wrap(super(__collection.SynchronizedCollection, self).toArray(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.add(E,int)"""
        return bool.__wrap(super(__SynchronizedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int.__wrap(super(collection.SynchronizedCollection, self).size())

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
    def synchronizedCollection(arg0: 'Collection') -> 'collection.SynchronizedCollection':
        """public static <T> org.apache.commons.collections4.collection.SynchronizedCollection<T> org.apache.commons.collections4.collection.SynchronizedCollection.synchronizedCollection(java.util.Collection<T>)"""
        return collection.SynchronizedCollection.__wrap(__SynchronizedCollection.synchronizedCollection(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.SynchronizedBag.hashCode()"""
        return int.__wrap(super(SynchronizedBag, self).hashCode())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).addAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.SynchronizedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__SynchronizedBag, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.isEmpty()"""
        return bool.__wrap(super(collection.SynchronizedCollection, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.bag.TransformedBag
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.collection.TransformedCollection as __TransformedCollection
__TransformedCollection = __TransformedCollection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.bag.TransformedBag as __TransformedBag
__TransformedBag = __TransformedBag
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TransformedBag(collections4.__TransformedCollection, collection.TransformedCollection, pyapache.__Bag, collections4.Bag):
    """org.apache.commons.collections4.bag.TransformedBag"""
 
    @staticmethod
    def __wrap(java_value: __TransformedBag) -> 'TransformedBag':
        return TransformedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedBag):
        """
        Dynamic initializer for TransformedBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).addAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @staticmethod
    @overload
    def transformedBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag.__wrap(__TransformedBag.transformedBag(arg0, arg1))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.add(E,int)"""
        return bool.__wrap(super(__TransformedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__TransformedBag, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.TransformedBag.uniqueSet()"""
        return 'Set'.__wrap(super(TransformedBag, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__TransformedBag, self).getCount(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def transformingBag(arg0: 'Bag', arg1: 'Transformer') -> 'collections4.Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.bag.TransformedBag.transformingBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collections4.Bag.__wrap(__TransformedBag.transformingBag(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.TransformedBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformedBag, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformingCollection(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.TransformedBag.hashCode()"""
        return int.__wrap(super(TransformedBag, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.bag.PredicatedSortedBag
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.bag.PredicatedSortedBag as __PredicatedSortedBag
__PredicatedSortedBag = __PredicatedSortedBag
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection_Builder
__Builder = __PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bag.PredicatedBag as __PredicatedBag
__PredicatedBag = __PredicatedBag
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection
__PredicatedCollection = __PredicatedCollection
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class PredicatedSortedBag(__PredicatedBag, PredicatedBag, pyapache.__SortedBag, collections4.SortedBag):
    """org.apache.commons.collections4.bag.PredicatedSortedBag"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedSortedBag) -> 'PredicatedSortedBag':
        return PredicatedSortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedSortedBag):
        """
        Dynamic initializer for PredicatedSortedBag.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.remove(java.lang.Object,int)"""
        return bool.__wrap(super(__PredicatedBag, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).add(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.bag.PredicatedSortedBag.last()"""
        return object.__wrap(super(PredicatedSortedBag, self).last())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.getCount(java.lang.Object)"""
        return int.__wrap(super(__PredicatedBag, self).getCount(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.bag.PredicatedSortedBag.comparator()"""
        return 'Comparator'.__wrap(super(PredicatedSortedBag, self).comparator())

    @staticmethod
    @overload
    def predicatedSortedBag(arg0: 'SortedBag', arg1: 'Predicate') -> 'PredicatedSortedBag':
        """public static <E> org.apache.commons.collections4.bag.PredicatedSortedBag<E> org.apache.commons.collections4.bag.PredicatedSortedBag.predicatedSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSortedBag.__wrap(__PredicatedSortedBag.predicatedSortedBag(arg0, arg1))

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.add(E,int)"""
        return bool.__wrap(super(__PredicatedBag, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.bag.PredicatedSortedBag.first()"""
        return object.__wrap(super(PredicatedSortedBag, self).first())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder.__wrap(__PredicatedCollection.builder(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder.__wrap(__PredicatedCollection.notNullBuilder())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.bag.PredicatedBag.uniqueSet()"""
        return 'Set'.__wrap(super(PredicatedBag, self).uniqueSet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def predicatedBag(arg0: 'Bag', arg1: 'Predicate') -> 'PredicatedBag':
        """public static <E> org.apache.commons.collections4.bag.PredicatedBag<E> org.apache.commons.collections4.bag.PredicatedBag.predicatedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedBag.__wrap(__PredicatedBag.predicatedBag(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).addAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bag.PredicatedBag.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedBag, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bag.PredicatedBag.hashCode()"""
        return int.__wrap(super(PredicatedBag, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection.__wrap(__PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()