from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.ResettableListIterator as _ResettableListIterator
_ResettableListIterator = _ResettableListIterator
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.EmptyListIterator as _EmptyListIterator
_EmptyListIterator = _EmptyListIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.ListIterator as ListIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmptyListIterator():
    """org.apache.commons.collections4.iterators.EmptyListIterator"""
 
    @staticmethod
    def _wrap(java_value: _EmptyListIterator) -> 'EmptyListIterator':
        return EmptyListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmptyListIterator):
        """
        Dynamic initializer for EmptyListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmptyListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmptyListIterator__wrapper":
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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

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

    @staticmethod
    @overload
    def emptyListIterator() -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.iterators.EmptyListIterator.emptyListIterator()"""
        return ListIterator._wrap(_EmptyListIterator.emptyListIterator())

    @staticmethod
    @overload
    def resettableEmptyListIterator() -> 'collections4.ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.iterators.EmptyListIterator.resettableEmptyListIterator()"""
        return collections4.ResettableListIterator._wrap(_EmptyListIterator.resettableEmptyListIterator())

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

 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyListIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.ResettableListIterator as _ResettableListIterator
_ResettableListIterator = _ResettableListIterator
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.EmptyListIterator as _EmptyListIterator
_EmptyListIterator = _EmptyListIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.ListIterator as ListIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmptyListIterator():
    """org.apache.commons.collections4.iterators.EmptyListIterator"""
 
    @staticmethod
    def _wrap(java_value: _EmptyListIterator) -> 'EmptyListIterator':
        return EmptyListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmptyListIterator):
        """
        Dynamic initializer for EmptyListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmptyListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmptyListIterator__wrapper":
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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

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

    @staticmethod
    @overload
    def emptyListIterator() -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.iterators.EmptyListIterator.emptyListIterator()"""
        return ListIterator._wrap(_EmptyListIterator.emptyListIterator())

    @staticmethod
    @overload
    def resettableEmptyListIterator() -> 'collections4.ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.iterators.EmptyListIterator.resettableEmptyListIterator()"""
        return collections4.ResettableListIterator._wrap(_EmptyListIterator.resettableEmptyListIterator())

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

 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyListIterator 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator as _UnmodifiableOrderedMapIterator
