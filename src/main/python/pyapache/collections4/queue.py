from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.queue.AbstractQueueDecorator as __AbstractQueueDecorator
__AbstractQueueDecorator = __AbstractQueueDecorator
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
 
class AbstractQueueDecorator(ABC, collections4.__AbstractCollectionDecorator, collection.AbstractCollectionDecorator, __Queue, Queue):
    """org.apache.commons.collections4.queue.AbstractQueueDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractQueueDecorator) -> 'AbstractQueueDecorator':
        return AbstractQueueDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractQueueDecorator):
        """
        Dynamic initializer for AbstractQueueDecorator.
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
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.peek()"""
        return object.__wrap(super(AbstractQueueDecorator, self).peek())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.element()"""
        return object.__wrap(super(AbstractQueueDecorator, self).element())

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

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.AbstractQueueDecorator.offer(E)"""
        return bool.__wrap(super(__AbstractQueueDecorator, self).offer(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.remove()"""
        return object.__wrap(super(AbstractQueueDecorator, self).remove())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.poll()"""
        return object.__wrap(super(AbstractQueueDecorator, self).poll())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: org.apache.commons.collections4.queue.AbstractQueueDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.queue.AbstractQueueDecorator as __AbstractQueueDecorator
__AbstractQueueDecorator = __AbstractQueueDecorator
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
 
class AbstractQueueDecorator(ABC, collections4.__AbstractCollectionDecorator, collection.AbstractCollectionDecorator, __Queue, Queue):
    """org.apache.commons.collections4.queue.AbstractQueueDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractQueueDecorator) -> 'AbstractQueueDecorator':
        return AbstractQueueDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractQueueDecorator):
        """
        Dynamic initializer for AbstractQueueDecorator.
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
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.peek()"""
        return object.__wrap(super(AbstractQueueDecorator, self).peek())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.element()"""
        return object.__wrap(super(AbstractQueueDecorator, self).element())

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

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.AbstractQueueDecorator.offer(E)"""
        return bool.__wrap(super(__AbstractQueueDecorator, self).offer(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.remove()"""
        return object.__wrap(super(AbstractQueueDecorator, self).remove())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.poll()"""
        return object.__wrap(super(AbstractQueueDecorator, self).poll())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: org.apache.commons.collections4.queue.AbstractQueueDecorator 
 
 
# CLASS: org.apache.commons.collections4.queue.UnmodifiableQueue
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.queue.AbstractQueueDecorator as __AbstractQueueDecorator
__AbstractQueueDecorator = __AbstractQueueDecorator
from builtins import type
import org.apache.commons.collections4.queue.UnmodifiableQueue as __UnmodifiableQueue
__UnmodifiableQueue = __UnmodifiableQueue
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
from builtins import object
import java.util.Iterator as Iterator
import java.util.Queue as Queue
import java.util.Queue as __Queue
__Queue = __Queue
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
 
class UnmodifiableQueue(__AbstractQueueDecorator, AbstractQueueDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.queue.UnmodifiableQueue"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableQueue) -> 'UnmodifiableQueue':
        return UnmodifiableQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableQueue):
        """
        Dynamic initializer for UnmodifiableQueue.
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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.add(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).add(arg0))

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

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.queue.UnmodifiableQueue.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableQueue, self).iterator())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).removeIf(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).removeAll(arg0))

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
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.peek()"""
        return object.__wrap(super(AbstractQueueDecorator, self).peek())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.AbstractQueueDecorator.element()"""
        return object.__wrap(super(AbstractQueueDecorator, self).element())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).addAll(arg0))

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
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.UnmodifiableQueue.remove()"""
        return object.__wrap(super(UnmodifiableQueue, self).remove())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.queue.UnmodifiableQueue.clear()"""
        super(UnmodifiableQueue, self).clear()

    @staticmethod
    @overload
    def unmodifiableQueue(arg0: 'Queue') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.queue.UnmodifiableQueue.unmodifiableQueue(java.util.Queue<? extends E>)"""
        return Queue.__wrap(__UnmodifiableQueue.unmodifiableQueue(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.offer(E)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).offer(arg0))

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.queue.UnmodifiableQueue.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableQueue, self).retainAll(arg0))

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
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.UnmodifiableQueue.poll()"""
        return object.__wrap(super(UnmodifiableQueue, self).poll()) 
 
 
# CLASS: org.apache.commons.collections4.queue.TransformedQueue
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
import org.apache.commons.collections4.queue.TransformedQueue as __TransformedQueue
__TransformedQueue = __TransformedQueue
from builtins import object
import java.util.Queue as Queue
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class TransformedQueue(collections4.__TransformedCollection, collection.TransformedCollection, __Queue, Queue):
    """org.apache.commons.collections4.queue.TransformedQueue"""
 
    @staticmethod
    def __wrap(java_value: __TransformedQueue) -> 'TransformedQueue':
        return TransformedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedQueue):
        """
        Dynamic initializer for TransformedQueue.
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

    @staticmethod
    @overload
    def transformedQueue(arg0: 'Queue', arg1: 'Transformer') -> 'TransformedQueue':
        """public static <E> org.apache.commons.collections4.queue.TransformedQueue<E> org.apache.commons.collections4.queue.TransformedQueue.transformedQueue(java.util.Queue<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedQueue.__wrap(__TransformedQueue.transformedQueue(arg0, arg1))

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
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.poll()"""
        return object.__wrap(super(TransformedQueue, self).poll())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def transformingQueue(arg0: 'Queue', arg1: 'Transformer') -> 'TransformedQueue':
        """public static <E> org.apache.commons.collections4.queue.TransformedQueue<E> org.apache.commons.collections4.queue.TransformedQueue.transformingQueue(java.util.Queue<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedQueue.__wrap(__TransformedQueue.transformingQueue(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.element()"""
        return object.__wrap(super(TransformedQueue, self).element())

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.remove()"""
        return object.__wrap(super(TransformedQueue, self).remove())

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

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.TransformedQueue.peek()"""
        return object.__wrap(super(TransformedQueue, self).peek())

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
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.TransformedQueue.offer(E)"""
        return bool.__wrap(super(__TransformedQueue, self).offer(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.queue.PredicatedQueue
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
from builtins import object
import org.apache.commons.collections4.queue.PredicatedQueue as __PredicatedQueue
__PredicatedQueue = __PredicatedQueue
import java.util.Queue as Queue
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class PredicatedQueue(collections4.__PredicatedCollection, collection.PredicatedCollection, __Queue, Queue):
    """org.apache.commons.collections4.queue.PredicatedQueue"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedQueue) -> 'PredicatedQueue':
        return PredicatedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedQueue):
        """
        Dynamic initializer for PredicatedQueue.
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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool.__wrap(super(__collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.remove()"""
        return object.__wrap(super(PredicatedQueue, self).remove())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.peek()"""
        return object.__wrap(super(PredicatedQueue, self).peek())

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.poll()"""
        return object.__wrap(super(PredicatedQueue, self).poll())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def predicatedQueue(arg0: 'Queue', arg1: 'Predicate') -> 'PredicatedQueue':
        """public static <E> org.apache.commons.collections4.queue.PredicatedQueue<E> org.apache.commons.collections4.queue.PredicatedQueue.predicatedQueue(java.util.Queue<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedQueue.__wrap(__PredicatedQueue.predicatedQueue(arg0, arg1))

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

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.PredicatedQueue.offer(E)"""
        return bool.__wrap(super(__PredicatedQueue, self).offer(arg0))

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

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.PredicatedQueue.element()"""
        return object.__wrap(super(PredicatedQueue, self).element()) 
 
 
# CLASS: org.apache.commons.collections4.queue.CircularFifoQueue
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
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.queue.CircularFifoQueue as __CircularFifoQueue
__CircularFifoQueue = __CircularFifoQueue
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
 
class CircularFifoQueue(__AbstractCollection, AbstractCollection, __Queue, Queue, pyapache.__BoundedCollection, collections4.BoundedCollection, __Serializable, Serializable):
    """org.apache.commons.collections4.queue.CircularFifoQueue"""
 
    @staticmethod
    def __wrap(java_value: __CircularFifoQueue) -> 'CircularFifoQueue':
        return CircularFifoQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CircularFifoQueue):
        """
        Dynamic initializer for CircularFifoQueue.
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
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.remove()"""
        return object.__wrap(super(CircularFifoQueue, self).remove())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.queue.CircularFifoQueue.iterator()"""
        return 'Iterator'.__wrap(super(CircularFifoQueue, self).iterator())

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
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.queue.CircularFifoQueue.size()"""
        return int.__wrap(super(CircularFifoQueue, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).removeAll(arg0))

    @overload
    def isAtFullCapacity(self) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.isAtFullCapacity()"""
        return bool.__wrap(super(CircularFifoQueue, self).isAtFullCapacity())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.peek()"""
        return object.__wrap(super(CircularFifoQueue, self).peek())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.isFull()"""
        return bool.__wrap(super(CircularFifoQueue, self).isFull())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.queue.CircularFifoQueue()"""
        val = __CircularFifoQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.get(int)"""
        return object.__wrap(super(__CircularFifoQueue, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.element()"""
        return object.__wrap(super(CircularFifoQueue, self).element())

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.queue.CircularFifoQueue.maxSize()"""
        return int.__wrap(super(CircularFifoQueue, self).maxSize())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.add(E)"""
        return bool.__wrap(super(__CircularFifoQueue, self).add(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.queue.CircularFifoQueue(java.util.Collection<? extends E>)"""
        val = __CircularFifoQueue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.isEmpty()"""
        return bool.__wrap(super(CircularFifoQueue, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.queue.CircularFifoQueue(int)"""
        val = __CircularFifoQueue(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.queue.CircularFifoQueue.clear()"""
        super(CircularFifoQueue, self).clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.CircularFifoQueue.poll()"""
        return object.__wrap(super(CircularFifoQueue, self).poll())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractCollection, self).remove(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.CircularFifoQueue.offer(E)"""
        return bool.__wrap(super(__CircularFifoQueue, self).offer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractCollection, self).contains(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.queue.CircularFifoQueue()"""
        val = __CircularFifoQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.queue.SynchronizedQueue
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
import org.apache.commons.collections4.queue.SynchronizedQueue as __SynchronizedQueue
__SynchronizedQueue = __SynchronizedQueue
from builtins import object
import java.util.Queue as Queue
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
 
class SynchronizedQueue(collections4.__SynchronizedCollection, collection.SynchronizedCollection, __Queue, Queue):
    """org.apache.commons.collections4.queue.SynchronizedQueue"""
 
    @staticmethod
    def __wrap(java_value: __SynchronizedQueue) -> 'SynchronizedQueue':
        return SynchronizedQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SynchronizedQueue):
        """
        Dynamic initializer for SynchronizedQueue.
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
    def peek(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.peek()"""
        return object.__wrap(super(SynchronizedQueue, self).peek())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def offer(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.SynchronizedQueue.offer(E)"""
        return bool.__wrap(super(__SynchronizedQueue, self).offer(arg0))

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).remove(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.SynchronizedCollection, self).retainAll(arg0))

    @staticmethod
    @overload
    def synchronizedQueue(arg0: 'Queue') -> 'SynchronizedQueue':
        """public static <E> org.apache.commons.collections4.queue.SynchronizedQueue<E> org.apache.commons.collections4.queue.SynchronizedQueue.synchronizedQueue(java.util.Queue<E>)"""
        return SynchronizedQueue.__wrap(__SynchronizedQueue.synchronizedQueue(arg0))

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
    def element(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.element()"""
        return object.__wrap(super(SynchronizedQueue, self).element())

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

    @override
    @overload
    def poll(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.poll()"""
        return object.__wrap(super(SynchronizedQueue, self).poll())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object].__wrap(super(__collection.SynchronizedCollection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.queue.SynchronizedQueue.hashCode()"""
        return int.__wrap(super(SynchronizedQueue, self).hashCode())

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
    def remove(self) -> object:
        """public E org.apache.commons.collections4.queue.SynchronizedQueue.remove()"""
        return object.__wrap(super(SynchronizedQueue, self).remove())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.queue.SynchronizedQueue.equals(java.lang.Object)"""
        return bool.__wrap(super(__SynchronizedQueue, self).equals(arg0))