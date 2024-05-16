from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_LinkedSubListIterator
__LinkedSubListIterator = __AbstractLinkedList_LinkedSubListIterator.LinkedSubListIterator
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_LinkedListIterator
__LinkedListIterator = __AbstractLinkedList_LinkedListIterator.LinkedListIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinkedSubListIterator():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedSubListIterator"""
 
    @staticmethod
    def __wrap(java_value: __LinkedSubListIterator) -> 'LinkedSubListIterator':
        return LinkedSubListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedSubListIterator):
        """
        Dynamic initializer for LinkedSubListIterator.
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
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previousIndex()"""
        return int.__wrap(super(LinkedListIterator, self).previousIndex())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.hasNext()"""
        return bool.__wrap(super(LinkedSubListIterator, self).hasNext())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.nextIndex()"""
        return int.__wrap(super(LinkedSubListIterator, self).nextIndex())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.hasPrevious()"""
        return bool.__wrap(super(LinkedSubListIterator, self).hasPrevious())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.next()"""
        return object.__wrap(super(LinkedListIterator, self).next())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previous()"""
        return object.__wrap(super(LinkedListIterator, self).previous())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.set(E)"""
        super(__LinkedListIterator, self).set(arg0)

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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.add(E)"""
        super(__LinkedSubListIterator, self).add(arg0)

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

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.remove()"""
        super(LinkedSubListIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_LinkedSubListIterator
__LinkedSubListIterator = __AbstractLinkedList_LinkedSubListIterator.LinkedSubListIterator
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_LinkedListIterator
__LinkedListIterator = __AbstractLinkedList_LinkedListIterator.LinkedListIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinkedSubListIterator():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedSubListIterator"""
 
    @staticmethod
    def __wrap(java_value: __LinkedSubListIterator) -> 'LinkedSubListIterator':
        return LinkedSubListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedSubListIterator):
        """
        Dynamic initializer for LinkedSubListIterator.
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
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previousIndex()"""
        return int.__wrap(super(LinkedListIterator, self).previousIndex())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.hasNext()"""
        return bool.__wrap(super(LinkedSubListIterator, self).hasNext())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.nextIndex()"""
        return int.__wrap(super(LinkedSubListIterator, self).nextIndex())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.hasPrevious()"""
        return bool.__wrap(super(LinkedSubListIterator, self).hasPrevious())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.next()"""
        return object.__wrap(super(LinkedListIterator, self).next())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previous()"""
        return object.__wrap(super(LinkedListIterator, self).previous())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.set(E)"""
        super(__LinkedListIterator, self).set(arg0)

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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.add(E)"""
        super(__LinkedSubListIterator, self).add(arg0)

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

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.remove()"""
        super(LinkedSubListIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator 
 
 
# CLASS: org.apache.commons.collections4.list.TreeList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
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
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.list.TreeList as __TreeList
__TreeList = __TreeList
import java.util.AbstractList as __AbstractList
__AbstractList = __AbstractList
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class TreeList():
    """org.apache.commons.collections4.list.TreeList"""
 
    @staticmethod
    def __wrap(java_value: __TreeList) -> 'TreeList':
        return TreeList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeList):
        """
        Dynamic initializer for TreeList.
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
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.TreeList.size()"""
        return int.__wrap(super(TreeList, self).size())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.AbstractList.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.TreeList.clear()"""
        super(TreeList, self).clear()

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TreeList.get(int)"""
        return object.__wrap(super(__TreeList, self).get(__int.valueOf(arg0)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.TreeList.contains(java.lang.Object)"""
        return bool.__wrap(super(__TreeList, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.AbstractList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.TreeList()"""
        val = __TreeList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractCollection, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractList, self).equals(arg0))

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.TreeList.iterator()"""
        return 'Iterator'.__wrap(super(TreeList, self).iterator())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.TreeList.set(int,E)"""
        return object.__wrap(super(__TreeList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.TreeList.add(int,E)"""
        super(__TreeList, self).add(__int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).removeAll(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.list.TreeList(java.util.Collection<? extends E>)"""
        val = __TreeList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TreeList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__TreeList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractList.hashCode()"""
        return int.__wrap(super(AbstractList, self).hashCode())

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.TreeList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__TreeList, self).addAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TreeList.remove(int)"""
        return object.__wrap(super(__TreeList, self).remove(__int.valueOf(arg0)))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.add(E)"""
        return bool.__wrap(super(__AbstractList, self).add(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.TreeList.toArray()"""
        return List[object].__wrap(super(TreeList, self).toArray())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.AbstractList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractList, self).lastIndexOf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.TreeList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__TreeList, self).indexOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TreeList.listIterator()"""
        return 'ListIterator'.__wrap(super(TreeList, self).listIterator())

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
    def __init__(self, ):
        """public org.apache.commons.collections4.list.TreeList()"""
        val = __TreeList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractSerializableListDecorator
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.list.AbstractSerializableListDecorator as __AbstractSerializableListDecorator
__AbstractSerializableListDecorator = __AbstractSerializableListDecorator
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class AbstractSerializableListDecorator(ABC):
    """org.apache.commons.collections4.list.AbstractSerializableListDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSerializableListDecorator) -> 'AbstractSerializableListDecorator':
        return AbstractSerializableListDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSerializableListDecorator):
        """
        Dynamic initializer for AbstractSerializableListDecorator.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractListDecorator.add(int,E)"""
        super(__AbstractListDecorator, self).add(__int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractListDecorator, self).listIterator())

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).remove(__int.valueOf(arg0)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.set(int,E)"""
        return object.__wrap(super(__AbstractListDecorator, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractListDecorator, self).addAll(__int.valueOf(arg0), arg1))

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).indexOf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractListDecorator, self).listIterator(__int.valueOf(arg0)))

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
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractListDecorator.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractListDecorator, self).subList(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.collections4.list.TransformedList$TransformedListIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.iterators.AbstractListIteratorDecorator as __AbstractListIteratorDecorator
__AbstractListIteratorDecorator = __AbstractListIteratorDecorator
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
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.list.TransformedList as __TransformedList_TransformedListIterator
__TransformedListIterator = __TransformedList_TransformedListIterator.TransformedListIterator
from builtins import int
 
class TransformedListIterator():
    """org.apache.commons.collections4.list.TransformedList.TransformedListIterator"""
 
    @staticmethod
    def __wrap(java_value: __TransformedListIterator) -> 'TransformedListIterator':
        return TransformedListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedListIterator):
        """
        Dynamic initializer for TransformedListIterator.
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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.TransformedList$TransformedListIterator.add(E)"""
        super(__TransformedListIterator, self).add(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.TransformedList$TransformedListIterator.set(E)"""
        super(__TransformedListIterator, self).set(arg0)

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasNext()"""
        return bool.__wrap(super(iterators.AbstractListIteratorDecorator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasPrevious()"""
        return bool.__wrap(super(iterators.AbstractListIteratorDecorator, self).hasPrevious())

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
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previous()"""
        return object.__wrap(super(iterators.AbstractListIteratorDecorator, self).previous())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.nextIndex()"""
        return int.__wrap(super(iterators.AbstractListIteratorDecorator, self).nextIndex())

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

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.next()"""
        return object.__wrap(super(iterators.AbstractListIteratorDecorator, self).next())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previousIndex()"""
        return int.__wrap(super(iterators.AbstractListIteratorDecorator, self).previousIndex())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.remove()"""
        super(iterators.AbstractListIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.list.LazyList
from pyquantum_helper import import_once as __import_once__
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.list.LazyList as __LazyList
__LazyList = __LazyList
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class LazyList():
    """org.apache.commons.collections4.list.LazyList"""
 
    @staticmethod
    def __wrap(java_value: __LazyList) -> 'LazyList':
        return LazyList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazyList):
        """
        Dynamic initializer for LazyList.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractListDecorator.add(int,E)"""
        super(__AbstractListDecorator, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Transformer') -> 'LazyList':
        """public static <E> org.apache.commons.collections4.list.LazyList<E> org.apache.commons.collections4.list.LazyList.lazyList(java.util.List<E>,org.apache.commons.collections4.Transformer<java.lang.Integer, ? extends E>)"""
        return LazyList.__wrap(__LazyList.lazyList(arg0, arg1))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractListDecorator, self).listIterator())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).remove(__int.valueOf(arg0)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.set(int,E)"""
        return object.__wrap(super(__AbstractListDecorator, self).set(__int.valueOf(arg0), arg1))

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractListDecorator, self).listIterator(__int.valueOf(arg0)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Factory') -> 'LazyList':
        """public static <E> org.apache.commons.collections4.list.LazyList<E> org.apache.commons.collections4.list.LazyList.lazyList(java.util.List<E>,org.apache.commons.collections4.Factory<? extends E>)"""
        return LazyList.__wrap(__LazyList.lazyList(arg0, arg1))

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.LazyList.subList(int,int)"""
        return 'List'.__wrap(super(__LazyList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

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
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractListDecorator, self).addAll(__int.valueOf(arg0), arg1))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.LazyList.get(int)"""
        return object.__wrap(super(__LazyList, self).get(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).indexOf(arg0))

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
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.CursorableLinkedList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import org.apache.commons.collections4.list.CursorableLinkedList as __CursorableLinkedList_Cursor
__Cursor = __CursorableLinkedList_Cursor.Cursor
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.list.CursorableLinkedList as __CursorableLinkedList
__CursorableLinkedList = __CursorableLinkedList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList
__AbstractLinkedList = __AbstractLinkedList
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class CursorableLinkedList():
    """org.apache.commons.collections4.list.CursorableLinkedList"""
 
    @staticmethod
    def __wrap(java_value: __CursorableLinkedList) -> 'CursorableLinkedList':
        return CursorableLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CursorableLinkedList):
        """
        Dynamic initializer for CursorableLinkedList.
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
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).containsAll(arg0))

    @overload
    def cursor(self, arg0: int) -> 'Cursor':
        """public org.apache.commons.collections4.list.CursorableLinkedList$Cursor<E> org.apache.commons.collections4.list.CursorableLinkedList.cursor(int)"""
        return 'Cursor'.__wrap(super(__CursorableLinkedList, self).cursor(__int.valueOf(arg0)))

    @overload
    def cursor(self) -> 'Cursor':
        """public org.apache.commons.collections4.list.CursorableLinkedList$Cursor<E> org.apache.commons.collections4.list.CursorableLinkedList.cursor()"""
        return 'Cursor'.__wrap(super(CursorableLinkedList, self).cursor())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.size()"""
        return int.__wrap(super(AbstractLinkedList, self).size())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractLinkedList, self).lastIndexOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.CursorableLinkedList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__CursorableLinkedList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractLinkedList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).retainAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.list.CursorableLinkedList(java.util.Collection<? extends E>)"""
        val = __CursorableLinkedList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def removeLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeLast()"""
        return object.__wrap(super(AbstractLinkedList, self).removeLast())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.set(int,E)"""
        return object.__wrap(super(__AbstractLinkedList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.add(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).add(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.CursorableLinkedList.iterator()"""
        return 'Iterator'.__wrap(super(CursorableLinkedList, self).iterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.list.AbstractLinkedList.toString()"""
        return str.__wrap(super(AbstractLinkedList, self).toString())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.AbstractLinkedList.toArray()"""
        return List[object].__wrap(super(AbstractLinkedList, self).toArray())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.remove(int)"""
        return object.__wrap(super(__AbstractLinkedList, self).remove(__int.valueOf(arg0)))

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.add(int,E)"""
        super(__AbstractLinkedList, self).add(__int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getLast()"""
        return object.__wrap(super(AbstractLinkedList, self).getLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addFirst(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addFirst(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addFirst(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.hashCode()"""
        return int.__wrap(super(AbstractLinkedList, self).hashCode())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractLinkedList, self).indexOf(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addAll(__int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.list.AbstractLinkedList.toArray(T[])"""
        return List[object].__wrap(super(__AbstractLinkedList, self).toArray(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.get(int)"""
        return object.__wrap(super(__AbstractLinkedList, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.isEmpty()"""
        return bool.__wrap(super(AbstractLinkedList, self).isEmpty())

    @override
    @overload
    def removeFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeFirst()"""
        return object.__wrap(super(AbstractLinkedList, self).removeFirst())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.CursorableLinkedList.listIterator()"""
        return 'ListIterator'.__wrap(super(CursorableLinkedList, self).listIterator())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.CursorableLinkedList()"""
        val = __CursorableLinkedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.clear()"""
        super(AbstractLinkedList, self).clear()

    @overload
    def addLast(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addLast(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addLast(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).remove(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getFirst()"""
        return object.__wrap(super(AbstractLinkedList, self).getFirst())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.list.CursorableLinkedList()"""
        val = __CursorableLinkedList()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).contains(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.CursorableLinkedList$SubCursor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.list.CursorableLinkedList as __CursorableLinkedList_SubCursor
__SubCursor = __CursorableLinkedList_SubCursor.SubCursor
import org.apache.commons.collections4.list.CursorableLinkedList as __CursorableLinkedList_Cursor
__Cursor = __CursorableLinkedList_Cursor.Cursor
import java.util.function.Consumer as Consumer
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
 
class SubCursor():
    """org.apache.commons.collections4.list.CursorableLinkedList.SubCursor"""
 
    @staticmethod
    def __wrap(java_value: __SubCursor) -> 'SubCursor':
        return SubCursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubCursor):
        """
        Dynamic initializer for SubCursor.
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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.add(E)"""
        super(__SubCursor, self).add(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.hasNext()"""
        return bool.__wrap(super(SubCursor, self).hasNext())

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
        """public boolean org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.hasPrevious()"""
        return bool.__wrap(super(SubCursor, self).hasPrevious())

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

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.nextIndex()"""
        return int.__wrap(super(SubCursor, self).nextIndex())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.remove()"""
        super(SubCursor, self).remove()

    @override
    @overload
    def close(self):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$Cursor.close()"""
        super(Cursor, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.list.PredicatedList$PredicatedListIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.iterators.AbstractListIteratorDecorator as __AbstractListIteratorDecorator
__AbstractListIteratorDecorator = __AbstractListIteratorDecorator
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.PredicatedList as __PredicatedList_PredicatedListIterator
__PredicatedListIterator = __PredicatedList_PredicatedListIterator.PredicatedListIterator
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
 
class PredicatedListIterator():
    """org.apache.commons.collections4.list.PredicatedList.PredicatedListIterator"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedListIterator) -> 'PredicatedListIterator':
        return PredicatedListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedListIterator):
        """
        Dynamic initializer for PredicatedListIterator.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasNext()"""
        return bool.__wrap(super(iterators.AbstractListIteratorDecorator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasPrevious()"""
        return bool.__wrap(super(iterators.AbstractListIteratorDecorator, self).hasPrevious())

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
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previous()"""
        return object.__wrap(super(iterators.AbstractListIteratorDecorator, self).previous())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.nextIndex()"""
        return int.__wrap(super(iterators.AbstractListIteratorDecorator, self).nextIndex())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.PredicatedList$PredicatedListIterator.set(E)"""
        super(__PredicatedListIterator, self).set(arg0)

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

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.next()"""
        return object.__wrap(super(iterators.AbstractListIteratorDecorator, self).next())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previousIndex()"""
        return int.__wrap(super(iterators.AbstractListIteratorDecorator, self).previousIndex())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.remove()"""
        super(iterators.AbstractListIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.PredicatedList$PredicatedListIterator.add(E)"""
        super(__PredicatedListIterator, self).add(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.UnmodifiableList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.list.UnmodifiableList as __UnmodifiableList
__UnmodifiableList = __UnmodifiableList
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableList():
    """org.apache.commons.collections4.list.UnmodifiableList"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableList) -> 'UnmodifiableList':
        return UnmodifiableList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableList):
        """
        Dynamic initializer for UnmodifiableList.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__UnmodifiableList, self).removeIf(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.UnmodifiableList.set(int,E)"""
        return object.__wrap(super(__UnmodifiableList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableList, self).retainAll(arg0))

    @staticmethod
    @overload
    def unmodifiableList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.list.UnmodifiableList.unmodifiableList(java.util.List<? extends E>)"""
        return List.__wrap(__UnmodifiableList.unmodifiableList(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.UnmodifiableList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__UnmodifiableList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.UnmodifiableList.add(int,E)"""
        super(__UnmodifiableList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableList, self).addAll(__int.valueOf(arg0), arg1))

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.list.UnmodifiableList(java.util.List<? extends E>)"""
        val = __UnmodifiableList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__UnmodifiableList, self).addAll(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableList, self).removeAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.UnmodifiableList.clear()"""
        super(UnmodifiableList, self).clear()

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.add(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableList, self).add(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.UnmodifiableList.remove(int)"""
        return object.__wrap(super(__UnmodifiableList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.UnmodifiableList.listIterator()"""
        return 'ListIterator'.__wrap(super(UnmodifiableList, self).listIterator())

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.UnmodifiableList.subList(int,int)"""
        return 'List'.__wrap(super(__UnmodifiableList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).indexOf(arg0))

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
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableList, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.UnmodifiableList.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableList, self).iterator())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.PredicatedList
from pyquantum_helper import import_once as __import_once__
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection_Builder
__Builder = __PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.list.PredicatedList as __PredicatedList
__PredicatedList = __PredicatedList
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
import java.util.function.UnaryOperator as UnaryOperator
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
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import org.apache.commons.collections4.collection.PredicatedCollection as __PredicatedCollection
__PredicatedCollection = __PredicatedCollection
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
 
class PredicatedList():
    """org.apache.commons.collections4.list.PredicatedList"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedList) -> 'PredicatedList':
        return PredicatedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedList):
        """
        Dynamic initializer for PredicatedList.
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
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.PredicatedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__PredicatedList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.PredicatedList.listIterator()"""
        return 'ListIterator'.__wrap(super(PredicatedList, self).listIterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object].__wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.PredicatedList.get(int)"""
        return object.__wrap(super(__PredicatedList, self).get(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def predicatedList(arg0: 'List', arg1: 'Predicate') -> 'PredicatedList':
        """public static <T> org.apache.commons.collections4.list.PredicatedList<T> org.apache.commons.collections4.list.PredicatedList.predicatedList(java.util.List<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return PredicatedList.__wrap(__PredicatedList.predicatedList(arg0, arg1))

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

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.PredicatedList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__PredicatedList, self).indexOf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.PredicatedList.subList(int,int)"""
        return 'List'.__wrap(super(__PredicatedList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.PredicatedList.set(int,E)"""
        return object.__wrap(super(__PredicatedList, self).set(__int.valueOf(arg0), arg1))

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.PredicatedList.add(int,E)"""
        super(__PredicatedList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.PredicatedList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__PredicatedList, self).lastIndexOf(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.PredicatedList.hashCode()"""
        return int.__wrap(super(PredicatedList, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder.__wrap(__PredicatedCollection.builder(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

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

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.PredicatedList.remove(int)"""
        return object.__wrap(super(__PredicatedList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.PredicatedList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__PredicatedList, self).listIterator(__int.valueOf(arg0)))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.PredicatedList.equals(java.lang.Object)"""
        return bool.__wrap(super(__PredicatedList, self).equals(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection.__wrap(__PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
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
import java.util.function.UnaryOperator as UnaryOperator
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
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList
__AbstractLinkedList = __AbstractLinkedList
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class AbstractLinkedList(ABC):
    """org.apache.commons.collections4.list.AbstractLinkedList"""
 
    @staticmethod
    def __wrap(java_value: __AbstractLinkedList) -> 'AbstractLinkedList':
        return AbstractLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractLinkedList):
        """
        Dynamic initializer for AbstractLinkedList.
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
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).containsAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.size()"""
        return int.__wrap(super(AbstractLinkedList, self).size())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractLinkedList, self).lastIndexOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractLinkedList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).retainAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def removeLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeLast()"""
        return object.__wrap(super(AbstractLinkedList, self).removeLast())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.set(int,E)"""
        return object.__wrap(super(__AbstractLinkedList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.add(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).add(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.list.AbstractLinkedList.toString()"""
        return str.__wrap(super(AbstractLinkedList, self).toString())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.AbstractLinkedList.toArray()"""
        return List[object].__wrap(super(AbstractLinkedList, self).toArray())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.remove(int)"""
        return object.__wrap(super(__AbstractLinkedList, self).remove(__int.valueOf(arg0)))

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.add(int,E)"""
        super(__AbstractLinkedList, self).add(__int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).removeAll(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractLinkedList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def getLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getLast()"""
        return object.__wrap(super(AbstractLinkedList, self).getLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addFirst(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addFirst(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addFirst(arg0))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractLinkedList, self).listIterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.hashCode()"""
        return int.__wrap(super(AbstractLinkedList, self).hashCode())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractLinkedList, self).indexOf(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addAll(__int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.list.AbstractLinkedList.toArray(T[])"""
        return List[object].__wrap(super(__AbstractLinkedList, self).toArray(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.get(int)"""
        return object.__wrap(super(__AbstractLinkedList, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.isEmpty()"""
        return bool.__wrap(super(AbstractLinkedList, self).isEmpty())

    @override
    @overload
    def removeFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeFirst()"""
        return object.__wrap(super(AbstractLinkedList, self).removeFirst())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.clear()"""
        super(AbstractLinkedList, self).clear()

    @overload
    def addLast(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addLast(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addLast(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).remove(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getFirst()"""
        return object.__wrap(super(AbstractLinkedList, self).getFirst())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.AbstractLinkedList.iterator()"""
        return 'Iterator'.__wrap(super(AbstractLinkedList, self).iterator())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).contains(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.FixedSizeList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import org.apache.commons.collections4.list.FixedSizeList as __FixedSizeList
__FixedSizeList = __FixedSizeList
import java.util.ListIterator as ListIterator
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
 
class FixedSizeList():
    """org.apache.commons.collections4.list.FixedSizeList"""
 
    @staticmethod
    def __wrap(java_value: __FixedSizeList) -> 'FixedSizeList':
        return FixedSizeList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FixedSizeList):
        """
        Dynamic initializer for FixedSizeList.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.FixedSizeList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__FixedSizeList, self).listIterator(__int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__FixedSizeList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__FixedSizeList, self).lastIndexOf(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__FixedSizeList, self).removeAll(arg0))

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
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.remove(int)"""
        return object.__wrap(super(__FixedSizeList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.FixedSizeList.clear()"""
        super(FixedSizeList, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

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
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.FixedSizeList.subList(int,int)"""
        return 'List'.__wrap(super(__FixedSizeList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.add(E)"""
        return bool.__wrap(super(__FixedSizeList, self).add(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__FixedSizeList, self).addAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.remove(java.lang.Object)"""
        return bool.__wrap(super(__FixedSizeList, self).remove(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.isFull()"""
        return bool.__wrap(super(FixedSizeList, self).isFull())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__FixedSizeList, self).removeIf(arg0))

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.maxSize()"""
        return int.__wrap(super(FixedSizeList, self).maxSize())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__FixedSizeList, self).retainAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.FixedSizeList.listIterator()"""
        return 'ListIterator'.__wrap(super(FixedSizeList, self).listIterator())

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.get(int)"""
        return object.__wrap(super(__FixedSizeList, self).get(__int.valueOf(arg0)))

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.FixedSizeList.iterator()"""
        return 'Iterator'.__wrap(super(FixedSizeList, self).iterator())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.FixedSizeList.add(int,E)"""
        super(__FixedSizeList, self).add(__int.valueOf(arg0), arg1)

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.set(int,E)"""
        return object.__wrap(super(__FixedSizeList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__FixedSizeList, self).indexOf(arg0))

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
    def fixedSizeList(arg0: 'List') -> 'FixedSizeList':
        """public static <E> org.apache.commons.collections4.list.FixedSizeList<E> org.apache.commons.collections4.list.FixedSizeList.fixedSizeList(java.util.List<E>)"""
        return FixedSizeList.__wrap(__FixedSizeList.fixedSizeList(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.GrowthList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.list.GrowthList as __GrowthList
__GrowthList = __GrowthList
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class GrowthList():
    """org.apache.commons.collections4.list.GrowthList"""
 
    @staticmethod
    def __wrap(java_value: __GrowthList) -> 'GrowthList':
        return GrowthList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GrowthList):
        """
        Dynamic initializer for GrowthList.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.GrowthList.add(int,E)"""
        super(__GrowthList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.list.GrowthList(int)"""
        val = __GrowthList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.list.GrowthList()"""
        val = __GrowthList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.GrowthList.set(int,E)"""
        return object.__wrap(super(__GrowthList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractListDecorator, self).listIterator())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).remove(__int.valueOf(arg0)))

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractListDecorator, self).listIterator(__int.valueOf(arg0)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

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
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractListDecorator.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractListDecorator, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.GrowthList()"""
        val = __GrowthList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.GrowthList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__GrowthList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @staticmethod
    @overload
    def growthList(arg0: 'List') -> 'GrowthList':
        """public static <E> org.apache.commons.collections4.list.GrowthList<E> org.apache.commons.collections4.list.GrowthList.growthList(java.util.List<E>)"""
        return GrowthList.__wrap(__GrowthList.growthList(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).indexOf(arg0))

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
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.NodeCachingLinkedList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
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
import org.apache.commons.collections4.list.NodeCachingLinkedList as __NodeCachingLinkedList
__NodeCachingLinkedList = __NodeCachingLinkedList
import java.util.function.UnaryOperator as UnaryOperator
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
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList
__AbstractLinkedList = __AbstractLinkedList
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class NodeCachingLinkedList():
    """org.apache.commons.collections4.list.NodeCachingLinkedList"""
 
    @staticmethod
    def __wrap(java_value: __NodeCachingLinkedList) -> 'NodeCachingLinkedList':
        return NodeCachingLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodeCachingLinkedList):
        """
        Dynamic initializer for NodeCachingLinkedList.
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
    def __init__(self):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList()"""
        val = __NodeCachingLinkedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).containsAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.size()"""
        return int.__wrap(super(AbstractLinkedList, self).size())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractLinkedList, self).lastIndexOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractLinkedList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).retainAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def removeLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeLast()"""
        return object.__wrap(super(AbstractLinkedList, self).removeLast())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.set(int,E)"""
        return object.__wrap(super(__AbstractLinkedList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.add(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).add(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.list.AbstractLinkedList.toString()"""
        return str.__wrap(super(AbstractLinkedList, self).toString())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.AbstractLinkedList.toArray()"""
        return List[object].__wrap(super(AbstractLinkedList, self).toArray())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.remove(int)"""
        return object.__wrap(super(__AbstractLinkedList, self).remove(__int.valueOf(arg0)))

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
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList(int)"""
        val = __NodeCachingLinkedList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.add(int,E)"""
        super(__AbstractLinkedList, self).add(__int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).removeAll(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList(java.util.Collection<? extends E>)"""
        val = __NodeCachingLinkedList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractLinkedList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def getLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getLast()"""
        return object.__wrap(super(AbstractLinkedList, self).getLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addFirst(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addFirst(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addFirst(arg0))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractLinkedList, self).listIterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.hashCode()"""
        return int.__wrap(super(AbstractLinkedList, self).hashCode())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractLinkedList, self).indexOf(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addAll(__int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.list.AbstractLinkedList.toArray(T[])"""
        return List[object].__wrap(super(__AbstractLinkedList, self).toArray(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.get(int)"""
        return object.__wrap(super(__AbstractLinkedList, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.isEmpty()"""
        return bool.__wrap(super(AbstractLinkedList, self).isEmpty())

    @override
    @overload
    def removeFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeFirst()"""
        return object.__wrap(super(AbstractLinkedList, self).removeFirst())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.clear()"""
        super(AbstractLinkedList, self).clear()

    @overload
    def addLast(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addLast(E)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addLast(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).remove(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getFirst()"""
        return object.__wrap(super(AbstractLinkedList, self).getFirst())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.AbstractLinkedList.iterator()"""
        return 'Iterator'.__wrap(super(AbstractLinkedList, self).iterator())

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
    def __init__(self, ):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList()"""
        val = __NodeCachingLinkedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractLinkedList, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedList, self).contains(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_LinkedSubList
__LinkedSubList = __AbstractLinkedList_LinkedSubList.LinkedSubList
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
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.AbstractList as __AbstractList
__AbstractList = __AbstractList
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class LinkedSubList():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedSubList"""
 
    @staticmethod
    def __wrap(java_value: __LinkedSubList) -> 'LinkedSubList':
        return LinkedSubList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedSubList):
        """
        Dynamic initializer for LinkedSubList.
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
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.clear()"""
        super(LinkedSubList, self).clear()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.add(int,E)"""
        super(__LinkedSubList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.AbstractList.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractList, self).listIterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.remove(int)"""
        return object.__wrap(super(__LinkedSubList, self).remove(__int.valueOf(arg0)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__LinkedSubList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractList.hashCode()"""
        return int.__wrap(super(AbstractList, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.AbstractList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractList, self).indexOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.add(E)"""
        return bool.__wrap(super(__AbstractList, self).add(arg0))

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.size()"""
        return int.__wrap(super(LinkedSubList, self).size())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.AbstractList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractList, self).lastIndexOf(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.get(int)"""
        return object.__wrap(super(__LinkedSubList, self).get(__int.valueOf(arg0)))

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
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.set(int,E)"""
        return object.__wrap(super(__LinkedSubList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractCollection, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractList, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.iterator()"""
        return 'Iterator'.__wrap(super(LinkedSubList, self).iterator())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__LinkedSubList, self).listIterator(__int.valueOf(arg0)))

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
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.subList(int,int)"""
        return 'List'.__wrap(super(__LinkedSubList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__LinkedSubList, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.list.TransformedList
from pyquantum_helper import import_once as __import_once__
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
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
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
import org.apache.commons.collections4.list.TransformedList as __TransformedList
__TransformedList = __TransformedList
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class TransformedList():
    """org.apache.commons.collections4.list.TransformedList"""
 
    @staticmethod
    def __wrap(java_value: __TransformedList) -> 'TransformedList':
        return TransformedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedList):
        """
        Dynamic initializer for TransformedList.
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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.TransformedList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__TransformedList, self).lastIndexOf(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool.__wrap(super(__collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.TransformedList.add(int,E)"""
        super(__TransformedList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def transformingList(arg0: 'List', arg1: 'Transformer') -> 'TransformedList':
        """public static <E> org.apache.commons.collections4.list.TransformedList<E> org.apache.commons.collections4.list.TransformedList.transformingList(java.util.List<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedList.__wrap(__TransformedList.transformingList(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.TransformedList.subList(int,int)"""
        return 'List'.__wrap(super(__TransformedList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.TransformedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__TransformedList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.TransformedList.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformedList, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TransformedList.get(int)"""
        return object.__wrap(super(__TransformedList, self).get(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection.__wrap(__TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.TransformedList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__TransformedList, self).indexOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TransformedList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__TransformedList, self).listIterator(__int.valueOf(arg0)))

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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TransformedList.remove(int)"""
        return object.__wrap(super(__TransformedList, self).remove(__int.valueOf(arg0)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.TransformedList.hashCode()"""
        return int.__wrap(super(TransformedList, self).hashCode())

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
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TransformedList.listIterator()"""
        return 'ListIterator'.__wrap(super(TransformedList, self).listIterator())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.TransformedList.set(int,E)"""
        return object.__wrap(super(__TransformedList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @staticmethod
    @overload
    def transformedList(arg0: 'List', arg1: 'Transformer') -> 'TransformedList':
        """public static <E> org.apache.commons.collections4.list.TransformedList<E> org.apache.commons.collections4.list.TransformedList.transformedList(java.util.List<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedList.__wrap(__TransformedList.transformedList(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractListDecorator
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
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
 
class AbstractListDecorator(ABC):
    """org.apache.commons.collections4.list.AbstractListDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractListDecorator) -> 'AbstractListDecorator':
        return AbstractListDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractListDecorator):
        """
        Dynamic initializer for AbstractListDecorator.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

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
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

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
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractListDecorator.add(int,E)"""
        super(__AbstractListDecorator, self).add(__int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractListDecorator, self).listIterator())

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).remove(__int.valueOf(arg0)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.set(int,E)"""
        return object.__wrap(super(__AbstractListDecorator, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractListDecorator, self).addAll(__int.valueOf(arg0), arg1))

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).indexOf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractListDecorator, self).listIterator(__int.valueOf(arg0)))

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
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractListDecorator.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractListDecorator, self).subList(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator
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
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_LinkedListIterator
__LinkedListIterator = __AbstractLinkedList_LinkedListIterator.LinkedListIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinkedListIterator():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedListIterator"""
 
    @staticmethod
    def __wrap(java_value: __LinkedListIterator) -> 'LinkedListIterator':
        return LinkedListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedListIterator):
        """
        Dynamic initializer for LinkedListIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.hasNext()"""
        return bool.__wrap(super(LinkedListIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.add(E)"""
        super(__LinkedListIterator, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previousIndex()"""
        return int.__wrap(super(LinkedListIterator, self).previousIndex())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.nextIndex()"""
        return int.__wrap(super(LinkedListIterator, self).nextIndex())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.next()"""
        return object.__wrap(super(LinkedListIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.remove()"""
        super(LinkedListIterator, self).remove()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previous()"""
        return object.__wrap(super(LinkedListIterator, self).previous())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.set(E)"""
        super(__LinkedListIterator, self).set(arg0)

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
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.hasPrevious()"""
        return bool.__wrap(super(LinkedListIterator, self).hasPrevious())

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
 
 
# CLASS: org.apache.commons.collections4.list.SetUniqueList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
import org.apache.commons.collections4.list.SetUniqueList as __SetUniqueList
__SetUniqueList = __SetUniqueList
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.AbstractListDecorator as __AbstractListDecorator
__AbstractListDecorator = __AbstractListDecorator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SetUniqueList():
    """org.apache.commons.collections4.list.SetUniqueList"""
 
    @staticmethod
    def __wrap(java_value: __SetUniqueList) -> 'SetUniqueList':
        return SetUniqueList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetUniqueList):
        """
        Dynamic initializer for SetUniqueList.
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
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int.__wrap(super(AbstractListDecorator, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__SetUniqueList, self).addAll(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.SetUniqueList.remove(int)"""
        return object.__wrap(super(__SetUniqueList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.SetUniqueList.listIterator()"""
        return 'ListIterator'.__wrap(super(SetUniqueList, self).listIterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__SetUniqueList, self).containsAll(arg0))

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
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.SetUniqueList.clear()"""
        super(SetUniqueList, self).clear()

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.SetUniqueList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__SetUniqueList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__SetUniqueList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.SetUniqueList.add(int,E)"""
        super(__SetUniqueList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.SetUniqueList.iterator()"""
        return 'Iterator'.__wrap(super(SetUniqueList, self).iterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__SetUniqueList, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object].__wrap(super(__collection.AbstractCollectionDecorator, self).toArray(arg0))

    @staticmethod
    @overload
    def setUniqueList(arg0: 'List') -> 'SetUniqueList':
        """public static <E> org.apache.commons.collections4.list.SetUniqueList<E> org.apache.commons.collections4.list.SetUniqueList.setUniqueList(java.util.List<E>)"""
        return SetUniqueList.__wrap(__SetUniqueList.setUniqueList(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.add(E)"""
        return bool.__wrap(super(__SetUniqueList, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).lastIndexOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.remove(java.lang.Object)"""
        return bool.__wrap(super(__SetUniqueList, self).remove(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.contains(java.lang.Object)"""
        return bool.__wrap(super(__SetUniqueList, self).contains(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.SetUniqueList.subList(int,int)"""
        return 'List'.__wrap(super(__SetUniqueList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractListDecorator, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int.__wrap(super(__AbstractListDecorator, self).indexOf(arg0))

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
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.SetUniqueList.set(int,E)"""
        return object.__wrap(super(__SetUniqueList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__SetUniqueList, self).removeAll(arg0))

    @overload
    def asSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.list.SetUniqueList.asSet()"""
        return 'Set'.__wrap(super(SetUniqueList, self).asSet())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object.__wrap(super(__AbstractListDecorator, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__SetUniqueList, self).retainAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$Node
import org.apache.commons.collections4.list.AbstractLinkedList as __AbstractLinkedList_Node
__Node = __AbstractLinkedList_Node.Node
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Node():
    """org.apache.commons.collections4.list.AbstractLinkedList.Node"""
 
    @staticmethod
    def __wrap(java_value: __Node) -> 'Node':
        return Node(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Node):
        """
        Dynamic initializer for Node.
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.list.CursorableLinkedList$Cursor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.list.CursorableLinkedList as __CursorableLinkedList_Cursor
__Cursor = __CursorableLinkedList_Cursor.Cursor
import java.util.function.Consumer as Consumer
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
 
class Cursor():
    """org.apache.commons.collections4.list.CursorableLinkedList.Cursor"""
 
    @staticmethod
    def __wrap(java_value: __Cursor) -> 'Cursor':
        return Cursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cursor):
        """
        Dynamic initializer for Cursor.
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
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.CursorableLinkedList$Cursor.nextIndex()"""
        return int.__wrap(super(Cursor, self).nextIndex())

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

    @overload
    def close(self):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$Cursor.close()"""
        super(Cursor, self).close()

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
    def remove(self):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$Cursor.remove()"""
        super(Cursor, self).remove()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$Cursor.add(E)"""
        super(__Cursor, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))