from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.list.SizedList as __SizedList
__SizedList = __SizedList
from builtins import str
from pyquantum_helper import transform as __transform
import dev.ultreon.libs.collections.v0.util.Range as __Range
__Range = __Range
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = __import_once__("pycorelibs.functions.v0.misc")

from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.collections.v0 import util
except ImportError:
    util = __import_once__("pycorelibs.collections.v0.util")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import java.lang.Double as Double
from builtins import int
 
class SizedList():
    """dev.ultreon.libs.collections.v0.list.SizedList"""
 
    @staticmethod
    def __wrap(java_value: __SizedList) -> 'SizedList':
        return SizedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SizedList):
        """
        Dynamic initializer for SizedList.
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
    def editLengths(self, arg0: 'Applier'):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.editLengths(dev.ultreon.libs.functions.v0.misc.Applier<T, java.lang.Double>)"""
        super(__SizedList, self).editLengths(arg0)

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.indexOf(T)"""
        return int.__wrap(super(__SizedList, self).indexOf(arg0))

    @overload
    def getValue(self, arg0: float) -> object:
        """public T dev.ultreon.libs.collections.v0.list.SizedList.getValue(double)"""
        return object.__wrap(super(__SizedList, self).getValue(__double.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.list.SizedList()"""
        val = __SizedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def getSize(self, arg0: int) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.getSize(int)"""
        return __transform(super(__SizedList, self).getSize(__int.valueOf(arg0))).'Double'Value()

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.remove(int)"""
        super(__SizedList, self).remove(__int.valueOf(arg0))

    @overload
    def edit(self, arg0: object, arg1: float) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.edit(T,double)"""
        return __transform(super(__SizedList, self).edit(arg0, __double.valueOf(arg1))).'Double'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def add(self, arg0: float, arg1: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.add(double,T)"""
        return int.__wrap(super(__SizedList, self).add(__double.valueOf(arg0), arg1))

    @overload
    def rangeOf(self, arg0: object) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.libs.collections.v0.list.SizedList.rangeOf(T)"""
        return 'util.Range'.__wrap(super(__SizedList, self).rangeOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getRanges(self) -> List['util.Range']:
        """public dev.ultreon.libs.collections.v0.util.Range[] dev.ultreon.libs.collections.v0.list.SizedList.getRanges()"""
        return List['util.Range'].__wrap(super(SizedList, self).getRanges())

    @overload
    def insert(self, arg0: int, arg1: float, arg2: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.insert(int,double,T)"""
        return int.__wrap(super(__SizedList, self).insert(__int.valueOf(arg0), __double.valueOf(arg1), arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.list.SizedList()"""
        val = __SizedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTotalSize(self) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.getTotalSize()"""
        return __transform(super(SizedList, self).getTotalSize()).'Double'Value()

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
    def edit(self, arg0: object, arg1: float, arg2: object) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.edit(T,double,T)"""
        return __transform(super(__SizedList, self).edit(arg0, __double.valueOf(arg1), arg2)).'Double'Value()

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
    def getRange(self, arg0: int) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.libs.collections.v0.list.SizedList.getRange(int)"""
        return 'util.Range'.__wrap(super(__SizedList, self).getRange(__int.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.list.SizedList
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.collections.v0.list.SizedList as __SizedList
__SizedList = __SizedList
from builtins import str
from pyquantum_helper import transform as __transform
import dev.ultreon.libs.collections.v0.util.Range as __Range
__Range = __Range
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = __import_once__("pycorelibs.functions.v0.misc")

from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.collections.v0 import util
except ImportError:
    util = __import_once__("pycorelibs.collections.v0.util")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import java.lang.Double as Double
from builtins import int
 
class SizedList():
    """dev.ultreon.libs.collections.v0.list.SizedList"""
 
    @staticmethod
    def __wrap(java_value: __SizedList) -> 'SizedList':
        return SizedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SizedList):
        """
        Dynamic initializer for SizedList.
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
    def editLengths(self, arg0: 'Applier'):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.editLengths(dev.ultreon.libs.functions.v0.misc.Applier<T, java.lang.Double>)"""
        super(__SizedList, self).editLengths(arg0)

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.indexOf(T)"""
        return int.__wrap(super(__SizedList, self).indexOf(arg0))

    @overload
    def getValue(self, arg0: float) -> object:
        """public T dev.ultreon.libs.collections.v0.list.SizedList.getValue(double)"""
        return object.__wrap(super(__SizedList, self).getValue(__double.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.list.SizedList()"""
        val = __SizedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def getSize(self, arg0: int) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.getSize(int)"""
        return __transform(super(__SizedList, self).getSize(__int.valueOf(arg0))).'Double'Value()

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.libs.collections.v0.list.SizedList.remove(int)"""
        super(__SizedList, self).remove(__int.valueOf(arg0))

    @overload
    def edit(self, arg0: object, arg1: float) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.edit(T,double)"""
        return __transform(super(__SizedList, self).edit(arg0, __double.valueOf(arg1))).'Double'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def add(self, arg0: float, arg1: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.add(double,T)"""
        return int.__wrap(super(__SizedList, self).add(__double.valueOf(arg0), arg1))

    @overload
    def rangeOf(self, arg0: object) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.libs.collections.v0.list.SizedList.rangeOf(T)"""
        return 'util.Range'.__wrap(super(__SizedList, self).rangeOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getRanges(self) -> List['util.Range']:
        """public dev.ultreon.libs.collections.v0.util.Range[] dev.ultreon.libs.collections.v0.list.SizedList.getRanges()"""
        return List['util.Range'].__wrap(super(SizedList, self).getRanges())

    @overload
    def insert(self, arg0: int, arg1: float, arg2: object) -> int:
        """public int dev.ultreon.libs.collections.v0.list.SizedList.insert(int,double,T)"""
        return int.__wrap(super(__SizedList, self).insert(__int.valueOf(arg0), __double.valueOf(arg1), arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.list.SizedList()"""
        val = __SizedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTotalSize(self) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.getTotalSize()"""
        return __transform(super(SizedList, self).getTotalSize()).'Double'Value()

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
    def edit(self, arg0: object, arg1: float, arg2: object) -> 'Double':
        """public java.lang.Double dev.ultreon.libs.collections.v0.list.SizedList.edit(T,double,T)"""
        return __transform(super(__SizedList, self).edit(arg0, __double.valueOf(arg1), arg2)).'Double'Value()

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
    def getRange(self, arg0: int) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.libs.collections.v0.list.SizedList.getRange(int)"""
        return 'util.Range'.__wrap(super(__SizedList, self).getRange(__int.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.list.SizedList 
 
 
# CLASS: dev.ultreon.libs.collections.v0.list.PagedList
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
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import dev.ultreon.libs.collections.v0.list.PagedList as __PagedList
__PagedList = __PagedList
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
 
class PagedList():
    """dev.ultreon.libs.collections.v0.list.PagedList"""
 
    @staticmethod
    def __wrap(java_value: __PagedList) -> 'PagedList':
        return PagedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PagedList):
        """
        Dynamic initializer for PagedList.
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
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object.__wrap(super(__ArrayList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool.__wrap(super(ArrayList, self).isEmpty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'.__wrap(super(__ArrayList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'.__wrap(super(ArrayList, self).iterator())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int)"""
        val = __PagedList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).retainAll(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Collection'):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int,java.util.Collection<? extends T>)"""
        val = __PagedList(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(__ArrayList, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool.__wrap(super(__ArrayList, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(__ArrayList, self).sort(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object].__wrap(super(__ArrayList, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object.__wrap(super(__ArrayList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object.__wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object].__wrap(super(ArrayList, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__ArrayList, self).removeIf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.collections.v0.list.PagedList(int,int)"""
        val = __PagedList(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'.__wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int.__wrap(super(ArrayList, self).size())

    @overload
    def __init__(self, arg0: 'PagedList'):
        """public dev.ultreon.libs.collections.v0.list.PagedList(dev.ultreon.libs.collections.v0.list.PagedList<? extends T>)"""
        val = __PagedList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(__ArrayList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object.__wrap(super(ArrayList, self).clone())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).indexOf(arg0))

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
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__ArrayList, self).listIterator(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object.__wrap(super(__ArrayList, self).get(__int.valueOf(arg0)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(__ArrayList, self).addFirst(arg0)

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object.__wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object.__wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int.__wrap(super(ArrayList, self).hashCode())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).contains(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(__int.valueOf(arg0), arg1))

    @overload
    def get(self, arg0: int, arg1: int) -> object:
        """public T dev.ultreon.libs.collections.v0.list.PagedList.get(int,int)"""
        return object.__wrap(super(__PagedList, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object.__wrap(super(ArrayList, self).getLast())

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
    def getFullPage(self, arg0: int) -> 'List':
        """public java.util.List<T> dev.ultreon.libs.collections.v0.list.PagedList.getFullPage(int)"""
        return 'List'.__wrap(super(__PagedList, self).getFullPage(__int.valueOf(arg0)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).remove(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(__ArrayList, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).equals(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).lastIndexOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(__ArrayList, self).forEach(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'.__wrap(super(ArrayList, self).listIterator())