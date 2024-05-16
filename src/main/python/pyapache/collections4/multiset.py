from __future__ import annotations
from overload import overload


 
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
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
from builtins import bool
import java.util.AbstractSet as __AbstractSet
__AbstractSet = __AbstractSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet_UniqueSet
__UniqueSet = __AbstractMultiSet_UniqueSet.UniqueSet
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
 
class UniqueSet(__AbstractSet, AbstractSet):
    """org.apache.commons.collections4.multiset.AbstractMultiSet.UniqueSet"""
 
    @staticmethod
    def __wrap(java_value: __UniqueSet) -> 'UniqueSet':
        return UniqueSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniqueSet):
        """
        Dynamic initializer for UniqueSet.
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
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.clear()"""
        super(UniqueSet, self).clear()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool.__wrap(super(__AbstractCollection, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UniqueSet, self).containsAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UniqueSet, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.iterator()"""
        return 'Iterator'.__wrap(super(UniqueSet, self).iterator())

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
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__UniqueSet, self).contains(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.size()"""
        return int.__wrap(super(UniqueSet, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet
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
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
from builtins import bool
import java.util.AbstractSet as __AbstractSet
__AbstractSet = __AbstractSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet_UniqueSet
__UniqueSet = __AbstractMultiSet_UniqueSet.UniqueSet
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
 
class UniqueSet(__AbstractSet, AbstractSet):
    """org.apache.commons.collections4.multiset.AbstractMultiSet.UniqueSet"""
 
    @staticmethod
    def __wrap(java_value: __UniqueSet) -> 'UniqueSet':
        return UniqueSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniqueSet):
        """
        Dynamic initializer for UniqueSet.
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
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.clear()"""
        super(UniqueSet, self).clear()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool.__wrap(super(__AbstractCollection, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UniqueSet, self).containsAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UniqueSet, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.iterator()"""
        return 'Iterator'.__wrap(super(UniqueSet, self).iterator())

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
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__UniqueSet, self).contains(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.size()"""
        return int.__wrap(super(UniqueSet, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet_AbstractEntry
__AbstractEntry = __AbstractMultiSet_AbstractEntry.AbstractEntry
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet_Entry
__Entry = __MultiSet_Entry.Entry
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractEntry(ABC, pyapache.__MultiSet_Entry, collections4.MultiSet$Entry):
    """org.apache.commons.collections4.multiset.AbstractMultiSet.AbstractEntry"""
 
    @staticmethod
    def __wrap(java_value: __AbstractEntry) -> 'AbstractEntry':
        return AbstractEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractEntry):
        """
        Dynamic initializer for AbstractEntry.
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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.hashCode()"""
        return int.__wrap(super(AbstractEntry, self).hashCode())

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
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.toString()"""
        return str.__wrap(super(AbstractEntry, self).toString())

    @abstractmethod
    def getElement(self, ):
        """public abstract E org.apache.commons.collections4.MultiSet$Entry.getElement()"""
        pass

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
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractEntry, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def getCount(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet$Entry.getCount()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet
__AbstractMultiSet = __AbstractMultiSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as __AbstractMapMultiSet
__AbstractMapMultiSet = __AbstractMapMultiSet
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
 
class AbstractMapMultiSet(ABC, __AbstractMultiSet, AbstractMultiSet):
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMapMultiSet) -> 'AbstractMapMultiSet':
        return AbstractMapMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMapMultiSet):
        """
        Dynamic initializer for AbstractMapMultiSet.
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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSet, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapMultiSet, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.add(E)"""
        return bool.__wrap(super(__AbstractMultiSet, self).add(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMultiSet, self).removeAll(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray(T[])"""
        return List[object].__wrap(super(__AbstractMapMultiSet, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMapMultiSet.iterator()"""
        return 'Iterator'.__wrap(super(AbstractMapMultiSet, self).iterator())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSet.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMultiSet, self).uniqueSet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.hashCode()"""
        return int.__wrap(super(AbstractMapMultiSet, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray()"""
        return List[object].__wrap(super(AbstractMapMultiSet, self).toArray())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet.clear()"""
        super(AbstractMapMultiSet, self).clear()

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.add(E,int)"""
        return int.__wrap(super(__AbstractMapMultiSet, self).add(arg0, __int.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.size()"""
        return int.__wrap(super(AbstractMapMultiSet, self).size())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMapMultiSet, self).getCount(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.remove(java.lang.Object,int)"""
        return int.__wrap(super(__AbstractMapMultiSet, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapMultiSet, self).contains(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet.entrySet()"""
        return 'Set'.__wrap(super(AbstractMultiSet, self).entrySet())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet.toString()"""
        return str.__wrap(super(AbstractMultiSet, self).toString())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.setCount(E,int)"""
        return int.__wrap(super(__AbstractMultiSet, self).setCount(arg0, __int.valueOf(arg1)))

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.isEmpty()"""
        return bool.__wrap(super(AbstractMapMultiSet, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.SynchronizedMultiSet
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
import org.apache.commons.collections4.multiset.SynchronizedMultiSet as __SynchronizedMultiSet
__SynchronizedMultiSet = __SynchronizedMultiSet
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
 
class SynchronizedMultiSet(collections4.__SynchronizedCollection, collection.SynchronizedCollection, pyapache.__MultiSet, collections4.MultiSet):
    """org.apache.commons.collections4.multiset.SynchronizedMultiSet"""
 
    @staticmethod
    def __wrap(java_value: __SynchronizedMultiSet) -> 'SynchronizedMultiSet':
        return SynchronizedMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SynchronizedMultiSet):
        """
        Dynamic initializer for SynchronizedMultiSet.
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
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.SynchronizedMultiSet.uniqueSet()"""
        return 'Set'.__wrap(super(SynchronizedMultiSet, self).uniqueSet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str.__wrap(super(collection.SynchronizedCollection, self).toString())

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
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.getCount(java.lang.Object)"""
        return int.__wrap(super(__SynchronizedMultiSet, self).getCount(arg0))

    @staticmethod
    @overload
    def synchronizedMultiSet(arg0: 'MultiSet') -> 'SynchronizedMultiSet':
        """public static <E> org.apache.commons.collections4.multiset.SynchronizedMultiSet<E> org.apache.commons.collections4.multiset.SynchronizedMultiSet.synchronizedMultiSet(org.apache.commons.collections4.MultiSet<E>)"""
        return SynchronizedMultiSet.__wrap(__SynchronizedMultiSet.synchronizedMultiSet(arg0))

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.SynchronizedMultiSet.entrySet()"""
        return 'Set'.__wrap(super(SynchronizedMultiSet, self).entrySet())

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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).add(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object].__wrap(super(__collection.SynchronizedCollection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.remove(java.lang.Object,int)"""
        return int.__wrap(super(__SynchronizedMultiSet, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.hashCode()"""
        return int.__wrap(super(SynchronizedMultiSet, self).hashCode())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.SynchronizedMultiSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__SynchronizedMultiSet, self).equals(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.add(E,int)"""
        return int.__wrap(super(__SynchronizedMultiSet, self).add(arg0, __int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.setCount(E,int)"""
        return int.__wrap(super(__SynchronizedMultiSet, self).setCount(arg0, __int.valueOf(arg1)))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).addAll(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet
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
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
from builtins import bool
import java.util.AbstractSet as __AbstractSet
__AbstractSet = __AbstractSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet_EntrySet
__EntrySet = __AbstractMultiSet_EntrySet.EntrySet
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
 
class EntrySet(__AbstractSet, AbstractSet):
    """org.apache.commons.collections4.multiset.AbstractMultiSet.EntrySet"""
 
    @staticmethod
    def __wrap(java_value: __EntrySet) -> 'EntrySet':
        return EntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySet):
        """
        Dynamic initializer for EntrySet.
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
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__EntrySet, self).remove(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool.__wrap(super(__AbstractCollection, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.size()"""
        return int.__wrap(super(EntrySet, self).size())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.iterator()"""
        return 'Iterator'.__wrap(super(EntrySet, self).iterator())

    @override
    @overload
    def clear(self):
        """public void java.util.AbstractCollection.clear()"""
        super(AbstractCollection, self).clear()

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.contains(java.lang.Object)"""
        return bool.__wrap(super(__EntrySet, self).contains(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.PredicatedMultiSet
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
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.multiset.PredicatedMultiSet as __PredicatedMultiSet
__PredicatedMultiSet = __PredicatedMultiSet
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
 
class PredicatedMultiSet(collections4.__PredicatedCollection, collection.PredicatedCollection, pyapache.__MultiSet, collections4.MultiSet):
    """org.apache.commons.collections4.multiset.PredicatedMultiSet"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedMultiSet) -> 'PredicatedMultiSet':
        return PredicatedMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedMultiSet):
        """
        Dynamic initializer for PredicatedMultiSet.
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
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.PredicatedMultiSet.entrySet()"""
        return 'Set'.__wrap(super(PredicatedMultiSet, self).entrySet())

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

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.getCount(java.lang.Object)"""
        return int.__wrap(super(__PredicatedMultiSet, self).getCount(arg0))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @staticmethod
    @overload
    def predicatedMultiSet(arg0: 'MultiSet', arg1: 'Predicate') -> 'PredicatedMultiSet':
        """public static <E> org.apache.commons.collections4.multiset.PredicatedMultiSet<E> org.apache.commons.collections4.multiset.PredicatedMultiSet.predicatedMultiSet(org.apache.commons.collections4.MultiSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedMultiSet.__wrap(__PredicatedMultiSet.predicatedMultiSet(arg0, arg1))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.add(E,int)"""
        return int.__wrap(super(__PredicatedMultiSet, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.PredicatedMultiSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedMultiSet, self).equals(arg0))

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
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.setCount(E,int)"""
        return int.__wrap(super(__PredicatedMultiSet, self).setCount(arg0, __int.valueOf(arg1)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.remove(java.lang.Object,int)"""
        return int.__wrap(super(__PredicatedMultiSet, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.hashCode()"""
        return int.__wrap(super(PredicatedMultiSet, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.PredicatedMultiSet.uniqueSet()"""
        return 'Set'.__wrap(super(PredicatedMultiSet, self).uniqueSet())

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
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$UniqueSetIterator
from builtins import str
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as __AbstractMapMultiSet_UniqueSetIterator
__UniqueSetIterator = __AbstractMapMultiSet_UniqueSetIterator.UniqueSetIterator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as __AbstractUntypedIteratorDecorator
__AbstractUntypedIteratorDecorator = __AbstractUntypedIteratorDecorator
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
 
class UniqueSetIterator(collections4.__AbstractIteratorDecorator, iterators.AbstractIteratorDecorator):
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.UniqueSetIterator"""
 
    @staticmethod
    def __wrap(java_value: __UniqueSetIterator) -> 'UniqueSetIterator':
        return UniqueSetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniqueSetIterator):
        """
        Dynamic initializer for UniqueSetIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet$UniqueSetIterator.remove()"""
        super(UniqueSetIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool.__wrap(super(iterators.AbstractUntypedIteratorDecorator, self).hasNext())

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.multiset.AbstractMapMultiSet$UniqueSetIterator.next()"""
        return object.__wrap(super(UniqueSetIterator, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$MultiSetEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet_AbstractEntry
__AbstractEntry = __AbstractMultiSet_AbstractEntry.AbstractEntry
from builtins import type
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as __AbstractMapMultiSet_MultiSetEntry
__MultiSetEntry = __AbstractMapMultiSet_MultiSetEntry.MultiSetEntry
from builtins import object
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
 
class MultiSetEntry(__AbstractEntry, AbstractEntry):
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.MultiSetEntry"""
 
    @staticmethod
    def __wrap(java_value: __MultiSetEntry) -> 'MultiSetEntry':
        return MultiSetEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiSetEntry):
        """
        Dynamic initializer for MultiSetEntry.
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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.hashCode()"""
        return int.__wrap(super(AbstractEntry, self).hashCode())

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
    def getElement(self) -> object:
        """public E org.apache.commons.collections4.multiset.AbstractMapMultiSet$MultiSetEntry.getElement()"""
        return object.__wrap(super(MultiSetEntry, self).getElement())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.toString()"""
        return str.__wrap(super(AbstractEntry, self).toString())

    @override
    @overload
    def getCount(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet$MultiSetEntry.getCount()"""
        return int.__wrap(super(MultiSetEntry, self).getCount())

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
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractEntry, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.multiset.UnmodifiableMultiSet
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.multiset.AbstractMultiSetDecorator as __AbstractMultiSetDecorator
__AbstractMultiSetDecorator = __AbstractMultiSetDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.multiset.UnmodifiableMultiSet as __UnmodifiableMultiSet
__UnmodifiableMultiSet = __UnmodifiableMultiSet
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
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableMultiSet(__AbstractMultiSetDecorator, AbstractMultiSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.multiset.UnmodifiableMultiSet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableMultiSet) -> 'UnmodifiableMultiSet':
        return UnmodifiableMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableMultiSet):
        """
        Dynamic initializer for UnmodifiableMultiSet.
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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.add(E)"""
        return bool.__wrap(super(__UnmodifiableMultiSet, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableMultiSet, self).removeAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.remove(java.lang.Object,int)"""
        return int.__wrap(super(__UnmodifiableMultiSet, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableMultiSet, self).iterator())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableMultiSet, self).entrySet())

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
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableMultiSet, self).addAll(arg0))

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
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.uniqueSet()"""
        return 'Set'.__wrap(super(UnmodifiableMultiSet, self).uniqueSet())

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableMultiSet, self).remove(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.add(E,int)"""
        return int.__wrap(super(__UnmodifiableMultiSet, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableMultiSet, self).removeIf(arg0))

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
    def unmodifiableMultiSet(arg0: 'MultiSet') -> 'collections4.MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.unmodifiableMultiSet(org.apache.commons.collections4.MultiSet<? extends E>)"""
        return collections4.MultiSet.__wrap(__UnmodifiableMultiSet.unmodifiableMultiSet(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.setCount(E,int)"""
        return int.__wrap(super(__UnmodifiableMultiSet, self).setCount(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableMultiSet, self).retainAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.UnmodifiableMultiSet.clear()"""
        super(UnmodifiableMultiSet, self).clear()

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSetDecorator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractMultiSetDecorator, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMultiSetDecorator, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSetDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.multiset.AbstractMultiSetDecorator as __AbstractMultiSetDecorator
__AbstractMultiSetDecorator = __AbstractMultiSetDecorator
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
 
class AbstractMultiSetDecorator(ABC, collections4.__AbstractCollectionDecorator, collection.AbstractCollectionDecorator, pyapache.__MultiSet, collections4.MultiSet):
    """org.apache.commons.collections4.multiset.AbstractMultiSetDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMultiSetDecorator) -> 'AbstractMultiSetDecorator':
        return AbstractMultiSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMultiSetDecorator):
        """
        Dynamic initializer for AbstractMultiSetDecorator.
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
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMultiSetDecorator, self).entrySet())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.setCount(E,int)"""
        return int.__wrap(super(__AbstractMultiSetDecorator, self).setCount(arg0, __int.valueOf(arg1)))

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
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.remove(java.lang.Object,int)"""
        return int.__wrap(super(__AbstractMultiSetDecorator, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.add(E,int)"""
        return int.__wrap(super(__AbstractMultiSetDecorator, self).add(arg0, __int.valueOf(arg1)))

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
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSetDecorator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.hashCode()"""
        return int.__wrap(super(AbstractMultiSetDecorator, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMultiSetDecorator, self).getCount(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMultiSetDecorator, self).uniqueSet()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet
__AbstractMultiSet = __AbstractMultiSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
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
 
class AbstractMultiSet(ABC, __AbstractCollection, AbstractCollection, pyapache.__MultiSet, collections4.MultiSet):
    """org.apache.commons.collections4.multiset.AbstractMultiSet"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMultiSet) -> 'AbstractMultiSet':
        return AbstractMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMultiSet):
        """
        Dynamic initializer for AbstractMultiSet.
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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSet, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSet, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.hashCode()"""
        return int.__wrap(super(AbstractMultiSet, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.add(E)"""
        return bool.__wrap(super(__AbstractMultiSet, self).add(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMultiSet, self).removeAll(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object,int)"""
        return int.__wrap(super(__AbstractMultiSet, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSet.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMultiSet, self).uniqueSet())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSet, self).contains(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.add(E,int)"""
        return int.__wrap(super(__AbstractMultiSet, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMultiSet.iterator()"""
        return 'Iterator'.__wrap(super(AbstractMultiSet, self).iterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet.entrySet()"""
        return 'Set'.__wrap(super(AbstractMultiSet, self).entrySet())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet.toString()"""
        return str.__wrap(super(AbstractMultiSet, self).toString())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.setCount(E,int)"""
        return int.__wrap(super(__AbstractMultiSet, self).setCount(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.size()"""
        return int.__wrap(super(AbstractMultiSet, self).size())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMultiSet, self).getCount(arg0))

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMultiSet.clear()"""
        super(AbstractMultiSet, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.multiset.HashMultiSet
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.multiset.AbstractMultiSet as __AbstractMultiSet
__AbstractMultiSet = __AbstractMultiSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
import org.apache.commons.collections4.multiset.HashMultiSet as __HashMultiSet
__HashMultiSet = __HashMultiSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as __AbstractMapMultiSet
__AbstractMapMultiSet = __AbstractMapMultiSet
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
 
class HashMultiSet(__AbstractMapMultiSet, AbstractMapMultiSet, __Serializable, Serializable):
    """org.apache.commons.collections4.multiset.HashMultiSet"""
 
    @staticmethod
    def __wrap(java_value: __HashMultiSet) -> 'HashMultiSet':
        return HashMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashMultiSet):
        """
        Dynamic initializer for HashMultiSet.
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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiSet, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multiset.HashMultiSet()"""
        val = __HashMultiSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapMultiSet, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.add(E)"""
        return bool.__wrap(super(__AbstractMultiSet, self).add(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractMultiSet, self).removeAll(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray(T[])"""
        return List[object].__wrap(super(__AbstractMapMultiSet, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMapMultiSet.iterator()"""
        return 'Iterator'.__wrap(super(AbstractMapMultiSet, self).iterator())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSet.uniqueSet()"""
        return 'Set'.__wrap(super(AbstractMultiSet, self).uniqueSet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.hashCode()"""
        return int.__wrap(super(AbstractMapMultiSet, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.multiset.HashMultiSet(java.util.Collection<? extends E>)"""
        val = __HashMultiSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray()"""
        return List[object].__wrap(super(AbstractMapMultiSet, self).toArray())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet.clear()"""
        super(AbstractMapMultiSet, self).clear()

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.add(E,int)"""
        return int.__wrap(super(__AbstractMapMultiSet, self).add(arg0, __int.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.size()"""
        return int.__wrap(super(AbstractMapMultiSet, self).size())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.getCount(java.lang.Object)"""
        return int.__wrap(super(__AbstractMapMultiSet, self).getCount(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.remove(java.lang.Object,int)"""
        return int.__wrap(super(__AbstractMapMultiSet, self).remove(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapMultiSet, self).contains(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet.entrySet()"""
        return 'Set'.__wrap(super(AbstractMultiSet, self).entrySet())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet.toString()"""
        return str.__wrap(super(AbstractMultiSet, self).toString())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.setCount(E,int)"""
        return int.__wrap(super(__AbstractMultiSet, self).setCount(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.multiset.HashMultiSet()"""
        val = __HashMultiSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.isEmpty()"""
        return bool.__wrap(super(AbstractMapMultiSet, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.MultiSet as __MultiSet_Entry
__Entry = __MultiSet_Entry.Entry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as __AbstractMapMultiSet_EntrySetIterator
__EntrySetIterator = __AbstractMapMultiSet_EntrySetIterator.EntrySetIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntrySetIterator(__Iterator, Iterator):
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.EntrySetIterator"""
 
    @staticmethod
    def __wrap(java_value: __EntrySetIterator) -> 'EntrySetIterator':
        return EntrySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySetIterator):
        """
        Dynamic initializer for EntrySetIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator.hasNext()"""
        return bool.__wrap(super(EntrySetIterator, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator.remove()"""
        super(EntrySetIterator, self).remove()

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def next(self) -> 'collections4.MultiSet$Entry':
        """public org.apache.commons.collections4.MultiSet$Entry<E> org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator.next()"""
        return 'collections4.MultiSet$Entry'.__wrap(super(EntrySetIterator, self).next()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$MutableInteger
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as __AbstractMapMultiSet_MutableInteger
__MutableInteger = __AbstractMapMultiSet_MutableInteger.MutableInteger
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutableInteger():
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.MutableInteger"""
 
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet$MutableInteger.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableInteger, self).equals(arg0))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet$MutableInteger.hashCode()"""
        return int.__wrap(super(MutableInteger, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))