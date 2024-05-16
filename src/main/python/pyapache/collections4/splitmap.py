from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
from builtins import object
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator as __AbstractIterableGetMapDecorator
__AbstractIterableGetMapDecorator = __AbstractIterableGetMapDecorator
from builtins import int
 
class AbstractIterableGetMapDecorator():
    """org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractIterableGetMapDecorator) -> 'AbstractIterableGetMapDecorator':
        return AbstractIterableGetMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractIterableGetMapDecorator):
        """
        Dynamic initializer for AbstractIterableGetMapDecorator.
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
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator(java.util.Map<K, V>)"""
        val = __AbstractIterableGetMapDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.toString()"""
        return str.__wrap(super(AbstractIterableGetMapDecorator, self).toString())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractIterableGetMapDecorator, self).entrySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractIterableGetMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractIterableGetMapDecorator, self).keySet())

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractIterableGetMapDecorator, self).get(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractIterableGetMapDecorator, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.size()"""
        return int.__wrap(super(AbstractIterableGetMapDecorator, self).size())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractIterableGetMapDecorator, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractIterableGetMapDecorator, self).hashCode())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).equals(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableGetMapDecorator, self).mapIterator())

 
 
 
# CLASS: org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
from builtins import object
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator as __AbstractIterableGetMapDecorator
__AbstractIterableGetMapDecorator = __AbstractIterableGetMapDecorator
from builtins import int
 
class AbstractIterableGetMapDecorator():
    """org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractIterableGetMapDecorator) -> 'AbstractIterableGetMapDecorator':
        return AbstractIterableGetMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractIterableGetMapDecorator):
        """
        Dynamic initializer for AbstractIterableGetMapDecorator.
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
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator(java.util.Map<K, V>)"""
        val = __AbstractIterableGetMapDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.toString()"""
        return str.__wrap(super(AbstractIterableGetMapDecorator, self).toString())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractIterableGetMapDecorator, self).entrySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractIterableGetMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractIterableGetMapDecorator, self).keySet())

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractIterableGetMapDecorator, self).get(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractIterableGetMapDecorator, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.size()"""
        return int.__wrap(super(AbstractIterableGetMapDecorator, self).size())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractIterableGetMapDecorator, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractIterableGetMapDecorator, self).hashCode())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).equals(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableGetMapDecorator, self).mapIterator())

 
 
 
# CLASS: org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator 
 
 
# CLASS: org.apache.commons.collections4.splitmap.TransformedSplitMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
import org.apache.commons.collections4.splitmap.TransformedSplitMap as __TransformedSplitMap
__TransformedSplitMap = __TransformedSplitMap
from builtins import object
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator as __AbstractIterableGetMapDecorator
__AbstractIterableGetMapDecorator = __AbstractIterableGetMapDecorator
from builtins import int
 
class TransformedSplitMap():
    """org.apache.commons.collections4.splitmap.TransformedSplitMap"""
 
    @staticmethod
    def __wrap(java_value: __TransformedSplitMap) -> 'TransformedSplitMap':
        return TransformedSplitMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedSplitMap):
        """
        Dynamic initializer for TransformedSplitMap.
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
        """public java.lang.String org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.toString()"""
        return str.__wrap(super(AbstractIterableGetMapDecorator, self).toString())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractIterableGetMapDecorator, self).entrySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractIterableGetMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractIterableGetMapDecorator, self).keySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSplitMap':
        """public static <J,K,U,V> org.apache.commons.collections4.splitmap.TransformedSplitMap<J, K, U, V> org.apache.commons.collections4.splitmap.TransformedSplitMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super J, ? extends K>,org.apache.commons.collections4.Transformer<? super U, ? extends V>)"""
        return TransformedSplitMap.__wrap(__TransformedSplitMap.transformingMap(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractIterableGetMapDecorator, self).get(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractIterableGetMapDecorator, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.size()"""
        return int.__wrap(super(AbstractIterableGetMapDecorator, self).size())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractIterableGetMapDecorator, self).isEmpty())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.splitmap.TransformedSplitMap.putAll(java.util.Map<? extends J, ? extends U>)"""
        super(__TransformedSplitMap, self).putAll(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractIterableGetMapDecorator, self).hashCode())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.splitmap.TransformedSplitMap.put(J,U)"""
        return object.__wrap(super(__TransformedSplitMap, self).put(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.splitmap.TransformedSplitMap.clear()"""
        super(TransformedSplitMap, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractIterableGetMapDecorator, self).equals(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableGetMapDecorator, self).mapIterator())