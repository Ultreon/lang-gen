from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as __AbstractSortedSetDecorator
__AbstractSortedSetDecorator = __AbstractSortedSetDecorator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.set.UnmodifiableSortedSet as __UnmodifiableSortedSet
__UnmodifiableSortedSet = __UnmodifiableSortedSet
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableSortedSet(__AbstractSortedSetDecorator, AbstractSortedSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.set.UnmodifiableSortedSet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableSortedSet) -> 'UnmodifiableSortedSet':
        return UnmodifiableSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableSortedSet):
        """
        Dynamic initializer for UnmodifiableSortedSet.
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
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).remove(arg0))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).first())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'.__wrap(super(SortedSet, self).reversed())

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
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableSortedSet.clear()"""
        super(UnmodifiableSortedSet, self).clear()

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
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object.__wrap(super(SortedSet, self).removeLast())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableSortedSet, self).tailSet(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).last())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).retainAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @staticmethod
    @overload
    def unmodifiableSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.unmodifiableSortedSet(java.util.SortedSet<E>)"""
        return SortedSet.__wrap(__UnmodifiableSortedSet.unmodifiableSortedSet(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.add(E)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).removeAll(arg0))

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableSortedSet, self).subSet(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableSortedSet, self).headSet(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableSortedSet, self).iterator())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object.__wrap(super(SortedSet, self).removeFirst())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).removeIf(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedSetDecorator, self).comparator())

 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableSortedSet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as __AbstractSortedSetDecorator
__AbstractSortedSetDecorator = __AbstractSortedSetDecorator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.set.UnmodifiableSortedSet as __UnmodifiableSortedSet
__UnmodifiableSortedSet = __UnmodifiableSortedSet
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableSortedSet(__AbstractSortedSetDecorator, AbstractSortedSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.set.UnmodifiableSortedSet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableSortedSet) -> 'UnmodifiableSortedSet':
        return UnmodifiableSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableSortedSet):
        """
        Dynamic initializer for UnmodifiableSortedSet.
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
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).remove(arg0))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).first())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'.__wrap(super(SortedSet, self).reversed())

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
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableSortedSet.clear()"""
        super(UnmodifiableSortedSet, self).clear()

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
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object.__wrap(super(SortedSet, self).removeLast())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableSortedSet, self).tailSet(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).last())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).retainAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @staticmethod
    @overload
    def unmodifiableSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.unmodifiableSortedSet(java.util.SortedSet<E>)"""
        return SortedSet.__wrap(__UnmodifiableSortedSet.unmodifiableSortedSet(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.add(E)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).removeAll(arg0))

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableSortedSet, self).subSet(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableSortedSet, self).headSet(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableSortedSet, self).iterator())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object.__wrap(super(SortedSet, self).removeFirst())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableSortedSet, self).removeIf(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedSetDecorator, self).comparator())

 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableSortedSet 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractNavigableSetDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import java.lang.Boolean as __boolean
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
import java.util.NavigableSet as NavigableSet
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as __AbstractSortedSetDecorator
__AbstractSortedSetDecorator = __AbstractSortedSetDecorator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.NavigableSet as __NavigableSet
__NavigableSet = __NavigableSet
import org.apache.commons.collections4.set.AbstractNavigableSetDecorator as __AbstractNavigableSetDecorator
__AbstractNavigableSetDecorator = __AbstractNavigableSetDecorator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class AbstractNavigableSetDecorator(ABC, __AbstractSortedSetDecorator, AbstractSortedSetDecorator, __NavigableSet, NavigableSet):
    """org.apache.commons.collections4.set.AbstractNavigableSetDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractNavigableSetDecorator) -> 'AbstractNavigableSetDecorator':
        return AbstractNavigableSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractNavigableSetDecorator):
        """
        Dynamic initializer for AbstractNavigableSetDecorator.
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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.tailSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__AbstractNavigableSetDecorator, self).tailSet(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'.__wrap(super(NavigableSet, self).reversed())

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.headSet(E)"""
        return 'SortedSet'.__wrap(super(__AbstractSortedSetDecorator, self).headSet(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object.__wrap(super(NavigableSet, self).removeFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'.__wrap(super(__AbstractNavigableSetDecorator, self).subSet(arg0, __boolean.valueOf(arg1), arg2, __boolean.valueOf(arg3)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.headSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__AbstractNavigableSetDecorator, self).headSet(arg0, __boolean.valueOf(arg1)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollFirst()"""
        return object.__wrap(super(AbstractNavigableSetDecorator, self).pollFirst())

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollLast()"""
        return object.__wrap(super(AbstractNavigableSetDecorator, self).pollLast())

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.descendingSet()"""
        return 'NavigableSet'.__wrap(super(AbstractNavigableSetDecorator, self).descendingSet())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.ceiling(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).ceiling(arg0))

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.floor(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).floor(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedSetDecorator, self).comparator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).first())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__AbstractSortedSetDecorator, self).subSet(arg0, arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.higher(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).higher(arg0))

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
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).last())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__AbstractSortedSetDecorator, self).tailSet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.lower(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).lower(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object.__wrap(super(NavigableSet, self).removeLast())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.descendingIterator()"""
        return 'Iterator'.__wrap(super(AbstractNavigableSetDecorator, self).descendingIterator()) 
 
 
# CLASS: org.apache.commons.collections4.set.MapBackedSet
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
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
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.Map as Map
import org.apache.commons.collections4.set.MapBackedSet as __MapBackedSet
__MapBackedSet = __MapBackedSet
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MapBackedSet(__Set, Set, __Serializable, Serializable):
    """org.apache.commons.collections4.set.MapBackedSet"""
 
    @staticmethod
    def __wrap(java_value: __MapBackedSet) -> 'MapBackedSet':
        return MapBackedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapBackedSet):
        """
        Dynamic initializer for MapBackedSet.
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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__MapBackedSet, self).removeIf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.MapBackedSet.clear()"""
        super(MapBackedSet, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.MapBackedSet.hashCode()"""
        return int.__wrap(super(MapBackedSet, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__MapBackedSet, self).retainAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.MapBackedSet.toArray(T[])"""
        return List[object].__wrap(super(__MapBackedSet, self).toArray(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.MapBackedSet.toArray()"""
        return List[object].__wrap(super(MapBackedSet, self).toArray())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @staticmethod
    @overload
    def mapBackedSet(arg0: 'Map') -> 'MapBackedSet':
        """public static <E,V> org.apache.commons.collections4.set.MapBackedSet<E, V> org.apache.commons.collections4.set.MapBackedSet.mapBackedSet(java.util.Map<E, ? super V>)"""
        return MapBackedSet.__wrap(__MapBackedSet.mapBackedSet(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__MapBackedSet, self).addAll(arg0))

    @staticmethod
    @overload
    def mapBackedSet(arg0: 'Map', arg1: object) -> 'MapBackedSet':
        """public static <E,V> org.apache.commons.collections4.set.MapBackedSet<E, V> org.apache.commons.collections4.set.MapBackedSet.mapBackedSet(java.util.Map<E, ? super V>,V)"""
        return MapBackedSet.__wrap(__MapBackedSet.mapBackedSet(arg0, arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.add(E)"""
        return bool.__wrap(super(__MapBackedSet, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.MapBackedSet.iterator()"""
        return 'Iterator'.__wrap(super(MapBackedSet, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__MapBackedSet, self).containsAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__MapBackedSet, self).removeAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__MapBackedSet, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__MapBackedSet, self).contains(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.set.MapBackedSet.size()"""
        return int.__wrap(super(MapBackedSet, self).size())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__MapBackedSet, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.isEmpty()"""
        return bool.__wrap(super(MapBackedSet, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.set.TransformedSet
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
import org.apache.commons.collections4.set.TransformedSet as __TransformedSet
__TransformedSet = __TransformedSet
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
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TransformedSet(collections4.__TransformedCollection, collection.TransformedCollection, __Set, Set):
    """org.apache.commons.collections4.set.TransformedSet"""
 
    @staticmethod
    def __wrap(java_value: __TransformedSet) -> 'TransformedSet':
        return TransformedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedSet):
        """
        Dynamic initializer for TransformedSet.
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

    @staticmethod
    @overload
    def transformingSet(arg0: 'Set', arg1: 'Transformer') -> 'TransformedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSet<E> org.apache.commons.collections4.set.TransformedSet.transformingSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSet.__wrap(__TransformedSet.transformingSet(arg0, arg1))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.TransformedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformedSet, self).equals(arg0))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.TransformedSet.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set.__wrap(__TransformedSet.transformedSet(arg0, arg1))

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
        """public int org.apache.commons.collections4.set.TransformedSet.hashCode()"""
        return int.__wrap(super(TransformedSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.set.TransformedSortedSet
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
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
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
import org.apache.commons.collections4.set.TransformedSortedSet as __TransformedSortedSet
__TransformedSortedSet = __TransformedSortedSet
import org.apache.commons.collections4.set.TransformedSet as __TransformedSet
__TransformedSet = __TransformedSet
import java.util.Set as __Set
__Set = __Set
import java.util.SortedSet as SortedSet
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
 
class TransformedSortedSet(__TransformedSet, TransformedSet, __SortedSet, SortedSet):
    """org.apache.commons.collections4.set.TransformedSortedSet"""
 
    @staticmethod
    def __wrap(java_value: __TransformedSortedSet) -> 'TransformedSortedSet':
        return TransformedSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedSortedSet):
        """
        Dynamic initializer for TransformedSortedSet.
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

    @staticmethod
    @overload
    def transformingSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformingSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet.__wrap(__TransformedSortedSet.transformingSortedSet(arg0, arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.last()"""
        return object.__wrap(super(TransformedSortedSet, self).last())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__TransformedSortedSet, self).subSet(arg0, arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @staticmethod
    @overload
    def transformingSet(arg0: 'Set', arg1: 'Transformer') -> 'TransformedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSet<E> org.apache.commons.collections4.set.TransformedSet.transformingSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSet.__wrap(__TransformedSet.transformingSet(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'.__wrap(super(SortedSet, self).reversed())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object.__wrap(super(SortedSet, self).removeLast())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.TransformedSortedSet.comparator()"""
        return 'Comparator'.__wrap(super(TransformedSortedSet, self).comparator())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__TransformedSortedSet, self).headSet(arg0))

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
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__TransformedSortedSet, self).tailSet(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.first()"""
        return object.__wrap(super(TransformedSortedSet, self).first())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.TransformedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformedSet, self).equals(arg0))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object.__wrap(super(SortedSet, self).removeFirst())

    @staticmethod
    @overload
    def transformedSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet.__wrap(__TransformedSortedSet.transformedSortedSet(arg0, arg1))

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.TransformedSet.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set.__wrap(__TransformedSet.transformedSet(arg0, arg1))

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
        """public int org.apache.commons.collections4.set.TransformedSet.hashCode()"""
        return int.__wrap(super(TransformedSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableNavigableSet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import java.lang.Boolean as __boolean
from builtins import type
import org.apache.commons.collections4.set.UnmodifiableNavigableSet as __UnmodifiableNavigableSet
__UnmodifiableNavigableSet = __UnmodifiableNavigableSet
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.NavigableSet as NavigableSet
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as __AbstractSortedSetDecorator
__AbstractSortedSetDecorator = __AbstractSortedSetDecorator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.NavigableSet as __NavigableSet
__NavigableSet = __NavigableSet
import org.apache.commons.collections4.set.AbstractNavigableSetDecorator as __AbstractNavigableSetDecorator
__AbstractNavigableSetDecorator = __AbstractNavigableSetDecorator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableNavigableSet(__AbstractNavigableSetDecorator, AbstractNavigableSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.set.UnmodifiableNavigableSet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableNavigableSet) -> 'UnmodifiableNavigableSet':
        return UnmodifiableNavigableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableNavigableSet):
        """
        Dynamic initializer for UnmodifiableNavigableSet.
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
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableNavigableSet.clear()"""
        super(UnmodifiableNavigableSet, self).clear()

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
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'.__wrap(super(NavigableSet, self).reversed())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableNavigableSet, self).addAll(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object.__wrap(super(NavigableSet, self).removeFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.descendingIterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableNavigableSet, self).descendingIterator())

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableNavigableSet, self).headSet(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableNavigableSet, self).removeAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @staticmethod
    @overload
    def unmodifiableNavigableSet(arg0: 'NavigableSet') -> 'NavigableSet':
        """public static <E> java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.unmodifiableNavigableSet(java.util.NavigableSet<E>)"""
        return NavigableSet.__wrap(__UnmodifiableNavigableSet.unmodifiableNavigableSet(arg0))

    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.tailSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__UnmodifiableNavigableSet, self).tailSet(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollFirst()"""
        return object.__wrap(super(AbstractNavigableSetDecorator, self).pollFirst())

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollLast()"""
        return object.__wrap(super(AbstractNavigableSetDecorator, self).pollLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableNavigableSet, self).iterator())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableNavigableSet, self).subSet(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableNavigableSet, self).remove(arg0))

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.ceiling(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).ceiling(arg0))

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.floor(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).floor(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedSetDecorator, self).comparator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableNavigableSet, self).removeIf(arg0))

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.descendingSet()"""
        return 'NavigableSet'.__wrap(super(UnmodifiableNavigableSet, self).descendingSet())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).first())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__UnmodifiableNavigableSet, self).tailSet(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.higher(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).higher(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).last())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.headSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__UnmodifiableNavigableSet, self).headSet(arg0, __boolean.valueOf(arg1)))

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.lower(E)"""
        return object.__wrap(super(__AbstractNavigableSetDecorator, self).lower(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableNavigableSet, self).retainAll(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object.__wrap(super(NavigableSet, self).removeLast())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.add(E)"""
        return bool.__wrap(super(__UnmodifiableNavigableSet, self).add(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'.__wrap(super(__UnmodifiableNavigableSet, self).subSet(arg0, __boolean.valueOf(arg1), arg2, __boolean.valueOf(arg3))) 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractSortedSetDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as __AbstractSortedSetDecorator
__AbstractSortedSetDecorator = __AbstractSortedSetDecorator
import java.util.Comparator as Comparator
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
 
class AbstractSortedSetDecorator(ABC, __AbstractSetDecorator, AbstractSetDecorator, __SortedSet, SortedSet):
    """org.apache.commons.collections4.set.AbstractSortedSetDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSortedSetDecorator) -> 'AbstractSortedSetDecorator':
        return AbstractSortedSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSortedSetDecorator):
        """
        Dynamic initializer for AbstractSortedSetDecorator.
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

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).first())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__AbstractSortedSetDecorator, self).subSet(arg0, arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'.__wrap(super(SortedSet, self).reversed())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object.__wrap(super(SortedSet, self).removeLast())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object.__wrap(super(AbstractSortedSetDecorator, self).last())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__AbstractSortedSetDecorator, self).tailSet(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.headSet(E)"""
        return 'SortedSet'.__wrap(super(__AbstractSortedSetDecorator, self).headSet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

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
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

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

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

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

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object.__wrap(super(SortedSet, self).removeFirst())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedSetDecorator, self).comparator()) 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractSerializableSetDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
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
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
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
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.set.AbstractSerializableSetDecorator as __AbstractSerializableSetDecorator
__AbstractSerializableSetDecorator = __AbstractSerializableSetDecorator
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class AbstractSerializableSetDecorator(ABC, __AbstractSetDecorator, AbstractSetDecorator):
    """org.apache.commons.collections4.set.AbstractSerializableSetDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSerializableSetDecorator) -> 'AbstractSerializableSetDecorator':
        return AbstractSerializableSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSerializableSetDecorator):
        """
        Dynamic initializer for AbstractSerializableSetDecorator.
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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractSetDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
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
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
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
 
