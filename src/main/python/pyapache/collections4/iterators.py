from __future__ import annotations
from overload import overload


 
import org.apache.commons.collections4.iterators.UnmodifiableIterator as __UnmodifiableIterator
__UnmodifiableIterator = __UnmodifiableIterator
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
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
 
class UnmodifiableIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableIterator"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableIterator) -> 'UnmodifiableIterator':
        return UnmodifiableIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableIterator):
        """
        Dynamic initializer for UnmodifiableIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableIterator.hasNext()"""
        return bool.__wrap(super(UnmodifiableIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableIterator.next()"""
        return object.__wrap(super(UnmodifiableIterator, self).next())

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

    @staticmethod
    @overload
    def unmodifiableIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.iterators.UnmodifiableIterator.unmodifiableIterator(java.util.Iterator<? extends E>)"""
        return Iterator.__wrap(__UnmodifiableIterator.unmodifiableIterator(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableIterator.remove()"""
        super(UnmodifiableIterator, self).remove()

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

 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableIterator
import org.apache.commons.collections4.iterators.UnmodifiableIterator as __UnmodifiableIterator
__UnmodifiableIterator = __UnmodifiableIterator
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
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
 
class UnmodifiableIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableIterator"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableIterator) -> 'UnmodifiableIterator':
        return UnmodifiableIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableIterator):
        """
        Dynamic initializer for UnmodifiableIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableIterator.hasNext()"""
        return bool.__wrap(super(UnmodifiableIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableIterator.next()"""
        return object.__wrap(super(UnmodifiableIterator, self).next())

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

    @staticmethod
    @overload
    def unmodifiableIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.iterators.UnmodifiableIterator.unmodifiableIterator(java.util.Iterator<? extends E>)"""
        return Iterator.__wrap(__UnmodifiableIterator.unmodifiableIterator(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableIterator.remove()"""
        super(UnmodifiableIterator, self).remove()

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

 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableIterator 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.iterators.EmptyIterator as __EmptyIterator
__EmptyIterator = __EmptyIterator
import org.apache.commons.collections4.ResettableIterator as __ResettableIterator
__ResettableIterator = __ResettableIterator
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class EmptyIterator():
    """org.apache.commons.collections4.iterators.EmptyIterator"""
 
    @staticmethod
    def __wrap(java_value: __EmptyIterator) -> 'EmptyIterator':
        return EmptyIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmptyIterator):
        """
        Dynamic initializer for EmptyIterator.
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

    @staticmethod
    @overload
    def resettableEmptyIterator() -> 'collections4.ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.iterators.EmptyIterator.resettableEmptyIterator()"""
        return collections4.ResettableIterator.__wrap(__EmptyIterator.resettableEmptyIterator())

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

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @staticmethod
    @overload
    def emptyIterator() -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.iterators.EmptyIterator.emptyIterator()"""
        return Iterator.__wrap(__EmptyIterator.emptyIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator as __AbstractMapIteratorDecorator
__AbstractMapIteratorDecorator = __AbstractMapIteratorDecorator
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
 
class AbstractMapIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMapIteratorDecorator) -> 'AbstractMapIteratorDecorator':
        return AbstractMapIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMapIteratorDecorator):
        """
        Dynamic initializer for AbstractMapIteratorDecorator.
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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.getKey()"""
        return object.__wrap(super(AbstractMapIteratorDecorator, self).getKey())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.hasNext()"""
        return bool.__wrap(super(AbstractMapIteratorDecorator, self).hasNext())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.setValue(V)"""
        return object.__wrap(super(__AbstractMapIteratorDecorator, self).setValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.getValue()"""
        return object.__wrap(super(AbstractMapIteratorDecorator, self).getValue())

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
    def __init__(self, arg0: 'MapIterator'):
        """public org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator(org.apache.commons.collections4.MapIterator<K, V>)"""
        val = __AbstractMapIteratorDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractMapIteratorDecorator.next()"""
        return object.__wrap(super(AbstractMapIteratorDecorator, self).next())

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
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyListIterator
from pyquantum_helper import import_once as __import_once__
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
from builtins import str
import org.apache.commons.collections4.iterators.EmptyListIterator as __EmptyListIterator
__EmptyListIterator = __EmptyListIterator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.ResettableListIterator as __ResettableListIterator
__ResettableListIterator = __ResettableListIterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EmptyListIterator():
    """org.apache.commons.collections4.iterators.EmptyListIterator"""
 
    @staticmethod
    def __wrap(java_value: __EmptyListIterator) -> 'EmptyListIterator':
        return EmptyListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmptyListIterator):
        """
        Dynamic initializer for EmptyListIterator.
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

    @staticmethod
    @overload
    def resettableEmptyListIterator() -> 'collections4.ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.iterators.EmptyListIterator.resettableEmptyListIterator()"""
        return collections4.ResettableListIterator.__wrap(__EmptyListIterator.resettableEmptyListIterator())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @staticmethod
    @overload
    def emptyListIterator() -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.iterators.EmptyListIterator.emptyListIterator()"""
        return ListIterator.__wrap(__EmptyListIterator.emptyListIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ObjectGraphIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import org.apache.commons.collections4.iterators.ObjectGraphIterator as __ObjectGraphIterator
__ObjectGraphIterator = __ObjectGraphIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjectGraphIterator():
    """org.apache.commons.collections4.iterators.ObjectGraphIterator"""
 
    @staticmethod
    def __wrap(java_value: __ObjectGraphIterator) -> 'ObjectGraphIterator':
        return ObjectGraphIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectGraphIterator):
        """
        Dynamic initializer for ObjectGraphIterator.
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
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ObjectGraphIterator(java.util.Iterator<? extends E>)"""
        val = __ObjectGraphIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectGraphIterator.hasNext()"""
        return bool.__wrap(super(ObjectGraphIterator, self).hasNext())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectGraphIterator.next()"""
        return object.__wrap(super(ObjectGraphIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ObjectGraphIterator.remove()"""
        super(ObjectGraphIterator, self).remove()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: object, arg1: 'Transformer'):
        """public org.apache.commons.collections4.iterators.ObjectGraphIterator(E,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        val = __ObjectGraphIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.iterators.UniqueFilterIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.iterators.FilterIterator as __FilterIterator
__FilterIterator = __FilterIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.iterators.UniqueFilterIterator as __UniqueFilterIterator
__UniqueFilterIterator = __UniqueFilterIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UniqueFilterIterator():
    """org.apache.commons.collections4.iterators.UniqueFilterIterator"""
 
    @staticmethod
    def __wrap(java_value: __UniqueFilterIterator) -> 'UniqueFilterIterator':
        return UniqueFilterIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniqueFilterIterator):
        """
        Dynamic initializer for UniqueFilterIterator.
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
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.UniqueFilterIterator(java.util.Iterator<? extends E>)"""
        val = __UniqueFilterIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends E> org.apache.commons.collections4.iterators.FilterIterator.getIterator()"""
        return 'Iterator'.__wrap(super(FilterIterator, self).getIterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.iterators.FilterIterator.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(FilterIterator, self).getPredicate())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.FilterIterator.remove()"""
        super(FilterIterator, self).remove()

    @override
    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setIterator(java.util.Iterator<? extends E>)"""
        super(__FilterIterator, self).setIterator(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setPredicate(self, arg0: 'Predicate'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setPredicate(org.apache.commons.collections4.Predicate<? super E>)"""
        super(__FilterIterator, self).setPredicate(arg0)

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterIterator.hasNext()"""
        return bool.__wrap(super(FilterIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterIterator.next()"""
        return object.__wrap(super(FilterIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.LoopingListIterator
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
import java.lang.Integer as __int
import org.apache.commons.collections4.iterators.LoopingListIterator as __LoopingListIterator
__LoopingListIterator = __LoopingListIterator
from builtins import bool
from builtins import int
import java.util.List as List
 
class LoopingListIterator():
    """org.apache.commons.collections4.iterators.LoopingListIterator"""
 
    @staticmethod
    def __wrap(java_value: __LoopingListIterator) -> 'LoopingListIterator':
        return LoopingListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoopingListIterator):
        """
        Dynamic initializer for LoopingListIterator.
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
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.set(E)"""
        super(__LoopingListIterator, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.remove()"""
        super(LoopingListIterator, self).remove()

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingListIterator.size()"""
        return int.__wrap(super(LoopingListIterator, self).size())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingListIterator.nextIndex()"""
        return int.__wrap(super(LoopingListIterator, self).nextIndex())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LoopingListIterator.hasNext()"""
        return bool.__wrap(super(LoopingListIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.LoopingListIterator.next()"""
        return object.__wrap(super(LoopingListIterator, self).next())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LoopingListIterator.hasPrevious()"""
        return bool.__wrap(super(LoopingListIterator, self).hasPrevious())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingListIterator.previousIndex()"""
        return int.__wrap(super(LoopingListIterator, self).previousIndex())

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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.LoopingListIterator.add(E)"""
        super(__LoopingListIterator, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.LoopingListIterator.previous()"""
        return object.__wrap(super(LoopingListIterator, self).previous())

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

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.iterators.LoopingListIterator(java.util.List<E>)"""
        val = __LoopingListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.SingletonListIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.iterators.SingletonListIterator as __SingletonListIterator
__SingletonListIterator = __SingletonListIterator
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
from builtins import int
 
class SingletonListIterator():
    """org.apache.commons.collections4.iterators.SingletonListIterator"""
 
    @staticmethod
    def __wrap(java_value: __SingletonListIterator) -> 'SingletonListIterator':
        return SingletonListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SingletonListIterator):
        """
        Dynamic initializer for SingletonListIterator.
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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.SingletonListIterator.hasPrevious()"""
        return bool.__wrap(super(SingletonListIterator, self).hasPrevious())

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
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.SingletonListIterator.previous()"""
        return object.__wrap(super(SingletonListIterator, self).previous())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.SingletonListIterator.set(E)"""
        super(__SingletonListIterator, self).set(arg0)

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
        """public int org.apache.commons.collections4.iterators.SingletonListIterator.nextIndex()"""
        return int.__wrap(super(SingletonListIterator, self).nextIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.SingletonListIterator.add(E)"""
        super(__SingletonListIterator, self).add(arg0)

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.SingletonListIterator.previousIndex()"""
        return int.__wrap(super(SingletonListIterator, self).previousIndex())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.SingletonListIterator.hasNext()"""
        return bool.__wrap(super(SingletonListIterator, self).hasNext())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.SingletonListIterator(E)"""
        val = __SingletonListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.SingletonListIterator.next()"""
        return object.__wrap(super(SingletonListIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractIteratorDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.AbstractIteratorDecorator as __AbstractIteratorDecorator
__AbstractIteratorDecorator = __AbstractIteratorDecorator
from builtins import object
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as __AbstractUntypedIteratorDecorator
__AbstractUntypedIteratorDecorator = __AbstractUntypedIteratorDecorator
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
 
class AbstractIteratorDecorator(ABC):
    """org.apache.commons.collections4.iterators.AbstractIteratorDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractIteratorDecorator) -> 'AbstractIteratorDecorator':
        return AbstractIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractIteratorDecorator):
        """
        Dynamic initializer for AbstractIteratorDecorator.
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
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool.__wrap(super(AbstractUntypedIteratorDecorator, self).hasNext())

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractIteratorDecorator.next()"""
        return object.__wrap(super(AbstractIteratorDecorator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.remove()"""
        super(AbstractUntypedIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableListIterator
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import org.apache.commons.collections4.iterators.UnmodifiableListIterator as __UnmodifiableListIterator
__UnmodifiableListIterator = __UnmodifiableListIterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnmodifiableListIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableListIterator"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableListIterator) -> 'UnmodifiableListIterator':
        return UnmodifiableListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableListIterator):
        """
        Dynamic initializer for UnmodifiableListIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableListIterator.remove()"""
        super(UnmodifiableListIterator, self).remove()

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.UnmodifiableListIterator.nextIndex()"""
        return int.__wrap(super(UnmodifiableListIterator, self).nextIndex())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableListIterator.hasPrevious()"""
        return bool.__wrap(super(UnmodifiableListIterator, self).hasPrevious())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.UnmodifiableListIterator.set(E)"""
        super(__UnmodifiableListIterator, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableListIterator.next()"""
        return object.__wrap(super(UnmodifiableListIterator, self).next())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.UnmodifiableListIterator.previousIndex()"""
        return int.__wrap(super(UnmodifiableListIterator, self).previousIndex())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.UnmodifiableListIterator.add(E)"""
        super(__UnmodifiableListIterator, self).add(arg0)

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableListIterator.hasNext()"""
        return bool.__wrap(super(UnmodifiableListIterator, self).hasNext())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.UnmodifiableListIterator.previous()"""
        return object.__wrap(super(UnmodifiableListIterator, self).previous())

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

    @staticmethod
    @overload
    def umodifiableListIterator(arg0: 'ListIterator') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.iterators.UnmodifiableListIterator.umodifiableListIterator(java.util.ListIterator<? extends E>)"""
        return ListIterator.__wrap(__UnmodifiableListIterator.umodifiableListIterator(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.FilterListIterator
from pyquantum_helper import import_once as __import_once__
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.iterators.FilterListIterator as __FilterListIterator
__FilterListIterator = __FilterListIterator
from builtins import int
 
class FilterListIterator():
    """org.apache.commons.collections4.iterators.FilterListIterator"""
 
    @staticmethod
    def __wrap(java_value: __FilterListIterator) -> 'FilterListIterator':
        return FilterListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FilterListIterator):
        """
        Dynamic initializer for FilterListIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.remove()"""
        super(FilterListIterator, self).remove()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterListIterator.hasPrevious()"""
        return bool.__wrap(super(FilterListIterator, self).hasPrevious())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterListIterator.previous()"""
        return object.__wrap(super(FilterListIterator, self).previous())

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.iterators.FilterListIterator.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(FilterListIterator, self).getPredicate())

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.add(E)"""
        super(__FilterListIterator, self).add(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.set(E)"""
        super(__FilterListIterator, self).set(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.iterators.FilterListIterator(org.apache.commons.collections4.Predicate<? super E>)"""
        val = __FilterListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.FilterListIterator()"""
        val = __FilterListIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.FilterListIterator.previousIndex()"""
        return int.__wrap(super(FilterListIterator, self).previousIndex())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def setPredicate(self, arg0: 'Predicate'):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.setPredicate(org.apache.commons.collections4.Predicate<? super E>)"""
        super(__FilterListIterator, self).setPredicate(arg0)

    @overload
    def setListIterator(self, arg0: 'ListIterator'):
        """public void org.apache.commons.collections4.iterators.FilterListIterator.setListIterator(java.util.ListIterator<? extends E>)"""
        super(__FilterListIterator, self).setListIterator(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ListIterator'):
        """public org.apache.commons.collections4.iterators.FilterListIterator(java.util.ListIterator<? extends E>)"""
        val = __FilterListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterListIterator.hasNext()"""
        return bool.__wrap(super(FilterListIterator, self).hasNext())

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterListIterator.next()"""
        return object.__wrap(super(FilterListIterator, self).next())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.FilterListIterator()"""
        val = __FilterListIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getListIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<? extends E> org.apache.commons.collections4.iterators.FilterListIterator.getListIterator()"""
        return 'ListIterator'.__wrap(super(FilterListIterator, self).getListIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ListIterator', arg1: 'Predicate'):
        """public org.apache.commons.collections4.iterators.FilterListIterator(java.util.ListIterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        val = __FilterListIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.FilterListIterator.nextIndex()"""
        return int.__wrap(super(FilterListIterator, self).nextIndex()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.PushbackIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.PushbackIterator as __PushbackIterator
__PushbackIterator = __PushbackIterator
from builtins import object
import java.util.Iterator as Iterator
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
 
class PushbackIterator():
    """org.apache.commons.collections4.iterators.PushbackIterator"""
 
    @staticmethod
    def __wrap(java_value: __PushbackIterator) -> 'PushbackIterator':
        return PushbackIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PushbackIterator):
        """
        Dynamic initializer for PushbackIterator.
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
    def pushback(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.PushbackIterator.pushback(E)"""
        super(__PushbackIterator, self).pushback(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.PushbackIterator.remove()"""
        super(PushbackIterator, self).remove()

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.PushbackIterator(java.util.Iterator<? extends E>)"""
        val = __PushbackIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.PushbackIterator.next()"""
        return object.__wrap(super(PushbackIterator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.PushbackIterator.hasNext()"""
        return bool.__wrap(super(PushbackIterator, self).hasNext())

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

    @staticmethod
    @overload
    def pushbackIterator(arg0: 'Iterator') -> 'PushbackIterator':
        """public static <E> org.apache.commons.collections4.iterators.PushbackIterator<E> org.apache.commons.collections4.iterators.PushbackIterator.pushbackIterator(java.util.Iterator<? extends E>)"""
        return PushbackIterator.__wrap(__PushbackIterator.pushbackIterator(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.iterators.ArrayIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.ArrayIterator as __ArrayIterator
__ArrayIterator = __ArrayIterator
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
from builtins import int
 
class ArrayIterator():
    """org.apache.commons.collections4.iterators.ArrayIterator"""
 
    @staticmethod
    def __wrap(java_value: __ArrayIterator) -> 'ArrayIterator':
        return ArrayIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayIterator):
        """
        Dynamic initializer for ArrayIterator.
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
    def __init__(self, arg0: object, arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ArrayIterator(java.lang.Object,int,int)"""
        val = __ArrayIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: int):
        """public org.apache.commons.collections4.iterators.ArrayIterator(java.lang.Object,int)"""
        val = __ArrayIterator(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ArrayIterator.reset()"""
        super(ArrayIterator, self).reset()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getStartIndex()"""
        return int.__wrap(super(ArrayIterator, self).getStartIndex())

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ArrayIterator.remove()"""
        super(ArrayIterator, self).remove()

    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getEndIndex()"""
        return int.__wrap(super(ArrayIterator, self).getEndIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ArrayIterator.next()"""
        return object.__wrap(super(ArrayIterator, self).next())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ArrayIterator.hasNext()"""
        return bool.__wrap(super(ArrayIterator, self).hasNext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.ArrayIterator(java.lang.Object)"""
        val = __ArrayIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def getArray(self) -> object:
        """public java.lang.Object org.apache.commons.collections4.iterators.ArrayIterator.getArray()"""
        return object.__wrap(super(ArrayIterator, self).getArray()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyOrderedMapIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import org.apache.commons.collections4.iterators.AbstractEmptyMapIterator as __AbstractEmptyMapIterator
__AbstractEmptyMapIterator = __AbstractEmptyMapIterator
from builtins import object
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.iterators.EmptyOrderedMapIterator as __EmptyOrderedMapIterator
__EmptyOrderedMapIterator = __EmptyOrderedMapIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EmptyOrderedMapIterator():
    """org.apache.commons.collections4.iterators.EmptyOrderedMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __EmptyOrderedMapIterator) -> 'EmptyOrderedMapIterator':
        return EmptyOrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmptyOrderedMapIterator):
        """
        Dynamic initializer for EmptyOrderedMapIterator.
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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.setValue(V)"""
        return object.__wrap(super(__AbstractEmptyMapIterator, self).setValue(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getValue()"""
        return object.__wrap(super(AbstractEmptyMapIterator, self).getValue())

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

    @staticmethod
    @overload
    def emptyOrderedMapIterator() -> 'collections4.OrderedMapIterator':
        """public static <K,V> org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.iterators.EmptyOrderedMapIterator.emptyOrderedMapIterator()"""
        return collections4.OrderedMapIterator.__wrap(__EmptyOrderedMapIterator.emptyOrderedMapIterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getKey()"""
        return object.__wrap(super(AbstractEmptyMapIterator, self).getKey())

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
 
 
# CLASS: org.apache.commons.collections4.iterators.PeekingIterator
import org.apache.commons.collections4.iterators.PeekingIterator as __PeekingIterator
__PeekingIterator = __PeekingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
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
 
class PeekingIterator():
    """org.apache.commons.collections4.iterators.PeekingIterator"""
 
    @staticmethod
    def __wrap(java_value: __PeekingIterator) -> 'PeekingIterator':
        return PeekingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PeekingIterator):
        """
        Dynamic initializer for PeekingIterator.
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
    def element(self) -> object:
        """public E org.apache.commons.collections4.iterators.PeekingIterator.element()"""
        return object.__wrap(super(PeekingIterator, self).element())

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
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.PeekingIterator(java.util.Iterator<? extends E>)"""
        val = __PeekingIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.PeekingIterator.next()"""
        return object.__wrap(super(PeekingIterator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.PeekingIterator.hasNext()"""
        return bool.__wrap(super(PeekingIterator, self).hasNext())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.iterators.PeekingIterator.peek()"""
        return object.__wrap(super(PeekingIterator, self).peek())

    @staticmethod
    @overload
    def peekingIterator(arg0: 'Iterator') -> 'PeekingIterator':
        """public static <E> org.apache.commons.collections4.iterators.PeekingIterator<E> org.apache.commons.collections4.iterators.PeekingIterator.peekingIterator(java.util.Iterator<? extends E>)"""
        return PeekingIterator.__wrap(__PeekingIterator.peekingIterator(arg0))

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
        """public void org.apache.commons.collections4.iterators.PeekingIterator.remove()"""
        super(PeekingIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.NodeListIterator
import org.apache.commons.collections4.iterators.NodeListIterator as __NodeListIterator
__NodeListIterator = __NodeListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.w3c.dom.NodeList as NodeList
import java.lang.Object as __Object
__Object = __Object
import org.w3c.dom.Node as __Node
__Node = __Node
import java.lang.Integer as __int
from builtins import bool
import org.w3c.dom.Node as Node
from builtins import int
 
class NodeListIterator():
    """org.apache.commons.collections4.iterators.NodeListIterator"""
 
    @staticmethod
    def __wrap(java_value: __NodeListIterator) -> 'NodeListIterator':
        return NodeListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodeListIterator):
        """
        Dynamic initializer for NodeListIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.NodeListIterator.hasNext()"""
        return bool.__wrap(super(NodeListIterator, self).hasNext())

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

    @overload
    def __init__(self, arg0: 'Node'):
        """public org.apache.commons.collections4.iterators.NodeListIterator(org.w3c.dom.Node)"""
        val = __NodeListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.NodeListIterator.remove()"""
        super(NodeListIterator, self).remove()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'NodeList'):
        """public org.apache.commons.collections4.iterators.NodeListIterator(org.w3c.dom.NodeList)"""
        val = __NodeListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def next(self) -> 'Node':
        """public org.w3c.dom.Node org.apache.commons.collections4.iterators.NodeListIterator.next()"""
        return 'Node'.__wrap(super(NodeListIterator, self).next()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ListIteratorWrapper
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.ListIteratorWrapper as __ListIteratorWrapper
__ListIteratorWrapper = __ListIteratorWrapper
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
 
class ListIteratorWrapper():
    """org.apache.commons.collections4.iterators.ListIteratorWrapper"""
 
    @staticmethod
    def __wrap(java_value: __ListIteratorWrapper) -> 'ListIteratorWrapper':
        return ListIteratorWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListIteratorWrapper):
        """
        Dynamic initializer for ListIteratorWrapper.
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
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.set(E) throws java.lang.UnsupportedOperationException"""
        super(__ListIteratorWrapper, self).set(arg0)

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ListIteratorWrapper.hasPrevious()"""
        return bool.__wrap(super(ListIteratorWrapper, self).hasPrevious())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ListIteratorWrapper(java.util.Iterator<? extends E>)"""
        val = __ListIteratorWrapper(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.remove() throws java.lang.UnsupportedOperationException"""
        super(ListIteratorWrapper, self).remove()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ListIteratorWrapper.add(E) throws java.lang.UnsupportedOperationException"""
        super(__ListIteratorWrapper, self).add(arg0)

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
        return object.__wrap(super(ListIteratorWrapper, self).previous())

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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ListIteratorWrapper.next() throws java.util.NoSuchElementException"""
        return object.__wrap(super(ListIteratorWrapper, self).next())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ListIteratorWrapper.previousIndex()"""
        return int.__wrap(super(ListIteratorWrapper, self).previousIndex())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ListIteratorWrapper.nextIndex()"""
        return int.__wrap(super(ListIteratorWrapper, self).nextIndex())

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

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ListIteratorWrapper.hasNext()"""
        return bool.__wrap(super(ListIteratorWrapper, self).hasNext()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ZippingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.ZippingIterator as __ZippingIterator
__ZippingIterator = __ZippingIterator
from builtins import object
import java.util.Iterator as Iterator
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
 
class ZippingIterator():
    """org.apache.commons.collections4.iterators.ZippingIterator"""
 
    @staticmethod
    def __wrap(java_value: __ZippingIterator) -> 'ZippingIterator':
        return ZippingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ZippingIterator):
        """
        Dynamic initializer for ZippingIterator.
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

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Iterator', arg2: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ZippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = __ZippingIterator(arg0, arg1, arg2)
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ZippingIterator.hasNext()"""
        return bool.__wrap(super(ZippingIterator, self).hasNext())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ZippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = __ZippingIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ZippingIterator.remove()"""
        super(ZippingIterator, self).remove()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ZippingIterator.next() throws java.util.NoSuchElementException"""
        return object.__wrap(super(ZippingIterator, self).next())

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
    def __init__(self, *arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.ZippingIterator(java.util.Iterator<? extends E>...)"""
        val = __ZippingIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyMapIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.AbstractEmptyMapIterator as __AbstractEmptyMapIterator
__AbstractEmptyMapIterator = __AbstractEmptyMapIterator
from builtins import object
import org.apache.commons.collections4.iterators.EmptyMapIterator as __EmptyMapIterator
__EmptyMapIterator = __EmptyMapIterator
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class EmptyMapIterator():
    """org.apache.commons.collections4.iterators.EmptyMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __EmptyMapIterator) -> 'EmptyMapIterator':
        return EmptyMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmptyMapIterator):
        """
        Dynamic initializer for EmptyMapIterator.
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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.setValue(V)"""
        return object.__wrap(super(__AbstractEmptyMapIterator, self).setValue(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getValue()"""
        return object.__wrap(super(AbstractEmptyMapIterator, self).getValue())

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

    @staticmethod
    @overload
    def emptyMapIterator() -> 'collections4.MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.iterators.EmptyMapIterator.emptyMapIterator()"""
        return collections4.MapIterator.__wrap(__EmptyMapIterator.emptyMapIterator())

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getKey()"""
        return object.__wrap(super(AbstractEmptyMapIterator, self).getKey())

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
 
 
# CLASS: org.apache.commons.collections4.iterators.LoopingIterator
import org.apache.commons.collections4.iterators.LoopingIterator as __LoopingIterator
__LoopingIterator = __LoopingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Collection as Collection
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
from builtins import int
 
class LoopingIterator():
    """org.apache.commons.collections4.iterators.LoopingIterator"""
 
    @staticmethod
    def __wrap(java_value: __LoopingIterator) -> 'LoopingIterator':
        return LoopingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoopingIterator):
        """
        Dynamic initializer for LoopingIterator.
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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.LoopingIterator.next()"""
        return object.__wrap(super(LoopingIterator, self).next())

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.iterators.LoopingIterator.size()"""
        return int.__wrap(super(LoopingIterator, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LoopingIterator.hasNext()"""
        return bool.__wrap(super(LoopingIterator, self).hasNext())

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
    def reset(self):
        """public void org.apache.commons.collections4.iterators.LoopingIterator.reset()"""
        super(LoopingIterator, self).reset()

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.LoopingIterator.remove()"""
        super(LoopingIterator, self).remove()

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

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.iterators.LoopingIterator(java.util.Collection<? extends E>)"""
        val = __LoopingIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractEmptyMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.iterators.AbstractEmptyMapIterator as __AbstractEmptyMapIterator
__AbstractEmptyMapIterator = __AbstractEmptyMapIterator
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
 
class AbstractEmptyMapIterator(ABC):
    """org.apache.commons.collections4.iterators.AbstractEmptyMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractEmptyMapIterator) -> 'AbstractEmptyMapIterator':
        return AbstractEmptyMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractEmptyMapIterator):
        """
        Dynamic initializer for AbstractEmptyMapIterator.
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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.setValue(V)"""
        return object.__wrap(super(__AbstractEmptyMapIterator, self).setValue(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getKey()"""
        return object.__wrap(super(AbstractEmptyMapIterator, self).getKey())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.AbstractEmptyMapIterator()"""
        val = __AbstractEmptyMapIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.AbstractEmptyMapIterator()"""
        val = __AbstractEmptyMapIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractEmptyMapIterator.getValue()"""
        return object.__wrap(super(AbstractEmptyMapIterator, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.BoundedIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import org.apache.commons.collections4.iterators.BoundedIterator as __BoundedIterator
__BoundedIterator = __BoundedIterator
import java.util.Iterator as Iterator
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
 
class BoundedIterator():
    """org.apache.commons.collections4.iterators.BoundedIterator"""
 
    @staticmethod
    def __wrap(java_value: __BoundedIterator) -> 'BoundedIterator':
        return BoundedIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundedIterator):
        """
        Dynamic initializer for BoundedIterator.
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
    def __init__(self, arg0: 'Iterator', arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.BoundedIterator(java.util.Iterator<? extends E>,long,long)"""
        val = __BoundedIterator(arg0, __long.valueOf(arg1), __long.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.BoundedIterator.remove()"""
        super(BoundedIterator, self).remove()

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.BoundedIterator.hasNext()"""
        return bool.__wrap(super(BoundedIterator, self).hasNext())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.BoundedIterator.next()"""
        return object.__wrap(super(BoundedIterator, self).next())

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
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractListIteratorDecorator
from builtins import str
import org.apache.commons.collections4.iterators.AbstractListIteratorDecorator as __AbstractListIteratorDecorator
__AbstractListIteratorDecorator = __AbstractListIteratorDecorator
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
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractListIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractListIteratorDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractListIteratorDecorator) -> 'AbstractListIteratorDecorator':
        return AbstractListIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractListIteratorDecorator):
        """
        Dynamic initializer for AbstractListIteratorDecorator.
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
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.add(E)"""
        super(__AbstractListIteratorDecorator, self).add(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasPrevious()"""
        return bool.__wrap(super(AbstractListIteratorDecorator, self).hasPrevious())

    @overload
    def __init__(self, arg0: 'ListIterator'):
        """public org.apache.commons.collections4.iterators.AbstractListIteratorDecorator(java.util.ListIterator<E>)"""
        val = __AbstractListIteratorDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.hasNext()"""
        return bool.__wrap(super(AbstractListIteratorDecorator, self).hasNext())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.nextIndex()"""
        return int.__wrap(super(AbstractListIteratorDecorator, self).nextIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.next()"""
        return object.__wrap(super(AbstractListIteratorDecorator, self).next())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.set(E)"""
        super(__AbstractListIteratorDecorator, self).set(arg0)

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previous()"""
        return object.__wrap(super(AbstractListIteratorDecorator, self).previous())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.previousIndex()"""
        return int.__wrap(super(AbstractListIteratorDecorator, self).previousIndex())

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
        """public void org.apache.commons.collections4.iterators.AbstractListIteratorDecorator.remove()"""
        super(AbstractListIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.CollatingIterator
from builtins import str
import org.apache.commons.collections4.iterators.CollatingIterator as __CollatingIterator
__CollatingIterator = __CollatingIterator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class CollatingIterator():
    """org.apache.commons.collections4.iterators.CollatingIterator"""
 
    @staticmethod
    def __wrap(java_value: __CollatingIterator) -> 'CollatingIterator':
        return CollatingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollatingIterator):
        """
        Dynamic initializer for CollatingIterator.
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
    def __init__(self, arg0: 'Comparator', arg1: 'Collection'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,java.util.Collection<java.util.Iterator<? extends E>>)"""
        val = __CollatingIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.addIterator(java.util.Iterator<? extends E>)"""
        super(__CollatingIterator, self).addIterator(arg0)

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.CollatingIterator.next() throws java.util.NoSuchElementException"""
        return object.__wrap(super(CollatingIterator, self).next())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Iterator', arg2: 'Iterator'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = __CollatingIterator(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setComparator(self, arg0: 'Comparator'):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.setComparator(java.util.Comparator<? super E>)"""
        super(__CollatingIterator, self).setComparator(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: int):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,int)"""
        val = __CollatingIterator(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.CollatingIterator.hasNext()"""
        return bool.__wrap(super(CollatingIterator, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>)"""
        val = __CollatingIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.iterators.CollatingIterator.getComparator()"""
        return 'Comparator'.__wrap(super(CollatingIterator, self).getComparator())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Iterator'):
        """public org.apache.commons.collections4.iterators.CollatingIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>[])"""
        val = __CollatingIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setIterator(self, arg0: int, arg1: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.setIterator(int,java.util.Iterator<? extends E>)"""
        super(__CollatingIterator, self).setIterator(__int.valueOf(arg0), arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.CollatingIterator()"""
        val = __CollatingIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.CollatingIterator.remove()"""
        super(CollatingIterator, self).remove()

    @overload
    def getIteratorIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.CollatingIterator.getIteratorIndex()"""
        return int.__wrap(super(CollatingIterator, self).getIteratorIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getIterators(self) -> 'List':
        """public java.util.List<java.util.Iterator<? extends E>> org.apache.commons.collections4.iterators.CollatingIterator.getIterators()"""
        return 'List'.__wrap(super(CollatingIterator, self).getIterators())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.CollatingIterator()"""
        val = __CollatingIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.ObjectArrayListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import org.apache.commons.collections4.iterators.ObjectArrayIterator as __ObjectArrayIterator
__ObjectArrayIterator = __ObjectArrayIterator
from typing import List
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.iterators.ObjectArrayListIterator as __ObjectArrayListIterator
__ObjectArrayListIterator = __ObjectArrayListIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjectArrayListIterator():
    """org.apache.commons.collections4.iterators.ObjectArrayListIterator"""
 
    @staticmethod
    def __wrap(java_value: __ObjectArrayListIterator) -> 'ObjectArrayListIterator':
        return ObjectArrayListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectArrayListIterator):
        """
        Dynamic initializer for ObjectArrayListIterator.
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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectArrayListIterator.hasPrevious()"""
        return bool.__wrap(super(ObjectArrayListIterator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayListIterator.reset()"""
        super(ObjectArrayListIterator, self).reset()

    @overload
    def __init__(self, arg0: 'Object', arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayListIterator(E[],int,int)"""
        val = __ObjectArrayListIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: object):
        """public org.apache.commons.collections4.iterators.ObjectArrayListIterator(E...)"""
        val = __ObjectArrayListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Object', arg1: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayListIterator(E[],int)"""
        val = __ObjectArrayListIterator(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectArrayIterator.hasNext()"""
        return bool.__wrap(super(ObjectArrayIterator, self).hasNext())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def getArray(self) -> List[object]:
        """public E[] org.apache.commons.collections4.iterators.ObjectArrayIterator.getArray()"""
        return List[object].__wrap(super(ObjectArrayIterator, self).getArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ObjectArrayListIterator.add(E)"""
        super(__ObjectArrayListIterator, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ObjectArrayListIterator.set(E)"""
        super(__ObjectArrayListIterator, self).set(arg0)

    @override
    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getEndIndex()"""
        return int.__wrap(super(ObjectArrayIterator, self).getEndIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayIterator.remove()"""
        super(ObjectArrayIterator, self).remove()

    @override
    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getStartIndex()"""
        return int.__wrap(super(ObjectArrayIterator, self).getStartIndex())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectArrayListIterator.previous()"""
        return object.__wrap(super(ObjectArrayListIterator, self).previous())

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayListIterator.nextIndex()"""
        return int.__wrap(super(ObjectArrayListIterator, self).nextIndex())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayListIterator.previousIndex()"""
        return int.__wrap(super(ObjectArrayListIterator, self).previousIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectArrayListIterator.next()"""
        return object.__wrap(super(ObjectArrayListIterator, self).next()) 
 
 
# CLASS: org.apache.commons.collections4.iterators.SingletonIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.SingletonIterator as __SingletonIterator
__SingletonIterator = __SingletonIterator
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
from builtins import int
 
class SingletonIterator():
    """org.apache.commons.collections4.iterators.SingletonIterator"""
 
    @staticmethod
    def __wrap(java_value: __SingletonIterator) -> 'SingletonIterator':
        return SingletonIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SingletonIterator):
        """
        Dynamic initializer for SingletonIterator.
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
        """public boolean org.apache.commons.collections4.iterators.SingletonIterator.hasNext()"""
        return bool.__wrap(super(SingletonIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.SingletonIterator.next()"""
        return object.__wrap(super(SingletonIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.SingletonIterator.reset()"""
        super(SingletonIterator, self).reset()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.SingletonIterator.remove()"""
        super(SingletonIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.SingletonIterator(E)"""
        val = __SingletonIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: bool):
        """public org.apache.commons.collections4.iterators.SingletonIterator(E,boolean)"""
        val = __SingletonIterator(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.iterators.FilterIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.iterators.FilterIterator as __FilterIterator
__FilterIterator = __FilterIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FilterIterator():
    """org.apache.commons.collections4.iterators.FilterIterator"""
 
    @staticmethod
    def __wrap(java_value: __FilterIterator) -> 'FilterIterator':
        return FilterIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FilterIterator):
        """
        Dynamic initializer for FilterIterator.
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
    def __init__(self, arg0: 'Iterator', arg1: 'Predicate'):
        """public org.apache.commons.collections4.iterators.FilterIterator(java.util.Iterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        val = __FilterIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.FilterIterator()"""
        val = __FilterIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends E> org.apache.commons.collections4.iterators.FilterIterator.getIterator()"""
        return 'Iterator'.__wrap(super(FilterIterator, self).getIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setIterator(java.util.Iterator<? extends E>)"""
        super(__FilterIterator, self).setIterator(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.FilterIterator()"""
        val = __FilterIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.FilterIterator.remove()"""
        super(FilterIterator, self).remove()

    @overload
    def setPredicate(self, arg0: 'Predicate'):
        """public void org.apache.commons.collections4.iterators.FilterIterator.setPredicate(org.apache.commons.collections4.Predicate<? super E>)"""
        super(__FilterIterator, self).setPredicate(arg0)

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.FilterIterator.hasNext()"""
        return bool.__wrap(super(FilterIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.FilterIterator.next()"""
        return object.__wrap(super(FilterIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.iterators.FilterIterator.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(FilterIterator, self).getPredicate())

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.FilterIterator(java.util.Iterator<? extends E>)"""
        val = __FilterIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.EntrySetMapIterator
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
import org.apache.commons.collections4.iterators.EntrySetMapIterator as __EntrySetMapIterator
__EntrySetMapIterator = __EntrySetMapIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class EntrySetMapIterator():
    """org.apache.commons.collections4.iterators.EntrySetMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __EntrySetMapIterator) -> 'EntrySetMapIterator':
        return EntrySetMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySetMapIterator):
        """
        Dynamic initializer for EntrySetMapIterator.
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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.EntrySetMapIterator.setValue(V)"""
        return object.__wrap(super(__EntrySetMapIterator, self).setValue(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.EntrySetMapIterator.getValue()"""
        return object.__wrap(super(EntrySetMapIterator, self).getValue())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.EntrySetMapIterator.remove()"""
        super(EntrySetMapIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.EntrySetMapIterator.hasNext()"""
        return bool.__wrap(super(EntrySetMapIterator, self).hasNext())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.iterators.EntrySetMapIterator(java.util.Map<K, V>)"""
        val = __EntrySetMapIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.EntrySetMapIterator.getKey()"""
        return object.__wrap(super(EntrySetMapIterator, self).getKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.EntrySetMapIterator.next()"""
        return object.__wrap(super(EntrySetMapIterator, self).next())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.iterators.EntrySetMapIterator.toString()"""
        return str.__wrap(super(EntrySetMapIterator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.EntrySetMapIterator.reset()"""
        super(EntrySetMapIterator, self).reset() 
 
 
# CLASS: org.apache.commons.collections4.iterators.TransformIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.iterators.TransformIterator as __TransformIterator
__TransformIterator = __TransformIterator
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import int
 
class TransformIterator():
    """org.apache.commons.collections4.iterators.TransformIterator"""
 
    @staticmethod
    def __wrap(java_value: __TransformIterator) -> 'TransformIterator':
        return TransformIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformIterator):
        """
        Dynamic initializer for TransformIterator.
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
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.iterators.TransformIterator.getTransformer()"""
        return 'collections4.Transformer'.__wrap(super(TransformIterator, self).getTransformer())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.TransformIterator()"""
        val = __TransformIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Transformer'):
        """public org.apache.commons.collections4.iterators.TransformIterator(java.util.Iterator<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = __TransformIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.TransformIterator.hasNext()"""
        return bool.__wrap(super(TransformIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.TransformIterator()"""
        val = __TransformIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends I> org.apache.commons.collections4.iterators.TransformIterator.getIterator()"""
        return 'Iterator'.__wrap(super(TransformIterator, self).getIterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setTransformer(self, arg0: 'Transformer'):
        """public void org.apache.commons.collections4.iterators.TransformIterator.setTransformer(org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        super(__TransformIterator, self).setTransformer(arg0)

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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.TransformIterator.remove()"""
        super(TransformIterator, self).remove()

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
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.TransformIterator(java.util.Iterator<? extends I>)"""
        val = __TransformIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def next(self) -> object:
        """public O org.apache.commons.collections4.iterators.TransformIterator.next()"""
        return object.__wrap(super(TransformIterator, self).next())

    @overload
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.TransformIterator.setIterator(java.util.Iterator<? extends I>)"""
        super(__TransformIterator, self).setIterator(arg0) 
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator as __AbstractOrderedMapIteratorDecorator
__AbstractOrderedMapIteratorDecorator = __AbstractOrderedMapIteratorDecorator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractOrderedMapIteratorDecorator():
    """org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractOrderedMapIteratorDecorator) -> 'AbstractOrderedMapIteratorDecorator':
        return AbstractOrderedMapIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractOrderedMapIteratorDecorator):
        """
        Dynamic initializer for AbstractOrderedMapIteratorDecorator.
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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.getValue()"""
        return object.__wrap(super(AbstractOrderedMapIteratorDecorator, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.getKey()"""
        return object.__wrap(super(AbstractOrderedMapIteratorDecorator, self).getKey())

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

    @overload
    def __init__(self, arg0: 'OrderedMapIterator'):
        """public org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator(org.apache.commons.collections4.OrderedMapIterator<K, V>)"""
        val = __AbstractOrderedMapIteratorDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.previous()"""
        return object.__wrap(super(AbstractOrderedMapIteratorDecorator, self).previous())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.hasNext()"""
        return bool.__wrap(super(AbstractOrderedMapIteratorDecorator, self).hasNext())

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.next()"""
        return object.__wrap(super(AbstractOrderedMapIteratorDecorator, self).next())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.hasPrevious()"""
        return bool.__wrap(super(AbstractOrderedMapIteratorDecorator, self).hasPrevious())

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
        """public void org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.remove()"""
        super(AbstractOrderedMapIteratorDecorator, self).remove()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.AbstractOrderedMapIteratorDecorator.setValue(V)"""
        return object.__wrap(super(__AbstractOrderedMapIteratorDecorator, self).setValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.EnumerationIterator
import org.apache.commons.collections4.iterators.EnumerationIterator as __EnumerationIterator
__EnumerationIterator = __EnumerationIterator
from builtins import str
import java.util.Enumeration as __Enumeration
__Enumeration = __Enumeration
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.Enumeration as Enumeration
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EnumerationIterator():
    """org.apache.commons.collections4.iterators.EnumerationIterator"""
 
    @staticmethod
    def __wrap(java_value: __EnumerationIterator) -> 'EnumerationIterator':
        return EnumerationIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumerationIterator):
        """
        Dynamic initializer for EnumerationIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.EnumerationIterator.remove()"""
        super(EnumerationIterator, self).remove()

    @overload
    def __init__(self, arg0: 'Enumeration', arg1: 'Collection'):
        """public org.apache.commons.collections4.iterators.EnumerationIterator(java.util.Enumeration<? extends E>,java.util.Collection<? super E>)"""
        val = __EnumerationIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Enumeration'):
        """public org.apache.commons.collections4.iterators.EnumerationIterator(java.util.Enumeration<? extends E>)"""
        val = __EnumerationIterator(arg0)
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
    def __init__(self):
        """public org.apache.commons.collections4.iterators.EnumerationIterator()"""
        val = __EnumerationIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getEnumeration(self) -> 'Enumeration':
        """public java.util.Enumeration<? extends E> org.apache.commons.collections4.iterators.EnumerationIterator.getEnumeration()"""
        return 'Enumeration'.__wrap(super(EnumerationIterator, self).getEnumeration())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.EnumerationIterator.next()"""
        return object.__wrap(super(EnumerationIterator, self).next())

    @overload
    def setEnumeration(self, arg0: 'Enumeration'):
        """public void org.apache.commons.collections4.iterators.EnumerationIterator.setEnumeration(java.util.Enumeration<? extends E>)"""
        super(__EnumerationIterator, self).setEnumeration(arg0)

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.EnumerationIterator.hasNext()"""
        return bool.__wrap(super(EnumerationIterator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.EnumerationIterator()"""
        val = __EnumerationIterator()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableMapIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.iterators.UnmodifiableMapIterator as __UnmodifiableMapIterator
__UnmodifiableMapIterator = __UnmodifiableMapIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnmodifiableMapIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableMapIterator) -> 'UnmodifiableMapIterator':
        return UnmodifiableMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableMapIterator):
        """
        Dynamic initializer for UnmodifiableMapIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableMapIterator.remove()"""
        super(UnmodifiableMapIterator, self).remove()

    @staticmethod
    @overload
    def unmodifiableMapIterator(arg0: 'MapIterator') -> 'collections4.MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.iterators.UnmodifiableMapIterator.unmodifiableMapIterator(org.apache.commons.collections4.MapIterator<? extends K, ? extends V>)"""
        return collections4.MapIterator.__wrap(__UnmodifiableMapIterator.unmodifiableMapIterator(arg0))

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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableMapIterator.getValue()"""
        return object.__wrap(super(UnmodifiableMapIterator, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableMapIterator.getKey()"""
        return object.__wrap(super(UnmodifiableMapIterator, self).getKey())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableMapIterator.hasNext()"""
        return bool.__wrap(super(UnmodifiableMapIterator, self).hasNext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableMapIterator.next()"""
        return object.__wrap(super(UnmodifiableMapIterator, self).next())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableMapIterator.setValue(V)"""
        return object.__wrap(super(__UnmodifiableMapIterator, self).setValue(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as __AbstractUntypedIteratorDecorator
__AbstractUntypedIteratorDecorator = __AbstractUntypedIteratorDecorator
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
 
class AbstractUntypedIteratorDecorator(ABC):
    """org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractUntypedIteratorDecorator) -> 'AbstractUntypedIteratorDecorator':
        return AbstractUntypedIteratorDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractUntypedIteratorDecorator):
        """
        Dynamic initializer for AbstractUntypedIteratorDecorator.
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
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool.__wrap(super(AbstractUntypedIteratorDecorator, self).hasNext())

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

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.Iterator.next()"""
        pass

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
        """public void org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.remove()"""
        super(AbstractUntypedIteratorDecorator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ArrayListIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.iterators.ArrayIterator as __ArrayIterator
__ArrayIterator = __ArrayIterator
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
import org.apache.commons.collections4.iterators.ArrayListIterator as __ArrayListIterator
__ArrayListIterator = __ArrayListIterator
from builtins import int
 
class ArrayListIterator():
    """org.apache.commons.collections4.iterators.ArrayListIterator"""
 
    @staticmethod
    def __wrap(java_value: __ArrayListIterator) -> 'ArrayListIterator':
        return ArrayListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayListIterator):
        """
        Dynamic initializer for ArrayListIterator.
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
    def __init__(self, arg0: object, arg1: int):
        """public org.apache.commons.collections4.iterators.ArrayListIterator(java.lang.Object,int)"""
        val = __ArrayListIterator(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayListIterator.previousIndex()"""
        return int.__wrap(super(ArrayListIterator, self).previousIndex())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: object, arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ArrayListIterator(java.lang.Object,int,int)"""
        val = __ArrayListIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ArrayListIterator.hasPrevious()"""
        return bool.__wrap(super(ArrayListIterator, self).hasPrevious())

    @override
    @overload
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getStartIndex()"""
        return int.__wrap(super(ArrayIterator, self).getStartIndex())

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
    def getArray(self) -> object:
        """public java.lang.Object org.apache.commons.collections4.iterators.ArrayIterator.getArray()"""
        return object.__wrap(super(ArrayIterator, self).getArray())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ArrayIterator.hasNext()"""
        return bool.__wrap(super(ArrayIterator, self).hasNext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ArrayListIterator.next()"""
        return object.__wrap(super(ArrayListIterator, self).next())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ArrayListIterator.previous()"""
        return object.__wrap(super(ArrayListIterator, self).previous())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.iterators.ArrayListIterator(java.lang.Object)"""
        val = __ArrayListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayIterator.getEndIndex()"""
        return int.__wrap(super(ArrayIterator, self).getEndIndex())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ArrayListIterator.set(java.lang.Object)"""
        super(__ArrayListIterator, self).set(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ArrayListIterator.nextIndex()"""
        return int.__wrap(super(ArrayListIterator, self).nextIndex())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ArrayListIterator.reset()"""
        super(ArrayListIterator, self).reset()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ArrayListIterator.add(java.lang.Object)"""
        super(__ArrayListIterator, self).add(arg0) 
 
 
# CLASS: org.apache.commons.collections4.iterators.LazyIteratorChain
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
import org.apache.commons.collections4.iterators.LazyIteratorChain as __LazyIteratorChain
__LazyIteratorChain = __LazyIteratorChain
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LazyIteratorChain(ABC):
    """org.apache.commons.collections4.iterators.LazyIteratorChain"""
 
    @staticmethod
    def __wrap(java_value: __LazyIteratorChain) -> 'LazyIteratorChain':
        return LazyIteratorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazyIteratorChain):
        """
        Dynamic initializer for LazyIteratorChain.
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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.LazyIteratorChain.next()"""
        return object.__wrap(super(LazyIteratorChain, self).next())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.LazyIteratorChain()"""
        val = __LazyIteratorChain()
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

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.LazyIteratorChain.hasNext()"""
        return bool.__wrap(super(LazyIteratorChain, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.LazyIteratorChain.remove()"""
        super(LazyIteratorChain, self).remove()

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
    def __init__(self):
        """public org.apache.commons.collections4.iterators.LazyIteratorChain()"""
        val = __LazyIteratorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.IteratorIterable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.iterators.IteratorIterable as __IteratorIterable
__IteratorIterable = __IteratorIterable
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IteratorIterable():
    """org.apache.commons.collections4.iterators.IteratorIterable"""
 
    @staticmethod
    def __wrap(java_value: __IteratorIterable) -> 'IteratorIterable':
        return IteratorIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IteratorIterable):
        """
        Dynamic initializer for IteratorIterable.
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
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorIterable(java.util.Iterator<? extends E>)"""
        val = __IteratorIterable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.iterators.IteratorIterable.iterator()"""
        return 'Iterator'.__wrap(super(IteratorIterable, self).iterator())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

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
    def __init__(self, arg0: 'Iterator', arg1: bool):
        """public org.apache.commons.collections4.iterators.IteratorIterable(java.util.Iterator<? extends E>,boolean)"""
        val = __IteratorIterable(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.SkippingIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as __AbstractUntypedIteratorDecorator
__AbstractUntypedIteratorDecorator = __AbstractUntypedIteratorDecorator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.iterators.SkippingIterator as __SkippingIterator
__SkippingIterator = __SkippingIterator
from builtins import bool
from builtins import int
 
class SkippingIterator():
    """org.apache.commons.collections4.iterators.SkippingIterator"""
 
    @staticmethod
    def __wrap(java_value: __SkippingIterator) -> 'SkippingIterator':
        return SkippingIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SkippingIterator):
        """
        Dynamic initializer for SkippingIterator.
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
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool.__wrap(super(AbstractUntypedIteratorDecorator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.SkippingIterator.remove()"""
        super(SkippingIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.SkippingIterator.next()"""
        return object.__wrap(super(SkippingIterator, self).next())

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

    @overload
    def __init__(self, arg0: 'Iterator', arg1: int):
        """public org.apache.commons.collections4.iterators.SkippingIterator(java.util.Iterator<E>,long)"""
        val = __SkippingIterator(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.iterators.ReverseListIterator
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
import org.apache.commons.collections4.iterators.ReverseListIterator as __ReverseListIterator
__ReverseListIterator = __ReverseListIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class ReverseListIterator():
    """org.apache.commons.collections4.iterators.ReverseListIterator"""
 
    @staticmethod
    def __wrap(java_value: __ReverseListIterator) -> 'ReverseListIterator':
        return ReverseListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReverseListIterator):
        """
        Dynamic initializer for ReverseListIterator.
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
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ReverseListIterator.next()"""
        return object.__wrap(super(ReverseListIterator, self).next())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.set(E)"""
        super(__ReverseListIterator, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def previousIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ReverseListIterator.previousIndex()"""
        return int.__wrap(super(ReverseListIterator, self).previousIndex())

    @override
    @overload
    def previous(self) -> object:
        """public E org.apache.commons.collections4.iterators.ReverseListIterator.previous()"""
        return object.__wrap(super(ReverseListIterator, self).previous())

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
        """public int org.apache.commons.collections4.iterators.ReverseListIterator.nextIndex()"""
        return int.__wrap(super(ReverseListIterator, self).nextIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def add(self, arg0: object):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.add(E)"""
        super(__ReverseListIterator, self).add(arg0)

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ReverseListIterator.hasNext()"""
        return bool.__wrap(super(ReverseListIterator, self).hasNext())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.reset()"""
        super(ReverseListIterator, self).reset()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ReverseListIterator.hasPrevious()"""
        return bool.__wrap(super(ReverseListIterator, self).hasPrevious())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.iterators.ReverseListIterator(java.util.List<E>)"""
        val = __ReverseListIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public void org.apache.commons.collections4.iterators.ReverseListIterator.remove()"""
        super(ReverseListIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.PermutationIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.PermutationIterator as __PermutationIterator
__PermutationIterator = __PermutationIterator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class PermutationIterator():
    """org.apache.commons.collections4.iterators.PermutationIterator"""
 
    @staticmethod
    def __wrap(java_value: __PermutationIterator) -> 'PermutationIterator':
        return PermutationIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PermutationIterator):
        """
        Dynamic initializer for PermutationIterator.
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
        """public boolean org.apache.commons.collections4.iterators.PermutationIterator.hasNext()"""
        return bool.__wrap(super(PermutationIterator, self).hasNext())

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
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.iterators.PermutationIterator(java.util.Collection<? extends E>)"""
        val = __PermutationIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.iterators.PermutationIterator.next()"""
        return 'List'.__wrap(super(PermutationIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.PermutationIterator.remove()"""
        super(PermutationIterator, self).remove()

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
 
 
# CLASS: org.apache.commons.collections4.iterators.EmptyOrderedIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import org.apache.commons.collections4.OrderedIterator as __OrderedIterator
__OrderedIterator = __OrderedIterator
from builtins import type
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import org.apache.commons.collections4.iterators.EmptyOrderedIterator as __EmptyOrderedIterator
__EmptyOrderedIterator = __EmptyOrderedIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EmptyOrderedIterator():
    """org.apache.commons.collections4.iterators.EmptyOrderedIterator"""
 
    @staticmethod
    def __wrap(java_value: __EmptyOrderedIterator) -> 'EmptyOrderedIterator':
        return EmptyOrderedIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmptyOrderedIterator):
        """
        Dynamic initializer for EmptyOrderedIterator.
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

    @staticmethod
    @overload
    def emptyOrderedIterator() -> 'collections4.OrderedIterator':
        """public static <E> org.apache.commons.collections4.OrderedIterator<E> org.apache.commons.collections4.iterators.EmptyOrderedIterator.emptyOrderedIterator()"""
        return collections4.OrderedIterator.__wrap(__EmptyOrderedIterator.emptyOrderedIterator())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.IteratorEnumeration
from builtins import str
import java.util.Enumeration as __Enumeration
__Enumeration = __Enumeration
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.iterators.IteratorEnumeration as __IteratorEnumeration
__IteratorEnumeration = __IteratorEnumeration
from builtins import object
import java.util.Iterator as Iterator
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
 
class IteratorEnumeration():
    """org.apache.commons.collections4.iterators.IteratorEnumeration"""
 
    @staticmethod
    def __wrap(java_value: __IteratorEnumeration) -> 'IteratorEnumeration':
        return IteratorEnumeration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IteratorEnumeration):
        """
        Dynamic initializer for IteratorEnumeration.
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
    def __init__(self):
        """public org.apache.commons.collections4.iterators.IteratorEnumeration()"""
        val = __IteratorEnumeration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasMoreElements(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.IteratorEnumeration.hasMoreElements()"""
        return bool.__wrap(super(IteratorEnumeration, self).hasMoreElements())

    @override
    @overload
    def nextElement(self) -> object:
        """public E org.apache.commons.collections4.iterators.IteratorEnumeration.nextElement()"""
        return object.__wrap(super(IteratorEnumeration, self).nextElement())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.IteratorEnumeration()"""
        val = __IteratorEnumeration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def asIterator(self) -> 'Iterator':
        """public default java.util.Iterator<E> java.util.Enumeration.asIterator()"""
        return 'Iterator'.__wrap(super(Enumeration, self).asIterator())

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
    def setIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.IteratorEnumeration.setIterator(java.util.Iterator<? extends E>)"""
        super(__IteratorEnumeration, self).setIterator(arg0)

    @overload
    def getIterator(self) -> 'Iterator':
        """public java.util.Iterator<? extends E> org.apache.commons.collections4.iterators.IteratorEnumeration.getIterator()"""
        return 'Iterator'.__wrap(super(IteratorEnumeration, self).getIterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorEnumeration(java.util.Iterator<? extends E>)"""
        val = __IteratorEnumeration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
from builtins import object
import java.util.function.Consumer as Consumer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator as __UnmodifiableOrderedMapIterator
__UnmodifiableOrderedMapIterator = __UnmodifiableOrderedMapIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnmodifiableOrderedMapIterator():
    """org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableOrderedMapIterator) -> 'UnmodifiableOrderedMapIterator':
        return UnmodifiableOrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableOrderedMapIterator):
        """
        Dynamic initializer for UnmodifiableOrderedMapIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.remove()"""
        super(UnmodifiableOrderedMapIterator, self).remove()

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.previous()"""
        return object.__wrap(super(UnmodifiableOrderedMapIterator, self).previous())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.hasNext()"""
        return bool.__wrap(super(UnmodifiableOrderedMapIterator, self).hasNext())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.getValue()"""
        return object.__wrap(super(UnmodifiableOrderedMapIterator, self).getValue())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.hasPrevious()"""
        return bool.__wrap(super(UnmodifiableOrderedMapIterator, self).hasPrevious())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.next()"""
        return object.__wrap(super(UnmodifiableOrderedMapIterator, self).next())

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.getKey()"""
        return object.__wrap(super(UnmodifiableOrderedMapIterator, self).getKey())

    @staticmethod
    @overload
    def unmodifiableOrderedMapIterator(arg0: 'OrderedMapIterator') -> 'collections4.OrderedMapIterator':
        """public static <K,V> org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.unmodifiableOrderedMapIterator(org.apache.commons.collections4.OrderedMapIterator<K, ? extends V>)"""
        return collections4.OrderedMapIterator.__wrap(__UnmodifiableOrderedMapIterator.unmodifiableOrderedMapIterator(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.iterators.UnmodifiableOrderedMapIterator.setValue(V)"""
        return object.__wrap(super(__UnmodifiableOrderedMapIterator, self).setValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.IteratorChain
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.iterators.IteratorChain as __IteratorChain
__IteratorChain = __IteratorChain
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
 
class IteratorChain():
    """org.apache.commons.collections4.iterators.IteratorChain"""
 
    @staticmethod
    def __wrap(java_value: __IteratorChain) -> 'IteratorChain':
        return IteratorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IteratorChain):
        """
        Dynamic initializer for IteratorChain.
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
    def remove(self):
        """public void org.apache.commons.collections4.iterators.IteratorChain.remove()"""
        super(IteratorChain, self).remove()

    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.IteratorChain.isLocked()"""
        return bool.__wrap(super(IteratorChain, self).isLocked())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.IteratorChain.hasNext()"""
        return bool.__wrap(super(IteratorChain, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.IteratorChain.next()"""
        return object.__wrap(super(IteratorChain, self).next())

    @overload
    def __init__(self, arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Iterator<? extends E>)"""
        val = __IteratorChain(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, *arg0: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Iterator<? extends E>...)"""
        val = __IteratorChain(arg0)
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
    def __init__(self, ):
        """public org.apache.commons.collections4.iterators.IteratorChain()"""
        val = __IteratorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Iterator'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        val = __IteratorChain(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Collection'):
        """public org.apache.commons.collections4.iterators.IteratorChain(java.util.Collection<java.util.Iterator<? extends E>>)"""
        val = __IteratorChain(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.iterators.IteratorChain()"""
        val = __IteratorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.iterators.IteratorChain.size()"""
        return int.__wrap(super(IteratorChain, self).size())

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
    def addIterator(self, arg0: 'Iterator'):
        """public void org.apache.commons.collections4.iterators.IteratorChain.addIterator(java.util.Iterator<? extends E>)"""
        super(__IteratorChain, self).addIterator(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.iterators.ObjectArrayIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import org.apache.commons.collections4.iterators.ObjectArrayIterator as __ObjectArrayIterator
__ObjectArrayIterator = __ObjectArrayIterator
from typing import List
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
 
class ObjectArrayIterator():
    """org.apache.commons.collections4.iterators.ObjectArrayIterator"""
 
    @staticmethod
    def __wrap(java_value: __ObjectArrayIterator) -> 'ObjectArrayIterator':
        return ObjectArrayIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectArrayIterator):
        """
        Dynamic initializer for ObjectArrayIterator.
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
    def getStartIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getStartIndex()"""
        return int.__wrap(super(ObjectArrayIterator, self).getStartIndex())

    @overload
    def __init__(self, arg0: 'Object', arg1: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayIterator(E[],int)"""
        val = __ObjectArrayIterator(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def next(self) -> object:
        """public E org.apache.commons.collections4.iterators.ObjectArrayIterator.next()"""
        return object.__wrap(super(ObjectArrayIterator, self).next())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Object', arg1: int, arg2: int):
        """public org.apache.commons.collections4.iterators.ObjectArrayIterator(E[],int,int)"""
        val = __ObjectArrayIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: object):
        """public org.apache.commons.collections4.iterators.ObjectArrayIterator(E...)"""
        val = __ObjectArrayIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.ObjectArrayIterator.hasNext()"""
        return bool.__wrap(super(ObjectArrayIterator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayIterator.remove()"""
        super(ObjectArrayIterator, self).remove()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getEndIndex(self) -> int:
        """public int org.apache.commons.collections4.iterators.ObjectArrayIterator.getEndIndex()"""
        return int.__wrap(super(ObjectArrayIterator, self).getEndIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.iterators.ObjectArrayIterator.reset()"""
        super(ObjectArrayIterator, self).reset()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getArray(self) -> List[object]:
        """public E[] org.apache.commons.collections4.iterators.ObjectArrayIterator.getArray()"""
        return List[object].__wrap(super(ObjectArrayIterator, self).getArray())

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