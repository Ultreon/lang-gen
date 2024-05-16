from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import org.apache.commons.collections4.list.FixedSizeList as _FixedSizeList
_FixedSizeList = _FixedSizeList
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class FixedSizeList():
    """org.apache.commons.collections4.list.FixedSizeList"""
 
    @staticmethod
    def _wrap(java_value: _FixedSizeList) -> 'FixedSizeList':
        return FixedSizeList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FixedSizeList):
        """
        Dynamic initializer for FixedSizeList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FixedSizeList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FixedSizeList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.FixedSizeList.subList(int,int)"""
        return 'List'._wrap(super(_FixedSizeList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.remove(java.lang.Object)"""
        return bool._wrap(super(_FixedSizeList, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.FixedSizeList.add(int,E)"""
        super(_FixedSizeList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.FixedSizeList.listIterator()"""
        return 'ListIterator'._wrap(super(FixedSizeList, self).listIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.get(int)"""
        return object._wrap(super(_FixedSizeList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.isFull()"""
        return bool._wrap(super(FixedSizeList, self).isFull())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.FixedSizeList.clear()"""
        super(FixedSizeList, self).clear()

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.set(int,E)"""
        return object._wrap(super(_FixedSizeList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.indexOf(java.lang.Object)"""
        return int._wrap(super(_FixedSizeList, self).indexOf(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_FixedSizeList, self).removeIf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.FixedSizeList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_FixedSizeList, self).listIterator(_int.valueOf(arg0)))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_FixedSizeList, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_FixedSizeList, self).addAll(_int.valueOf(arg0), arg1))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_FixedSizeList, self).retainAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_FixedSizeList, self).lastIndexOf(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.maxSize()"""
        return int._wrap(super(FixedSizeList, self).maxSize())

    @staticmethod
    @overload
    def fixedSizeList(arg0: 'List') -> 'FixedSizeList':
        """public static <E> org.apache.commons.collections4.list.FixedSizeList<E> org.apache.commons.collections4.list.FixedSizeList.fixedSizeList(java.util.List<E>)"""
        return FixedSizeList._wrap(_FixedSizeList.fixedSizeList(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.remove(int)"""
        return object._wrap(super(_FixedSizeList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.FixedSizeList.iterator()"""
        return 'Iterator'._wrap(super(FixedSizeList, self).iterator())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_FixedSizeList, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.add(E)"""
        return bool._wrap(super(_FixedSizeList, self).add(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.list.FixedSizeList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import org.apache.commons.collections4.list.FixedSizeList as _FixedSizeList
_FixedSizeList = _FixedSizeList
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class FixedSizeList():
    """org.apache.commons.collections4.list.FixedSizeList"""
 
    @staticmethod
    def _wrap(java_value: _FixedSizeList) -> 'FixedSizeList':
        return FixedSizeList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FixedSizeList):
        """
        Dynamic initializer for FixedSizeList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FixedSizeList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FixedSizeList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.FixedSizeList.subList(int,int)"""
        return 'List'._wrap(super(_FixedSizeList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.remove(java.lang.Object)"""
        return bool._wrap(super(_FixedSizeList, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.FixedSizeList.add(int,E)"""
        super(_FixedSizeList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.FixedSizeList.listIterator()"""
        return 'ListIterator'._wrap(super(FixedSizeList, self).listIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.get(int)"""
        return object._wrap(super(_FixedSizeList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.isFull()"""
        return bool._wrap(super(FixedSizeList, self).isFull())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.FixedSizeList.clear()"""
        super(FixedSizeList, self).clear()

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.set(int,E)"""
        return object._wrap(super(_FixedSizeList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.indexOf(java.lang.Object)"""
        return int._wrap(super(_FixedSizeList, self).indexOf(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_FixedSizeList, self).removeIf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.FixedSizeList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_FixedSizeList, self).listIterator(_int.valueOf(arg0)))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_FixedSizeList, self).addAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_FixedSizeList, self).addAll(_int.valueOf(arg0), arg1))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_FixedSizeList, self).retainAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_FixedSizeList, self).lastIndexOf(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.list.FixedSizeList.maxSize()"""
        return int._wrap(super(FixedSizeList, self).maxSize())

    @staticmethod
    @overload
    def fixedSizeList(arg0: 'List') -> 'FixedSizeList':
        """public static <E> org.apache.commons.collections4.list.FixedSizeList<E> org.apache.commons.collections4.list.FixedSizeList.fixedSizeList(java.util.List<E>)"""
        return FixedSizeList._wrap(_FixedSizeList.fixedSizeList(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.FixedSizeList.remove(int)"""
        return object._wrap(super(_FixedSizeList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.FixedSizeList.iterator()"""
        return 'Iterator'._wrap(super(FixedSizeList, self).iterator())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_FixedSizeList, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.FixedSizeList.add(E)"""
        return bool._wrap(super(_FixedSizeList, self).add(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.list.FixedSizeList 
 
 
# CLASS: org.apache.commons.collections4.list.PredicatedList$PredicatedListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.AbstractListIteratorDecorator as _AbstractListIteratorDecorator
_AbstractListIteratorDecorator = _AbstractListIteratorDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.list.PredicatedList as _PredicatedList_PredicatedListIterator
_PredicatedListIterator = _PredicatedList_PredicatedListIterator.PredicatedListIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedListIterator():
    """org.apache.commons.collections4.list.PredicatedList.PredicatedListIterator"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedListIterator) -> 'PredicatedListIterator':
        return PredicatedListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedListIterator):
        """
        Dynamic initializer for PredicatedListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasNext()"""
        return bool._wrap(super(iterators.AbstractListIteratorDecorator, self).hasNext())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasPrevious()"""
        return bool._wrap(super(iterators.AbstractListIteratorDecorator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.PredicatedList$PredicatedListIterator.set(E)"""
        super(_PredicatedListIterator, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previous()"""
        return object._wrap(super(iterators.AbstractListIteratorDecorator, self).previous())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.PredicatedList$PredicatedListIterator.add(E)"""
        super(_PredicatedListIterator, self).add(arg0)

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
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previousIndex()"""
        return int._wrap(super(iterators.AbstractListIteratorDecorator, self).previousIndex())

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
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.nextIndex()"""
        return int._wrap(super(iterators.AbstractListIteratorDecorator, self).nextIndex())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.next()"""
        return object._wrap(super(iterators.AbstractListIteratorDecorator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.remove()"""
        super(iterators.AbstractListIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$Node
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList_Node
_Node = _AbstractLinkedList_Node.Node
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Node():
    """org.apache.commons.collections4.list.AbstractLinkedList.Node"""
 
    @staticmethod
    def _wrap(java_value: _Node) -> 'Node':
        return Node(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Node):
        """
        Dynamic initializer for Node.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Node__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Node__wrapper":
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList_LinkedListIterator
_LinkedListIterator = _AbstractLinkedList_LinkedListIterator.LinkedListIterator
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinkedListIterator():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedListIterator"""
 
    @staticmethod
    def _wrap(java_value: _LinkedListIterator) -> 'LinkedListIterator':
        return LinkedListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkedListIterator):
        """
        Dynamic initializer for LinkedListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkedListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkedListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previous()"""
        return object._wrap(super(LinkedListIterator, self).previous())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.next()"""
        return object._wrap(super(LinkedListIterator, self).next())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.remove()"""
        super(LinkedListIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.hasNext()"""
        return bool._wrap(super(LinkedListIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.add(E)"""
        super(_LinkedListIterator, self).add(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.hasPrevious()"""
        return bool._wrap(super(LinkedListIterator, self).hasPrevious())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.set(E)"""
        super(_LinkedListIterator, self).set(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.nextIndex()"""
        return int._wrap(super(LinkedListIterator, self).nextIndex())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previousIndex()"""
        return int._wrap(super(LinkedListIterator, self).previousIndex())

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
 
 
# CLASS: org.apache.commons.collections4.list.GrowthList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.list.GrowthList as _GrowthList
_GrowthList = _GrowthList
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GrowthList():
    """org.apache.commons.collections4.list.GrowthList"""
 
    @staticmethod
    def _wrap(java_value: _GrowthList) -> 'GrowthList':
        return GrowthList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GrowthList):
        """
        Dynamic initializer for GrowthList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GrowthList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GrowthList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractListDecorator, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.GrowthList.set(int,E)"""
        return object._wrap(super(_GrowthList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object._wrap(super(_AbstractListDecorator, self).remove(_int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).indexOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @staticmethod
    @overload
    def growthList(arg0: 'List') -> 'GrowthList':
        """public static <E> org.apache.commons.collections4.list.GrowthList<E> org.apache.commons.collections4.list.GrowthList.growthList(java.util.List<E>)"""
        return GrowthList._wrap(_GrowthList.growthList(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.GrowthList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_GrowthList, self).addAll(_int.valueOf(arg0), arg1))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.GrowthList()"""
        val = _GrowthList()
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.list.GrowthList()"""
        val = _GrowthList()
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object._wrap(super(_AbstractListDecorator, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractListDecorator, self).listIterator())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

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

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractListDecorator.subList(int,int)"""
        return 'List'._wrap(super(_AbstractListDecorator, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.GrowthList.add(int,E)"""
        super(_GrowthList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.list.GrowthList(int)"""
        val = _GrowthList(_int.valueOf(arg0))
        self.__wrapper = val

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
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.LazyList
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.list.LazyList as _LazyList
_LazyList = _LazyList
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazyList():
    """org.apache.commons.collections4.list.LazyList"""
 
    @staticmethod
    def _wrap(java_value: _LazyList) -> 'LazyList':
        return LazyList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazyList):
        """
        Dynamic initializer for LazyList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazyList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazyList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractListDecorator, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractListDecorator, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object._wrap(super(_AbstractListDecorator, self).remove(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Factory') -> 'LazyList':
        """public static <E> org.apache.commons.collections4.list.LazyList<E> org.apache.commons.collections4.list.LazyList.lazyList(java.util.List<E>,org.apache.commons.collections4.Factory<? extends E>)"""
        return LazyList._wrap(_LazyList.lazyList(arg0, arg1))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).indexOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.LazyList.get(int)"""
        return object._wrap(super(_LazyList, self).get(_int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.LazyList.subList(int,int)"""
        return 'List'._wrap(super(_LazyList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.set(int,E)"""
        return object._wrap(super(_AbstractListDecorator, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractListDecorator.add(int,E)"""
        super(_AbstractListDecorator, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractListDecorator, self).listIterator())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

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

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Transformer') -> 'LazyList':
        """public static <E> org.apache.commons.collections4.list.LazyList<E> org.apache.commons.collections4.list.LazyList.lazyList(java.util.List<E>,org.apache.commons.collections4.Transformer<java.lang.Integer, ? extends E>)"""
        return LazyList._wrap(_LazyList.lazyList(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.TransformedList$TransformedListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.AbstractListIteratorDecorator as _AbstractListIteratorDecorator
_AbstractListIteratorDecorator = _AbstractListIteratorDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.list.TransformedList as _TransformedList_TransformedListIterator
_TransformedListIterator = _TransformedList_TransformedListIterator.TransformedListIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedListIterator():
    """org.apache.commons.collections4.list.TransformedList.TransformedListIterator"""
 
    @staticmethod
    def _wrap(java_value: _TransformedListIterator) -> 'TransformedListIterator':
        return TransformedListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedListIterator):
        """
        Dynamic initializer for TransformedListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasNext()"""
        return bool._wrap(super(iterators.AbstractListIteratorDecorator, self).hasNext())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasPrevious()"""
        return bool._wrap(super(iterators.AbstractListIteratorDecorator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.TransformedList$TransformedListIterator.set(E)"""
        super(_TransformedListIterator, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previous()"""
        return object._wrap(super(iterators.AbstractListIteratorDecorator, self).previous())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.TransformedList$TransformedListIterator.add(E)"""
        super(_TransformedListIterator, self).add(arg0)

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
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previousIndex()"""
        return int._wrap(super(iterators.AbstractListIteratorDecorator, self).previousIndex())

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
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.nextIndex()"""
        return int._wrap(super(iterators.AbstractListIteratorDecorator, self).nextIndex())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.next()"""
        return object._wrap(super(iterators.AbstractListIteratorDecorator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.remove()"""
        super(iterators.AbstractListIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.list.TreeList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.AbstractList as _AbstractList
_AbstractList = _AbstractList
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import org.apache.commons.collections4.list.TreeList as _TreeList
_TreeList = _TreeList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class TreeList():
    """org.apache.commons.collections4.list.TreeList"""
 
    @staticmethod
    def _wrap(java_value: _TreeList) -> 'TreeList':
        return TreeList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeList):
        """
        Dynamic initializer for TreeList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TreeList.get(int)"""
        return object._wrap(super(_TreeList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.TreeList.size()"""
        return int._wrap(super(TreeList, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.TreeList.indexOf(java.lang.Object)"""
        return int._wrap(super(_TreeList, self).indexOf(arg0))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TreeList.listIterator()"""
        return 'ListIterator'._wrap(super(TreeList, self).listIterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.AbstractList.subList(int,int)"""
        return 'List'._wrap(super(_AbstractList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.TreeList.contains(java.lang.Object)"""
        return bool._wrap(super(_TreeList, self).contains(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.TreeList()"""
        val = _TreeList()
        self.__wrapper = val

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.TreeList.clear()"""
        super(TreeList, self).clear()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.add(E)"""
        return bool._wrap(super(_AbstractList, self).add(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TreeList.remove(int)"""
        return object._wrap(super(_TreeList, self).remove(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.TreeList.set(int,E)"""
        return object._wrap(super(_TreeList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractList, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.AbstractList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.AbstractList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractList, self).lastIndexOf(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.TreeList.iterator()"""
        return 'Iterator'._wrap(super(TreeList, self).iterator())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.list.TreeList()"""
        val = _TreeList()
        self.__wrapper = val

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TreeList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_TreeList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.list.TreeList(java.util.Collection<? extends E>)"""
        val = _TreeList(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractList.hashCode()"""
        return int._wrap(super(AbstractList, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.TreeList.add(int,E)"""
        super(_TreeList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.TreeList.toArray()"""
        return List[object]._wrap(super(TreeList, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).removeAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollection, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.TreeList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_TreeList, self).addAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.SetUniqueList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.list.SetUniqueList as _SetUniqueList
_SetUniqueList = _SetUniqueList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SetUniqueList():
    """org.apache.commons.collections4.list.SetUniqueList"""
 
    @staticmethod
    def _wrap(java_value: _SetUniqueList) -> 'SetUniqueList':
        return SetUniqueList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetUniqueList):
        """
        Dynamic initializer for SetUniqueList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetUniqueList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetUniqueList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_SetUniqueList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.remove(java.lang.Object)"""
        return bool._wrap(super(_SetUniqueList, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_SetUniqueList, self).addAll(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.SetUniqueList.set(int,E)"""
        return object._wrap(super(_SetUniqueList, self).set(_int.valueOf(arg0), arg1))

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
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).indexOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.SetUniqueList.iterator()"""
        return 'Iterator'._wrap(super(SetUniqueList, self).iterator())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.SetUniqueList.clear()"""
        super(SetUniqueList, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_SetUniqueList, self).containsAll(arg0))

    @staticmethod
    @overload
    def setUniqueList(arg0: 'List') -> 'SetUniqueList':
        """public static <E> org.apache.commons.collections4.list.SetUniqueList<E> org.apache.commons.collections4.list.SetUniqueList.setUniqueList(java.util.List<E>)"""
        return SetUniqueList._wrap(_SetUniqueList.setUniqueList(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_SetUniqueList, self).removeIf(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_SetUniqueList, self).removeAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).lastIndexOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.add(E)"""
        return bool._wrap(super(_SetUniqueList, self).add(arg0))

    @overload
    def asSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.list.SetUniqueList.asSet()"""
        return 'Set'._wrap(super(SetUniqueList, self).asSet())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.SetUniqueList.subList(int,int)"""
        return 'List'._wrap(super(_SetUniqueList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.SetUniqueList.listIterator()"""
        return 'ListIterator'._wrap(super(SetUniqueList, self).listIterator())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.SetUniqueList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_SetUniqueList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object._wrap(super(_AbstractListDecorator, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.SetUniqueList.add(int,E)"""
        super(_SetUniqueList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.SetUniqueList.remove(int)"""
        return object._wrap(super(_SetUniqueList, self).remove(_int.valueOf(arg0)))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.contains(java.lang.Object)"""
        return bool._wrap(super(_SetUniqueList, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.SetUniqueList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_SetUniqueList, self).retainAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.UnmodifiableList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.list.UnmodifiableList as _UnmodifiableList
_UnmodifiableList = _UnmodifiableList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableList():
    """org.apache.commons.collections4.list.UnmodifiableList"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableList) -> 'UnmodifiableList':
        return UnmodifiableList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableList):
        """
        Dynamic initializer for UnmodifiableList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def unmodifiableList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.list.UnmodifiableList.unmodifiableList(java.util.List<? extends E>)"""
        return List._wrap(_UnmodifiableList.unmodifiableList(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.UnmodifiableList.remove(int)"""
        return object._wrap(super(_UnmodifiableList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.add(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableList, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableList, self).addAll(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.UnmodifiableList.add(int,E)"""
        super(_UnmodifiableList, self).add(_int.valueOf(arg0), arg1)

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
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.UnmodifiableList.listIterator()"""
        return 'ListIterator'._wrap(super(UnmodifiableList, self).listIterator())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).indexOf(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableList, self).removeIf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.UnmodifiableList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_UnmodifiableList, self).listIterator(_int.valueOf(arg0)))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).lastIndexOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.UnmodifiableList.clear()"""
        super(UnmodifiableList, self).clear()

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.UnmodifiableList.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableList, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object._wrap(super(_AbstractListDecorator, self).get(_int.valueOf(arg0)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableList, self).removeAll(arg0))

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.list.UnmodifiableList(java.util.List<? extends E>)"""
        val = _UnmodifiableList(arg0)
        self.__wrapper = val

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableList, self).remove(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.UnmodifiableList.set(int,E)"""
        return object._wrap(super(_UnmodifiableList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableList, self).retainAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.UnmodifiableList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.UnmodifiableList.subList(int,int)"""
        return 'List'._wrap(super(_UnmodifiableList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList
_AbstractLinkedList = _AbstractLinkedList
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class AbstractLinkedList():
    """org.apache.commons.collections4.list.AbstractLinkedList"""
 
    @staticmethod
    def _wrap(java_value: _AbstractLinkedList) -> 'AbstractLinkedList':
        return AbstractLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractLinkedList):
        """
        Dynamic initializer for AbstractLinkedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractLinkedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractLinkedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addFirst(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addFirst(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).addFirst(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.list.AbstractLinkedList.toArray(T[])"""
        return List[object]._wrap(super(_AbstractLinkedList, self).toArray(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractLinkedList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList.subList(int,int)"""
        return 'List'._wrap(super(_AbstractLinkedList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractLinkedList, self).lastIndexOf(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getLast()"""
        return object._wrap(super(AbstractLinkedList, self).getLast())

    @override
    @overload
    def getFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getFirst()"""
        return object._wrap(super(AbstractLinkedList, self).getFirst())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractLinkedList, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.AbstractLinkedList.toArray()"""
        return List[object]._wrap(super(AbstractLinkedList, self).toArray())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractLinkedList, self).listIterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeLast()"""
        return object._wrap(super(AbstractLinkedList, self).removeLast())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.set(int,E)"""
        return object._wrap(super(_AbstractLinkedList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).retainAll(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractLinkedList, self).indexOf(arg0))

    @overload
    def addLast(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addLast(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).addLast(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.add(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).add(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.size()"""
        return int._wrap(super(AbstractLinkedList, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).removeAll(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).containsAll(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeFirst()"""
        return object._wrap(super(AbstractLinkedList, self).removeFirst())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.clear()"""
        super(AbstractLinkedList, self).clear()

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.hashCode()"""
        return int._wrap(super(AbstractLinkedList, self).hashCode())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.get(int)"""
        return object._wrap(super(_AbstractLinkedList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.add(int,E)"""
        super(_AbstractLinkedList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.remove(int)"""
        return object._wrap(super(_AbstractLinkedList, self).remove(_int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractLinkedList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.list.AbstractLinkedList.toString()"""
        return str._wrap(super(AbstractLinkedList, self).toString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.isEmpty()"""
        return bool._wrap(super(AbstractLinkedList, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.AbstractLinkedList.iterator()"""
        return 'Iterator'._wrap(super(AbstractLinkedList, self).iterator())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.NodeCachingLinkedList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import org.apache.commons.collections4.list.NodeCachingLinkedList as _NodeCachingLinkedList
_NodeCachingLinkedList = _NodeCachingLinkedList
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList
_AbstractLinkedList = _AbstractLinkedList
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class NodeCachingLinkedList():
    """org.apache.commons.collections4.list.NodeCachingLinkedList"""
 
    @staticmethod
    def _wrap(java_value: _NodeCachingLinkedList) -> 'NodeCachingLinkedList':
        return NodeCachingLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NodeCachingLinkedList):
        """
        Dynamic initializer for NodeCachingLinkedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NodeCachingLinkedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NodeCachingLinkedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addFirst(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addFirst(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).addFirst(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.list.AbstractLinkedList.toArray(T[])"""
        return List[object]._wrap(super(_AbstractLinkedList, self).toArray(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractLinkedList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList.subList(int,int)"""
        return 'List'._wrap(super(_AbstractLinkedList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractLinkedList, self).lastIndexOf(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getLast()"""
        return object._wrap(super(AbstractLinkedList, self).getLast())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList(int)"""
        val = _NodeCachingLinkedList(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getFirst()"""
        return object._wrap(super(AbstractLinkedList, self).getFirst())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList()"""
        val = _NodeCachingLinkedList()
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).remove(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList(java.util.Collection<? extends E>)"""
        val = _NodeCachingLinkedList(arg0)
        self.__wrapper = val

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractLinkedList, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.AbstractLinkedList.toArray()"""
        return List[object]._wrap(super(AbstractLinkedList, self).toArray())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractLinkedList, self).listIterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeLast()"""
        return object._wrap(super(AbstractLinkedList, self).removeLast())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.set(int,E)"""
        return object._wrap(super(_AbstractLinkedList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).retainAll(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractLinkedList, self).indexOf(arg0))

    @overload
    def addLast(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addLast(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).addLast(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.add(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).add(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.size()"""
        return int._wrap(super(AbstractLinkedList, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).removeAll(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).containsAll(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeFirst()"""
        return object._wrap(super(AbstractLinkedList, self).removeFirst())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.list.NodeCachingLinkedList()"""
        val = _NodeCachingLinkedList()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.clear()"""
        super(AbstractLinkedList, self).clear()

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.hashCode()"""
        return int._wrap(super(AbstractLinkedList, self).hashCode())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.get(int)"""
        return object._wrap(super(_AbstractLinkedList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.add(int,E)"""
        super(_AbstractLinkedList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.remove(int)"""
        return object._wrap(super(_AbstractLinkedList, self).remove(_int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractLinkedList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.list.AbstractLinkedList.toString()"""
        return str._wrap(super(AbstractLinkedList, self).toString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.isEmpty()"""
        return bool._wrap(super(AbstractLinkedList, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.AbstractLinkedList.iterator()"""
        return 'Iterator'._wrap(super(AbstractLinkedList, self).iterator())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.CursorableLinkedList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.list.CursorableLinkedList as _CursorableLinkedList
_CursorableLinkedList = _CursorableLinkedList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.list.CursorableLinkedList as _CursorableLinkedList_Cursor
_Cursor = _CursorableLinkedList_Cursor.Cursor
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList
_AbstractLinkedList = _AbstractLinkedList
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class CursorableLinkedList():
    """org.apache.commons.collections4.list.CursorableLinkedList"""
 
    @staticmethod
    def _wrap(java_value: _CursorableLinkedList) -> 'CursorableLinkedList':
        return CursorableLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CursorableLinkedList):
        """
        Dynamic initializer for CursorableLinkedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CursorableLinkedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CursorableLinkedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.CursorableLinkedList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_CursorableLinkedList, self).listIterator(_int.valueOf(arg0)))

    @overload
    def addFirst(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addFirst(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).addFirst(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.list.AbstractLinkedList.toArray(T[])"""
        return List[object]._wrap(super(_AbstractLinkedList, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList.subList(int,int)"""
        return 'List'._wrap(super(_AbstractLinkedList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractLinkedList, self).lastIndexOf(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getLast()"""
        return object._wrap(super(AbstractLinkedList, self).getLast())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.CursorableLinkedList.listIterator()"""
        return 'ListIterator'._wrap(super(CursorableLinkedList, self).listIterator())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.CursorableLinkedList.iterator()"""
        return 'Iterator'._wrap(super(CursorableLinkedList, self).iterator())

    @override
    @overload
    def getFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.getFirst()"""
        return object._wrap(super(AbstractLinkedList, self).getFirst())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).remove(arg0))

    @overload
    def cursor(self, arg0: int) -> 'Cursor':
        """public org.apache.commons.collections4.list.CursorableLinkedList$Cursor<E> org.apache.commons.collections4.list.CursorableLinkedList.cursor(int)"""
        return 'Cursor'._wrap(super(_CursorableLinkedList, self).cursor(_int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractLinkedList, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.list.AbstractLinkedList.toArray()"""
        return List[object]._wrap(super(AbstractLinkedList, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeLast()"""
        return object._wrap(super(AbstractLinkedList, self).removeLast())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.list.CursorableLinkedList()"""
        val = _CursorableLinkedList()
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.set(int,E)"""
        return object._wrap(super(_AbstractLinkedList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedList, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).retainAll(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.list.CursorableLinkedList(java.util.Collection<? extends E>)"""
        val = _CursorableLinkedList(arg0)
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractLinkedList, self).indexOf(arg0))

    @overload
    def addLast(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addLast(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).addLast(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.add(E)"""
        return bool._wrap(super(_AbstractLinkedList, self).add(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def cursor(self) -> 'Cursor':
        """public org.apache.commons.collections4.list.CursorableLinkedList$Cursor<E> org.apache.commons.collections4.list.CursorableLinkedList.cursor()"""
        return 'Cursor'._wrap(super(CursorableLinkedList, self).cursor())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.size()"""
        return int._wrap(super(AbstractLinkedList, self).size())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).removeAll(arg0))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractLinkedList, self).containsAll(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.removeFirst()"""
        return object._wrap(super(AbstractLinkedList, self).removeFirst())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.clear()"""
        super(AbstractLinkedList, self).clear()

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList.hashCode()"""
        return int._wrap(super(AbstractLinkedList, self).hashCode())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.get(int)"""
        return object._wrap(super(_AbstractLinkedList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList.add(int,E)"""
        super(_AbstractLinkedList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList.remove(int)"""
        return object._wrap(super(_AbstractLinkedList, self).remove(_int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractLinkedList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.list.AbstractLinkedList.toString()"""
        return str._wrap(super(AbstractLinkedList, self).toString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList.isEmpty()"""
        return bool._wrap(super(AbstractLinkedList, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.list.CursorableLinkedList()"""
        val = _CursorableLinkedList()
        self.__wrapper = val

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.CursorableLinkedList$Cursor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.list.CursorableLinkedList as _CursorableLinkedList_Cursor
_Cursor = _CursorableLinkedList_Cursor.Cursor
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Cursor():
    """org.apache.commons.collections4.list.CursorableLinkedList.Cursor"""
 
    @staticmethod
    def _wrap(java_value: _Cursor) -> 'Cursor':
        return Cursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cursor):
        """
        Dynamic initializer for Cursor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cursor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cursor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.CursorableLinkedList$Cursor.nextIndex()"""
        return int._wrap(super(Cursor, self).nextIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$Cursor.add(E)"""
        super(_Cursor, self).add(arg0)

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
    def remove(self):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$Cursor.remove()"""
        super(Cursor, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.AbstractList as _AbstractList
_AbstractList = _AbstractList
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList_LinkedSubList
_LinkedSubList = _AbstractLinkedList_LinkedSubList.LinkedSubList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class LinkedSubList():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedSubList"""
 
    @staticmethod
    def _wrap(java_value: _LinkedSubList) -> 'LinkedSubList':
        return LinkedSubList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkedSubList):
        """
        Dynamic initializer for LinkedSubList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkedSubList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkedSubList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.clear()"""
        super(LinkedSubList, self).clear()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.get(int)"""
        return object._wrap(super(_LinkedSubList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.AbstractList.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractList, self).listIterator())

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
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

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
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.set(int,E)"""
        return object._wrap(super(_LinkedSubList, self).set(_int.valueOf(arg0), arg1))

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
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.subList(int,int)"""
        return 'List'._wrap(super(_LinkedSubList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_LinkedSubList, self).addAll(_int.valueOf(arg0), arg1))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.AbstractList.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractList, self).indexOf(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.remove(int)"""
        return object._wrap(super(_LinkedSubList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.size()"""
        return int._wrap(super(LinkedSubList, self).size())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.iterator()"""
        return 'Iterator'._wrap(super(LinkedSubList, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_LinkedSubList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.add(int,E)"""
        super(_LinkedSubList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.add(E)"""
        return bool._wrap(super(_AbstractList, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractList.hashCode()"""
        return int._wrap(super(AbstractList, self).hashCode())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractList, self).equals(arg0))

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_LinkedSubList, self).addAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollection, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.AbstractList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractList, self).lastIndexOf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractListDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class AbstractListDecorator():
    """org.apache.commons.collections4.list.AbstractListDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractListDecorator) -> 'AbstractListDecorator':
        return AbstractListDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractListDecorator):
        """
        Dynamic initializer for AbstractListDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractListDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractListDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractListDecorator, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object._wrap(super(_AbstractListDecorator, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.set(int,E)"""
        return object._wrap(super(_AbstractListDecorator, self).set(_int.valueOf(arg0), arg1))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractListDecorator, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object._wrap(super(_AbstractListDecorator, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractListDecorator.add(int,E)"""
        super(_AbstractListDecorator, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).indexOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractListDecorator, self).listIterator())

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).lastIndexOf(arg0))

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractListDecorator.subList(int,int)"""
        return 'List'._wrap(super(_AbstractListDecorator, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

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
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.CursorableLinkedList$SubCursor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.list.CursorableLinkedList as _CursorableLinkedList_SubCursor
_SubCursor = _CursorableLinkedList_SubCursor.SubCursor
import java.lang.Integer as _int
import org.apache.commons.collections4.list.CursorableLinkedList as _CursorableLinkedList_Cursor
_Cursor = _CursorableLinkedList_Cursor.Cursor
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SubCursor():
    """org.apache.commons.collections4.list.CursorableLinkedList.SubCursor"""
 
    @staticmethod
    def _wrap(java_value: _SubCursor) -> 'SubCursor':
        return SubCursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubCursor):
        """
        Dynamic initializer for SubCursor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubCursor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubCursor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.hasNext()"""
        return bool._wrap(super(SubCursor, self).hasNext())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.nextIndex()"""
        return int._wrap(super(SubCursor, self).nextIndex())

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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.add(E)"""
        super(_SubCursor, self).add(arg0)

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.list.CursorableLinkedList$SubCursor.hasPrevious()"""
        return bool._wrap(super(SubCursor, self).hasPrevious())

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
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.list.PredicatedList
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
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
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection_Builder
_Builder = _PredicatedCollection_Builder.Builder
import org.apache.commons.collections4.list.PredicatedList as _PredicatedList
_PredicatedList = _PredicatedList
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedList():
    """org.apache.commons.collections4.list.PredicatedList"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedList) -> 'PredicatedList':
        return PredicatedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedList):
        """
        Dynamic initializer for PredicatedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.PredicatedList.indexOf(java.lang.Object)"""
        return int._wrap(super(_PredicatedList, self).indexOf(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.PredicatedList.hashCode()"""
        return int._wrap(super(PredicatedList, self).hashCode())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.PredicatedList.get(int)"""
        return object._wrap(super(_PredicatedList, self).get(_int.valueOf(arg0)))

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
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

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
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.PredicatedList.remove(int)"""
        return object._wrap(super(_PredicatedList, self).remove(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def predicatedList(arg0: 'List', arg1: 'Predicate') -> 'PredicatedList':
        """public static <T> org.apache.commons.collections4.list.PredicatedList<T> org.apache.commons.collections4.list.PredicatedList.predicatedList(java.util.List<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return PredicatedList._wrap(_PredicatedList.predicatedList(arg0, arg1))

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.PredicatedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_PredicatedList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.PredicatedList.listIterator()"""
        return 'ListIterator'._wrap(super(PredicatedList, self).listIterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.PredicatedList.subList(int,int)"""
        return 'List'._wrap(super(_PredicatedList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.PredicatedList.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedList, self).equals(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.PredicatedList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_PredicatedList, self).listIterator(_int.valueOf(arg0)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.PredicatedList.set(int,E)"""
        return object._wrap(super(_PredicatedList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.PredicatedList.add(int,E)"""
        super(_PredicatedList, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

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

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.PredicatedList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_PredicatedList, self).lastIndexOf(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

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

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList_LinkedSubListIterator
_LinkedSubListIterator = _AbstractLinkedList_LinkedSubListIterator.LinkedSubListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.list.AbstractLinkedList as _AbstractLinkedList_LinkedListIterator
_LinkedListIterator = _AbstractLinkedList_LinkedListIterator.LinkedListIterator
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinkedSubListIterator():
    """org.apache.commons.collections4.list.AbstractLinkedList.LinkedSubListIterator"""
 
    @staticmethod
    def _wrap(java_value: _LinkedSubListIterator) -> 'LinkedSubListIterator':
        return LinkedSubListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkedSubListIterator):
        """
        Dynamic initializer for LinkedSubListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkedSubListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkedSubListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previous()"""
        return object._wrap(super(LinkedListIterator, self).previous())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.next()"""
        return object._wrap(super(LinkedListIterator, self).next())

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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.hasPrevious()"""
        return bool._wrap(super(LinkedSubListIterator, self).hasPrevious())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.hasNext()"""
        return bool._wrap(super(LinkedSubListIterator, self).hasNext())

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
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.set(E)"""
        super(_LinkedListIterator, self).set(arg0)

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
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedListIterator.previousIndex()"""
        return int._wrap(super(LinkedListIterator, self).previousIndex())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.nextIndex()"""
        return int._wrap(super(LinkedSubListIterator, self).nextIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.remove()"""
        super(LinkedSubListIterator, self).remove()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.list.AbstractLinkedList$LinkedSubListIterator.add(E)"""
        super(_LinkedSubListIterator, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.list.AbstractSerializableListDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.list.AbstractListDecorator as _AbstractListDecorator
_AbstractListDecorator = _AbstractListDecorator
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import org.apache.commons.collections4.list.AbstractSerializableListDecorator as _AbstractSerializableListDecorator
_AbstractSerializableListDecorator = _AbstractSerializableListDecorator
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSerializableListDecorator():
    """org.apache.commons.collections4.list.AbstractSerializableListDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSerializableListDecorator) -> 'AbstractSerializableListDecorator':
        return AbstractSerializableListDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSerializableListDecorator):
        """
        Dynamic initializer for AbstractSerializableListDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSerializableListDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSerializableListDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractListDecorator, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.get(int)"""
        return object._wrap(super(_AbstractListDecorator, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.set(int,E)"""
        return object._wrap(super(_AbstractListDecorator, self).set(_int.valueOf(arg0), arg1))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator(int)"""
        return 'ListIterator'._wrap(super(_AbstractListDecorator, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.AbstractListDecorator.remove(int)"""
        return object._wrap(super(_AbstractListDecorator, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.AbstractListDecorator.add(int,E)"""
        super(_AbstractListDecorator, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.indexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).indexOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.AbstractListDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractListDecorator, self).equals(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.hashCode()"""
        return int._wrap(super(AbstractListDecorator, self).hashCode())

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
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.AbstractListDecorator.listIterator()"""
        return 'ListIterator'._wrap(super(AbstractListDecorator, self).listIterator())

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.AbstractListDecorator.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_AbstractListDecorator, self).lastIndexOf(arg0))

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
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.AbstractListDecorator.subList(int,int)"""
        return 'List'._wrap(super(_AbstractListDecorator, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

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
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: org.apache.commons.collections4.list.TransformedList
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.list.TransformedList as _TransformedList
_TransformedList = _TransformedList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
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
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class TransformedList():
    """org.apache.commons.collections4.list.TransformedList"""
 
    @staticmethod
    def _wrap(java_value: _TransformedList) -> 'TransformedList':
        return TransformedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedList):
        """
        Dynamic initializer for TransformedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

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
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TransformedList.remove(int)"""
        return object._wrap(super(_TransformedList, self).remove(_int.valueOf(arg0)))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.TransformedList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_TransformedList, self).lastIndexOf(arg0))

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
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.list.TransformedList.add(int,E)"""
        super(_TransformedList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.list.TransformedList.get(int)"""
        return object._wrap(super(_TransformedList, self).get(_int.valueOf(arg0)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @staticmethod
    @overload
    def transformingList(arg0: 'List', arg1: 'Transformer') -> 'TransformedList':
        """public static <E> org.apache.commons.collections4.list.TransformedList<E> org.apache.commons.collections4.list.TransformedList.transformingList(java.util.List<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedList._wrap(_TransformedList.transformingList(arg0, arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E org.apache.commons.collections4.list.TransformedList.set(int,E)"""
        return object._wrap(super(_TransformedList, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.list.TransformedList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_TransformedList, self).addAll(_int.valueOf(arg0), arg1))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.list.TransformedList.indexOf(java.lang.Object)"""
        return int._wrap(super(_TransformedList, self).indexOf(arg0))

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TransformedList.listIterator()"""
        return 'ListIterator'._wrap(super(TransformedList, self).listIterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.list.TransformedList.subList(int,int)"""
        return 'List'._wrap(super(_TransformedList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @staticmethod
    @overload
    def transformedList(arg0: 'List', arg1: 'Transformer') -> 'TransformedList':
        """public static <E> org.apache.commons.collections4.list.TransformedList<E> org.apache.commons.collections4.list.TransformedList.transformedList(java.util.List<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedList._wrap(_TransformedList.transformedList(arg0, arg1))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> org.apache.commons.collections4.list.TransformedList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_TransformedList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.list.TransformedList.hashCode()"""
        return int._wrap(super(TransformedList, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.list.TransformedList.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformedList, self).equals(arg0))

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

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0)