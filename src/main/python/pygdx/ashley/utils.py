from __future__ import annotations
from overload import overload


 
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
from builtins import bool
import com.badlogic.ashley.utils.Bag as _Bag
_Bag = _Bag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bag():
    """com.badlogic.ashley.utils.Bag"""
 
    @staticmethod
    def _wrap(java_value: _Bag) -> 'Bag':
        return Bag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bag):
        """
        Dynamic initializer for Bag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def size(self) -> int:
        """public int com.badlogic.ashley.utils.Bag.size()"""
        return int._wrap(super(Bag, self).size())

    @overload
    def remove(self, arg0: int) -> object:
        """public E com.badlogic.ashley.utils.Bag.remove(int)"""
        return object._wrap(super(_Bag, self).remove(_int.valueOf(arg0)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.remove(E)"""
        return bool._wrap(super(_Bag, self).remove(arg0))

    @overload
    def getCapacity(self) -> int:
        """public int com.badlogic.ashley.utils.Bag.getCapacity()"""
        return int._wrap(super(Bag, self).getCapacity())

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
    def clear(self):
        """public void com.badlogic.ashley.utils.Bag.clear()"""
        super(Bag, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isIndexWithinBounds(self, arg0: int) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.isIndexWithinBounds(int)"""
        return bool._wrap(super(_Bag, self).isIndexWithinBounds(_int.valueOf(arg0)))

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
    def __init__(self, ):
        """public com.badlogic.ashley.utils.Bag()"""
        val = _Bag()
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object):
        """public void com.badlogic.ashley.utils.Bag.set(int,E)"""
        super(_Bag, self).set(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.ashley.utils.Bag(int)"""
        val = _Bag(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.ashley.utils.Bag.add(E)"""
        super(_Bag, self).add(arg0)

    @overload
    def get(self, arg0: int) -> object:
        """public E com.badlogic.ashley.utils.Bag.get(int)"""
        return object._wrap(super(_Bag, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.ashley.utils.Bag()"""
        val = _Bag()
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.isEmpty()"""
        return bool._wrap(super(Bag, self).isEmpty())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.contains(E)"""
        return bool._wrap(super(_Bag, self).contains(arg0))

    @overload
    def removeLast(self) -> object:
        """public E com.badlogic.ashley.utils.Bag.removeLast()"""
        return object._wrap(super(Bag, self).removeLast())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.ashley.utils.Bag
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
from builtins import bool
import com.badlogic.ashley.utils.Bag as _Bag
_Bag = _Bag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bag():
    """com.badlogic.ashley.utils.Bag"""
 
    @staticmethod
    def _wrap(java_value: _Bag) -> 'Bag':
        return Bag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bag):
        """
        Dynamic initializer for Bag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def size(self) -> int:
        """public int com.badlogic.ashley.utils.Bag.size()"""
        return int._wrap(super(Bag, self).size())

    @overload
    def remove(self, arg0: int) -> object:
        """public E com.badlogic.ashley.utils.Bag.remove(int)"""
        return object._wrap(super(_Bag, self).remove(_int.valueOf(arg0)))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.remove(E)"""
        return bool._wrap(super(_Bag, self).remove(arg0))

    @overload
    def getCapacity(self) -> int:
        """public int com.badlogic.ashley.utils.Bag.getCapacity()"""
        return int._wrap(super(Bag, self).getCapacity())

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
    def clear(self):
        """public void com.badlogic.ashley.utils.Bag.clear()"""
        super(Bag, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isIndexWithinBounds(self, arg0: int) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.isIndexWithinBounds(int)"""
        return bool._wrap(super(_Bag, self).isIndexWithinBounds(_int.valueOf(arg0)))

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
    def __init__(self, ):
        """public com.badlogic.ashley.utils.Bag()"""
        val = _Bag()
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object):
        """public void com.badlogic.ashley.utils.Bag.set(int,E)"""
        super(_Bag, self).set(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.ashley.utils.Bag(int)"""
        val = _Bag(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.ashley.utils.Bag.add(E)"""
        super(_Bag, self).add(arg0)

    @overload
    def get(self, arg0: int) -> object:
        """public E com.badlogic.ashley.utils.Bag.get(int)"""
        return object._wrap(super(_Bag, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.ashley.utils.Bag()"""
        val = _Bag()
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.isEmpty()"""
        return bool._wrap(super(Bag, self).isEmpty())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.Bag.contains(E)"""
        return bool._wrap(super(_Bag, self).contains(arg0))

    @overload
    def removeLast(self) -> object:
        """public E com.badlogic.ashley.utils.Bag.removeLast()"""
        return object._wrap(super(Bag, self).removeLast())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.ashley.utils.Bag 
 
 
# CLASS: com.badlogic.ashley.utils.ImmutableArray
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableArray():
    """com.badlogic.ashley.utils.ImmutableArray"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableArray) -> 'ImmutableArray':
        return ImmutableArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableArray):
        """
        Dynamic initializer for ImmutableArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.hashCode()"""
        return int._wrap(super(ImmutableArray, self).hashCode())

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.get(int)"""
        return object._wrap(super(_ImmutableArray, self).get(_int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.indexOf(T,boolean)"""
        return int._wrap(super(_ImmutableArray, self).indexOf(arg0, _boolean.valueOf(arg1)))

    @overload
    def random(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.random()"""
        return object._wrap(super(ImmutableArray, self).random())

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
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.ashley.utils.ImmutableArray.toArray()"""
        return List[object]._wrap(super(ImmutableArray, self).toArray())

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.ashley.utils.ImmutableArray.contains(T,boolean)"""
        return bool._wrap(super(_ImmutableArray, self).contains(arg0, _boolean.valueOf(arg1)))

    @overload
    def first(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.first()"""
        return object._wrap(super(ImmutableArray, self).first())

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.ashley.utils.ImmutableArray.toArray(java.lang.Class<V>)"""
        return List[object]._wrap(super(_ImmutableArray, self).toArray(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.ashley.utils.ImmutableArray.toString()"""
        return str._wrap(super(ImmutableArray, self).toString())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.ashley.utils.ImmutableArray.toString(java.lang.String)"""
        return str._wrap(super(_ImmutableArray, self).toString(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.utils.ImmutableArray.equals(java.lang.Object)"""
        return bool._wrap(super(_ImmutableArray, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.lastIndexOf(T,boolean)"""
        return int._wrap(super(_ImmutableArray, self).lastIndexOf(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def size(self) -> int:
        """public int com.badlogic.ashley.utils.ImmutableArray.size()"""
        return int._wrap(super(ImmutableArray, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.ashley.utils.ImmutableArray.iterator()"""
        return 'Iterator'._wrap(super(ImmutableArray, self).iterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def peek(self) -> object:
        """public T com.badlogic.ashley.utils.ImmutableArray.peek()"""
        return object._wrap(super(ImmutableArray, self).peek())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.ashley.utils.ImmutableArray(com.badlogic.gdx.utils.Array<T>)"""
        val = _ImmutableArray(arg0)
        self.__wrapper = val