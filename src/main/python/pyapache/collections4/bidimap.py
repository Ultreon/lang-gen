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
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_View
__View = __AbstractDualBidiMap_View.View
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_KeySet
__KeySet = __AbstractDualBidiMap_KeySet.KeySet
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
 
class KeySet(__View, View, __Set, Set):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.KeySet"""
 
    @staticmethod
    def __wrap(java_value: __KeySet) -> 'KeySet':
        return KeySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeySet):
        """
        Dynamic initializer for KeySet.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool.__wrap(super(__View, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__View, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__KeySet, self).remove(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).removeAll(arg0))

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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.contains(java.lang.Object)"""
        return bool.__wrap(super(__KeySet, self).contains(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int.__wrap(super(View, self).hashCode())

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.iterator()"""
        return 'Iterator'.__wrap(super(KeySet, self).iterator())

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

 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_View
__View = __AbstractDualBidiMap_View.View
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_KeySet
__KeySet = __AbstractDualBidiMap_KeySet.KeySet
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
 
class KeySet(__View, View, __Set, Set):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.KeySet"""
 
    @staticmethod
    def __wrap(java_value: __KeySet) -> 'KeySet':
        return KeySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeySet):
        """
        Dynamic initializer for KeySet.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool.__wrap(super(__View, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__View, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__KeySet, self).remove(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).removeAll(arg0))

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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.contains(java.lang.Object)"""
        return bool.__wrap(super(__KeySet, self).contains(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int.__wrap(super(View, self).hashCode())

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.iterator()"""
        return 'Iterator'.__wrap(super(KeySet, self).iterator())

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

 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_View
__View = __AbstractDualBidiMap_View.View
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_EntrySet
__EntrySet = __AbstractDualBidiMap_EntrySet.EntrySet
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
 
class EntrySet(__View, View, __Set, Set):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.EntrySet"""
 
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool.__wrap(super(__View, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__View, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).retainAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).removeAll(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int.__wrap(super(View, self).hashCode())

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

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__EntrySet, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySet.iterator()"""
        return 'Iterator'.__wrap(super(EntrySet, self).iterator())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.OrderedBidiMap as __OrderedBidiMap
__OrderedBidiMap = __OrderedBidiMap
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as __AbstractOrderedBidiMapDecorator
__AbstractOrderedBidiMapDecorator = __AbstractOrderedBidiMapDecorator
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as __AbstractBidiMapDecorator
__AbstractBidiMapDecorator = __AbstractBidiMapDecorator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractOrderedBidiMapDecorator(ABC, __AbstractBidiMapDecorator, AbstractBidiMapDecorator, pyapache.__OrderedBidiMap, collections4.OrderedBidiMap):
    """org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractOrderedBidiMapDecorator) -> 'AbstractOrderedBidiMapDecorator':
        return AbstractOrderedBidiMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractOrderedBidiMapDecorator):
        """
        Dynamic initializer for AbstractOrderedBidiMapDecorator.
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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).entrySet())

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
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.inverseBidiMap()"""
        return 'collections4.OrderedBidiMap'.__wrap(super(AbstractOrderedBidiMapDecorator, self).inverseBidiMap())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__map.AbstractMapDecorator, self).putAll(arg0)

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).removeValue(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsValue(arg0))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.values()"""
        return 'Set'.__wrap(super(AbstractBidiMapDecorator, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).keySet())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(map.AbstractMapDecorator, self).clear()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractOrderedBidiMapDecorator, self).mapIterator())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_View
__View = __AbstractDualBidiMap_View.View
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
 
