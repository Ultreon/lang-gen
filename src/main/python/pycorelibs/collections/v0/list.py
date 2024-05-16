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
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import dev.ultreon.libs.collections.v0.list.PagedList as _PagedList
_PagedList = _PagedList
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PagedList():
    """dev.ultreon.libs.collections.v0.list.PagedList"""
 
    @staticmethod
    def _wrap(java_value: _PagedList) -> 'PagedList':
        return PagedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PagedList):
        """
        Dynamic initializer for PagedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PagedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PagedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(_ArrayList, self).addLast(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int._wrap(super(ArrayList, self).hashCode())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_ArrayList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object._wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'._wrap(super(ArrayList, self).listIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(_ArrayList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).removeAll(arg0))

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
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool._wrap(super(_ArrayList, self).add(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool._wrap(super(ArrayList, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_ArrayList, self).removeIf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).indexOf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'._wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(_ArrayList, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PagedList'):
        """public dev.ultreon.libs.collections.v0.list.PagedList(dev.ultreon.libs.collections.v0.list.PagedList<? extends T>)"""
        val = _PagedList(arg0)
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(_ArrayList, self).forEach(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(_ArrayList, self).addFirst(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int)"""
        val = _PagedList(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(_ArrayList, self).sort(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object._wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object._wrap(super(ArrayList, self).clone())

    @overload
    def getFullPage(self, arg0: int) -> 'List':
        """public java.util.List<T> dev.ultreon.libs.collections.v0.list.PagedList.getFullPage(int)"""
        return 'List'._wrap(super(_PagedList, self).getFullPage(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object._wrap(super(_ArrayList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def get(self, arg0: int, arg1: int) -> object:
        """public T dev.ultreon.libs.collections.v0.list.PagedList.get(int,int)"""
        return object._wrap(super(_PagedList, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object]._wrap(super(_ArrayList, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object._wrap(super(_ArrayList, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: 'Collection'):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int,java.util.Collection<? extends T>)"""
        val = _PagedList(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object._wrap(super(ArrayList, self).getLast())

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).lastIndexOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'._wrap(super(_ArrayList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).contains(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object._wrap(super(_ArrayList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int._wrap(super(ArrayList, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object]._wrap(super(ArrayList, self).toArray())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).equals(arg0))

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
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object._wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'._wrap(super(ArrayList, self).iterator())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int,int)"""
        val = _PagedList(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.list.PagedList
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
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import dev.ultreon.libs.collections.v0.list.PagedList as _PagedList
_PagedList = _PagedList
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PagedList():
    """dev.ultreon.libs.collections.v0.list.PagedList"""
 
    @staticmethod
    def _wrap(java_value: _PagedList) -> 'PagedList':
        return PagedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PagedList):
        """
        Dynamic initializer for PagedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PagedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PagedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(_ArrayList, self).addLast(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int._wrap(super(ArrayList, self).hashCode())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_ArrayList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object._wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'._wrap(super(ArrayList, self).listIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(_ArrayList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).removeAll(arg0))

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
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool._wrap(super(_ArrayList, self).add(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool._wrap(super(ArrayList, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_ArrayList, self).removeIf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).indexOf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'._wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(_ArrayList, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PagedList'):
        """public dev.ultreon.libs.collections.v0.list.PagedList(dev.ultreon.libs.collections.v0.list.PagedList<? extends T>)"""
        val = _PagedList(arg0)
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(_ArrayList, self).forEach(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(_ArrayList, self).addFirst(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int)"""
        val = _PagedList(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(_ArrayList, self).sort(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object._wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object._wrap(super(ArrayList, self).clone())

    @overload
    def getFullPage(self, arg0: int) -> 'List':
        """public java.util.List<T> dev.ultreon.libs.collections.v0.list.PagedList.getFullPage(int)"""
        return 'List'._wrap(super(_PagedList, self).getFullPage(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object._wrap(super(_ArrayList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def get(self, arg0: int, arg1: int) -> object:
        """public T dev.ultreon.libs.collections.v0.list.PagedList.get(int,int)"""
        return object._wrap(super(_PagedList, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object]._wrap(super(_ArrayList, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object._wrap(super(_ArrayList, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: 'Collection'):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int,java.util.Collection<? extends T>)"""
        val = _PagedList(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object._wrap(super(ArrayList, self).getLast())

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).lastIndexOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'._wrap(super(_ArrayList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).contains(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object._wrap(super(_ArrayList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int._wrap(super(ArrayList, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object]._wrap(super(ArrayList, self).toArray())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).equals(arg0))

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
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object._wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'._wrap(super(ArrayList, self).iterator())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int,int)"""
        val = _PagedList(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.list.PagedList 
 
 
# CLASS: dev.ultreon.libs.collections.v0.list.SizedList
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = _import_once("pycorelibs.functions.v0.misc")

from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.collections.v0.util.Range as _Range
_Range = _Range
from typing import List
import java.lang.Integer as _int
try:
    from pycorelibs.collections.v0 import util
except ImportError:
    util = _import_once("pycorelibs.collections.v0.util")

import dev.ultreon.libs.collections.v0.list.SizedList as _SizedList
_SizedList = _SizedList
from builtins import bool
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SizedList():
    """dev.ultreon.libs.collections.v0.list.SizedList"""
 
    @staticmethod
    def _wrap(java_value: _SizedList) -> 'SizedList':
        return SizedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SizedList):
        """
        Dynamic initializer for SizedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SizedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SizedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getValue(self, arg0: float) -> object:
        """public T dev.ultreon.libs.collections.v0.list.SizedList.getValue(double)"""
        return object._wrap(super(_SizedList, self).getValue(_double.valueOf(arg0)))

    @overload
    def edit(self, arg0: object, arg1: float) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.edit(T,double)"""
        return _transform(super(_SizedList, self).edit(arg0, _double.valueOf(arg1))).'Double'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def editLengths(self, arg0: 'Applier'):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.editLengths(dev.ultreon.libs.functions.v0.misc.Applier<T, java.lang.Double>)"""
        super(_SizedList, self).editLengths(arg0)

    @overload
    def insert(self, arg0: int, arg1: float, arg2: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.insert(int,double,T)"""
        return int._wrap(super(_SizedList, self).insert(_int.valueOf(arg0), _double.valueOf(arg1), arg2))

    @overload
    def add(self, arg0: float, arg1: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.add(double,T)"""
        return int._wrap(super(_SizedList, self).add(_double.valueOf(arg0), arg1))

    @overload
    def getRanges(self) -> List['util.Range']:
        """public dev.ultreon.libs.collections.v0.util.Range[] dev.ultreon.libs.collections.v0.list.SizedList.getRanges()"""
        return List['util.Range']._wrap(super(SizedList, self).getRanges())

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
    def getSize(self, arg0: int) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.getSize(int)"""
        return _transform(super(_SizedList, self).getSize(_int.valueOf(arg0))).'Double'Value()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.list.SizedList()"""
        val = _SizedList()
        self.__wrapper = val

    @overload
    def rangeOf(self, arg0: object) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.libs.collections.v0.list.SizedList.rangeOf(T)"""
        return 'util.Range'._wrap(super(_SizedList, self).rangeOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.indexOf(T)"""
        return int._wrap(super(_SizedList, self).indexOf(arg0))

    @overload
    def getRange(self, arg0: int) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.libs.collections.v0.list.SizedList.getRange(int)"""
        return 'util.Range'._wrap(super(_SizedList, self).getRange(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.remove(int)"""
        super(_SizedList, self).remove(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTotalSize(self) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.getTotalSize()"""
        return _transform(super(SizedList, self).getTotalSize()).'Double'Value()

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.list.SizedList()"""
        val = _SizedList()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.clear()"""
        super(SizedList, self).clear()

    @overload
    def edit(self, arg0: object, arg1: float, arg2: object) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.edit(T,double,T)"""
        return _transform(super(_SizedList, self).edit(arg0, _double.valueOf(arg1), arg2)).'Double'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())