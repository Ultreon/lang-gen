from __future__ import annotations
from overload import overload


 
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

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.queue.PredicatedQueue as _PredicatedQueue
_PredicatedQueue = _PredicatedQueue
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
import java.util.Queue as Queue
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

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
 
class PredicatedQueue():
    """org.apache.commons.collections4.queue.PredicatedQueue"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedQueue) -> 'PredicatedQueue':
        return PredicatedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedQueue):
        """
        Dynamic initializer for PredicatedQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.element()"""
        return object._wrap(super(PredicatedQueue, self).element())

    @staticmethod
    @overload
    def predicatedQueue(arg0: 'Queue', arg1: 'Predicate') -> 'PredicatedQueue':
        """public static <E> org.apache.commons.collections4.queue.PredicatedQueue<E> org.apache.commons.collections4.queue.PredicatedQueue.predicatedQueue(java.util.Queue<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedQueue._wrap(_PredicatedQueue.predicatedQueue(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.remove()"""
        return object._wrap(super(PredicatedQueue, self).remove())

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.poll()"""
        return object._wrap(super(PredicatedQueue, self).poll())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.PredicatedQueue.offer(E)"""
        return bool._wrap(super(_PredicatedQueue, self).offer(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.peek()"""
        return object._wrap(super(PredicatedQueue, self).peek())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.queue.PredicatedQueue
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

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.queue.PredicatedQueue as _PredicatedQueue
_PredicatedQueue = _PredicatedQueue
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
import java.util.Queue as Queue
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

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
 
class PredicatedQueue():
    """org.apache.commons.collections4.queue.PredicatedQueue"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedQueue) -> 'PredicatedQueue':
        return PredicatedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedQueue):
        """
        Dynamic initializer for PredicatedQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.element()"""
        return object._wrap(super(PredicatedQueue, self).element())

    @staticmethod
    @overload
    def predicatedQueue(arg0: 'Queue', arg1: 'Predicate') -> 'PredicatedQueue':
        """public static <E> org.apache.commons.collections4.queue.PredicatedQueue<E> org.apache.commons.collections4.queue.PredicatedQueue.predicatedQueue(java.util.Queue<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedQueue._wrap(_PredicatedQueue.predicatedQueue(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.remove()"""
        return object._wrap(super(PredicatedQueue, self).remove())

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.poll()"""
        return object._wrap(super(PredicatedQueue, self).poll())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.PredicatedQueue.offer(E)"""
        return bool._wrap(super(_PredicatedQueue, self).offer(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.peek()"""
        return object._wrap(super(PredicatedQueue, self).peek())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.queue.PredicatedQueue 
 
 
# CLASS: org.apache.commons.collections4.queue.UnmodifiableQueue
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.queue.AbstractQueueDecorator as _AbstractQueueDecorator
_AbstractQueueDecorator = _AbstractQueueDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.queue.UnmodifiableQueue as _UnmodifiableQueue
_UnmodifiableQueue = _UnmodifiableQueue
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
import java.util.Queue as Queue
import java.util.Queue as _Queue
_Queue = _Queue
from typing import List
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
 
class UnmodifiableQueue():
    """org.apache.commons.collections4.queue.UnmodifiableQueue"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableQueue) -> 'UnmodifiableQueue':
        return UnmodifiableQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableQueue):
        """
        Dynamic initializer for UnmodifiableQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.offer(E)"""
        return bool._wrap(super(_UnmodifiableQueue, self).offer(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableQueue, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.peek()"""
        return object._wrap(super(AbstractQueueDecorator, self).peek())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableQueue, self).retainAll(arg0))

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableQueue, self).removeIf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableQueue, self).removeAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.queue.UnmodifiableQueue.clear()"""
        super(UnmodifiableQueue, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.queue.UnmodifiableQueue.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableQueue, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableQueue, self).addAll(arg0))

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.UnmodifiableQueue.remove()"""
        return object._wrap(super(UnmodifiableQueue, self).remove())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.add(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableQueue, self).add(arg0))

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.UnmodifiableQueue.poll()"""
        return object._wrap(super(UnmodifiableQueue, self).poll())

    @staticmethod
    @overload
    def unmodifiableQueue(arg0: 'Queue') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.queue.UnmodifiableQueue.unmodifiableQueue(java.util.Queue<? extends E>)"""
        return Queue._wrap(_UnmodifiableQueue.unmodifiableQueue(arg0))

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
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.element()"""
        return object._wrap(super(AbstractQueueDecorator, self).element())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.queue.SynchronizedQueue
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.queue.SynchronizedQueue as _SynchronizedQueue
_SynchronizedQueue = _SynchronizedQueue
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Queue as Queue
import java.util.Iterator as Iterator
from typing import List
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
 
class SynchronizedQueue():
    """org.apache.commons.collections4.queue.SynchronizedQueue"""
 
    @staticmethod
    def _wrap(java_value: _SynchronizedQueue) -> 'SynchronizedQueue':
        return SynchronizedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronizedQueue):
        """
        Dynamic initializer for SynchronizedQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronizedQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronizedQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.poll()"""
        return object._wrap(super(SynchronizedQueue, self).poll())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object]._wrap(super(collection.SynchronizedCollection, self).toArray())

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

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.element()"""
        return object._wrap(super(SynchronizedQueue, self).element())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.queue.SynchronizedQueue.hashCode()"""
        return int._wrap(super(SynchronizedQueue, self).hashCode())

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.remove()"""
        return object._wrap(super(SynchronizedQueue, self).remove())

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

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.peek()"""
        return object._wrap(super(SynchronizedQueue, self).peek())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.SynchronizedQueue.equals(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedQueue, self).equals(arg0))

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
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.SynchronizedQueue.offer(E)"""
        return bool._wrap(super(_SynchronizedQueue, self).offer(arg0))

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

    @staticmethod
    @overload
    def synchronizedQueue(arg0: 'Queue') -> 'SynchronizedQueue':
        """public static <E> org.apache.commons.collections4.queue.SynchronizedQueue<E> org.apache.commons.collections4.queue.SynchronizedQueue.synchronizedQueue(java.util.Queue<E>)"""
        return SynchronizedQueue._wrap(_SynchronizedQueue.synchronizedQueue(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.queue.AbstractQueueDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.queue.AbstractQueueDecorator as _AbstractQueueDecorator
_AbstractQueueDecorator = _AbstractQueueDecorator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
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
 
class AbstractQueueDecorator():
    """org.apache.commons.collections4.queue.AbstractQueueDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractQueueDecorator) -> 'AbstractQueueDecorator':
        return AbstractQueueDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractQueueDecorator):
        """
        Dynamic initializer for AbstractQueueDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractQueueDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractQueueDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.AbstractQueueDecorator.offer(E)"""
        return bool._wrap(super(_AbstractQueueDecorator, self).offer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.peek()"""
        return object._wrap(super(AbstractQueueDecorator, self).peek())

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
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.poll()"""
        return object._wrap(super(AbstractQueueDecorator, self).poll())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.remove()"""
        return object._wrap(super(AbstractQueueDecorator, self).remove())

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
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.element()"""
        return object._wrap(super(AbstractQueueDecorator, self).element())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.queue.CircularFifoQueue
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.queue.CircularFifoQueue as _CircularFifoQueue
_CircularFifoQueue = _CircularFifoQueue
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
 
class CircularFifoQueue():
    """org.apache.commons.collections4.queue.CircularFifoQueue"""
 
    @staticmethod
    def _wrap(java_value: _CircularFifoQueue) -> 'CircularFifoQueue':
        return CircularFifoQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircularFifoQueue):
        """
        Dynamic initializer for CircularFifoQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircularFifoQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircularFifoQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.queue.CircularFifoQueue()"""
        val = _CircularFifoQueue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.queue.CircularFifoQueue(int)"""
        val = _CircularFifoQueue(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.queue.CircularFifoQueue(java.util.Collection<? extends E>)"""
        val = _CircularFifoQueue(arg0)
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

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.element()"""
        return object._wrap(super(CircularFifoQueue, self).element())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.get(int)"""
        return object._wrap(super(_CircularFifoQueue, self).get(_int.valueOf(arg0)))

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

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.isEmpty()"""
        return bool._wrap(super(CircularFifoQueue, self).isEmpty())

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.isFull()"""
        return bool._wrap(super(CircularFifoQueue, self).isFull())

    @overload
    def isAtFullCapacity(self) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.isAtFullCapacity()"""
        return bool._wrap(super(CircularFifoQueue, self).isAtFullCapacity())

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.poll()"""
        return object._wrap(super(CircularFifoQueue, self).poll())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.remove()"""
        return object._wrap(super(CircularFifoQueue, self).remove())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.queue.CircularFifoQueue()"""
        val = _CircularFifoQueue()
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.queue.CircularFifoQueue.size()"""
        return int._wrap(super(CircularFifoQueue, self).size())

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
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.add(E)"""
        return bool._wrap(super(_CircularFifoQueue, self).add(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.queue.CircularFifoQueue.iterator()"""
        return 'Iterator'._wrap(super(CircularFifoQueue, self).iterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.queue.CircularFifoQueue.clear()"""
        super(CircularFifoQueue, self).clear()

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.peek()"""
        return object._wrap(super(CircularFifoQueue, self).peek())

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.offer(E)"""
        return bool._wrap(super(_CircularFifoQueue, self).offer(arg0))

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
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).removeAll(arg0))

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.queue.CircularFifoQueue.maxSize()"""
        return int._wrap(super(CircularFifoQueue, self).maxSize())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.queue.TransformedQueue
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import org.apache.commons.collections4.queue.TransformedQueue as _TransformedQueue
_TransformedQueue = _TransformedQueue
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Queue as Queue
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

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
 
class TransformedQueue():
    """org.apache.commons.collections4.queue.TransformedQueue"""
 
    @staticmethod
    def _wrap(java_value: _TransformedQueue) -> 'TransformedQueue':
        return TransformedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedQueue):
        """
        Dynamic initializer for TransformedQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.TransformedQueue.offer(E)"""
        return bool._wrap(super(_TransformedQueue, self).offer(arg0))

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.element()"""
        return object._wrap(super(TransformedQueue, self).element())

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

    @staticmethod
    @overload
    def transformingQueue(arg0: 'Queue', arg1: 'Transformer') -> 'TransformedQueue':
        """public static <E> org.apache.commons.collections4.queue.TransformedQueue<E> org.apache.commons.collections4.queue.TransformedQueue.transformingQueue(java.util.Queue<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedQueue._wrap(_TransformedQueue.transformingQueue(arg0, arg1))

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
    def transformedQueue(arg0: 'Queue', arg1: 'Transformer') -> 'TransformedQueue':
        """public static <E> org.apache.commons.collections4.queue.TransformedQueue<E> org.apache.commons.collections4.queue.TransformedQueue.transformedQueue(java.util.Queue<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedQueue._wrap(_TransformedQueue.transformedQueue(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.peek()"""
        return object._wrap(super(TransformedQueue, self).peek())

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

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.poll()"""
        return object._wrap(super(TransformedQueue, self).poll())

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
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.remove()"""
        return object._wrap(super(TransformedQueue, self).remove())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())