class View(ABC, collections4.__AbstractCollectionDecorator, collection.AbstractCollectionDecorator):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.View"""
 
    @staticmethod
    def __wrap(java_value: __View) -> 'View':
        return View(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __View):
        """
        Dynamic initializer for View.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool.__wrap(super(__View, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__View, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).retainAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).removeAll(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int.__wrap(super(View, self).hashCode())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_EntrySetIterator
__EntrySetIterator = __AbstractDualBidiMap_EntrySetIterator.EntrySetIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
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
 
class EntrySetIterator(collections4.__AbstractIteratorDecorator, iterators.AbstractIteratorDecorator):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.EntrySetIterator"""
 
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
    def next(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySetIterator.next()"""
        return 'Entry.Map$Entry'.__wrap(super(EntrySetIterator, self).next())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySetIterator.remove()"""
        super(EntrySetIterator, self).remove()

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as __AbstractSortedMapDecorator
__AbstractSortedMapDecorator = __AbstractSortedMapDecorator
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as __DualTreeBidiMap_ViewMap
__ViewMap = __DualTreeBidiMap_ViewMap.ViewMap
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class ViewMap(collections4.__AbstractSortedMapDecorator, map.AbstractSortedMapDecorator):
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap.ViewMap"""
 
    @staticmethod
    def __wrap(java_value: __ViewMap) -> 'ViewMap':
        return ViewMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ViewMap):
        """
        Dynamic initializer for ViewMap.
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
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__ViewMap, self).headMap(arg0))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object.__wrap(super(map.AbstractSortedMapDecorator, self).lastKey())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__ViewMap, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.nextKey(K)"""
        return object.__wrap(super(__ViewMap, self).nextKey(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.clear()"""
        super(ViewMap, self).clear()

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).keySet())

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__ViewMap, self).subMap(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__map.AbstractMapDecorator, self).putAll(arg0)

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.previousKey(K)"""
        return object.__wrap(super(__ViewMap, self).previousKey(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'.__wrap(super(map.AbstractSortedMapDecorator, self).comparator())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(map.AbstractMapDecorator, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(map.AbstractSortedMapDecorator, self).mapIterator())

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__ViewMap, self).tailMap(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object.__wrap(super(map.AbstractSortedMapDecorator, self).firstKey())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.TreeBidiMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.OrderedBidiMap as __OrderedBidiMap
__OrderedBidiMap = __OrderedBidiMap
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.lang.Comparable as Comparable
from builtins import object
import org.apache.commons.collections4.bidimap.TreeBidiMap as __TreeBidiMap
__TreeBidiMap = __TreeBidiMap
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class TreeBidiMap(pyapache.__OrderedBidiMap, collections4.OrderedBidiMap, __Serializable, Serializable):
    """org.apache.commons.collections4.bidimap.TreeBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __TreeBidiMap) -> 'TreeBidiMap':
        return TreeBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeBidiMap):
        """
        Dynamic initializer for TreeBidiMap.
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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.TreeBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__TreeBidiMap, self).putAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.TreeBidiMap.keySet()"""
        return 'Set'.__wrap(super(TreeBidiMap, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.TreeBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = __TreeBidiMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.TreeBidiMap.size()"""
        return int.__wrap(super(TreeBidiMap, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__TreeBidiMap, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__TreeBidiMap, self).containsValue(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def nextKey(self, arg0: 'Comparable') -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.nextKey(K)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).nextKey(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.TreeBidiMap()"""
        val = __TreeBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.isEmpty()"""
        return bool.__wrap(super(TreeBidiMap, self).isEmpty())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.lastKey()"""
        return 'Comparable'.__wrap(super(TreeBidiMap, self).lastKey())

    @overload
    def get(self, arg0: object) -> 'Comparable':
        """public V org.apache.commons.collections4.bidimap.TreeBidiMap.get(java.lang.Object)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).get(arg0))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def removeValue(self, arg0: object) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.removeValue(java.lang.Object)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).removeValue(arg0))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.TreeBidiMap.values()"""
        return 'Set'.__wrap(super(TreeBidiMap, self).values())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.TreeBidiMap.clear()"""
        super(TreeBidiMap, self).clear()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.TreeBidiMap.entrySet()"""
        return 'Set'.__wrap(super(TreeBidiMap, self).entrySet())

    @overload
    def remove(self, arg0: object) -> 'Comparable':
        """public V org.apache.commons.collections4.bidimap.TreeBidiMap.remove(java.lang.Object)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__TreeBidiMap, self).containsKey(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.TreeBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(TreeBidiMap, self).mapIterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.TreeBidiMap.hashCode()"""
        return int.__wrap(super(TreeBidiMap, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.firstKey()"""
        return 'Comparable'.__wrap(super(TreeBidiMap, self).firstKey())

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.TreeBidiMap.inverseBidiMap()"""
        return 'collections4.OrderedBidiMap'.__wrap(super(TreeBidiMap, self).inverseBidiMap())

    @overload
    def put(self, arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public V org.apache.commons.collections4.bidimap.TreeBidiMap.put(K,V)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.TreeBidiMap.toString()"""
        return str.__wrap(super(TreeBidiMap, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def previousKey(self, arg0: 'Comparable') -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.previousKey(K)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).previousKey(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def getKey(self, arg0: object) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.getKey(java.lang.Object)"""
        return 'Comparable'.__wrap(super(__TreeBidiMap, self).getKey(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.TreeBidiMap()"""
        val = __TreeBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.bidimap.UnmodifiableBidiMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as __AbstractBidiMapDecorator
__AbstractBidiMapDecorator = __AbstractBidiMapDecorator
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.bidimap.UnmodifiableBidiMap as __UnmodifiableBidiMap
__UnmodifiableBidiMap = __UnmodifiableBidiMap
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableBidiMap(__AbstractBidiMapDecorator, AbstractBidiMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.bidimap.UnmodifiableBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableBidiMap) -> 'UnmodifiableBidiMap':
        return UnmodifiableBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableBidiMap):
        """
        Dynamic initializer for UnmodifiableBidiMap.
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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableBidiMap, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableBidiMap, self).removeValue(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.put(K,V)"""
        return object.__wrap(super(__UnmodifiableBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableBidiMap, self).entrySet())

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public synchronized org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'.__wrap(super(UnmodifiableBidiMap, self).inverseBidiMap())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableBidiMap, self).putAll(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableBidiMap(arg0: 'BidiMap') -> 'collections4.BidiMap':
        """public static <K,V> org.apache.commons.collections4.BidiMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.unmodifiableBidiMap(org.apache.commons.collections4.BidiMap<? extends K, ? extends V>)"""
        return collections4.BidiMap.__wrap(__UnmodifiableBidiMap.unmodifiableBidiMap(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsValue(arg0))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.values()"""
        return 'Set'.__wrap(super(UnmodifiableBidiMap, self).values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableBidiMap, self).keySet())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.clear()"""
        super(UnmodifiableBidiMap, self).clear()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(UnmodifiableBidiMap, self).mapIterator()) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$ValuesIterator
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_ValuesIterator
__ValuesIterator = __AbstractDualBidiMap_ValuesIterator.ValuesIterator
from builtins import str
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
 
class ValuesIterator(collections4.__AbstractIteratorDecorator, iterators.AbstractIteratorDecorator):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.ValuesIterator"""
 
    @staticmethod
    def __wrap(java_value: __ValuesIterator) -> 'ValuesIterator':
        return ValuesIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValuesIterator):
        """
        Dynamic initializer for ValuesIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$ValuesIterator.remove()"""
        super(ValuesIterator, self).remove()

    @override
    @overload
    def next(self) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$ValuesIterator.next()"""
        return object.__wrap(super(ValuesIterator, self).next())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as __AbstractBidiMapDecorator
__AbstractBidiMapDecorator = __AbstractBidiMapDecorator
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import int
 
class AbstractBidiMapDecorator(ABC, collections4.__AbstractMapDecorator, map.AbstractMapDecorator, pyapache.__BidiMap, collections4.BidiMap):
    """org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractBidiMapDecorator) -> 'AbstractBidiMapDecorator':
        return AbstractBidiMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractBidiMapDecorator):
        """
        Dynamic initializer for AbstractBidiMapDecorator.
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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).entrySet())

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
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__map.AbstractMapDecorator, self).putAll(arg0)

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.inverseBidiMap()"""
        return 'collections4.BidiMap'.__wrap(super(AbstractBidiMapDecorator, self).inverseBidiMap())

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).removeValue(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsValue(arg0))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.values()"""
        return 'Set'.__wrap(super(AbstractBidiMapDecorator, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).keySet())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(map.AbstractMapDecorator, self).clear()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractBidiMapDecorator, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.OrderedBidiMap as __OrderedBidiMap
