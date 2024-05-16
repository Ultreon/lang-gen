from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.multiset.AbstractMultiSetDecorator as _AbstractMultiSetDecorator
_AbstractMultiSetDecorator = _AbstractMultiSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
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

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.multiset.UnmodifiableMultiSet as _UnmodifiableMultiSet
_UnmodifiableMultiSet = _UnmodifiableMultiSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableMultiSet():
    """org.apache.commons.collections4.multiset.UnmodifiableMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableMultiSet) -> 'UnmodifiableMultiSet':
        return UnmodifiableMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableMultiSet):
        """
        Dynamic initializer for UnmodifiableMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSetDecorator, self).equals(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).removeIf(arg0))

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

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableMultiSet, self).entrySet())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableMultiSet, self).iterator())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMultiSetDecorator, self).getCount(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(UnmodifiableMultiSet, self).uniqueSet())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiSetDecorator, self).hashCode())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).addAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.add(E)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).add(arg0))

    @staticmethod
    @overload
    def unmodifiableMultiSet(arg0: 'MultiSet') -> 'collections4.MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.unmodifiableMultiSet(org.apache.commons.collections4.MultiSet<? extends E>)"""
        return collections4.MultiSet._wrap(_UnmodifiableMultiSet.unmodifiableMultiSet(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_UnmodifiableMultiSet, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.UnmodifiableMultiSet.clear()"""
        super(UnmodifiableMultiSet, self).clear()

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).remove(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.setCount(E,int)"""
        return int._wrap(super(_UnmodifiableMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

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
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).retainAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).removeAll(arg0))

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
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.add(E,int)"""
        return int._wrap(super(_UnmodifiableMultiSet, self).add(arg0, _int.valueOf(arg1)))

 
 
 
# CLASS: org.apache.commons.collections4.multiset.UnmodifiableMultiSet
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.multiset.AbstractMultiSetDecorator as _AbstractMultiSetDecorator
_AbstractMultiSetDecorator = _AbstractMultiSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
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

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.multiset.UnmodifiableMultiSet as _UnmodifiableMultiSet
_UnmodifiableMultiSet = _UnmodifiableMultiSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableMultiSet():
    """org.apache.commons.collections4.multiset.UnmodifiableMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableMultiSet) -> 'UnmodifiableMultiSet':
        return UnmodifiableMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableMultiSet):
        """
        Dynamic initializer for UnmodifiableMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSetDecorator, self).equals(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).removeIf(arg0))

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

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableMultiSet, self).entrySet())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableMultiSet, self).iterator())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMultiSetDecorator, self).getCount(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(UnmodifiableMultiSet, self).uniqueSet())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiSetDecorator, self).hashCode())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).addAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.add(E)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).add(arg0))

    @staticmethod
    @overload
    def unmodifiableMultiSet(arg0: 'MultiSet') -> 'collections4.MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.multiset.UnmodifiableMultiSet.unmodifiableMultiSet(org.apache.commons.collections4.MultiSet<? extends E>)"""
        return collections4.MultiSet._wrap(_UnmodifiableMultiSet.unmodifiableMultiSet(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_UnmodifiableMultiSet, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.UnmodifiableMultiSet.clear()"""
        super(UnmodifiableMultiSet, self).clear()

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).remove(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.setCount(E,int)"""
        return int._wrap(super(_UnmodifiableMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

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
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).retainAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.UnmodifiableMultiSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableMultiSet, self).removeAll(arg0))

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
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.UnmodifiableMultiSet.add(E,int)"""
        return int._wrap(super(_UnmodifiableMultiSet, self).add(arg0, _int.valueOf(arg1)))

 
 
 
# CLASS: org.apache.commons.collections4.multiset.UnmodifiableMultiSet 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$MultiSetEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as _AbstractMapMultiSet_MultiSetEntry
_MultiSetEntry = _AbstractMapMultiSet_MultiSetEntry.MultiSetEntry
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet_AbstractEntry
_AbstractEntry = _AbstractMultiSet_AbstractEntry.AbstractEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiSetEntry():
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.MultiSetEntry"""
 
    @staticmethod
    def _wrap(java_value: _MultiSetEntry) -> 'MultiSetEntry':
        return MultiSetEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiSetEntry):
        """
        Dynamic initializer for MultiSetEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiSetEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiSetEntry__wrapper":
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
    def getElement(self) -> object:
        """public E org.apache.commons.collections4.multiset.AbstractMapMultiSet$MultiSetEntry.getElement()"""
        return object._wrap(super(MultiSetEntry, self).getElement())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.toString()"""
        return str._wrap(super(AbstractEntry, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCount(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet$MultiSetEntry.getCount()"""
        return int._wrap(super(MultiSetEntry, self).getCount())

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
        return bool._wrap(super(_AbstractEntry, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.hashCode()"""
        return int._wrap(super(AbstractEntry, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.SynchronizedMultiSet
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.multiset.SynchronizedMultiSet as _SynchronizedMultiSet
_SynchronizedMultiSet = _SynchronizedMultiSet
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
 
class SynchronizedMultiSet():
    """org.apache.commons.collections4.multiset.SynchronizedMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _SynchronizedMultiSet) -> 'SynchronizedMultiSet':
        return SynchronizedMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronizedMultiSet):
        """
        Dynamic initializer for SynchronizedMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronizedMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronizedMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.SynchronizedMultiSet.entrySet()"""
        return 'Set'._wrap(super(SynchronizedMultiSet, self).entrySet())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object]._wrap(super(collection.SynchronizedCollection, self).toArray())

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.add(E,int)"""
        return int._wrap(super(_SynchronizedMultiSet, self).add(arg0, _int.valueOf(arg1)))

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
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.setCount(E,int)"""
        return int._wrap(super(_SynchronizedMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).contains(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).retainAll(arg0))

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
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_SynchronizedMultiSet, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.SynchronizedMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(SynchronizedMultiSet, self).uniqueSet())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.SynchronizedCollection, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.hashCode()"""
        return int._wrap(super(SynchronizedMultiSet, self).hashCode())

    @staticmethod
    @overload
    def synchronizedMultiSet(arg0: 'MultiSet') -> 'SynchronizedMultiSet':
        """public static <E> org.apache.commons.collections4.multiset.SynchronizedMultiSet<E> org.apache.commons.collections4.multiset.SynchronizedMultiSet.synchronizedMultiSet(org.apache.commons.collections4.MultiSet<E>)"""
        return SynchronizedMultiSet._wrap(_SynchronizedMultiSet.synchronizedMultiSet(arg0))

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.SynchronizedMultiSet.getCount(java.lang.Object)"""
        return int._wrap(super(_SynchronizedMultiSet, self).getCount(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int._wrap(super(collection.SynchronizedCollection, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.SynchronizedMultiSet.equals(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedMultiSet, self).equals(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet_UniqueSet
_UniqueSet = _AbstractMultiSet_UniqueSet.UniqueSet
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
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
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
 
class UniqueSet():
    """org.apache.commons.collections4.multiset.AbstractMultiSet.UniqueSet"""
 
    @staticmethod
    def _wrap(java_value: _UniqueSet) -> 'UniqueSet':
        return UniqueSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniqueSet):
        """
        Dynamic initializer for UniqueSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniqueSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniqueSet__wrapper":
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
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UniqueSet, self).containsAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.remove(java.lang.Object)"""
        return bool._wrap(super(_UniqueSet, self).remove(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.clear()"""
        super(UniqueSet, self).clear()

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

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.iterator()"""
        return 'Iterator'._wrap(super(UniqueSet, self).iterator())

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
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool._wrap(super(_AbstractCollection, self).add(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.size()"""
        return int._wrap(super(UniqueSet, self).size())

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

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$UniqueSet.contains(java.lang.Object)"""
        return bool._wrap(super(_UniqueSet, self).contains(arg0))

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

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$UniqueSetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as _AbstractMapMultiSet_UniqueSetIterator
_UniqueSetIterator = _AbstractMapMultiSet_UniqueSetIterator.UniqueSetIterator
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniqueSetIterator():
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.UniqueSetIterator"""
 
    @staticmethod
    def _wrap(java_value: _UniqueSetIterator) -> 'UniqueSetIterator':
        return UniqueSetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniqueSetIterator):
        """
        Dynamic initializer for UniqueSetIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniqueSetIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniqueSetIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.multiset.AbstractMapMultiSet$UniqueSetIterator.next()"""
        return object._wrap(super(UniqueSetIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet$UniqueSetIterator.remove()"""
        super(UniqueSetIterator, self).remove()

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

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(iterators.AbstractUntypedIteratorDecorator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$MutableInteger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as _AbstractMapMultiSet_MutableInteger
_MutableInteger = _AbstractMapMultiSet_MutableInteger.MutableInteger
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableInteger():
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.MutableInteger"""
 
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet$MutableInteger.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableInteger, self).equals(arg0))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet$MutableInteger.hashCode()"""
        return int._wrap(super(MutableInteger, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.HashMultiSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.multiset.HashMultiSet as _HashMultiSet
_HashMultiSet = _HashMultiSet
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet
_AbstractMultiSet = _AbstractMultiSet
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
import java.util.Set as Set
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as _AbstractMapMultiSet
_AbstractMapMultiSet = _AbstractMapMultiSet
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashMultiSet():
    """org.apache.commons.collections4.multiset.HashMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _HashMultiSet) -> 'HashMultiSet':
        return HashMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashMultiSet):
        """
        Dynamic initializer for HashMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapMultiSet, self).contains(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multiset.HashMultiSet()"""
        val = _HashMultiSet()
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSet, self).remove(arg0))

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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.add(E)"""
        return bool._wrap(super(_AbstractMultiSet, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMultiSet, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray()"""
        return List[object]._wrap(super(AbstractMapMultiSet, self).toArray())

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.multiset.HashMultiSet(java.util.Collection<? extends E>)"""
        val = _HashMultiSet(arg0)
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapMultiSet, self).equals(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.collections4.multiset.HashMultiSet()"""
        val = _HashMultiSet()
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.size()"""
        return int._wrap(super(AbstractMapMultiSet, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet.clear()"""
        super(AbstractMapMultiSet, self).clear()

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.add(E,int)"""
        return int._wrap(super(_AbstractMapMultiSet, self).add(arg0, _int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray(T[])"""
        return List[object]._wrap(super(_AbstractMapMultiSet, self).toArray(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMultiSet, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMapMultiSet, self).getCount(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet.toString()"""
        return str._wrap(super(AbstractMultiSet, self).toString())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMapMultiSet.iterator()"""
        return 'Iterator'._wrap(super(AbstractMapMultiSet, self).iterator())

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_AbstractMapMultiSet, self).remove(arg0, _int.valueOf(arg1)))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.isEmpty()"""
        return bool._wrap(super(AbstractMapMultiSet, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.hashCode()"""
        return int._wrap(super(AbstractMapMultiSet, self).hashCode())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.setCount(E,int)"""
        return int._wrap(super(_AbstractMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet.entrySet()"""
        return 'Set'._wrap(super(AbstractMultiSet, self).entrySet())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet
_AbstractMultiSet = _AbstractMultiSet
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
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMultiSet():
    """org.apache.commons.collections4.multiset.AbstractMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMultiSet) -> 'AbstractMultiSet':
        return AbstractMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMultiSet):
        """
        Dynamic initializer for AbstractMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSet, self).equals(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.add(E,int)"""
        return int._wrap(super(_AbstractMultiSet, self).add(arg0, _int.valueOf(arg1)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSet, self).remove(arg0))

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMultiSet, self).getCount(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.add(E)"""
        return bool._wrap(super(_AbstractMultiSet, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMultiSet, self).removeAll(arg0))

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
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_AbstractMultiSet, self).remove(arg0, _int.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMultiSet.iterator()"""
        return 'Iterator'._wrap(super(AbstractMultiSet, self).iterator())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.size()"""
        return int._wrap(super(AbstractMultiSet, self).size())

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMultiSet, self).uniqueSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet.toString()"""
        return str._wrap(super(AbstractMultiSet, self).toString())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

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
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMultiSet.clear()"""
        super(AbstractMultiSet, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.hashCode()"""
        return int._wrap(super(AbstractMultiSet, self).hashCode())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.setCount(E,int)"""
        return int._wrap(super(_AbstractMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSet, self).contains(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet.entrySet()"""
        return 'Set'._wrap(super(AbstractMultiSet, self).entrySet())

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
 
 
# CLASS: org.apache.commons.collections4.multiset.PredicatedMultiSet
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
import org.apache.commons.collections4.multiset.PredicatedMultiSet as _PredicatedMultiSet
_PredicatedMultiSet = _PredicatedMultiSet
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
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedMultiSet():
    """org.apache.commons.collections4.multiset.PredicatedMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedMultiSet) -> 'PredicatedMultiSet':
        return PredicatedMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedMultiSet):
        """
        Dynamic initializer for PredicatedMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.hashCode()"""
        return int._wrap(super(PredicatedMultiSet, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.setCount(E,int)"""
        return int._wrap(super(_PredicatedMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.PredicatedMultiSet.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedMultiSet, self).equals(arg0))

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
    def predicatedMultiSet(arg0: 'MultiSet', arg1: 'Predicate') -> 'PredicatedMultiSet':
        """public static <E> org.apache.commons.collections4.multiset.PredicatedMultiSet<E> org.apache.commons.collections4.multiset.PredicatedMultiSet.predicatedMultiSet(org.apache.commons.collections4.MultiSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedMultiSet._wrap(_PredicatedMultiSet.predicatedMultiSet(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_PredicatedMultiSet, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.PredicatedMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(PredicatedMultiSet, self).uniqueSet())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.PredicatedMultiSet.entrySet()"""
        return 'Set'._wrap(super(PredicatedMultiSet, self).entrySet())

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

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.notNullBuilder())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

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

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.getCount(java.lang.Object)"""
        return int._wrap(super(_PredicatedMultiSet, self).getCount(arg0))

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

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.PredicatedMultiSet.add(E,int)"""
        return int._wrap(super(_PredicatedMultiSet, self).add(arg0, _int.valueOf(arg1)))

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
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSetDecorator
import org.apache.commons.collections4.multiset.AbstractMultiSetDecorator as _AbstractMultiSetDecorator
_AbstractMultiSetDecorator = _AbstractMultiSetDecorator
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
 
class AbstractMultiSetDecorator():
    """org.apache.commons.collections4.multiset.AbstractMultiSetDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMultiSetDecorator) -> 'AbstractMultiSetDecorator':
        return AbstractMultiSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMultiSetDecorator):
        """
        Dynamic initializer for AbstractMultiSetDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMultiSetDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMultiSetDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.remove(java.lang.Object,int)"""
        return int._wrap(super(_AbstractMultiSetDecorator, self).remove(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMultiSetDecorator, self).entrySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSetDecorator, self).equals(arg0))

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
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMultiSetDecorator, self).getCount(arg0))

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.setCount(E,int)"""
        return int._wrap(super(_AbstractMultiSetDecorator, self).setCount(arg0, _int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.add(E,int)"""
        return int._wrap(super(_AbstractMultiSetDecorator, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiSetDecorator, self).hashCode())

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
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSetDecorator.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMultiSetDecorator, self).uniqueSet())

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
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet_Entry
_Entry = _MultiSet_Entry.Entry
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet_AbstractEntry
_AbstractEntry = _AbstractMultiSet_AbstractEntry.AbstractEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractEntry():
    """org.apache.commons.collections4.multiset.AbstractMultiSet.AbstractEntry"""
 
    @staticmethod
    def _wrap(java_value: _AbstractEntry) -> 'AbstractEntry':
        return AbstractEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractEntry):
        """
        Dynamic initializer for AbstractEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractEntry__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.toString()"""
        return str._wrap(super(AbstractEntry, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
        return bool._wrap(super(_AbstractEntry, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$AbstractEntry.hashCode()"""
        return int._wrap(super(AbstractEntry, self).hashCode())

    @abstractmethod
    def getCount(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet$Entry.getCount()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet
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
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet_EntrySet
_EntrySet = _AbstractMultiSet_EntrySet.EntrySet
from typing import List
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
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
 
class EntrySet():
    """org.apache.commons.collections4.multiset.AbstractMultiSet.EntrySet"""
 
    @staticmethod
    def _wrap(java_value: _EntrySet) -> 'EntrySet':
        return EntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySet):
        """
        Dynamic initializer for EntrySet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySet__wrapper":
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object]._wrap(super(AbstractCollection, self).toArray())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.contains(java.lang.Object)"""
        return bool._wrap(super(_EntrySet, self).contains(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.size()"""
        return int._wrap(super(EntrySet, self).size())

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

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.iterator()"""
        return 'Iterator'._wrap(super(EntrySet, self).iterator())

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
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet$EntrySet.remove(java.lang.Object)"""
        return bool._wrap(super(_EntrySet, self).remove(arg0))

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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet_Entry
_Entry = _MultiSet_Entry.Entry
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as _AbstractMapMultiSet_EntrySetIterator
_EntrySetIterator = _AbstractMapMultiSet_EntrySetIterator.EntrySetIterator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySetIterator():
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet.EntrySetIterator"""
 
    @staticmethod
    def _wrap(java_value: _EntrySetIterator) -> 'EntrySetIterator':
        return EntrySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySetIterator):
        """
        Dynamic initializer for EntrySetIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySetIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySetIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator.remove()"""
        super(EntrySetIterator, self).remove()

    @override
    @overload
    def next(self) -> 'collections4.MultiSet$Entry':
        """public org.apache.commons.collections4.MultiSet$Entry<E> org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator.next()"""
        return 'collections4.MultiSet$Entry'._wrap(super(EntrySetIterator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet$EntrySetIterator.hasNext()"""
        return bool._wrap(super(EntrySetIterator, self).hasNext())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

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
 
 
# CLASS: org.apache.commons.collections4.multiset.AbstractMapMultiSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.multiset.AbstractMultiSet as _AbstractMultiSet
_AbstractMultiSet = _AbstractMultiSet
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
import java.util.Set as Set
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.multiset.AbstractMapMultiSet as _AbstractMapMultiSet
_AbstractMapMultiSet = _AbstractMapMultiSet
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMapMultiSet():
    """org.apache.commons.collections4.multiset.AbstractMapMultiSet"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMapMultiSet) -> 'AbstractMapMultiSet':
        return AbstractMapMultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMapMultiSet):
        """
        Dynamic initializer for AbstractMapMultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMapMultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMapMultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapMultiSet, self).contains(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiSet, self).remove(arg0))

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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.add(E)"""
        return bool._wrap(super(_AbstractMultiSet, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMultiSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractMultiSet, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray()"""
        return List[object]._wrap(super(AbstractMapMultiSet, self).toArray())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapMultiSet, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.size()"""
        return int._wrap(super(AbstractMapMultiSet, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multiset.AbstractMapMultiSet.clear()"""
        super(AbstractMapMultiSet, self).clear()

    @overload
    def add(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.add(E,int)"""
        return int._wrap(super(_AbstractMapMultiSet, self).add(arg0, _int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.multiset.AbstractMapMultiSet.toArray(T[])"""
        return List[object]._wrap(super(_AbstractMapMultiSet, self).toArray(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def uniqueSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.multiset.AbstractMultiSet.uniqueSet()"""
        return 'Set'._wrap(super(AbstractMultiSet, self).uniqueSet())

    @overload
    def getCount(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.getCount(java.lang.Object)"""
        return int._wrap(super(_AbstractMapMultiSet, self).getCount(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multiset.AbstractMultiSet.toString()"""
        return str._wrap(super(AbstractMultiSet, self).toString())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.multiset.AbstractMapMultiSet.iterator()"""
        return 'Iterator'._wrap(super(AbstractMapMultiSet, self).iterator())

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.remove(java.lang.Object,int)"""
        return int._wrap(super(_AbstractMapMultiSet, self).remove(arg0, _int.valueOf(arg1)))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multiset.AbstractMapMultiSet.isEmpty()"""
        return bool._wrap(super(AbstractMapMultiSet, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMapMultiSet.hashCode()"""
        return int._wrap(super(AbstractMapMultiSet, self).hashCode())

    @overload
    def setCount(self, arg0: object, arg1: int) -> int:
        """public int org.apache.commons.collections4.multiset.AbstractMultiSet.setCount(E,int)"""
        return int._wrap(super(_AbstractMultiSet, self).setCount(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.multiset.AbstractMultiSet.entrySet()"""
        return 'Set'._wrap(super(AbstractMultiSet, self).entrySet())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)