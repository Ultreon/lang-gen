from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ImmutableArray(__Iterable, Iterable):
    """com.badlogic.ashley.utils.ImmutableArray"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableArray) -> 'ImmutableArray':
        return ImmutableArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableArray):
        """
        Dynamic initializer for ImmutableArray.
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
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.hashCode()"""
        return int.__wrap(super(ImmutableArray, self).hashCode())

    @overload
    def peek(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.peek()"""
        return object.__wrap(super(ImmutableArray, self).peek())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.ImmutableArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImmutableArray, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.ashley.utils.ImmutableArray.toArray(java.lang.Class<V>)"""
        return List[object].__wrap(super(__ImmutableArray, self).toArray(arg0))

    @overload
    def first(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.first()"""
        return object.__wrap(super(ImmutableArray, self).first())

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.lastIndexOf(T,boolean)"""
        return int.__wrap(super(__ImmutableArray, self).lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.ashley.utils.ImmutableArray.contains(T,boolean)"""
        return bool.__wrap(super(__ImmutableArray, self).contains(arg0, __boolean.valueOf(arg1)))

    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.ashley.utils.ImmutableArray.toArray()"""
        return List[object].__wrap(super(ImmutableArray, self).toArray())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.ashley.utils.ImmutableArray.iterator()"""
        return 'Iterator'.__wrap(super(ImmutableArray, self).iterator())

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.get(int)"""
        return object.__wrap(super(__ImmutableArray, self).get(__int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.indexOf(T,boolean)"""
        return int.__wrap(super(__ImmutableArray, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.ashley.utils.ImmutableArray.toString(java.lang.String)"""
        return str.__wrap(super(__ImmutableArray, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def size(self) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.size()"""
        return int.__wrap(super(ImmutableArray, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.ashley.utils.ImmutableArray.toString()"""
        return str.__wrap(super(ImmutableArray, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def random(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.random()"""
        return object.__wrap(super(ImmutableArray, self).random())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.ashley.utils.ImmutableArray(com.badlogic.gdx.utils.Array<T>)"""
        val = __ImmutableArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.ashley.utils.ImmutableArray
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ImmutableArray(__Iterable, Iterable):
    """com.badlogic.ashley.utils.ImmutableArray"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableArray) -> 'ImmutableArray':
        return ImmutableArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableArray):
        """
        Dynamic initializer for ImmutableArray.
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
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.hashCode()"""
        return int.__wrap(super(ImmutableArray, self).hashCode())

    @overload
    def peek(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.peek()"""
        return object.__wrap(super(ImmutableArray, self).peek())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.ImmutableArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImmutableArray, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.ashley.utils.ImmutableArray.toArray(java.lang.Class<V>)"""
        return List[object].__wrap(super(__ImmutableArray, self).toArray(arg0))

    @overload
    def first(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.first()"""
        return object.__wrap(super(ImmutableArray, self).first())

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.lastIndexOf(T,boolean)"""
        return int.__wrap(super(__ImmutableArray, self).lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.ashley.utils.ImmutableArray.contains(T,boolean)"""
        return bool.__wrap(super(__ImmutableArray, self).contains(arg0, __boolean.valueOf(arg1)))

    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.ashley.utils.ImmutableArray.toArray()"""
        return List[object].__wrap(super(ImmutableArray, self).toArray())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.ashley.utils.ImmutableArray.iterator()"""
        return 'Iterator'.__wrap(super(ImmutableArray, self).iterator())

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.get(int)"""
        return object.__wrap(super(__ImmutableArray, self).get(__int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.indexOf(T,boolean)"""
        return int.__wrap(super(__ImmutableArray, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.ashley.utils.ImmutableArray.toString(java.lang.String)"""
        return str.__wrap(super(__ImmutableArray, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def size(self) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.size()"""
        return int.__wrap(super(ImmutableArray, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.ashley.utils.ImmutableArray.toString()"""
        return str.__wrap(super(ImmutableArray, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def random(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.random()"""
        return object.__wrap(super(ImmutableArray, self).random())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.ashley.utils.ImmutableArray(com.badlogic.gdx.utils.Array<T>)"""
        val = __ImmutableArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.ashley.utils.ImmutableArray 
 
 
# CLASS: com.badlogic.ashley.utils.Bag
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.utils.Bag as __Bag
__Bag = __Bag
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
 
class Bag():
    """com.badlogic.ashley.utils.Bag"""
 
    @staticmethod
    def __wrap(java_value: __Bag) -> 'Bag':
        return Bag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bag):
        """
        Dynamic initializer for Bag.
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

    @overload
    def set(self, arg0: int, arg1: object):
        """public void com.badlogic.ashley.utils.Bag.set(int,E)"""
        super(__Bag, self).set(__int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.ashley.utils.Bag(int)"""
        val = __Bag(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.remove(E)"""
        return bool.__wrap(super(__Bag, self).remove(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.ashley.utils.Bag.clear()"""
        super(Bag, self).clear()

    @overload
    def getCapacity(self) -> int:
        """public int com.badlogic.ashley.utils.Bag.getCapacity()"""
        return int.__wrap(super(Bag, self).getCapacity())

    @overload
    def remove(self, arg0: int) -> object:
        """public E com.badlogic.ashley.utils.Bag.remove(int)"""
        return object.__wrap(super(__Bag, self).remove(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.utils.Bag()"""
        val = __Bag()
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.ashley.utils.Bag()"""
        val = __Bag()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isIndexWithinBounds(self, arg0: int) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.isIndexWithinBounds(int)"""
        return bool.__wrap(super(__Bag, self).isIndexWithinBounds(__int.valueOf(arg0)))

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.ashley.utils.Bag.add(E)"""
        super(__Bag, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self, arg0: int) -> object:
        """public E com.badlogic.ashley.utils.Bag.get(int)"""
        return object.__wrap(super(__Bag, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.contains(E)"""
        return bool.__wrap(super(__Bag, self).contains(arg0))

    @overload
    def removeLast(self) -> object:
        """public E com.badlogic.ashley.utils.Bag.removeLast()"""
        return object.__wrap(super(Bag, self).removeLast())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.isEmpty()"""
        return bool.__wrap(super(Bag, self).isEmpty())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def size(self) -> int:
        """public int com.badlogic.ashley.utils.Bag.size()"""
        return int.__wrap(super(Bag, self).size())