__OrderedBidiMap = __OrderedBidiMap
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as __AbstractOrderedBidiMapDecorator
__AbstractOrderedBidiMapDecorator = __AbstractOrderedBidiMapDecorator
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as __AbstractBidiMapDecorator
__AbstractBidiMapDecorator = __AbstractBidiMapDecorator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap as __UnmodifiableOrderedBidiMap
__UnmodifiableOrderedBidiMap = __UnmodifiableOrderedBidiMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableOrderedBidiMap(__AbstractOrderedBidiMapDecorator, AbstractOrderedBidiMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableOrderedBidiMap) -> 'UnmodifiableOrderedBidiMap':
        return UnmodifiableOrderedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableOrderedBidiMap):
        """
        Dynamic initializer for UnmodifiableOrderedBidiMap.
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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableOrderedBidiMap, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.inverseBidiMap()"""
        return 'collections4.OrderedBidiMap'.__wrap(super(UnmodifiableOrderedBidiMap, self).inverseBidiMap())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(UnmodifiableOrderedBidiMap, self).mapIterator())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.put(K,V)"""
        return object.__wrap(super(__UnmodifiableOrderedBidiMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableOrderedBidiMap(arg0: 'OrderedBidiMap') -> 'collections4.OrderedBidiMap':
        """public static <K,V> org.apache.commons.collections4.OrderedBidiMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.unmodifiableOrderedBidiMap(org.apache.commons.collections4.OrderedBidiMap<? extends K, ? extends V>)"""
        return collections4.OrderedBidiMap.__wrap(__UnmodifiableOrderedBidiMap.unmodifiableOrderedBidiMap(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableOrderedBidiMap, self).putAll(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.values()"""
        return 'Set'.__wrap(super(UnmodifiableOrderedBidiMap, self).values())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.clear()"""
        super(UnmodifiableOrderedBidiMap, self).clear()

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableOrderedBidiMap, self).removeValue(arg0))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableOrderedBidiMap, self).remove(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsValue(arg0))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableOrderedBidiMap, self).entrySet())

    @overload
    def inverseOrderedBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.inverseOrderedBidiMap()"""
        return 'collections4.OrderedBidiMap'.__wrap(super(UnmodifiableOrderedBidiMap, self).inverseOrderedBidiMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.SortedBidiMap as __SortedBidiMap
__SortedBidiMap = __SortedBidiMap
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as __AbstractOrderedBidiMapDecorator
__AbstractOrderedBidiMapDecorator = __AbstractOrderedBidiMapDecorator
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as __AbstractBidiMapDecorator
__AbstractBidiMapDecorator = __AbstractBidiMapDecorator
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator as __AbstractSortedBidiMapDecorator
__AbstractSortedBidiMapDecorator = __AbstractSortedBidiMapDecorator
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap as __UnmodifiableSortedBidiMap
__UnmodifiableSortedBidiMap = __UnmodifiableSortedBidiMap
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableSortedBidiMap(__AbstractSortedBidiMapDecorator, AbstractSortedBidiMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableSortedBidiMap) -> 'UnmodifiableSortedBidiMap':
        return UnmodifiableSortedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableSortedBidiMap):
        """
        Dynamic initializer for UnmodifiableSortedBidiMap.
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
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableSortedBidiMap, self).remove(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.values()"""
        return 'Set'.__wrap(super(UnmodifiableSortedBidiMap, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableSortedBidiMap, self).tailMap(arg0))

    @override
    @overload
    def valueComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.valueComparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBidiMapDecorator, self).valueComparator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableSortedBidiMap, self).headMap(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableSortedBidiMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.put(K,V)"""
        return object.__wrap(super(__UnmodifiableSortedBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableSortedBidiMap, self).keySet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(UnmodifiableSortedBidiMap, self).mapIterator())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBidiMapDecorator, self).comparator())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.inverseBidiMap()"""
        return 'collections4.SortedBidiMap'.__wrap(super(UnmodifiableSortedBidiMap, self).inverseBidiMap())

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).getKey(arg0))

    @staticmethod
    @overload
    def unmodifiableSortedBidiMap(arg0: 'SortedBidiMap') -> 'collections4.SortedBidiMap':
        """public static <K,V> org.apache.commons.collections4.SortedBidiMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.unmodifiableSortedBidiMap(org.apache.commons.collections4.SortedBidiMap<K, ? extends V>)"""
        return collections4.SortedBidiMap.__wrap(__UnmodifiableSortedBidiMap.unmodifiableSortedBidiMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableSortedBidiMap, self).subMap(arg0, arg1))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableSortedBidiMap, self).putAll(arg0)

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableSortedBidiMap, self).removeValue(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.clear()"""
        super(UnmodifiableSortedBidiMap, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap
__AbstractDualBidiMap = __AbstractDualBidiMap
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap as __DualLinkedHashBidiMap
__DualLinkedHashBidiMap = __DualLinkedHashBidiMap
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class DualLinkedHashBidiMap(__AbstractDualBidiMap, AbstractDualBidiMap, __Serializable, Serializable):
    """org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __DualLinkedHashBidiMap) -> 'DualLinkedHashBidiMap':
        return DualLinkedHashBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DualLinkedHashBidiMap):
        """
        Dynamic initializer for DualLinkedHashBidiMap.
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
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str.__wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int.__wrap(super(AbstractDualBidiMap, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap()"""
        val = __DualLinkedHashBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'.__wrap(super(AbstractDualBidiMap, self).inverseBidiMap())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap()"""
        val = __DualLinkedHashBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool.__wrap(super(AbstractDualBidiMap, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractDualBidiMap, self).mapIterator())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = __DualLinkedHashBidiMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int.__wrap(super(AbstractDualBidiMap, self).size())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).keySet())

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).values())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).getKey(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.SortedBidiMap as __SortedBidiMap
__SortedBidiMap = __SortedBidiMap
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as __AbstractOrderedBidiMapDecorator
__AbstractOrderedBidiMapDecorator = __AbstractOrderedBidiMapDecorator
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as __AbstractBidiMapDecorator
__AbstractBidiMapDecorator = __AbstractBidiMapDecorator
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator as __AbstractSortedBidiMapDecorator
__AbstractSortedBidiMapDecorator = __AbstractSortedBidiMapDecorator
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractSortedBidiMapDecorator(ABC, __AbstractOrderedBidiMapDecorator, AbstractOrderedBidiMapDecorator, pyapache.__SortedBidiMap, collections4.SortedBidiMap):
    """org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSortedBidiMapDecorator) -> 'AbstractSortedBidiMapDecorator':
        return AbstractSortedBidiMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSortedBidiMapDecorator):
        """
        Dynamic initializer for AbstractSortedBidiMapDecorator.
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
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).size())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def __init__(self, arg0: 'SortedBidiMap'):
        """public org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator(org.apache.commons.collections4.SortedBidiMap<K, V>)"""
        val = __AbstractSortedBidiMapDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def valueComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.valueComparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBidiMapDecorator, self).valueComparator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.values()"""
        return 'Set'.__wrap(super(AbstractBidiMapDecorator, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).keySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractOrderedBidiMapDecorator, self).mapIterator())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(map.AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractSortedBidiMapDecorator, self).tailMap(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedBidiMapDecorator, self).comparator())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__map.AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.inverseBidiMap()"""
        return 'collections4.SortedBidiMap'.__wrap(super(AbstractSortedBidiMapDecorator, self).inverseBidiMap())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).removeValue(arg0))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.headMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractSortedBidiMapDecorator, self).headMap(arg0))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__map.AbstractMapDecorator, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__AbstractSortedBidiMapDecorator, self).subMap(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(map.AbstractMapDecorator, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__map.AbstractMapDecorator, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_Values
__Values = __AbstractDualBidiMap_Values.Values
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_View
__View = __AbstractDualBidiMap_View.View
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
 
class Values(__View, View, __Set, Set):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool.__wrap(super(__View, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__View, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).retainAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__View, self).removeAll(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int.__wrap(super(View, self).hashCode())

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
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values.iterator()"""
        return 'Iterator'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values.contains(java.lang.Object)"""
        return bool.__wrap(super(__Values, self).contains(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values.remove(java.lang.Object)"""
        return bool.__wrap(super(__Values, self).remove(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_BidiMapIterator
__BidiMapIterator = __AbstractDualBidiMap_BidiMapIterator.BidiMapIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BidiMapIterator(pyapache.__MapIterator, collections4.MapIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.BidiMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __BidiMapIterator) -> 'BidiMapIterator':
        return BidiMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BidiMapIterator):
        """
        Dynamic initializer for BidiMapIterator.
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
    def reset(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.reset()"""
        super(BidiMapIterator, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.remove()"""
        super(BidiMapIterator, self).remove()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.hasNext()"""
        return bool.__wrap(super(BidiMapIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.next()"""
        return object.__wrap(super(BidiMapIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.toString()"""
        return str.__wrap(super(BidiMapIterator, self).toString())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.getValue()"""
        return object.__wrap(super(BidiMapIterator, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.getKey()"""
        return object.__wrap(super(BidiMapIterator, self).getKey())

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

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.setValue(V)"""
        return object.__wrap(super(__BidiMapIterator, self).setValue(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap
__AbstractDualBidiMap = __AbstractDualBidiMap
import org.apache.commons.collections4.OrderedBidiMap as __OrderedBidiMap
__OrderedBidiMap = __OrderedBidiMap
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as __DualTreeBidiMap
__DualTreeBidiMap = __DualTreeBidiMap
import org.apache.commons.collections4.SortedBidiMap as __SortedBidiMap
__SortedBidiMap = __SortedBidiMap
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class DualTreeBidiMap(__AbstractDualBidiMap, AbstractDualBidiMap, pyapache.__SortedBidiMap, collections4.SortedBidiMap, __Serializable, Serializable):
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __DualTreeBidiMap) -> 'DualTreeBidiMap':
        return DualTreeBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DualTreeBidiMap):
        """
        Dynamic initializer for DualTreeBidiMap.
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
    def inverseOrderedBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.inverseOrderedBidiMap()"""
        return 'collections4.OrderedBidiMap'.__wrap(super(DualTreeBidiMap, self).inverseOrderedBidiMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str.__wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.inverseBidiMap()"""
        return 'collections4.SortedBidiMap'.__wrap(super(DualTreeBidiMap, self).inverseBidiMap())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__DualTreeBidiMap, self).tailMap(arg0))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = __DualTreeBidiMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap()"""
        val = __DualTreeBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.firstKey()"""
        return object.__wrap(super(DualTreeBidiMap, self).firstKey())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Comparator'):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap(java.util.Comparator<? super K>,java.util.Comparator<? super V>)"""
        val = __DualTreeBidiMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.nextKey(K)"""
        return object.__wrap(super(__DualTreeBidiMap, self).nextKey(arg0))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.comparator()"""
        return 'Comparator'.__wrap(super(DualTreeBidiMap, self).comparator())

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__DualTreeBidiMap, self).subMap(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def valueComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.valueComparator()"""
        return 'Comparator'.__wrap(super(DualTreeBidiMap, self).valueComparator())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int.__wrap(super(AbstractDualBidiMap, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(DualTreeBidiMap, self).mapIterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool.__wrap(super(AbstractDualBidiMap, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.previousKey(K)"""
        return object.__wrap(super(__DualTreeBidiMap, self).previousKey(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap()"""
        val = __DualTreeBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsValue(arg0))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__DualTreeBidiMap, self).headMap(arg0))

    @overload
    def inverseSortedBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.inverseSortedBidiMap()"""
        return 'collections4.SortedBidiMap'.__wrap(super(DualTreeBidiMap, self).inverseSortedBidiMap())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.lastKey()"""
        return object.__wrap(super(DualTreeBidiMap, self).lastKey())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int.__wrap(super(AbstractDualBidiMap, self).size())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).keySet())

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).values())

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).getKey(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as __DualTreeBidiMap_BidiOrderedMapIterator
__BidiOrderedMapIterator = __DualTreeBidiMap_BidiOrderedMapIterator.BidiOrderedMapIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BidiOrderedMapIterator(pyapache.__OrderedMapIterator, collections4.OrderedMapIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap.BidiOrderedMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __BidiOrderedMapIterator) -> 'BidiOrderedMapIterator':
        return BidiOrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BidiOrderedMapIterator):
        """
        Dynamic initializer for BidiOrderedMapIterator.
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
    def previous(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.previous()"""
        return object.__wrap(super(BidiOrderedMapIterator, self).previous())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.getValue()"""
        return object.__wrap(super(BidiOrderedMapIterator, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.reset()"""
        super(BidiOrderedMapIterator, self).reset()

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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.hasPrevious()"""
        return bool.__wrap(super(BidiOrderedMapIterator, self).hasPrevious())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.next()"""
        return object.__wrap(super(BidiOrderedMapIterator, self).next())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.setValue(V)"""
        return object.__wrap(super(__BidiOrderedMapIterator, self).setValue(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.hasNext()"""
        return bool.__wrap(super(BidiOrderedMapIterator, self).hasNext())

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

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.getKey()"""
        return object.__wrap(super(BidiOrderedMapIterator, self).getKey())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.toString()"""
        return str.__wrap(super(BidiOrderedMapIterator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.remove()"""
        super(BidiOrderedMapIterator, self).remove() 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap
__AbstractDualBidiMap = __AbstractDualBidiMap
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractDualBidiMap(ABC, pyapache.__BidiMap, collections4.BidiMap):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractDualBidiMap) -> 'AbstractDualBidiMap':
        return AbstractDualBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractDualBidiMap):
        """
        Dynamic initializer for AbstractDualBidiMap.
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
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str.__wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int.__wrap(super(AbstractDualBidiMap, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'.__wrap(super(AbstractDualBidiMap, self).inverseBidiMap())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool.__wrap(super(AbstractDualBidiMap, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractDualBidiMap, self).mapIterator())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int.__wrap(super(AbstractDualBidiMap, self).size())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).keySet())

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).values())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).getKey(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualHashBidiMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap
__AbstractDualBidiMap = __AbstractDualBidiMap
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.bidimap.DualHashBidiMap as __DualHashBidiMap
__DualHashBidiMap = __DualHashBidiMap
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class DualHashBidiMap(__AbstractDualBidiMap, AbstractDualBidiMap, __Serializable, Serializable):
    """org.apache.commons.collections4.bidimap.DualHashBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __DualHashBidiMap) -> 'DualHashBidiMap':
        return DualHashBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DualHashBidiMap):
        """
        Dynamic initializer for DualHashBidiMap.
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
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str.__wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int.__wrap(super(AbstractDualBidiMap, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'.__wrap(super(AbstractDualBidiMap, self).inverseBidiMap())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool.__wrap(super(AbstractDualBidiMap, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.DualHashBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = __DualHashBidiMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractDualBidiMap, self).mapIterator())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.DualHashBidiMap()"""
        val = __DualHashBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractDualBidiMap, self).equals(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.DualHashBidiMap()"""
        val = __DualHashBidiMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int.__wrap(super(AbstractDualBidiMap, self).size())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).keySet())

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'.__wrap(super(AbstractDualBidiMap, self).values())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).getKey(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractDualBidiMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$MapEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator as __AbstractMapEntryDecorator
__AbstractMapEntryDecorator = __AbstractMapEntryDecorator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_MapEntry
__MapEntry = __AbstractDualBidiMap_MapEntry.MapEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MapEntry(collections4.__AbstractMapEntryDecorator, keyvalue.AbstractMapEntryDecorator):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.MapEntry"""
 
    @staticmethod
    def __wrap(java_value: __MapEntry) -> 'MapEntry':
        return MapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapEntry):
        """
        Dynamic initializer for MapEntry.
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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getValue()"""
        return object.__wrap(super(keyvalue.AbstractMapEntryDecorator, self).getValue())

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
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__keyvalue.AbstractMapEntryDecorator, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.toString()"""
        return str.__wrap(super(keyvalue.AbstractMapEntryDecorator, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.hashCode()"""
        return int.__wrap(super(keyvalue.AbstractMapEntryDecorator, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$MapEntry.setValue(V)"""
        return object.__wrap(super(__MapEntry, self).setValue(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getKey()"""
        return object.__wrap(super(keyvalue.AbstractMapEntryDecorator, self).getKey())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySetIterator
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as __AbstractDualBidiMap_KeySetIterator
__KeySetIterator = __AbstractDualBidiMap_KeySetIterator.KeySetIterator
from builtins import str
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
 
class KeySetIterator(collections4.__AbstractIteratorDecorator, iterators.AbstractIteratorDecorator):
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.KeySetIterator"""
 
    @staticmethod
    def __wrap(java_value: __KeySetIterator) -> 'KeySetIterator':
        return KeySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeySetIterator):
        """
        Dynamic initializer for KeySetIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySetIterator.remove()"""
        super(KeySetIterator, self).remove()

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySetIterator.next()"""
        return object.__wrap(super(KeySetIterator, self).next())