class AbstractSetDecorator(ABC, collections4.__AbstractCollectionDecorator, collection.AbstractCollectionDecorator, __Set, Set):
    """org.apache.commons.collections4.set.AbstractSetDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSetDecorator) -> 'AbstractSetDecorator':
        return AbstractSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSetDecorator):
        """
        Dynamic initializer for AbstractSetDecorator.
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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableSet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
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
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.set.UnmodifiableSet as __UnmodifiableSet
__UnmodifiableSet = __UnmodifiableSet
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
 
class UnmodifiableSet(__AbstractSerializableSetDecorator, AbstractSerializableSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.set.UnmodifiableSet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableSet) -> 'UnmodifiableSet':
        return UnmodifiableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableSet):
        """
        Dynamic initializer for UnmodifiableSet.
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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableSet.clear()"""
        super(UnmodifiableSet, self).clear()

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def unmodifiableSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.UnmodifiableSet.unmodifiableSet(java.util.Set<? extends E>)"""
        return Set.__wrap(__UnmodifiableSet.unmodifiableSet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSet, self).removeAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.add(E)"""
        return bool.__wrap(super(__UnmodifiableSet, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableSet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableSet, self).iterator())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableSet, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableSet, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableSet, self).retainAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

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
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableSet, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.CompositeSet$SetMutator
import java.util.Set as Set
import java.util.Collection as Collection
import org.apache.commons.collections4.set.CompositeSet as __CompositeSet_SetMutator
__SetMutator = __CompositeSet_SetMutator.SetMutator
from abc import abstractmethod, ABC
import java.util.List as List
 