_UnmodifiableOrderedMapIterator = _UnmodifiableOrderedMapIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableOrderedMapIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableOrderedMapIterator) -> 'UnmodifiableOrderedMapIterator':
        return UnmodifiableOrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableOrderedMapIterator):
        """
        Dynamic initializer for UnmodifiableOrderedMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableOrderedMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableOrderedMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.getValue()"""
        return object._wrap(super(UnmodifiableOrderedMapIterator, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.getKey()"""
        return object._wrap(super(UnmodifiableOrderedMapIterator, self).getKey())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.remove()"""
        super(UnmodifiableOrderedMapIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.setValue(V)"""
        return object._wrap(super(_UnmodifiableOrderedMapIterator, self).setValue(arg0))

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.next()"""
        return object._wrap(super(UnmodifiableOrderedMapIterator, self).next())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.previous()"""
        return object._wrap(super(UnmodifiableOrderedMapIterator, self).previous())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.hasNext()"""
        return bool._wrap(super(UnmodifiableOrderedMapIterator, self).hasNext())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.hasPrevious()"""
        return bool._wrap(super(UnmodifiableOrderedMapIterator, self).hasPrevious())

    @staticmethod
    @overload
    def unmodifiableOrderedMapIterator(arg0: 'OrderedMapIterator') -> 'collections4.OrderedMapIterator':
        """public static <K,V> org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.unmodifiableOrderedMapIterator(org.apache.commons.collections4.OrderedMapIterator<K, ? extends V>)"""
        return collections4.OrderedMapIterator._wrap(_UnmodifiableOrderedMapIterator.unmodifiableOrderedMapIterator(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.iterators.SingletonIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.SingletonIterator as _SingletonIterator
_SingletonIterator = _SingletonIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SingletonIterator():
    """org.apache.commons.collections4.iterators.SingletonIterator"""
 
    @staticmethod
    def _wrap(java_value: _SingletonIterator) -> 'SingletonIterator':
        return SingletonIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SingletonIterator):
        """
        Dynamic initializer for SingletonIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SingletonIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SingletonIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.SingletonIterator.hasNext()"""
        return bool._wrap(super(SingletonIterator, self).hasNext())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.SingletonIterator.reset()"""
        super(SingletonIterator, self).reset()

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
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.SingletonIterator(E)"""
        val = _SingletonIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.SingletonIterator.remove()"""
        super(SingletonIterator, self).remove()

    @overload
    def __init__(self, arg0: object, arg1: bool):
        """public org.apache.commons.collections4.iterators.SingletonIterator(E,boolean)"""
        val = _SingletonIterator(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.SingletonIterator.next()"""
        return object._wrap(super(SingletonIterator, self).next())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ZippingIterator
from builtins import str
import org.apache.commons.collections4.iterators.ZippingIterator as _ZippingIterator
_ZippingIterator = _ZippingIterator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ZippingIterator():
    """org.apache.commons.collections4.iterators.ZippingIterator"""
 
    @staticmethod
    def _wrap(java_value: _ZippingIterator) -> 'ZippingIterator':
        return ZippingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ZippingIterator):
        """
        Dynamic initializer for ZippingIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ZippingIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ZippingIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, *arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ZippingIterator(java.util.Iterator<? extends E>...)"""
        val = _ZippingIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ZippingIterator.hasNext()"""
        return bool._wrap(super(ZippingIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ZippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = _ZippingIterator(arg0, arg1)
        self.__wrapper = val

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ZippingIterator.next() throws java.util.NoSuchElementException"""
        return object._wrap(super(ZippingIterator, self).next())

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

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Iterator', arg2: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ZippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = _ZippingIterator(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ZippingIterator.remove()"""
        super(ZippingIterator, self).remove()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableMapIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.iterators.UnmodifiableMapIterator as _UnmodifiableMapIterator
_UnmodifiableMapIterator = _UnmodifiableMapIterator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableMapIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableMapIterator) -> 'UnmodifiableMapIterator':
        return UnmodifiableMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableMapIterator):
        """
        Dynamic initializer for UnmodifiableMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableMapIterator.getKey()"""
        return object._wrap(super(UnmodifiableMapIterator, self).getKey())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableMapIterator.remove()"""
        super(UnmodifiableMapIterator, self).remove()

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

    @staticmethod
    @overload
    def unmodifiableMapIterator(arg0: 'MapIterator') -> 'collections4.MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.iterators.UnmodifiableMapIterator.unmodifiableMapIterator(org.apache.commons.collections4.MapIterator<? extends K, ? extends V>)"""
        return collections4.MapIterator._wrap(_UnmodifiableMapIterator.unmodifiableMapIterator(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableMapIterator.hasNext()"""
        return bool._wrap(super(UnmodifiableMapIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableMapIterator.next()"""
        return object._wrap(super(UnmodifiableMapIterator, self).next())

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

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableMapIterator.setValue(V)"""
        return object._wrap(super(_UnmodifiableMapIterator, self).setValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableMapIterator.getValue()"""
        return object._wrap(super(UnmodifiableMapIterator, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ObjectArrayIterator
import org.apache.commons.collections4.iterators.ObjectArrayIterator as _ObjectArrayIterator
_ObjectArrayIterator = _ObjectArrayIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectArrayIterator():
    """org.apache.commons.collections4.iterators.ObjectArrayIterator"""
 
    @staticmethod
    def _wrap(java_value: _ObjectArrayIterator) -> 'ObjectArrayIterator':
        return ObjectArrayIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectArrayIterator):
        """
        Dynamic initializer for ObjectArrayIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectArrayIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectArrayIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getArray(self) -> List[object]:
        """public E[] org.apache.commons.collections4.iterators.ObjectArrayIterator.getArray()"""
        return List[object]._wrap(super(ObjectArrayIterator, self).getArray())

    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getStartIndex()"""
        return int._wrap(super(ObjectArrayIterator, self).getStartIndex())

    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getEndIndex()"""
        return int._wrap(super(ObjectArrayIterator, self).getEndIndex())

    @overload
    def __init__(self, *arg0: object):
        """public org.apache.commons.collections4.iterators.ObjectArrayIterator(E...)"""
        val = _ObjectArrayIterator(arg0)
        self.__wrapper = val

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
    def __init__(self, arg0: 'Object', arg1: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayIterator(E[],int)"""
        val = _ObjectArrayIterator(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectArrayIterator.hasNext()"""
        return bool._wrap(super(ObjectArrayIterator, self).hasNext())

    @overload
    def __init__(self, arg0: 'Object', arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayIterator(E[],int,int)"""
        val = _ObjectArrayIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayIterator.remove()"""
        super(ObjectArrayIterator, self).remove()

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectArrayIterator.next()"""
        return object._wrap(super(ObjectArrayIterator, self).next())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayIterator.reset()"""
        super(ObjectArrayIterator, self).reset()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ArrayListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.ArrayListIterator as _ArrayListIterator
_ArrayListIterator = _ArrayListIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.ArrayIterator as _ArrayIterator
_ArrayIterator = _ArrayIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayListIterator():
    """org.apache.commons.collections4.iterators.ArrayListIterator"""
 
    @staticmethod
    def _wrap(java_value: _ArrayListIterator) -> 'ArrayListIterator':
        return ArrayListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayListIterator):
        """
        Dynamic initializer for ArrayListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: int):
        """public org.apache.commons.collections4.iterators.ArrayListIterator(java.lang.Object,int)"""
        val = _ArrayListIterator(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ArrayListIterator.set(java.lang.Object)"""
        super(_ArrayListIterator, self).set(arg0)

    @override
    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getStartIndex()"""
        return int._wrap(super(ArrayIterator, self).getStartIndex())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayListIterator.previousIndex()"""
        return int._wrap(super(ArrayListIterator, self).previousIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ArrayIterator.remove()"""
        super(ArrayIterator, self).remove()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ArrayListIterator.previous()"""
        return object._wrap(super(ArrayListIterator, self).previous())

    @override
    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getEndIndex()"""
        return int._wrap(super(ArrayIterator, self).getEndIndex())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.ArrayListIterator(java.lang.Object)"""
        val = _ArrayListIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ArrayListIterator.add(java.lang.Object)"""
        super(_ArrayListIterator, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ArrayListIterator(java.lang.Object,int,int)"""
        val = _ArrayListIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

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

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ArrayListIterator.hasPrevious()"""
        return bool._wrap(super(ArrayListIterator, self).hasPrevious())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayListIterator.nextIndex()"""
        return int._wrap(super(ArrayListIterator, self).nextIndex())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ArrayIterator.hasNext()"""
        return bool._wrap(super(ArrayIterator, self).hasNext())

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
    def getArray(self) -> object:
        """public java.lang.Object org.apache.commons.collections4.iterators.ArrayIterator.getArray()"""
        return object._wrap(super(ArrayIterator, self).getArray())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ArrayListIterator.reset()"""
        super(ArrayListIterator, self).reset()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ArrayListIterator.next()"""
        return object._wrap(super(ArrayListIterator, self).next())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractEmptyMapIterator
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
import java.lang.Long as _long
import org.apache.commons.collections4.iterators.AbstractEmptyMapIterator as _AbstractEmptyMapIterator
_AbstractEmptyMapIterator = _AbstractEmptyMapIterator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractEmptyMapIterator():
    """org.apache.commons.collections4.iterators.AbstractEmptyMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractEmptyMapIterator) -> 'AbstractEmptyMapIterator':
        return AbstractEmptyMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractEmptyMapIterator):
        """
        Dynamic initializer for AbstractEmptyMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractEmptyMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractEmptyMapIterator__wrapper":
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

    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getValue()"""
        return object._wrap(super(AbstractEmptyMapIterator, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.AbstractEmptyMapIterator()"""
        val = _AbstractEmptyMapIterator()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.setValue(V)"""
        return object._wrap(super(_AbstractEmptyMapIterator, self).setValue(arg0))

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

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.AbstractEmptyMapIterator()"""
        val = _AbstractEmptyMapIterator()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getKey()"""
        return object._wrap(super(AbstractEmptyMapIterator, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.LoopingListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.iterators.LoopingListIterator as _LoopingListIterator
_LoopingListIterator = _LoopingListIterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class LoopingListIterator():
    """org.apache.commons.collections4.iterators.LoopingListIterator"""
 
    @staticmethod
    def _wrap(java_value: _LoopingListIterator) -> 'LoopingListIterator':
        return LoopingListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoopingListIterator):
        """
        Dynamic initializer for LoopingListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoopingListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoopingListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.set(E)"""
        super(_LoopingListIterator, self).set(arg0)

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingListIterator.nextIndex()"""
        return int._wrap(super(LoopingListIterator, self).nextIndex())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LoopingListIterator.hasPrevious()"""
        return bool._wrap(super(LoopingListIterator, self).hasPrevious())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.remove()"""
        super(LoopingListIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingListIterator.size()"""
        return int._wrap(super(LoopingListIterator, self).size())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LoopingListIterator.hasNext()"""
        return bool._wrap(super(LoopingListIterator, self).hasNext())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.add(E)"""
        super(_LoopingListIterator, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingListIterator.previousIndex()"""
        return int._wrap(super(LoopingListIterator, self).previousIndex())

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.iterators.LoopingListIterator(java.util.List<E>)"""
        val = _LoopingListIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.reset()"""
        super(LoopingListIterator, self).reset()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.LoopingListIterator.next()"""
        return object._wrap(super(LoopingListIterator, self).next())

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
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.LoopingListIterator.previous()"""
        return object._wrap(super(LoopingListIterator, self).previous())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ReverseListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.ReverseListIterator as _ReverseListIterator
_ReverseListIterator = _ReverseListIterator
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
import java.util.List as List
 
class ReverseListIterator():
    """org.apache.commons.collections4.iterators.ReverseListIterator"""
 
    @staticmethod
    def _wrap(java_value: _ReverseListIterator) -> 'ReverseListIterator':
        return ReverseListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReverseListIterator):
        """
        Dynamic initializer for ReverseListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReverseListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReverseListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ReverseListIterator.hasNext()"""
        return bool._wrap(super(ReverseListIterator, self).hasNext())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ReverseListIterator.previous()"""
        return object._wrap(super(ReverseListIterator, self).previous())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.set(E)"""
        super(_ReverseListIterator, self).set(arg0)

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ReverseListIterator.hasPrevious()"""
        return bool._wrap(super(ReverseListIterator, self).hasPrevious())

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
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ReverseListIterator.previousIndex()"""
        return int._wrap(super(ReverseListIterator, self).previousIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.add(E)"""
        super(_ReverseListIterator, self).add(arg0)

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
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.reset()"""
        super(ReverseListIterator, self).reset()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ReverseListIterator.next()"""
        return object._wrap(super(ReverseListIterator, self).next())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.iterators.ReverseListIterator(java.util.List<E>)"""
        val = _ReverseListIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ReverseListIterator.nextIndex()"""
        return int._wrap(super(ReverseListIterator, self).nextIndex())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.remove()"""
        super(ReverseListIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractIteratorDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import org.apache.commons.collections4.iterators.AbstractIteratorDecorator as _AbstractIteratorDecorator
_AbstractIteratorDecorator = _AbstractIteratorDecorator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractIteratorDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractIteratorDecorator) -> 'AbstractIteratorDecorator':
        return AbstractIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractIteratorDecorator):
        """
        Dynamic initializer for AbstractIteratorDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractIteratorDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractIteratorDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractIteratorDecorator.next()"""
        return object._wrap(super(AbstractIteratorDecorator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(AbstractUntypedIteratorDecorator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.remove()"""
        super(AbstractUntypedIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractUntypedIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractUntypedIteratorDecorator) -> 'AbstractUntypedIteratorDecorator':
        return AbstractUntypedIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractUntypedIteratorDecorator):
        """
        Dynamic initializer for AbstractUntypedIteratorDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractUntypedIteratorDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractUntypedIteratorDecorator__wrapper":
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

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.Iterator.next()"""
        pass

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(AbstractUntypedIteratorDecorator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.remove()"""
        super(AbstractUntypedIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.PermutationIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.PermutationIterator as _PermutationIterator
_PermutationIterator = _PermutationIterator
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PermutationIterator():
    """org.apache.commons.collections4.iterators.PermutationIterator"""
 
    @staticmethod
    def _wrap(java_value: _PermutationIterator) -> 'PermutationIterator':
        return PermutationIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PermutationIterator):
        """
        Dynamic initializer for PermutationIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PermutationIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PermutationIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.iterators.PermutationIterator(java.util.Collection<? extends E>)"""
        val = _PermutationIterator(arg0)
        self.__wrapper = val

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.PermutationIterator.hasNext()"""
        return bool._wrap(super(PermutationIterator, self).hasNext())

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
    def next(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.iterators.PermutationIterator.next()"""
        return 'List'._wrap(super(PermutationIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.PermutationIterator.remove()"""
        super(PermutationIterator, self).remove()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.LoopingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.LoopingIterator as _LoopingIterator
_LoopingIterator = _LoopingIterator
import java.util.Collection as Collection
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
 
class LoopingIterator():
    """org.apache.commons.collections4.iterators.LoopingIterator"""
 
    @staticmethod
    def _wrap(java_value: _LoopingIterator) -> 'LoopingIterator':
        return LoopingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoopingIterator):
        """
        Dynamic initializer for LoopingIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoopingIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoopingIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.LoopingIterator.next()"""
        return object._wrap(super(LoopingIterator, self).next())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LoopingIterator.hasNext()"""
        return bool._wrap(super(LoopingIterator, self).hasNext())

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

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.iterators.LoopingIterator(java.util.Collection<? extends E>)"""
        val = _LoopingIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.LoopingIterator.reset()"""
        super(LoopingIterator, self).reset()

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingIterator.size()"""
        return int._wrap(super(LoopingIterator, self).size())

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.LoopingIterator.remove()"""
        super(LoopingIterator, self).remove()

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
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyOrderedMapIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.EmptyOrderedMapIterator as _EmptyOrderedMapIterator
_EmptyOrderedMapIterator = _EmptyOrderedMapIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.collections4.iterators.AbstractEmptyMapIterator as _AbstractEmptyMapIterator
_AbstractEmptyMapIterator = _AbstractEmptyMapIterator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmptyOrderedMapIterator():
    """org.apache.commons.collections4.iterators.EmptyOrderedMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _EmptyOrderedMapIterator) -> 'EmptyOrderedMapIterator':
        return EmptyOrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmptyOrderedMapIterator):
        """
        Dynamic initializer for EmptyOrderedMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmptyOrderedMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmptyOrderedMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getKey()"""
        return object._wrap(super(AbstractEmptyMapIterator, self).getKey())

    @staticmethod
    @overload
    def emptyOrderedMapIterator() -> 'collections4.OrderedMapIterator':
        """public static <K,V> org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.iterators.EmptyOrderedMapIterator.emptyOrderedMapIterator()"""
        return collections4.OrderedMapIterator._wrap(_EmptyOrderedMapIterator.emptyOrderedMapIterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getValue()"""
        return object._wrap(super(AbstractEmptyMapIterator, self).getValue())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.setValue(V)"""
        return object._wrap(super(_AbstractEmptyMapIterator, self).setValue(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EnumerationIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.Enumeration as _Enumeration
_Enumeration = _Enumeration
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.iterators.EnumerationIterator as _EnumerationIterator
_EnumerationIterator = _EnumerationIterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Enumeration as Enumeration
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EnumerationIterator():
    """org.apache.commons.collections4.iterators.EnumerationIterator"""
 
    @staticmethod
    def _wrap(java_value: _EnumerationIterator) -> 'EnumerationIterator':
        return EnumerationIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnumerationIterator):
        """
        Dynamic initializer for EnumerationIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnumerationIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnumerationIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.EnumerationIterator.hasNext()"""
        return bool._wrap(super(EnumerationIterator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.EnumerationIterator.remove()"""
        super(EnumerationIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Enumeration'):
        """public org.apache.commons.collections4.iterators.EnumerationIterator(java.util.Enumeration<? extends E>)"""
        val = _EnumerationIterator(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.EnumerationIterator()"""
        val = _EnumerationIterator()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getEnumeration(self) -> 'Enumeration':
        """public java.util.Enumeration<? extends E> org.apache.commons.collections4.iterators.EnumerationIterator.getEnumeration()"""
        return 'Enumeration'._wrap(super(EnumerationIterator, self).getEnumeration())

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

    @overload
    def __init__(self, arg0: 'Enumeration', arg1: 'Collection'):
        """public org.apache.commons.collections4.iterators.EnumerationIterator(java.util.Enumeration<? extends E>,java.util.Collection<? super E>)"""
        val = _EnumerationIterator(arg0, arg1)
        self.__wrapper = val

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.EnumerationIterator.next()"""
        return object._wrap(super(EnumerationIterator, self).next())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.EnumerationIterator()"""
        val = _EnumerationIterator()
        self.__wrapper = val

    @overload
    def setEnumeration(self, arg0: 'Enumeration'):
        """public void org.apache.commons.collections4.iterators.EnumerationIterator.setEnumeration(java.util.Enumeration<? extends E>)"""
        super(_EnumerationIterator, self).setEnumeration(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ArrayIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.ArrayIterator as _ArrayIterator
_ArrayIterator = _ArrayIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayIterator():
    """org.apache.commons.collections4.iterators.ArrayIterator"""
 
    @staticmethod
    def _wrap(java_value: _ArrayIterator) -> 'ArrayIterator':
        return ArrayIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayIterator):
        """
        Dynamic initializer for ArrayIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: int):
        """public org.apache.commons.collections4.iterators.ArrayIterator(java.lang.Object,int)"""
        val = _ArrayIterator(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getStartIndex()"""
        return int._wrap(super(ArrayIterator, self).getStartIndex())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ArrayIterator.reset()"""
        super(ArrayIterator, self).reset()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ArrayIterator.next()"""
        return object._wrap(super(ArrayIterator, self).next())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ArrayIterator(java.lang.Object,int,int)"""
        val = _ArrayIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.ArrayIterator(java.lang.Object)"""
        val = _ArrayIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ArrayIterator.remove()"""
        super(ArrayIterator, self).remove()

    @overload
    def getArray(self) -> object:
        """public java.lang.Object org.apache.commons.collections4.iterators.ArrayIterator.getArray()"""
        return object._wrap(super(ArrayIterator, self).getArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ArrayIterator.hasNext()"""
        return bool._wrap(super(ArrayIterator, self).hasNext())

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

    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getEndIndex()"""
        return int._wrap(super(ArrayIterator, self).getEndIndex())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import org.apache.commons.collections4.iterators.UnmodifiableListIterator as _UnmodifiableListIterator
_UnmodifiableListIterator = _UnmodifiableListIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.util.ListIterator as ListIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableListIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableListIterator"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableListIterator) -> 'UnmodifiableListIterator':
        return UnmodifiableListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableListIterator):
        """
        Dynamic initializer for UnmodifiableListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableListIterator.hasPrevious()"""
        return bool._wrap(super(UnmodifiableListIterator, self).hasPrevious())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableListIterator.remove()"""
        super(UnmodifiableListIterator, self).remove()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.UnmodifiableListIterator.add(E)"""
        super(_UnmodifiableListIterator, self).add(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.UnmodifiableListIterator.set(E)"""
        super(_UnmodifiableListIterator, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableListIterator.hasNext()"""
        return bool._wrap(super(UnmodifiableListIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableListIterator.next()"""
        return object._wrap(super(UnmodifiableListIterator, self).next())

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
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.UnmodifiableListIterator.nextIndex()"""
        return int._wrap(super(UnmodifiableListIterator, self).nextIndex())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableListIterator.previous()"""
        return object._wrap(super(UnmodifiableListIterator, self).previous())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.UnmodifiableListIterator.previousIndex()"""
        return int._wrap(super(UnmodifiableListIterator, self).previousIndex())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @staticmethod
    @overload
    def umodifiableListIterator(arg0: 'ListIterator') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.iterators.UnmodifiableListIterator.umodifiableListIterator(java.util.ListIterator<? extends E>)"""
        return ListIterator._wrap(_UnmodifiableListIterator.umodifiableListIterator(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.iterators.FilterListIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import org.apache.commons.collections4.iterators.FilterListIterator as _FilterListIterator
_FilterListIterator = _FilterListIterator
import java.util.ListIterator as ListIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FilterListIterator():
    """org.apache.commons.collections4.iterators.FilterListIterator"""
 
    @staticmethod
    def _wrap(java_value: _FilterListIterator) -> 'FilterListIterator':
        return FilterListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FilterListIterator):
        """
        Dynamic initializer for FilterListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FilterListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FilterListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.remove()"""
        super(FilterListIterator, self).remove()

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.FilterListIterator.nextIndex()"""
        return int._wrap(super(FilterListIterator, self).nextIndex())

    @overload
    def setPredicate(self, arg0: 'Predicate'):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.setPredicate(org.apache.commons.collections4.Predicate<? super E>)"""
        super(_FilterListIterator, self).setPredicate(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.iterators.FilterListIterator.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(FilterListIterator, self).getPredicate())

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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterListIterator.hasPrevious()"""
        return bool._wrap(super(FilterListIterator, self).hasPrevious())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.FilterListIterator()"""
        val = _FilterListIterator()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.iterators.FilterListIterator(org.apache.commons.collections4.Predicate<? super E>)"""
        val = _FilterListIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.set(E)"""
        super(_FilterListIterator, self).set(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.FilterListIterator.previousIndex()"""
        return int._wrap(super(FilterListIterator, self).previousIndex())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterListIterator.hasNext()"""
        return bool._wrap(super(FilterListIterator, self).hasNext())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.FilterListIterator()"""
        val = _FilterListIterator()
        self.__wrapper = val

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
    def getListIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<? extends E> org.apache.commons.collections4.iterators.FilterListIterator.getListIterator()"""
        return 'ListIterator'._wrap(super(FilterListIterator, self).getListIterator())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterListIterator.previous()"""
        return object._wrap(super(FilterListIterator, self).previous())

    @overload
    def __init__(self, arg0: 'ListIterator', arg1: 'Predicate'):
        """public org.apache.commons.collections4.iterators.FilterListIterator(java.util.ListIterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        val = _FilterListIterator(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.add(E)"""
        super(_FilterListIterator, self).add(arg0)

    @overload
    def setListIterator(self, arg0: 'ListIterator'):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.setListIterator(java.util.ListIterator<? extends E>)"""
        super(_FilterListIterator, self).setListIterator(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'ListIterator'):
        """public org.apache.commons.collections4.iterators.FilterListIterator(java.util.ListIterator<? extends E>)"""
        val = _FilterListIterator(arg0)
        self.__wrapper = val

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterListIterator.next()"""
        return object._wrap(super(FilterListIterator, self).next())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.ResettableIterator as _ResettableIterator
_ResettableIterator = _ResettableIterator
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.EmptyIterator as _EmptyIterator
_EmptyIterator = _EmptyIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmptyIterator():
    """org.apache.commons.collections4.iterators.EmptyIterator"""
 
    @staticmethod
    def _wrap(java_value: _EmptyIterator) -> 'EmptyIterator':
        return EmptyIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmptyIterator):
        """
        Dynamic initializer for EmptyIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmptyIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmptyIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def emptyIterator() -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.iterators.EmptyIterator.emptyIterator()"""
        return Iterator._wrap(_EmptyIterator.emptyIterator())

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

    @staticmethod
    @overload
    def resettableEmptyIterator() -> 'collections4.ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.iterators.EmptyIterator.resettableEmptyIterator()"""
        return collections4.ResettableIterator._wrap(_EmptyIterator.resettableEmptyIterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

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
 
 
# CLASS: org.apache.commons.collections4.iterators.SkippingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import org.apache.commons.collections4.iterators.SkippingIterator as _SkippingIterator
_SkippingIterator = _SkippingIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkippingIterator():
    """org.apache.commons.collections4.iterators.SkippingIterator"""
 
    @staticmethod
    def _wrap(java_value: _SkippingIterator) -> 'SkippingIterator':
        return SkippingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkippingIterator):
        """
        Dynamic initializer for SkippingIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkippingIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkippingIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.SkippingIterator.remove()"""
        super(SkippingIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.SkippingIterator.next()"""
        return object._wrap(super(SkippingIterator, self).next())

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

    @overload
    def __init__(self, arg0: 'Iterator', arg1: int):
        """public org.apache.commons.collections4.iterators.SkippingIterator(java.util.Iterator<E>,long)"""
        val = _SkippingIterator(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(AbstractUntypedIteratorDecorator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.TransformIterator
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.iterators.TransformIterator as _TransformIterator
_TransformIterator = _TransformIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformIterator():
    """org.apache.commons.collections4.iterators.TransformIterator"""
 
    @staticmethod
    def _wrap(java_value: _TransformIterator) -> 'TransformIterator':
        return TransformIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformIterator):
        """
        Dynamic initializer for TransformIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.TransformIterator.hasNext()"""
        return bool._wrap(super(TransformIterator, self).hasNext())

    @overload
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.iterators.TransformIterator.getTransformer()"""
        return 'collections4.Transformer'._wrap(super(TransformIterator, self).getTransformer())

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
    def next(self) -> object:
        """public O org.apache.commons.collections4.iterators.TransformIterator.next()"""
        return object._wrap(super(TransformIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.TransformIterator(java.util.Iterator<? extends I>)"""
        val = _TransformIterator(arg0)
        self.__wrapper = val

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
        """public org.apache.commons.collections4.iterators.TransformIterator()"""
        val = _TransformIterator()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends I> org.apache.commons.collections4.iterators.TransformIterator.getIterator()"""
        return 'Iterator'._wrap(super(TransformIterator, self).getIterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.TransformIterator.remove()"""
        super(TransformIterator, self).remove()

    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.TransformIterator.setIterator(java.util.Iterator<? extends I>)"""
        super(_TransformIterator, self).setIterator(arg0)

    @overload
    def setTransformer(self, arg0: 'Transformer'):
        """public void org.apache.commons.collections4.iterators.TransformIterator.setTransformer(org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        super(_TransformIterator, self).setTransformer(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.TransformIterator()"""
        val = _TransformIterator()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Transformer'):
        """public org.apache.commons.collections4.iterators.TransformIterator(java.util.Iterator<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = _TransformIterator(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.IteratorChain
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.IteratorChain as _IteratorChain
_IteratorChain = _IteratorChain
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IteratorChain():
    """org.apache.commons.collections4.iterators.IteratorChain"""
 
    @staticmethod
    def _wrap(java_value: _IteratorChain) -> 'IteratorChain':
        return IteratorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IteratorChain):
        """
        Dynamic initializer for IteratorChain.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IteratorChain__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IteratorChain__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.IteratorChain.remove()"""
        super(IteratorChain, self).remove()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.IteratorChain.next()"""
        return object._wrap(super(IteratorChain, self).next())

    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.IteratorChain.isLocked()"""
        return bool._wrap(super(IteratorChain, self).isLocked())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.iterators.IteratorChain.size()"""
        return int._wrap(super(IteratorChain, self).size())

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

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Collection<java.util.Iterator<? extends E>>)"""
        val = _IteratorChain(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Iterator<? extends E>)"""
        val = _IteratorChain(arg0)
        self.__wrapper = val

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
    def __init__(self, *arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Iterator<? extends E>...)"""
        val = _IteratorChain(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.IteratorChain.addIterator(java.util.Iterator<? extends E>)"""
        super(_IteratorChain, self).addIterator(arg0)

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.IteratorChain.hasNext()"""
        return bool._wrap(super(IteratorChain, self).hasNext())

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

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = _IteratorChain(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.IteratorChain()"""
        val = _IteratorChain()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.IteratorChain()"""
        val = _IteratorChain()
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.NodeListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.w3c.dom.Node as _Node
_Node = _Node
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.NodeListIterator as _NodeListIterator
_NodeListIterator = _NodeListIterator
import java.lang.Integer as _int
import org.w3c.dom.NodeList as NodeList
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
import org.w3c.dom.Node as Node
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NodeListIterator():
    """org.apache.commons.collections4.iterators.NodeListIterator"""
 
    @staticmethod
    def _wrap(java_value: _NodeListIterator) -> 'NodeListIterator':
        return NodeListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NodeListIterator):
        """
        Dynamic initializer for NodeListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NodeListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NodeListIterator__wrapper":
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.NodeListIterator.remove()"""
        super(NodeListIterator, self).remove()

    @override
    @overload
    def next(self) -> 'Node':
        """public org.w3c.dom.Node org.apache.commons.collections4.iterators.NodeListIterator.next()"""
        return 'Node'._wrap(super(NodeListIterator, self).next())

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
    def __init__(self, arg0: 'NodeList'):
        """public org.apache.commons.collections4.iterators.NodeListIterator(org.w3c.dom.NodeList)"""
        val = _NodeListIterator(arg0)
        self.__wrapper = val

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.NodeListIterator.hasNext()"""
        return bool._wrap(super(NodeListIterator, self).hasNext())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Node'):
        """public org.apache.commons.collections4.iterators.NodeListIterator(org.w3c.dom.Node)"""
        val = _NodeListIterator(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ObjectGraphIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.iterators.ObjectGraphIterator as _ObjectGraphIterator
_ObjectGraphIterator = _ObjectGraphIterator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectGraphIterator():
    """org.apache.commons.collections4.iterators.ObjectGraphIterator"""
 
    @staticmethod
    def _wrap(java_value: _ObjectGraphIterator) -> 'ObjectGraphIterator':
        return ObjectGraphIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectGraphIterator):
        """
        Dynamic initializer for ObjectGraphIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectGraphIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectGraphIterator__wrapper":
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectGraphIterator.hasNext()"""
        return bool._wrap(super(ObjectGraphIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectGraphIterator.next()"""
        return object._wrap(super(ObjectGraphIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'Transformer'):
        """public org.apache.commons.collections4.iterators.ObjectGraphIterator(E,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        val = _ObjectGraphIterator(arg0, arg1)
        self.__wrapper = val

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ObjectGraphIterator.remove()"""
        super(ObjectGraphIterator, self).remove()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ObjectGraphIterator(java.util.Iterator<? extends E>)"""
        val = _ObjectGraphIterator(arg0)
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.iterators.BoundedIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import org.apache.commons.collections4.iterators.BoundedIterator as _BoundedIterator
_BoundedIterator = _BoundedIterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BoundedIterator():
    """org.apache.commons.collections4.iterators.BoundedIterator"""
 
    @staticmethod
    def _wrap(java_value: _BoundedIterator) -> 'BoundedIterator':
        return BoundedIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundedIterator):
        """
        Dynamic initializer for BoundedIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundedIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundedIterator__wrapper":
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.BoundedIterator.remove()"""
        super(BoundedIterator, self).remove()

    @overload
    def __init__(self, arg0: 'Iterator', arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.BoundedIterator(java.util.Iterator<? extends E>,long,long)"""
        val = _BoundedIterator(arg0, _long.valueOf(arg1), _long.valueOf(arg2))
        self.__wrapper = val

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.BoundedIterator.next()"""
        return object._wrap(super(BoundedIterator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.BoundedIterator.hasNext()"""
        return bool._wrap(super(BoundedIterator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.PeekingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.PeekingIterator as _PeekingIterator
_PeekingIterator = _PeekingIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PeekingIterator():
    """org.apache.commons.collections4.iterators.PeekingIterator"""
 
    @staticmethod
    def _wrap(java_value: _PeekingIterator) -> 'PeekingIterator':
        return PeekingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PeekingIterator):
        """
        Dynamic initializer for PeekingIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PeekingIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PeekingIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def element(self) -> object:
        """public E org.apache.commons.collections4.iterators.PeekingIterator.element()"""
        return object._wrap(super(PeekingIterator, self).element())

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.PeekingIterator(java.util.Iterator<? extends E>)"""
        val = _PeekingIterator(arg0)
        self.__wrapper = val

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.iterators.PeekingIterator.peek()"""
        return object._wrap(super(PeekingIterator, self).peek())

    @staticmethod
    @overload
    def peekingIterator(arg0: 'Iterator') -> 'PeekingIterator':
        """public static <E> org.apache.commons.collections4.iterators.PeekingIterator<E> org.apache.commons.collections4.iterators.PeekingIterator.peekingIterator(java.util.Iterator<? extends E>)"""
        return PeekingIterator._wrap(_PeekingIterator.peekingIterator(arg0))

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.PeekingIterator.hasNext()"""
        return bool._wrap(super(PeekingIterator, self).hasNext())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.PeekingIterator.remove()"""
        super(PeekingIterator, self).remove()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.PeekingIterator.next()"""
        return object._wrap(super(PeekingIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ObjectArrayListIterator
import org.apache.commons.collections4.iterators.ObjectArrayIterator as _ObjectArrayIterator
_ObjectArrayIterator = _ObjectArrayIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.ObjectArrayListIterator as _ObjectArrayListIterator
_ObjectArrayListIterator = _ObjectArrayListIterator
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectArrayListIterator():
    """org.apache.commons.collections4.iterators.ObjectArrayListIterator"""
 
    @staticmethod
    def _wrap(java_value: _ObjectArrayListIterator) -> 'ObjectArrayListIterator':
        return ObjectArrayListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectArrayListIterator):
        """
        Dynamic initializer for ObjectArrayListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectArrayListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectArrayListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectArrayListIterator.next()"""
        return object._wrap(super(ObjectArrayListIterator, self).next())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayListIterator.reset()"""
        super(ObjectArrayListIterator, self).reset()

    @override
    @overload
    def getArray(self) -> List[object]:
        """public E[] org.apache.commons.collections4.iterators.ObjectArrayIterator.getArray()"""
        return List[object]._wrap(super(ObjectArrayIterator, self).getArray())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ObjectArrayListIterator.add(E)"""
        super(_ObjectArrayListIterator, self).add(arg0)

    @overload
    def __init__(self, *arg0: object):
        """public org.apache.commons.collections4.iterators.ObjectArrayListIterator(E...)"""
        val = _ObjectArrayListIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectArrayIterator.hasNext()"""
        return bool._wrap(super(ObjectArrayIterator, self).hasNext())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayListIterator.nextIndex()"""
        return int._wrap(super(ObjectArrayListIterator, self).nextIndex())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayListIterator.previousIndex()"""
        return int._wrap(super(ObjectArrayListIterator, self).previousIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ObjectArrayListIterator.set(E)"""
        super(_ObjectArrayListIterator, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Object', arg1: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayListIterator(E[],int)"""
        val = _ObjectArrayListIterator(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Object', arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayListIterator(E[],int,int)"""
        val = _ObjectArrayListIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

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

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectArrayListIterator.previous()"""
        return object._wrap(super(ObjectArrayListIterator, self).previous())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayIterator.remove()"""
        super(ObjectArrayIterator, self).remove()

    @override
    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getStartIndex()"""
        return int._wrap(super(ObjectArrayIterator, self).getStartIndex())

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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectArrayListIterator.hasPrevious()"""
        return bool._wrap(super(ObjectArrayListIterator, self).hasPrevious())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getEndIndex()"""
        return int._wrap(super(ObjectArrayIterator, self).getEndIndex())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ListIteratorWrapper
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.ListIteratorWrapper as _ListIteratorWrapper
_ListIteratorWrapper = _ListIteratorWrapper
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ListIteratorWrapper():
    """org.apache.commons.collections4.iterators.ListIteratorWrapper"""
 
    @staticmethod
    def _wrap(java_value: _ListIteratorWrapper) -> 'ListIteratorWrapper':
        return ListIteratorWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListIteratorWrapper):
        """
        Dynamic initializer for ListIteratorWrapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListIteratorWrapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListIteratorWrapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ListIteratorWrapper.hasPrevious()"""
        return bool._wrap(super(ListIteratorWrapper, self).hasPrevious())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ListIteratorWrapper.next() throws java.util.NoSuchElementException"""
        return object._wrap(super(ListIteratorWrapper, self).next())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.add(E) throws java.lang.UnsupportedOperationException"""
        super(_ListIteratorWrapper, self).add(arg0)

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ListIteratorWrapper.nextIndex()"""
        return int._wrap(super(ListIteratorWrapper, self).nextIndex())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.remove() throws java.lang.UnsupportedOperationException"""
        super(ListIteratorWrapper, self).remove()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.reset()"""
        super(ListIteratorWrapper, self).reset()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ListIteratorWrapper.previous() throws java.util.NoSuchElementException"""
        return object._wrap(super(ListIteratorWrapper, self).previous())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ListIteratorWrapper(java.util.Iterator<? extends E>)"""
        val = _ListIteratorWrapper(arg0)
        self.__wrapper = val

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ListIteratorWrapper.previousIndex()"""
        return int._wrap(super(ListIteratorWrapper, self).previousIndex())

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
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.set(E) throws java.lang.UnsupportedOperationException"""
        super(_ListIteratorWrapper, self).set(arg0)

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ListIteratorWrapper.hasNext()"""
        return bool._wrap(super(ListIteratorWrapper, self).hasNext())

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
 
 
# CLASS: org.apache.commons.collections4.iterators.FilterIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.FilterIterator as _FilterIterator
_FilterIterator = _FilterIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FilterIterator():
    """org.apache.commons.collections4.iterators.FilterIterator"""
 
    @staticmethod
    def _wrap(java_value: _FilterIterator) -> 'FilterIterator':
        return FilterIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FilterIterator):
        """
        Dynamic initializer for FilterIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FilterIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FilterIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends E> org.apache.commons.collections4.iterators.FilterIterator.getIterator()"""
        return 'Iterator'._wrap(super(FilterIterator, self).getIterator())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterIterator.next()"""
        return object._wrap(super(FilterIterator, self).next())

    @overload
    def setPredicate(self, arg0: 'Predicate'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setPredicate(org.apache.commons.collections4.Predicate<? super E>)"""
        super(_FilterIterator, self).setPredicate(arg0)

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.iterators.FilterIterator.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(FilterIterator, self).getPredicate())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterIterator.hasNext()"""
        return bool._wrap(super(FilterIterator, self).hasNext())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.FilterIterator()"""
        val = _FilterIterator()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.FilterIterator()"""
        val = _FilterIterator()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Predicate'):
        """public org.apache.commons.collections4.iterators.FilterIterator(java.util.Iterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        val = _FilterIterator(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.FilterIterator.remove()"""
        super(FilterIterator, self).remove()

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

    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setIterator(java.util.Iterator<? extends E>)"""
        super(_FilterIterator, self).setIterator(arg0)

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.FilterIterator(java.util.Iterator<? extends E>)"""
        val = _FilterIterator(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.IteratorIterable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.IteratorIterable as _IteratorIterable
_IteratorIterable = _IteratorIterable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IteratorIterable():
    """org.apache.commons.collections4.iterators.IteratorIterable"""
 
    @staticmethod
    def _wrap(java_value: _IteratorIterable) -> 'IteratorIterable':
        return IteratorIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IteratorIterable):
        """
        Dynamic initializer for IteratorIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IteratorIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IteratorIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.iterators.IteratorIterable.iterator()"""
        return 'Iterator'._wrap(super(IteratorIterable, self).iterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorIterable(java.util.Iterator<? extends E>)"""
        val = _IteratorIterable(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Iterator', arg1: bool):
        """public org.apache.commons.collections4.iterators.IteratorIterable(java.util.Iterator<? extends E>,boolean)"""
        val = _IteratorIterable(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator as _AbstractMapIteratorDecorator
_AbstractMapIteratorDecorator = _AbstractMapIteratorDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMapIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMapIteratorDecorator) -> 'AbstractMapIteratorDecorator':
        return AbstractMapIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMapIteratorDecorator):
        """
        Dynamic initializer for AbstractMapIteratorDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMapIteratorDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMapIteratorDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.getKey()"""
        return object._wrap(super(AbstractMapIteratorDecorator, self).getKey())

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.next()"""
        return object._wrap(super(AbstractMapIteratorDecorator, self).next())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'MapIterator'):
        """public org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator(org.apache.commons.collections4.MapIterator<K, V>)"""
        val = _AbstractMapIteratorDecorator(arg0)
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.remove()"""
        super(AbstractMapIteratorDecorator, self).remove()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.getValue()"""
        return object._wrap(super(AbstractMapIteratorDecorator, self).getValue())

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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.setValue(V)"""
        return object._wrap(super(_AbstractMapIteratorDecorator, self).setValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.hasNext()"""
        return bool._wrap(super(AbstractMapIteratorDecorator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.PushbackIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.PushbackIterator as _PushbackIterator
_PushbackIterator = _PushbackIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PushbackIterator():
    """org.apache.commons.collections4.iterators.PushbackIterator"""
 
    @staticmethod
    def _wrap(java_value: _PushbackIterator) -> 'PushbackIterator':
        return PushbackIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PushbackIterator):
        """
        Dynamic initializer for PushbackIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PushbackIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PushbackIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.PushbackIterator.next()"""
        return object._wrap(super(PushbackIterator, self).next())

    @staticmethod
    @overload
    def pushbackIterator(arg0: 'Iterator') -> 'PushbackIterator':
        """public static <E> org.apache.commons.collections4.iterators.PushbackIterator<E> org.apache.commons.collections4.iterators.PushbackIterator.pushbackIterator(java.util.Iterator<? extends E>)"""
        return PushbackIterator._wrap(_PushbackIterator.pushbackIterator(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.PushbackIterator.remove()"""
        super(PushbackIterator, self).remove()

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
    def pushback(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.PushbackIterator.pushback(E)"""
        super(_PushbackIterator, self).pushback(arg0)

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

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.PushbackIterator(java.util.Iterator<? extends E>)"""
        val = _PushbackIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.PushbackIterator.hasNext()"""
        return bool._wrap(super(PushbackIterator, self).hasNext())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.SingletonListIterator
from builtins import str
from pyquantum_helper import override
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
import org.apache.commons.collections4.iterators.SingletonListIterator as _SingletonListIterator
_SingletonListIterator = _SingletonListIterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SingletonListIterator():
    """org.apache.commons.collections4.iterators.SingletonListIterator"""
 
    @staticmethod
    def _wrap(java_value: _SingletonListIterator) -> 'SingletonListIterator':
        return SingletonListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SingletonListIterator):
        """
        Dynamic initializer for SingletonListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SingletonListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SingletonListIterator__wrapper":
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
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.SingletonListIterator.set(E)"""
        super(_SingletonListIterator, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.SingletonListIterator.next()"""
        return object._wrap(super(SingletonListIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.SingletonListIterator.add(E)"""
        super(_SingletonListIterator, self).add(arg0)

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.SingletonListIterator(E)"""
        val = _SingletonListIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.SingletonListIterator.hasNext()"""
        return bool._wrap(super(SingletonListIterator, self).hasNext())

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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.SingletonListIterator.hasPrevious()"""
        return bool._wrap(super(SingletonListIterator, self).hasPrevious())

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
    def reset(self):
        """public void org.apache.commons.collections4.iterators.SingletonListIterator.reset()"""
        super(SingletonListIterator, self).reset()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.SingletonListIterator.remove()"""
        super(SingletonListIterator, self).remove()

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.SingletonListIterator.previousIndex()"""
        return int._wrap(super(SingletonListIterator, self).previousIndex())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.SingletonListIterator.previous()"""
        return object._wrap(super(SingletonListIterator, self).previous())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.SingletonListIterator.nextIndex()"""
        return int._wrap(super(SingletonListIterator, self).nextIndex())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EntrySetMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import org.apache.commons.collections4.iterators.EntrySetMapIterator as _EntrySetMapIterator
_EntrySetMapIterator = _EntrySetMapIterator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySetMapIterator():
    """org.apache.commons.collections4.iterators.EntrySetMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _EntrySetMapIterator) -> 'EntrySetMapIterator':
        return EntrySetMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySetMapIterator):
        """
        Dynamic initializer for EntrySetMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySetMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySetMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.iterators.EntrySetMapIterator(java.util.Map<K, V>)"""
        val = _EntrySetMapIterator(arg0)
        self.__wrapper = val

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.EntrySetMapIterator.getKey()"""
        return object._wrap(super(EntrySetMapIterator, self).getKey())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.iterators.EntrySetMapIterator.toString()"""
        return str._wrap(super(EntrySetMapIterator, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.EntrySetMapIterator.hasNext()"""
        return bool._wrap(super(EntrySetMapIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.EntrySetMapIterator.remove()"""
        super(EntrySetMapIterator, self).remove()

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.EntrySetMapIterator.next()"""
        return object._wrap(super(EntrySetMapIterator, self).next())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.EntrySetMapIterator.setValue(V)"""
        return object._wrap(super(_EntrySetMapIterator, self).setValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.EntrySetMapIterator.getValue()"""
        return object._wrap(super(EntrySetMapIterator, self).getValue())

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
    def reset(self):
        """public void org.apache.commons.collections4.iterators.EntrySetMapIterator.reset()"""
        super(EntrySetMapIterator, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyOrderedIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.OrderedIterator as _OrderedIterator
_OrderedIterator = _OrderedIterator
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import org.apache.commons.collections4.iterators.EmptyOrderedIterator as _EmptyOrderedIterator
_EmptyOrderedIterator = _EmptyOrderedIterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmptyOrderedIterator():
    """org.apache.commons.collections4.iterators.EmptyOrderedIterator"""
 
    @staticmethod
    def _wrap(java_value: _EmptyOrderedIterator) -> 'EmptyOrderedIterator':
        return EmptyOrderedIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmptyOrderedIterator):
        """
        Dynamic initializer for EmptyOrderedIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmptyOrderedIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmptyOrderedIterator__wrapper":
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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

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

    @staticmethod
    @overload
    def emptyOrderedIterator() -> 'collections4.OrderedIterator':
        """public static <E> org.apache.commons.collections4.OrderedIterator<E> org.apache.commons.collections4.iterators.EmptyOrderedIterator.emptyOrderedIterator()"""
        return collections4.OrderedIterator._wrap(_EmptyOrderedIterator.emptyOrderedIterator())

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
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyMapIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.iterators.EmptyMapIterator as _EmptyMapIterator
_EmptyMapIterator = _EmptyMapIterator
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.collections4.iterators.AbstractEmptyMapIterator as _AbstractEmptyMapIterator
_AbstractEmptyMapIterator = _AbstractEmptyMapIterator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmptyMapIterator():
    """org.apache.commons.collections4.iterators.EmptyMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _EmptyMapIterator) -> 'EmptyMapIterator':
        return EmptyMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmptyMapIterator):
        """
        Dynamic initializer for EmptyMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmptyMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmptyMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getKey()"""
        return object._wrap(super(AbstractEmptyMapIterator, self).getKey())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getValue()"""
        return object._wrap(super(AbstractEmptyMapIterator, self).getValue())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.setValue(V)"""
        return object._wrap(super(_AbstractEmptyMapIterator, self).setValue(arg0))

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

    @staticmethod
    @overload
    def emptyMapIterator() -> 'collections4.MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.iterators.EmptyMapIterator.emptyMapIterator()"""
        return collections4.MapIterator._wrap(_EmptyMapIterator.emptyMapIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableIterator
import org.apache.commons.collections4.iterators.UnmodifiableIterator as _UnmodifiableIterator
_UnmodifiableIterator = _UnmodifiableIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableIterator"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableIterator) -> 'UnmodifiableIterator':
        return UnmodifiableIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableIterator):
        """
        Dynamic initializer for UnmodifiableIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableIterator.hasNext()"""
        return bool._wrap(super(UnmodifiableIterator, self).hasNext())

    @staticmethod
    @overload
    def unmodifiableIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.iterators.UnmodifiableIterator.unmodifiableIterator(java.util.Iterator<? extends E>)"""
        return Iterator._wrap(_UnmodifiableIterator.unmodifiableIterator(arg0))

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableIterator.remove()"""
        super(UnmodifiableIterator, self).remove()

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableIterator.next()"""
        return object._wrap(super(UnmodifiableIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractListIteratorDecorator
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
import java.util.ListIterator as ListIterator
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractListIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractListIteratorDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractListIteratorDecorator) -> 'AbstractListIteratorDecorator':
        return AbstractListIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractListIteratorDecorator):
        """
        Dynamic initializer for AbstractListIteratorDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractListIteratorDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractListIteratorDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.next()"""
        return object._wrap(super(AbstractListIteratorDecorator, self).next())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previous()"""
        return object._wrap(super(AbstractListIteratorDecorator, self).previous())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.set(E)"""
        super(_AbstractListIteratorDecorator, self).set(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.add(E)"""
        super(_AbstractListIteratorDecorator, self).add(arg0)

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previousIndex()"""
        return int._wrap(super(AbstractListIteratorDecorator, self).previousIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.nextIndex()"""
        return int._wrap(super(AbstractListIteratorDecorator, self).nextIndex())

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
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.remove()"""
        super(AbstractListIteratorDecorator, self).remove()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasNext()"""
        return bool._wrap(super(AbstractListIteratorDecorator, self).hasNext())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasPrevious()"""
        return bool._wrap(super(AbstractListIteratorDecorator, self).hasPrevious())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'ListIterator'):
        """public org.apache.commons.collections4.iterators.AbstractListIteratorDecorator(java.util.ListIterator<E>)"""
        val = _AbstractListIteratorDecorator(arg0)
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.UniqueFilterIterator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.iterators.FilterIterator as _FilterIterator
_FilterIterator = _FilterIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.iterators.UniqueFilterIterator as _UniqueFilterIterator
_UniqueFilterIterator = _UniqueFilterIterator
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniqueFilterIterator():
    """org.apache.commons.collections4.iterators.UniqueFilterIterator"""
 
    @staticmethod
    def _wrap(java_value: _UniqueFilterIterator) -> 'UniqueFilterIterator':
        return UniqueFilterIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniqueFilterIterator):
        """
        Dynamic initializer for UniqueFilterIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniqueFilterIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniqueFilterIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterIterator.next()"""
        return object._wrap(super(FilterIterator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterIterator.hasNext()"""
        return bool._wrap(super(FilterIterator, self).hasNext())

    @override
    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends E> org.apache.commons.collections4.iterators.FilterIterator.getIterator()"""
        return 'Iterator'._wrap(super(FilterIterator, self).getIterator())

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.FilterIterator.remove()"""
        super(FilterIterator, self).remove()

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
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.iterators.FilterIterator.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(FilterIterator, self).getPredicate())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setIterator(java.util.Iterator<? extends E>)"""
        super(_FilterIterator, self).setIterator(arg0)

    @override
    @overload
    def setPredicate(self, arg0: 'Predicate'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setPredicate(org.apache.commons.collections4.Predicate<? super E>)"""
        super(_FilterIterator, self).setPredicate(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.UniqueFilterIterator(java.util.Iterator<? extends E>)"""
        val = _UniqueFilterIterator(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.CollatingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import org.apache.commons.collections4.iterators.CollatingIterator as _CollatingIterator
_CollatingIterator = _CollatingIterator
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CollatingIterator():
    """org.apache.commons.collections4.iterators.CollatingIterator"""
 
    @staticmethod
    def _wrap(java_value: _CollatingIterator) -> 'CollatingIterator':
        return CollatingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollatingIterator):
        """
        Dynamic initializer for CollatingIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollatingIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollatingIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Comparator', arg1: int):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,int)"""
        val = _CollatingIterator(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.CollatingIterator()"""
        val = _CollatingIterator()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>)"""
        val = _CollatingIterator(arg0)
        self.__wrapper = val

    @overload
    def getIterators(self) -> 'List':
        """public java.util.List<java.util.Iterator<? extends E>> org.apache.commons.collections4.iterators.CollatingIterator.getIterators()"""
        return 'List'._wrap(super(CollatingIterator, self).getIterators())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.CollatingIterator.hasNext()"""
        return bool._wrap(super(CollatingIterator, self).hasNext())

    @overload
    def addIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.addIterator(java.util.Iterator<? extends E>)"""
        super(_CollatingIterator, self).addIterator(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.CollatingIterator.next() throws java.util.NoSuchElementException"""
        return object._wrap(super(CollatingIterator, self).next())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setIterator(self, arg0: int, arg1: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.setIterator(int,java.util.Iterator<? extends E>)"""
        super(_CollatingIterator, self).setIterator(_int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Iterator'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>[])"""
        val = _CollatingIterator(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Iterator', arg2: 'Iterator'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = _CollatingIterator(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getIteratorIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.CollatingIterator.getIteratorIndex()"""
        return int._wrap(super(CollatingIterator, self).getIteratorIndex())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Collection'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,java.util.Collection<java.util.Iterator<? extends E>>)"""
        val = _CollatingIterator(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.iterators.CollatingIterator.getComparator()"""
        return 'Comparator'._wrap(super(CollatingIterator, self).getComparator())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.CollatingIterator()"""
        val = _CollatingIterator()
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.remove()"""
        super(CollatingIterator, self).remove()

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

    @overload
    def setComparator(self, arg0: 'Comparator'):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.setComparator(java.util.Comparator<? super E>)"""
        super(_CollatingIterator, self).setComparator(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator as _AbstractOrderedMapIteratorDecorator
_AbstractOrderedMapIteratorDecorator = _AbstractOrderedMapIteratorDecorator
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractOrderedMapIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractOrderedMapIteratorDecorator) -> 'AbstractOrderedMapIteratorDecorator':
        return AbstractOrderedMapIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractOrderedMapIteratorDecorator):
        """
        Dynamic initializer for AbstractOrderedMapIteratorDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractOrderedMapIteratorDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractOrderedMapIteratorDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.getValue()"""
        return object._wrap(super(AbstractOrderedMapIteratorDecorator, self).getValue())

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.getKey()"""
        return object._wrap(super(AbstractOrderedMapIteratorDecorator, self).getKey())

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.previous()"""
        return object._wrap(super(AbstractOrderedMapIteratorDecorator, self).previous())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.setValue(V)"""
        return object._wrap(super(_AbstractOrderedMapIteratorDecorator, self).setValue(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.hasNext()"""
        return bool._wrap(super(AbstractOrderedMapIteratorDecorator, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.next()"""
        return object._wrap(super(AbstractOrderedMapIteratorDecorator, self).next())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.hasPrevious()"""
        return bool._wrap(super(AbstractOrderedMapIteratorDecorator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'OrderedMapIterator'):
        """public org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator(org.apache.commons.collections4.OrderedMapIterator<K, V>)"""
        val = _AbstractOrderedMapIteratorDecorator(arg0)
        self.__wrapper = val

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
        """public void org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.remove()"""
        super(AbstractOrderedMapIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.IteratorEnumeration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.Enumeration as _Enumeration
_Enumeration = _Enumeration
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.apache.commons.collections4.iterators.IteratorEnumeration as _IteratorEnumeration
_IteratorEnumeration = _IteratorEnumeration
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IteratorEnumeration():
    """org.apache.commons.collections4.iterators.IteratorEnumeration"""
 
    @staticmethod
    def _wrap(java_value: _IteratorEnumeration) -> 'IteratorEnumeration':
        return IteratorEnumeration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IteratorEnumeration):
        """
        Dynamic initializer for IteratorEnumeration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IteratorEnumeration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IteratorEnumeration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorEnumeration(java.util.Iterator<? extends E>)"""
        val = _IteratorEnumeration(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.IteratorEnumeration()"""
        val = _IteratorEnumeration()
        self.__wrapper = val

    @override
    @overload
    def hasMoreElements(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.IteratorEnumeration.hasMoreElements()"""
        return bool._wrap(super(IteratorEnumeration, self).hasMoreElements())

    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends E> org.apache.commons.collections4.iterators.IteratorEnumeration.getIterator()"""
        return 'Iterator'._wrap(super(IteratorEnumeration, self).getIterator())

    @override
    @overload
    def asIterator(self) -> 'Iterator':
        """public default java.util.Iterator<E> java.util.Enumeration.asIterator()"""
        return 'Iterator'._wrap(super(Enumeration, self).asIterator())

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
    def nextElement(self) -> object:
        """public E org.apache.commons.collections4.iterators.IteratorEnumeration.nextElement()"""
        return object._wrap(super(IteratorEnumeration, self).nextElement())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.IteratorEnumeration()"""
        val = _IteratorEnumeration()
        self.__wrapper = val

    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.IteratorEnumeration.setIterator(java.util.Iterator<? extends E>)"""
        super(_IteratorEnumeration, self).setIterator(arg0)

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
 
 
# CLASS: org.apache.commons.collections4.iterators.LazyIteratorChain
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.LazyIteratorChain as _LazyIteratorChain
_LazyIteratorChain = _LazyIteratorChain
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazyIteratorChain():
    """org.apache.commons.collections4.iterators.LazyIteratorChain"""
 
    @staticmethod
    def _wrap(java_value: _LazyIteratorChain) -> 'LazyIteratorChain':
        return LazyIteratorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazyIteratorChain):
        """
        Dynamic initializer for LazyIteratorChain.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazyIteratorChain__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazyIteratorChain__wrapper":
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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.LazyIteratorChain.next()"""
        return object._wrap(super(LazyIteratorChain, self).next())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.LazyIteratorChain()"""
        val = _LazyIteratorChain()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.LazyIteratorChain.remove()"""
        super(LazyIteratorChain, self).remove()

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LazyIteratorChain.hasNext()"""
        return bool._wrap(super(LazyIteratorChain, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.LazyIteratorChain()"""
        val = _LazyIteratorChain()
        self.__wrapper = val