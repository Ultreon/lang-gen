from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Queue as Queue
import java.util.Set as _Set
_Set = _Set
import java.util.Queue as _Queue
_Queue = _Queue
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
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """org.apache.commons.collections4.collection.PredicatedCollection.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createPredicatedQueue(self, arg0: 'Queue') -> 'Queue':
        """public java.util.Queue<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedQueue(java.util.Queue<E>)"""
        return 'Queue'._wrap(super(_Builder, self).createPredicatedQueue(arg0))

    @overload
    def add(self, arg0: object) -> 'Builder':
        """public org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.add(E)"""
        return 'Builder'._wrap(super(_Builder, self).add(arg0))

    @overload
    def createPredicatedMultiSet(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedMultiSet()"""
        return 'collections4.MultiSet'._wrap(super(Builder, self).createPredicatedMultiSet())

    @overload
    def addAll(self, arg0: 'Collection') -> 'Builder':
        """public org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.addAll(java.util.Collection<? extends E>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(arg0))

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

    @overload
    def createPredicatedBag(self, arg0: 'Bag') -> 'collections4.Bag':
        """public org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedBag(org.apache.commons.collections4.Bag<E>)"""
        return 'collections4.Bag'._wrap(super(_Builder, self).createPredicatedBag(arg0))

    @overload
    def createPredicatedSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedSet()"""
        return 'Set'._wrap(super(Builder, self).createPredicatedSet())

    @overload
    def createPredicatedList(self, arg0: 'List') -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedList(java.util.List<E>)"""
        return 'List'._wrap(super(_Builder, self).createPredicatedList(arg0))

    @overload
    def createPredicatedList(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedList()"""
        return 'List'._wrap(super(Builder, self).createPredicatedList())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def rejectedElements(self) -> 'Collection':
        """public java.util.Collection<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.rejectedElements()"""
        return 'Collection'._wrap(super(Builder, self).rejectedElements())

    @overload
    def createPredicatedBag(self) -> 'collections4.Bag':
        """public org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedBag()"""
        return 'collections4.Bag'._wrap(super(Builder, self).createPredicatedBag())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.collection.PredicatedCollection$Builder(org.apache.commons.collections4.Predicate<? super E>)"""
        val = _Builder(arg0)
        self.__wrapper = val

    @overload
    def createPredicatedMultiSet(self, arg0: 'MultiSet') -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedMultiSet(org.apache.commons.collections4.MultiSet<E>)"""
        return 'collections4.MultiSet'._wrap(super(_Builder, self).createPredicatedMultiSet(arg0))

    @overload
    def createPredicatedSet(self, arg0: 'Set') -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedSet(java.util.Set<E>)"""
        return 'Set'._wrap(super(_Builder, self).createPredicatedSet(arg0))

    @overload
    def createPredicatedQueue(self) -> 'Queue':
        """public java.util.Queue<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedQueue()"""
        return 'Queue'._wrap(super(Builder, self).createPredicatedQueue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.collection.PredicatedCollection$Builder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Queue as Queue
import java.util.Set as _Set
_Set = _Set
import java.util.Queue as _Queue
_Queue = _Queue
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
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """org.apache.commons.collections4.collection.PredicatedCollection.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createPredicatedQueue(self, arg0: 'Queue') -> 'Queue':
        """public java.util.Queue<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedQueue(java.util.Queue<E>)"""
        return 'Queue'._wrap(super(_Builder, self).createPredicatedQueue(arg0))

    @overload
    def add(self, arg0: object) -> 'Builder':
        """public org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.add(E)"""
        return 'Builder'._wrap(super(_Builder, self).add(arg0))

    @overload
    def createPredicatedMultiSet(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedMultiSet()"""
        return 'collections4.MultiSet'._wrap(super(Builder, self).createPredicatedMultiSet())

    @overload
    def addAll(self, arg0: 'Collection') -> 'Builder':
        """public org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.addAll(java.util.Collection<? extends E>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(arg0))

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

    @overload
    def createPredicatedBag(self, arg0: 'Bag') -> 'collections4.Bag':
        """public org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedBag(org.apache.commons.collections4.Bag<E>)"""
        return 'collections4.Bag'._wrap(super(_Builder, self).createPredicatedBag(arg0))

    @overload
    def createPredicatedSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedSet()"""
        return 'Set'._wrap(super(Builder, self).createPredicatedSet())

    @overload
    def createPredicatedList(self, arg0: 'List') -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedList(java.util.List<E>)"""
        return 'List'._wrap(super(_Builder, self).createPredicatedList(arg0))

    @overload
    def createPredicatedList(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedList()"""
        return 'List'._wrap(super(Builder, self).createPredicatedList())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def rejectedElements(self) -> 'Collection':
        """public java.util.Collection<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.rejectedElements()"""
        return 'Collection'._wrap(super(Builder, self).rejectedElements())

    @overload
    def createPredicatedBag(self) -> 'collections4.Bag':
        """public org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedBag()"""
        return 'collections4.Bag'._wrap(super(Builder, self).createPredicatedBag())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.collection.PredicatedCollection$Builder(org.apache.commons.collections4.Predicate<? super E>)"""
        val = _Builder(arg0)
        self.__wrapper = val

    @overload
    def createPredicatedMultiSet(self, arg0: 'MultiSet') -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedMultiSet(org.apache.commons.collections4.MultiSet<E>)"""
        return 'collections4.MultiSet'._wrap(super(_Builder, self).createPredicatedMultiSet(arg0))

    @overload
    def createPredicatedSet(self, arg0: 'Set') -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedSet(java.util.Set<E>)"""
        return 'Set'._wrap(super(_Builder, self).createPredicatedSet(arg0))

    @overload
    def createPredicatedQueue(self) -> 'Queue':
        """public java.util.Queue<E> org.apache.commons.collections4.collection.PredicatedCollection$Builder.createPredicatedQueue()"""
        return 'Queue'._wrap(super(Builder, self).createPredicatedQueue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.collection.PredicatedCollection$Builder 
 
 
# CLASS: org.apache.commons.collections4.collection.UnmodifiableBoundedCollection
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.collection.UnmodifiableBoundedCollection as _UnmodifiableBoundedCollection
_UnmodifiableBoundedCollection = _UnmodifiableBoundedCollection
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.BoundedCollection as _BoundedCollection
_BoundedCollection = _BoundedCollection
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
 
class UnmodifiableBoundedCollection():
    """org.apache.commons.collections4.collection.UnmodifiableBoundedCollection"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableBoundedCollection) -> 'UnmodifiableBoundedCollection':
        return UnmodifiableBoundedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableBoundedCollection):
        """
        Dynamic initializer for UnmodifiableBoundedCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableBoundedCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableBoundedCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.clear()"""
        super(UnmodifiableBoundedCollection, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableBoundedCollection, self).removeIf(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableBoundedCollection, self).iterator())

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.isFull()"""
        return bool._wrap(super(UnmodifiableBoundedCollection, self).isFull())

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
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableBoundedCollection, self).retainAll(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableBoundedCollection, self).removeAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def unmodifiableBoundedCollection(arg0: 'Collection') -> 'collections4.BoundedCollection':
        """public static <E> org.apache.commons.collections4.BoundedCollection<E> org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.unmodifiableBoundedCollection(java.util.Collection<? extends E>)"""
        return collections4.BoundedCollection._wrap(_UnmodifiableBoundedCollection.unmodifiableBoundedCollection(arg0))

    @staticmethod
    @overload
    def unmodifiableBoundedCollection(arg0: 'BoundedCollection') -> 'collections4.BoundedCollection':
        """public static <E> org.apache.commons.collections4.BoundedCollection<E> org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.unmodifiableBoundedCollection(org.apache.commons.collections4.BoundedCollection<? extends E>)"""
        return collections4.BoundedCollection._wrap(_UnmodifiableBoundedCollection.unmodifiableBoundedCollection(arg0))

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.maxSize()"""
        return int._wrap(super(UnmodifiableBoundedCollection, self).maxSize())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.add(E)"""
        return bool._wrap(super(_UnmodifiableBoundedCollection, self).add(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(AbstractCollectionDecorator, self).isEmpty())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableBoundedCollection, self).addAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(AbstractCollectionDecorator, self).toArray())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableBoundedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableBoundedCollection, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.collection.UnmodifiableCollection
import java.util.function.Predicate as Predicate
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
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import org.apache.commons.collections4.collection.UnmodifiableCollection as _UnmodifiableCollection
_UnmodifiableCollection = _UnmodifiableCollection
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
 
class UnmodifiableCollection():
    """org.apache.commons.collections4.collection.UnmodifiableCollection"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableCollection) -> 'UnmodifiableCollection':
        return UnmodifiableCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableCollection):
        """
        Dynamic initializer for UnmodifiableCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableCollection, self).addAll(arg0))

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(AbstractCollectionDecorator, self).toString())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableCollection, self).removeAll(arg0))

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
        """public boolean org.apache.commons.collections4.collection.UnmodifiableCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableCollection, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.UnmodifiableCollection.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableCollection, self).iterator())

    @staticmethod
    @overload
    def unmodifiableCollection(arg0: 'Collection') -> 'Collection':
        """public static <T> java.util.Collection<T> org.apache.commons.collections4.collection.UnmodifiableCollection.unmodifiableCollection(java.util.Collection<? extends T>)"""
        return Collection._wrap(_UnmodifiableCollection.unmodifiableCollection(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableCollection, self).removeIf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(AbstractCollectionDecorator, self).toArray())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableCollection.add(E)"""
        return bool._wrap(super(_UnmodifiableCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.UnmodifiableCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableCollection, self).remove(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.UnmodifiableCollection.clear()"""
        super(UnmodifiableCollection, self).clear()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.collection.CompositeCollection$CollectionMutator
import org.apache.commons.collections4.collection.CompositeCollection as _CompositeCollection_CollectionMutator
_CollectionMutator = _CompositeCollection_CollectionMutator.CollectionMutator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.List as List
 
class CollectionMutator():
    """org.apache.commons.collections4.collection.CompositeCollection.CollectionMutator"""
 
    @staticmethod
    def _wrap(java_value: _CollectionMutator) -> 'CollectionMutator':
        return CollectionMutator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectionMutator):
        """
        Dynamic initializer for CollectionMutator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectionMutator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectionMutator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def remove(self, arg0: 'CompositeCollection', arg1: 'List', arg2: object):
        """public abstract boolean org.apache.commons.collections4.collection.CompositeCollection$CollectionMutator.remove(org.apache.commons.collections4.collection.CompositeCollection<E>,java.util.List<java.util.Collection<E>>,java.lang.Object)"""
        pass

    @abstractmethod
    def add(self, arg0: 'CompositeCollection', arg1: 'List', arg2: object):
        """public abstract boolean org.apache.commons.collections4.collection.CompositeCollection$CollectionMutator.add(org.apache.commons.collections4.collection.CompositeCollection<E>,java.util.List<java.util.Collection<E>>,E)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'CompositeCollection', arg1: 'List', arg2: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.collection.CompositeCollection$CollectionMutator.addAll(org.apache.commons.collections4.collection.CompositeCollection<E>,java.util.List<java.util.Collection<E>>,java.util.Collection<? extends E>)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.collection.TransformedCollection
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
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
 
class TransformedCollection():
    """org.apache.commons.collections4.collection.TransformedCollection"""
 
    @staticmethod
    def _wrap(java_value: _TransformedCollection) -> 'TransformedCollection':
        return TransformedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedCollection):
        """
        Dynamic initializer for TransformedCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedCollection._wrap(_TransformedCollection.transformedCollection(arg0, arg1))

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(AbstractCollectionDecorator, self).toString())

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
        return bool._wrap(super(_AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_TransformedCollection, self).addAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(AbstractCollectionDecorator, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(AbstractCollectionDecorator, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedCollection._wrap(_TransformedCollection.transformingCollection(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_TransformedCollection, self).add(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.collection.PredicatedCollection
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection
_PredicatedCollection = _PredicatedCollection
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
 
class PredicatedCollection():
    """org.apache.commons.collections4.collection.PredicatedCollection"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedCollection) -> 'PredicatedCollection':
        return PredicatedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedCollection):
        """
        Dynamic initializer for PredicatedCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(AbstractCollectionDecorator, self).toString())

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
        return bool._wrap(super(_AbstractCollectionDecorator, self).retainAll(arg0))

    @staticmethod
    @overload
    def notNullBuilder() -> 'Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return Builder._wrap(_PredicatedCollection.notNullBuilder())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(AbstractCollectionDecorator, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return Builder._wrap(_PredicatedCollection.builder(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(AbstractCollectionDecorator, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(AbstractCollectionDecorator, self).isEmpty())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_PredicatedCollection, self).addAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(AbstractCollectionDecorator, self).toArray())

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
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool._wrap(super(_PredicatedCollection, self).add(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).contains(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return PredicatedCollection._wrap(_PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.collection.IndexedCollection
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.collection.IndexedCollection as _IndexedCollection
_IndexedCollection = _IndexedCollection
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
 
class IndexedCollection():
    """org.apache.commons.collections4.collection.IndexedCollection"""
 
    @staticmethod
    def _wrap(java_value: _IndexedCollection) -> 'IndexedCollection':
        return IndexedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedCollection):
        """
        Dynamic initializer for IndexedCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nonUniqueIndexedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'IndexedCollection':
        """public static <K,C> org.apache.commons.collections4.collection.IndexedCollection<K, C> org.apache.commons.collections4.collection.IndexedCollection.nonUniqueIndexedCollection(java.util.Collection<C>,org.apache.commons.collections4.Transformer<C, K>)"""
        return IndexedCollection._wrap(_IndexedCollection.nonUniqueIndexedCollection(arg0, arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.add(C)"""
        return bool._wrap(super(_IndexedCollection, self).add(arg0))

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
    def clear(self):
        """public void org.apache.commons.collections4.collection.IndexedCollection.clear()"""
        super(IndexedCollection, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(AbstractCollectionDecorator, self).toString())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_IndexedCollection, self).removeAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_IndexedCollection, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @overload
    def reindex(self):
        """public void org.apache.commons.collections4.collection.IndexedCollection.reindex()"""
        super(IndexedCollection, self).reindex()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object) -> object:
        """public C org.apache.commons.collections4.collection.IndexedCollection.get(K)"""
        return object._wrap(super(_IndexedCollection, self).get(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(AbstractCollectionDecorator, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.addAll(java.util.Collection<? extends C>)"""
        return bool._wrap(super(_IndexedCollection, self).addAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_IndexedCollection, self).retainAll(arg0))

    @staticmethod
    @overload
    def uniqueIndexedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'IndexedCollection':
        """public static <K,C> org.apache.commons.collections4.collection.IndexedCollection<K, C> org.apache.commons.collections4.collection.IndexedCollection.uniqueIndexedCollection(java.util.Collection<C>,org.apache.commons.collections4.Transformer<C, K>)"""
        return IndexedCollection._wrap(_IndexedCollection.uniqueIndexedCollection(arg0, arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_IndexedCollection, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(AbstractCollectionDecorator, self).toArray())

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
    def __init__(self, arg0: 'Collection', arg1: 'Transformer', arg2: 'MultiMap', arg3: bool):
        """public org.apache.commons.collections4.collection.IndexedCollection(java.util.Collection<C>,org.apache.commons.collections4.Transformer<C, K>,org.apache.commons.collections4.MultiMap<K, C>,boolean)"""
        val = _IndexedCollection(arg0, arg1, arg2, _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_IndexedCollection, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def values(self, arg0: object) -> 'Collection':
        """public java.util.Collection<C> org.apache.commons.collections4.collection.IndexedCollection.values(K)"""
        return 'Collection'._wrap(super(_IndexedCollection, self).values(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.IndexedCollection.removeIf(java.util.function.Predicate<? super C>)"""
        return bool._wrap(super(_IndexedCollection, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.collection.SynchronizedCollection
import java.util.function.Predicate as Predicate
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
import java.lang.String as _String
_String = _String
from builtins import object
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
 
class SynchronizedCollection():
    """org.apache.commons.collections4.collection.SynchronizedCollection"""
 
    @staticmethod
    def _wrap(java_value: _SynchronizedCollection) -> 'SynchronizedCollection':
        return SynchronizedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronizedCollection):
        """
        Dynamic initializer for SynchronizedCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronizedCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronizedCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.add(E)"""
        return bool._wrap(super(_SynchronizedCollection, self).add(arg0))

    @staticmethod
    @overload
    def synchronizedCollection(arg0: 'Collection') -> 'SynchronizedCollection':
        """public static <T> org.apache.commons.collections4.collection.SynchronizedCollection<T> org.apache.commons.collections4.collection.SynchronizedCollection.synchronizedCollection(java.util.Collection<T>)"""
        return SynchronizedCollection._wrap(_SynchronizedCollection.synchronizedCollection(arg0))

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
    def clear(self):
        """public void org.apache.commons.collections4.collection.SynchronizedCollection.clear()"""
        super(SynchronizedCollection, self).clear()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedCollection, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.equals(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedCollection, self).equals(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_SynchronizedCollection, self).contains(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.isEmpty()"""
        return bool._wrap(super(SynchronizedCollection, self).isEmpty())

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.size()"""
        return int._wrap(super(SynchronizedCollection, self).size())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_SynchronizedCollection, self).containsAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.SynchronizedCollection.iterator()"""
        return 'Iterator'._wrap(super(SynchronizedCollection, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_SynchronizedCollection, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray()"""
        return List[object]._wrap(super(SynchronizedCollection, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_SynchronizedCollection, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.SynchronizedCollection.toString()"""
        return str._wrap(super(SynchronizedCollection, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.collection.SynchronizedCollection.hashCode()"""
        return int._wrap(super(SynchronizedCollection, self).hashCode())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.SynchronizedCollection.toArray(T[])"""
        return List[object]._wrap(super(_SynchronizedCollection, self).toArray(arg0))

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
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_SynchronizedCollection, self).removeAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.SynchronizedCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_SynchronizedCollection, self).retainAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.collection.AbstractCollectionDecorator
import java.util.function.Predicate as Predicate
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
import java.lang.String as _String
_String = _String
from builtins import object
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
 
class AbstractCollectionDecorator():
    """org.apache.commons.collections4.collection.AbstractCollectionDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractCollectionDecorator) -> 'AbstractCollectionDecorator':
        return AbstractCollectionDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractCollectionDecorator):
        """
        Dynamic initializer for AbstractCollectionDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractCollectionDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractCollectionDecorator__wrapper":
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
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(AbstractCollectionDecorator, self).toString())

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
        return bool._wrap(super(_AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(AbstractCollectionDecorator, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(AbstractCollectionDecorator, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(AbstractCollectionDecorator, self).toArray())

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.collection.CompositeCollection
import java.util.function.Predicate as Predicate
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
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.CompositeCollection as _CompositeCollection
_CompositeCollection = _CompositeCollection
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
 
class CompositeCollection():
    """org.apache.commons.collections4.collection.CompositeCollection"""
 
    @staticmethod
    def _wrap(java_value: _CompositeCollection) -> 'CompositeCollection':
        return CompositeCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CompositeCollection):
        """
        Dynamic initializer for CompositeCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CompositeCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CompositeCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCollections(self) -> 'List':
        """public java.util.List<java.util.Collection<E>> org.apache.commons.collections4.collection.CompositeCollection.getCollections()"""
        return 'List'._wrap(super(CompositeCollection, self).getCollections())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CompositeCollection, self).removeAll(arg0))

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
    def toCollection(self) -> 'Collection':
        """public java.util.Collection<E> org.apache.commons.collections4.collection.CompositeCollection.toCollection()"""
        return 'Collection'._wrap(super(CompositeCollection, self).toCollection())

    @overload
    def removeComposited(self, arg0: 'Collection'):
        """public void org.apache.commons.collections4.collection.CompositeCollection.removeComposited(java.util.Collection<E>)"""
        super(_CompositeCollection, self).removeComposited(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.CompositeCollection.toArray(T[])"""
        return List[object]._wrap(super(_CompositeCollection, self).toArray(arg0))

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
    def __init__(self):
        """public org.apache.commons.collections4.collection.CompositeCollection()"""
        val = _CompositeCollection()
        self.__wrapper = val

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.add(E)"""
        return bool._wrap(super(_CompositeCollection, self).add(arg0))

    @overload
    def setMutator(self, arg0: 'CollectionMutator'):
        """public void org.apache.commons.collections4.collection.CompositeCollection.setMutator(org.apache.commons.collections4.collection.CompositeCollection$CollectionMutator<E>)"""
        super(_CompositeCollection, self).setMutator(arg0)

    @overload
    def __init__(self, *arg0: 'Collection'):
        """public org.apache.commons.collections4.collection.CompositeCollection(java.util.Collection<E>...)"""
        val = _CompositeCollection(arg0)
        self.__wrapper = val

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CompositeCollection, self).retainAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.CompositeCollection.size()"""
        return int._wrap(super(CompositeCollection, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.CompositeCollection.clear()"""
        super(CompositeCollection, self).clear()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_CompositeCollection, self).contains(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.CompositeCollection.toArray()"""
        return List[object]._wrap(super(CompositeCollection, self).toArray())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_CompositeCollection, self).remove(arg0))

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.collection.CompositeCollection(java.util.Collection<E>)"""
        val = _CompositeCollection(arg0)
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.CompositeCollection.iterator()"""
        return 'Iterator'._wrap(super(CompositeCollection, self).iterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CompositeCollection, self).containsAll(arg0))

    @overload
    def addComposited(self, arg0: 'Collection'):
        """public void org.apache.commons.collections4.collection.CompositeCollection.addComposited(java.util.Collection<E>)"""
        super(_CompositeCollection, self).addComposited(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_CompositeCollection, self).removeIf(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_CompositeCollection, self).addAll(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.collection.CompositeCollection()"""
        val = _CompositeCollection()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Collection', arg1: 'Collection'):
        """public org.apache.commons.collections4.collection.CompositeCollection(java.util.Collection<E>,java.util.Collection<E>)"""
        val = _CompositeCollection(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.CompositeCollection.isEmpty()"""
        return bool._wrap(super(CompositeCollection, self).isEmpty())

    @overload
    def addComposited(self, arg0: 'Collection', arg1: 'Collection'):
        """public void org.apache.commons.collections4.collection.CompositeCollection.addComposited(java.util.Collection<E>,java.util.Collection<E>)"""
        super(_CompositeCollection, self).addComposited(arg0, arg1)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def addComposited(self, *arg0: 'Collection'):
        """public void org.apache.commons.collections4.collection.CompositeCollection.addComposited(java.util.Collection<E>...)"""
        super(_CompositeCollection, self).addComposited(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())