class SetMutator(ABC, __Serializable, Serializable):
    """org.apache.commons.collections4.set.CompositeSet.SetMutator"""
 
    @staticmethod
    def __wrap(java_value: __SetMutator) -> 'SetMutator':
        return SetMutator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetMutator):
        """
        Dynamic initializer for SetMutator.
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
    def addAll(self, arg0: 'CompositeSet', arg1: 'List', arg2: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.set.CompositeSet$SetMutator.addAll(org.apache.commons.collections4.set.CompositeSet<E>,java.util.List<java.util.Set<E>>,java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: 'CompositeSet', arg1: 'List', arg2: object):
        """public abstract boolean org.apache.commons.collections4.set.CompositeSet$SetMutator.add(org.apache.commons.collections4.set.CompositeSet<E>,java.util.List<java.util.Set<E>>,E)"""
        pass

    @abstractmethod
    def resolveCollision(self, arg0: 'CompositeSet', arg1: 'Set', arg2: 'Set', arg3: 'Collection'):
        """public abstract void org.apache.commons.collections4.set.CompositeSet$SetMutator.resolveCollision(org.apache.commons.collections4.set.CompositeSet<E>,java.util.Set<E>,java.util.Set<E>,java.util.Collection<E>)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.set.TransformedNavigableSet
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import java.lang.Boolean as __boolean
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.set.TransformedNavigableSet as __TransformedNavigableSet
__TransformedNavigableSet = __TransformedNavigableSet
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.collection.TransformedCollection as __TransformedCollection
__TransformedCollection = __TransformedCollection
from builtins import str
import java.util.NavigableSet as NavigableSet
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.set.TransformedSortedSet as __TransformedSortedSet
__TransformedSortedSet = __TransformedSortedSet
import org.apache.commons.collections4.set.TransformedSet as __TransformedSet
__TransformedSet = __TransformedSet
import java.util.Set as __Set
__Set = __Set
import java.util.SortedSet as SortedSet
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
import java.util.NavigableSet as __NavigableSet
__NavigableSet = __NavigableSet
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TransformedNavigableSet(__TransformedSortedSet, TransformedSortedSet, __NavigableSet, NavigableSet):
    """org.apache.commons.collections4.set.TransformedNavigableSet"""
 
    @staticmethod
    def __wrap(java_value: __TransformedNavigableSet) -> 'TransformedNavigableSet':
        return TransformedNavigableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedNavigableSet):
        """
        Dynamic initializer for TransformedNavigableSet.
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
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.tailSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__TransformedNavigableSet, self).tailSet(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @staticmethod
    @overload
    def transformingSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformingSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet.__wrap(__TransformedSortedSet.transformingSortedSet(arg0, arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).add(arg0))

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.lower(E)"""
        return object.__wrap(super(__TransformedNavigableSet, self).lower(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.last()"""
        return object.__wrap(super(TransformedSortedSet, self).last())

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
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.TransformedSortedSet.comparator()"""
        return 'Comparator'.__wrap(super(TransformedSortedSet, self).comparator())

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.headSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__TransformedNavigableSet, self).headSet(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'.__wrap(super(NavigableSet, self).reversed())

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__TransformedSortedSet, self).headSet(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @staticmethod
    @overload
    def transformingNavigableSet(arg0: 'NavigableSet', arg1: 'Transformer') -> 'TransformedNavigableSet':
        """public static <E> org.apache.commons.collections4.set.TransformedNavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.transformingNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedNavigableSet.__wrap(__TransformedNavigableSet.transformingNavigableSet(arg0, arg1))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object.__wrap(super(NavigableSet, self).removeFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'.__wrap(super(__TransformedNavigableSet, self).subSet(arg0, __boolean.valueOf(arg1), arg2, __boolean.valueOf(arg3)))

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.descendingSet()"""
        return 'NavigableSet'.__wrap(super(TransformedNavigableSet, self).descendingSet())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.TransformedNavigableSet.descendingIterator()"""
        return 'Iterator'.__wrap(super(TransformedNavigableSet, self).descendingIterator())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.first()"""
        return object.__wrap(super(TransformedSortedSet, self).first())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.pollLast()"""
        return object.__wrap(super(TransformedNavigableSet, self).pollLast())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.TransformedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformedSet, self).equals(arg0))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformedCollection(arg0, arg1))

    @staticmethod
    @overload
    def transformedSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet.__wrap(__TransformedSortedSet.transformedSortedSet(arg0, arg1))

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.TransformedSet.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set.__wrap(__TransformedSet.transformedSet(arg0, arg1))

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
        """public int org.apache.commons.collections4.set.TransformedSet.hashCode()"""
        return int.__wrap(super(TransformedSet, self).hashCode())

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
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__TransformedSortedSet, self).subSet(arg0, arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @staticmethod
    @overload
    def transformingSet(arg0: 'Set', arg1: 'Transformer') -> 'TransformedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSet<E> org.apache.commons.collections4.set.TransformedSet.transformingSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSet.__wrap(__TransformedSet.transformingSet(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.pollFirst()"""
        return object.__wrap(super(TransformedNavigableSet, self).pollFirst())

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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @staticmethod
    @overload
    def transformedNavigableSet(arg0: 'NavigableSet', arg1: 'Transformer') -> 'TransformedNavigableSet':
        """public static <E> org.apache.commons.collections4.set.TransformedNavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.transformedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedNavigableSet.__wrap(__TransformedNavigableSet.transformedNavigableSet(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__TransformedSortedSet, self).tailSet(arg0))

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.ceiling(E)"""
        return object.__wrap(super(__TransformedNavigableSet, self).ceiling(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.floor(E)"""
        return object.__wrap(super(__TransformedNavigableSet, self).floor(arg0))

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
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object.__wrap(super(NavigableSet, self).removeLast())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.higher(E)"""
        return object.__wrap(super(__TransformedNavigableSet, self).higher(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.PredicatedNavigableSet
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection_Builder
__Builder = __PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import java.lang.Boolean as __boolean
import org.apache.commons.collections4.set.PredicatedSet as __PredicatedSet
__PredicatedSet = __PredicatedSet
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.set.PredicatedNavigableSet as __PredicatedNavigableSet
__PredicatedNavigableSet = __PredicatedNavigableSet
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = __import_once__("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.PredicatedSortedSet as __PredicatedSortedSet
__PredicatedSortedSet = __PredicatedSortedSet
from builtins import bool
from builtins import str
import java.util.NavigableSet as NavigableSet
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
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
import java.util.NavigableSet as __NavigableSet
__NavigableSet = __NavigableSet
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
 
class PredicatedNavigableSet(__PredicatedSortedSet, PredicatedSortedSet, __NavigableSet, NavigableSet):
    """org.apache.commons.collections4.set.PredicatedNavigableSet"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedNavigableSet) -> 'PredicatedNavigableSet':
        return PredicatedNavigableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedNavigableSet):
        """
        Dynamic initializer for PredicatedNavigableSet.
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

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__PredicatedSortedSet, self).headSet(arg0))

    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.pollFirst()"""
        return object.__wrap(super(PredicatedNavigableSet, self).pollFirst())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.PredicatedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedSet, self).equals(arg0))

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
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.floor(E)"""
        return object.__wrap(super(__PredicatedNavigableSet, self).floor(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.lower(E)"""
        return object.__wrap(super(__PredicatedNavigableSet, self).lower(arg0))

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
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.higher(E)"""
        return object.__wrap(super(__PredicatedNavigableSet, self).higher(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'.__wrap(super(NavigableSet, self).reversed())

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'.__wrap(super(__PredicatedNavigableSet, self).subSet(arg0, __boolean.valueOf(arg1), arg2, __boolean.valueOf(arg3)))

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__PredicatedSortedSet, self).tailSet(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object.__wrap(super(NavigableSet, self).removeFirst())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.descendingSet()"""
        return 'NavigableSet'.__wrap(super(PredicatedNavigableSet, self).descendingSet())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).addAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'.__wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.PredicatedNavigableSet.descendingIterator()"""
        return 'Iterator'.__wrap(super(PredicatedNavigableSet, self).descendingIterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.PredicatedSortedSet.comparator()"""
        return 'Comparator'.__wrap(super(PredicatedSortedSet, self).comparator())

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.tailSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__PredicatedNavigableSet, self).tailSet(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.PredicatedSet.hashCode()"""
        return int.__wrap(super(PredicatedSet, self).hashCode())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__PredicatedSortedSet, self).subSet(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.pollLast()"""
        return object.__wrap(super(PredicatedNavigableSet, self).pollLast())

    @staticmethod
    @overload
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'PredicatedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSet<E> org.apache.commons.collections4.set.PredicatedSet.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSet.__wrap(__PredicatedSet.predicatedSet(arg0, arg1))

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder.__wrap(__PredicatedCollection.builder(arg0))

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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.headSet(E,boolean)"""
        return 'NavigableSet'.__wrap(super(__PredicatedNavigableSet, self).headSet(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def predicatedSortedSet(arg0: 'SortedSet', arg1: 'Predicate') -> 'PredicatedSortedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.predicatedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSortedSet.__wrap(__PredicatedSortedSet.predicatedSortedSet(arg0, arg1))

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.ceiling(E)"""
        return object.__wrap(super(__PredicatedNavigableSet, self).ceiling(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.last()"""
        return object.__wrap(super(PredicatedSortedSet, self).last())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def predicatedNavigableSet(arg0: 'NavigableSet', arg1: 'Predicate') -> 'PredicatedNavigableSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedNavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.predicatedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedNavigableSet.__wrap(__PredicatedNavigableSet.predicatedNavigableSet(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object.__wrap(super(NavigableSet, self).removeLast())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.first()"""
        return object.__wrap(super(PredicatedSortedSet, self).first())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection.__wrap(__PredicatedCollection.predicatedCollection(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.set.PredicatedSortedSet
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection_Builder
__Builder = __PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.set.PredicatedSet as __PredicatedSet
__PredicatedSet = __PredicatedSet
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
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.PredicatedSortedSet as __PredicatedSortedSet
__PredicatedSortedSet = __PredicatedSortedSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.SortedSet as SortedSet
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
 
class PredicatedSortedSet(__PredicatedSet, PredicatedSet, __SortedSet, SortedSet):
    """org.apache.commons.collections4.set.PredicatedSortedSet"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedSortedSet) -> 'PredicatedSortedSet':
        return PredicatedSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedSortedSet):
        """
        Dynamic initializer for PredicatedSortedSet.
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
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.headSet(E)"""
        return 'SortedSet'.__wrap(super(__PredicatedSortedSet, self).headSet(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.PredicatedSet.hashCode()"""
        return int.__wrap(super(PredicatedSet, self).hashCode())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.PredicatedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedSet, self).equals(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'.__wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.subSet(E,E)"""
        return 'SortedSet'.__wrap(super(__PredicatedSortedSet, self).subSet(arg0, arg1))

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'.__wrap(super(SortedSet, self).reversed())

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
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'PredicatedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSet<E> org.apache.commons.collections4.set.PredicatedSet.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSet.__wrap(__PredicatedSet.predicatedSet(arg0, arg1))

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

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object.__wrap(super(SortedSet, self).removeLast())

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
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(__SortedSet, self).addLast(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object.__wrap(super(SortedSet, self).getLast())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.tailSet(E)"""
        return 'SortedSet'.__wrap(super(__PredicatedSortedSet, self).tailSet(arg0))

    @staticmethod
    @overload
    def predicatedSortedSet(arg0: 'SortedSet', arg1: 'Predicate') -> 'PredicatedSortedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.predicatedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSortedSet.__wrap(__PredicatedSortedSet.predicatedSortedSet(arg0, arg1))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.last()"""
        return object.__wrap(super(PredicatedSortedSet, self).last())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object.__wrap(super(SortedSet, self).getFirst())

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

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(__SortedSet, self).addFirst(arg0)

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

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.first()"""
        return object.__wrap(super(PredicatedSortedSet, self).first())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.PredicatedSortedSet.comparator()"""
        return 'Comparator'.__wrap(super(PredicatedSortedSet, self).comparator())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object.__wrap(super(SortedSet, self).removeFirst())

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
 
 
# CLASS: org.apache.commons.collections4.set.PredicatedSet
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection_Builder
__Builder = __PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.set.PredicatedSet as __PredicatedSet
__PredicatedSet = __PredicatedSet
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
 
class PredicatedSet(collections4.__PredicatedCollection, collection.PredicatedCollection, __Set, Set):
    """org.apache.commons.collections4.set.PredicatedSet"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedSet) -> 'PredicatedSet':
        return PredicatedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedSet):
        """
        Dynamic initializer for PredicatedSet.
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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.PredicatedSet.hashCode()"""
        return int.__wrap(super(PredicatedSet, self).hashCode())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.PredicatedSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedSet, self).equals(arg0))

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
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'PredicatedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSet<E> org.apache.commons.collections4.set.PredicatedSet.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSet.__wrap(__PredicatedSet.predicatedSet(arg0, arg1))

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

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
 
 
# CLASS: org.apache.commons.collections4.set.CompositeSet
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.set.CompositeSet as __CompositeSet
__CompositeSet = __CompositeSet
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
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
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class CompositeSet(__Set, Set, __Serializable, Serializable):
    """org.apache.commons.collections4.set.CompositeSet"""
 
    @staticmethod
    def __wrap(java_value: __CompositeSet) -> 'CompositeSet':
        return CompositeSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CompositeSet):
        """
        Dynamic initializer for CompositeSet.
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.CompositeSet.iterator()"""
        return 'Iterator'.__wrap(super(CompositeSet, self).iterator())

    @overload
    def __init__(self, *arg0: 'Set'):
        """public org.apache.commons.collections4.set.CompositeSet(java.util.Set<E>...)"""
        val = __CompositeSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.set.CompositeSet.size()"""
        return int.__wrap(super(CompositeSet, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CompositeSet, self).removeAll(arg0))

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__CompositeSet, self).remove(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.set.CompositeSet()"""
        val = __CompositeSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.set.CompositeSet()"""
        val = __CompositeSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.add(E)"""
        return bool.__wrap(super(__CompositeSet, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.CompositeSet.hashCode()"""
        return int.__wrap(super(CompositeSet, self).hashCode())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.CompositeSet.clear()"""
        super(CompositeSet, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.isEmpty()"""
        return bool.__wrap(super(CompositeSet, self).isEmpty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def __init__(self, arg0: 'Set'):
        """public org.apache.commons.collections4.set.CompositeSet(java.util.Set<E>)"""
        val = __CompositeSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__CompositeSet, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CompositeSet, self).retainAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addComposited(self, arg0: 'Set'):
        """public synchronized void org.apache.commons.collections4.set.CompositeSet.addComposited(java.util.Set<E>)"""
        super(__CompositeSet, self).addComposited(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.set.CompositeSet.toSet()"""
        return 'Set'.__wrap(super(CompositeSet, self).toSet())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__CompositeSet, self).contains(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.CompositeSet.toArray(T[])"""
        return List[object].__wrap(super(__CompositeSet, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__CompositeSet, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def addComposited(self, *arg0: 'Set'):
        """public void org.apache.commons.collections4.set.CompositeSet.addComposited(java.util.Set<E>...)"""
        super(__CompositeSet, self).addComposited(arg0)

    @overload
    def removeComposited(self, arg0: 'Set'):
        """public void org.apache.commons.collections4.set.CompositeSet.removeComposited(java.util.Set<E>)"""
        super(__CompositeSet, self).removeComposited(arg0)

    @overload
    def addComposited(self, arg0: 'Set', arg1: 'Set'):
        """public void org.apache.commons.collections4.set.CompositeSet.addComposited(java.util.Set<E>,java.util.Set<E>)"""
        super(__CompositeSet, self).addComposited(arg0, arg1)

    @overload
    def setMutator(self, arg0: 'SetMutator'):
        """public void org.apache.commons.collections4.set.CompositeSet.setMutator(org.apache.commons.collections4.set.CompositeSet$SetMutator<E>)"""
        super(__CompositeSet, self).setMutator(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.CompositeSet.toArray()"""
        return List[object].__wrap(super(CompositeSet, self).toArray())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__CompositeSet, self).containsAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__CompositeSet, self).removeIf(arg0))

    @overload
    def getSets(self) -> 'List':
        """public java.util.List<java.util.Set<E>> org.apache.commons.collections4.set.CompositeSet.getSets()"""
        return 'List'.__wrap(super(CompositeSet, self).getSets()) 
 
 
# CLASS: org.apache.commons.collections4.set.ListOrderedSet
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.OrderedIterator as __OrderedIterator
__OrderedIterator = __OrderedIterator
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
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
import org.apache.commons.collections4.set.ListOrderedSet as __ListOrderedSet
__ListOrderedSet = __ListOrderedSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ListOrderedSet(__AbstractSerializableSetDecorator, AbstractSerializableSetDecorator):
    """org.apache.commons.collections4.set.ListOrderedSet"""
 
    @staticmethod
    def __wrap(java_value: __ListOrderedSet) -> 'ListOrderedSet':
        return ListOrderedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListOrderedSet):
        """
        Dynamic initializer for ListOrderedSet.
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
    def asList(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.set.ListOrderedSet.asList()"""
        return 'List'.__wrap(super(ListOrderedSet, self).asList())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.ListOrderedSet.clear()"""
        super(ListOrderedSet, self).clear()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @staticmethod
    @overload
    def listOrderedSet(arg0: 'Set') -> 'ListOrderedSet':
        """public static <E> org.apache.commons.collections4.set.ListOrderedSet<E> org.apache.commons.collections4.set.ListOrderedSet.listOrderedSet(java.util.Set<E>)"""
        return ListOrderedSet.__wrap(__ListOrderedSet.listOrderedSet(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.set.ListOrderedSet.get(int)"""
        return object.__wrap(super(__ListOrderedSet, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'collections4.OrderedIterator':
        """public org.apache.commons.collections4.OrderedIterator<E> org.apache.commons.collections4.set.ListOrderedSet.iterator()"""
        return 'collections4.OrderedIterator'.__wrap(super(ListOrderedSet, self).iterator())

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
    def __init__(self, ):
        """public org.apache.commons.collections4.set.ListOrderedSet()"""
        val = __ListOrderedSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ListOrderedSet, self).retainAll(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.set.ListOrderedSet.indexOf(java.lang.Object)"""
        return int.__wrap(super(__ListOrderedSet, self).indexOf(arg0))

    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.set.ListOrderedSet.add(int,E)"""
        super(__ListOrderedSet, self).add(__int.valueOf(arg0), arg1)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__ListOrderedSet, self).remove(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.set.ListOrderedSet()"""
        val = __ListOrderedSet()
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
        """public java.lang.String org.apache.commons.collections4.set.ListOrderedSet.toString()"""
        return str.__wrap(super(ListOrderedSet, self).toString())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.add(E)"""
        return bool.__wrap(super(__ListOrderedSet, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.ListOrderedSet.toArray()"""
        return List[object].__wrap(super(ListOrderedSet, self).toArray())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__ListOrderedSet, self).removeIf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def listOrderedSet(arg0: 'List') -> 'ListOrderedSet':
        """public static <E> org.apache.commons.collections4.set.ListOrderedSet<E> org.apache.commons.collections4.set.ListOrderedSet.listOrderedSet(java.util.List<E>)"""
        return ListOrderedSet.__wrap(__ListOrderedSet.listOrderedSet(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.ListOrderedSet.toArray(T[])"""
        return List[object].__wrap(super(__ListOrderedSet, self).toArray(arg0))

    @staticmethod
    @overload
    def listOrderedSet(arg0: 'Set', arg1: 'List') -> 'ListOrderedSet':
        """public static <E> org.apache.commons.collections4.set.ListOrderedSet<E> org.apache.commons.collections4.set.ListOrderedSet.listOrderedSet(java.util.Set<E>,java.util.List<E>)"""
        return ListOrderedSet.__wrap(__ListOrderedSet.listOrderedSet(arg0, arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.set.ListOrderedSet.remove(int)"""
        return object.__wrap(super(__ListOrderedSet, self).remove(__int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ListOrderedSet, self).addAll(__int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ListOrderedSet, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ListOrderedSet, self).addAll(arg0))