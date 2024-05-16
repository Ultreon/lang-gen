from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.google.common.cache.ForwardingLoadingCache as _ForwardingLoadingCache_SimpleForwardingLoadingCache
_SimpleForwardingLoadingCache = _ForwardingLoadingCache_SimpleForwardingLoadingCache.SimpleForwardingLoadingCache
import com.google.common.cache.ForwardingLoadingCache as _ForwardingLoadingCache
_ForwardingLoadingCache = _ForwardingLoadingCache
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.concurrent.ConcurrentMap as ConcurrentMap
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.cache.ForwardingCache as _ForwardingCache
_ForwardingCache = _ForwardingCache
import java.lang.Integer as _int
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleForwardingLoadingCache():
    """com.google.common.cache.ForwardingLoadingCache.SimpleForwardingLoadingCache"""
 
    @staticmethod
    def _wrap(java_value: _SimpleForwardingLoadingCache) -> 'SimpleForwardingLoadingCache':
        return SimpleForwardingLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleForwardingLoadingCache):
        """
        Dynamic initializer for SimpleForwardingLoadingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleForwardingLoadingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleForwardingLoadingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.getUnchecked(K)"""
        return object._wrap(super(_ForwardingLoadingCache, self).getUnchecked(key))

    @overload
    def apply(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.apply(K)"""
        return object._wrap(super(_ForwardingLoadingCache, self).apply(key))

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(ForwardingCache, self).asMap())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'._wrap(super(ForwardingCache, self).stats())

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingLoadingCache, self).getAll(keys))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(_ForwardingCache, self).put(key, value)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.ForwardingLoadingCache.refresh(K)"""
        super(_ForwardingLoadingCache, self).refresh(key)

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_ForwardingCache, self).putAll(m)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int._wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_ForwardingCache, self).invalidateAll(keys)

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingLoadingCache, self).get(key))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(_ForwardingCache, self).invalidate(key)

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object._wrap(super(_ForwardingCache, self).getIfPresent(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingCache, self).get(key, valueLoader))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.cache.ForwardingLoadingCache$SimpleForwardingLoadingCache
from pyquantum_helper import import_once as _import_once
import com.google.common.cache.ForwardingLoadingCache as _ForwardingLoadingCache_SimpleForwardingLoadingCache
_SimpleForwardingLoadingCache = _ForwardingLoadingCache_SimpleForwardingLoadingCache.SimpleForwardingLoadingCache
import com.google.common.cache.ForwardingLoadingCache as _ForwardingLoadingCache
_ForwardingLoadingCache = _ForwardingLoadingCache
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.concurrent.ConcurrentMap as ConcurrentMap
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.cache.ForwardingCache as _ForwardingCache
_ForwardingCache = _ForwardingCache
import java.lang.Integer as _int
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleForwardingLoadingCache():
    """com.google.common.cache.ForwardingLoadingCache.SimpleForwardingLoadingCache"""
 
    @staticmethod
    def _wrap(java_value: _SimpleForwardingLoadingCache) -> 'SimpleForwardingLoadingCache':
        return SimpleForwardingLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleForwardingLoadingCache):
        """
        Dynamic initializer for SimpleForwardingLoadingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleForwardingLoadingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleForwardingLoadingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.getUnchecked(K)"""
        return object._wrap(super(_ForwardingLoadingCache, self).getUnchecked(key))

    @overload
    def apply(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.apply(K)"""
        return object._wrap(super(_ForwardingLoadingCache, self).apply(key))

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(ForwardingCache, self).asMap())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'._wrap(super(ForwardingCache, self).stats())

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingLoadingCache, self).getAll(keys))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(_ForwardingCache, self).put(key, value)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.ForwardingLoadingCache.refresh(K)"""
        super(_ForwardingLoadingCache, self).refresh(key)

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_ForwardingCache, self).putAll(m)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int._wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_ForwardingCache, self).invalidateAll(keys)

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingLoadingCache, self).get(key))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(_ForwardingCache, self).invalidate(key)

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object._wrap(super(_ForwardingCache, self).getIfPresent(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingCache, self).get(key, valueLoader))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.cache.ForwardingLoadingCache$SimpleForwardingLoadingCache 
 
 
# CLASS: com.google.common.cache.ForwardingCache
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.cache.ForwardingCache as _ForwardingCache
_ForwardingCache = _ForwardingCache
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Integer as _int
import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.Callable as Callable
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForwardingCache():
    """com.google.common.cache.ForwardingCache"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingCache) -> 'ForwardingCache':
        return ForwardingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingCache):
        """
        Dynamic initializer for ForwardingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int._wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(ForwardingCache, self).asMap())

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_ForwardingCache, self).invalidateAll(keys)

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
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'._wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(_ForwardingCache, self).invalidate(key)

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(_ForwardingCache, self).put(key, value)

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object._wrap(super(_ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_ForwardingCache, self).putAll(m)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.LoadingCache
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.cache.Cache as _Cache
_Cache = _Cache
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Iterable as Iterable
import java.util.concurrent.Callable as Callable
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.Map as Map
import com.google.common.cache.LoadingCache as _LoadingCache
_LoadingCache = _LoadingCache
 
class LoadingCache():
    """com.google.common.cache.LoadingCache"""
 
    @staticmethod
    def _wrap(java_value: _LoadingCache) -> 'LoadingCache':
        return LoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadingCache):
        """
        Dynamic initializer for LoadingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invalidate(self, key: object):
        """public abstract void com.google.common.cache.Cache.invalidate(java.lang.Object)"""
        pass

    @abstractmethod
    def invalidateAll(self, keys: 'Iterable'):
        """public abstract void com.google.common.cache.Cache.invalidateAll(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @abstractmethod
    def refresh(self, key: object):
        """public abstract void com.google.common.cache.LoadingCache.refresh(K)"""
        pass

    @abstractmethod
    def cleanUp(self, ):
        """public abstract void com.google.common.cache.Cache.cleanUp()"""
        pass

    @abstractmethod
    def putAll(self, m: 'Map'):
        """public abstract void com.google.common.cache.Cache.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.LoadingCache.asMap()"""
        pass

    @abstractmethod
    def getUnchecked(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.getUnchecked(K)"""
        pass

    @abstractmethod
    def apply(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.apply(K)"""
        pass

    @abstractmethod
    def invalidateAll(self, ):
        """public abstract void com.google.common.cache.Cache.invalidateAll()"""
        pass

    @abstractmethod
    def getAllPresent(self, keys: 'Iterable'):
        """public abstract com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.Cache.getAllPresent(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def getAll(self, keys: 'Iterable'):
        """public abstract com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.LoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def stats(self, ):
        """public abstract com.google.common.cache.CacheStats com.google.common.cache.Cache.stats()"""
        pass

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @abstractmethod
    def get(self, key: object, loader: 'Callable'):
        """public abstract V com.google.common.cache.Cache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def get(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def put(self, key: object, value: object):
        """public abstract void com.google.common.cache.Cache.put(K,V)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract long com.google.common.cache.Cache.size()"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Function.equals(java.lang.Object)"""
        pass 
 
 
# CLASS: com.google.common.cache.CacheLoader$InvalidCacheLoadException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import com.google.common.cache.CacheLoader as _CacheLoader_InvalidCacheLoadException
_InvalidCacheLoadException = _CacheLoader_InvalidCacheLoadException.InvalidCacheLoadException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidCacheLoadException():
    """com.google.common.cache.CacheLoader.InvalidCacheLoadException"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCacheLoadException) -> 'InvalidCacheLoadException':
        return InvalidCacheLoadException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCacheLoadException):
        """
        Dynamic initializer for InvalidCacheLoadException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCacheLoadException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCacheLoadException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, message: str):
        """public com.google.common.cache.CacheLoader$InvalidCacheLoadException(java.lang.String)"""
        val = _InvalidCacheLoadException(message)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.ForwardingCache$SimpleForwardingCache
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.cache.ForwardingCache as _ForwardingCache
_ForwardingCache = _ForwardingCache
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Integer as _int
import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import com.google.common.cache.ForwardingCache as _ForwardingCache_SimpleForwardingCache
_SimpleForwardingCache = _ForwardingCache_SimpleForwardingCache.SimpleForwardingCache
import java.util.concurrent.Callable as Callable
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleForwardingCache():
    """com.google.common.cache.ForwardingCache.SimpleForwardingCache"""
 
    @staticmethod
    def _wrap(java_value: _SimpleForwardingCache) -> 'SimpleForwardingCache':
        return SimpleForwardingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleForwardingCache):
        """
        Dynamic initializer for SimpleForwardingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleForwardingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleForwardingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int._wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(ForwardingCache, self).asMap())

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_ForwardingCache, self).invalidateAll(keys)

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
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'._wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(_ForwardingCache, self).invalidate(key)

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(_ForwardingCache, self).put(key, value)

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object._wrap(super(_ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_ForwardingCache, self).putAll(m)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.Weigher
import com.google.common.cache.Weigher as _Weigher
_Weigher = _Weigher
from abc import abstractmethod, ABC
 
class Weigher():
    """com.google.common.cache.Weigher"""
 
    @staticmethod
    def _wrap(java_value: _Weigher) -> 'Weigher':
        return Weigher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Weigher):
        """
        Dynamic initializer for Weigher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Weigher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Weigher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def weigh(self, key: object, value: object):
        """public abstract int com.google.common.cache.Weigher.weigh(K,V)"""
        pass 
 
 
# CLASS: com.google.common.cache.CacheBuilder
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.CacheBuilder as _CacheBuilder
_CacheBuilder = _CacheBuilder
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.cache.Cache as _Cache
_Cache = _Cache
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
import com.google.common.cache.LoadingCache as _LoadingCache
_LoadingCache = _LoadingCache
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CacheBuilder():
    """com.google.common.cache.CacheBuilder"""
 
    @staticmethod
    def _wrap(java_value: _CacheBuilder) -> 'CacheBuilder':
        return CacheBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CacheBuilder):
        """
        Dynamic initializer for CacheBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CacheBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CacheBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def maximumSize(self, maximumSize: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.maximumSize(long)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).maximumSize(_long.valueOf(maximumSize)))

    @overload
    def weakValues(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.weakValues()"""
        return 'CacheBuilder'._wrap(super(CacheBuilder, self).weakValues())

    @overload
    def weigher(self, weigher: 'Weigher') -> 'CacheBuilder':
        """public <K1 extends K,V1 extends V> com.google.common.cache.CacheBuilder<K1, V1> com.google.common.cache.CacheBuilder.weigher(com.google.common.cache.Weigher<? super K1, ? super V1>)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).weigher(weigher))

    @overload
    def initialCapacity(self, initialCapacity: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.initialCapacity(int)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).initialCapacity(_int.valueOf(initialCapacity)))

    @overload
    def build(self, loader: 'CacheLoader') -> 'LoadingCache':
        """public <K1 extends K,V1 extends V> com.google.common.cache.LoadingCache<K1, V1> com.google.common.cache.CacheBuilder.build(com.google.common.cache.CacheLoader<? super K1, V1>)"""
        return 'LoadingCache'._wrap(super(_CacheBuilder, self).build(loader))

    @overload
    def build(self) -> 'Cache':
        """public <K1 extends K,V1 extends V> com.google.common.cache.Cache<K1, V1> com.google.common.cache.CacheBuilder.build()"""
        return 'Cache'._wrap(super(CacheBuilder, self).build())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def from(spec: str) -> 'CacheBuilder':
        """public static com.google.common.cache.CacheBuilder<java.lang.Object, java.lang.Object> com.google.common.cache.CacheBuilder.from(java.lang.String)"""
        return CacheBuilder._wrap(_CacheBuilder.from(spec))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheBuilder.toString()"""
        return str._wrap(super(CacheBuilder, self).toString())

    @overload
    def expireAfterAccess(self, duration: int, unit: 'TimeUnit') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterAccess(long,java.util.concurrent.TimeUnit)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).expireAfterAccess(_long.valueOf(duration), unit))

    @overload
    def refreshAfterWrite(self, duration: 'Duration') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.refreshAfterWrite(java.time.Duration)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).refreshAfterWrite(duration))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def softValues(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.softValues()"""
        return 'CacheBuilder'._wrap(super(CacheBuilder, self).softValues())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def from(spec: 'CacheBuilderSpec') -> 'CacheBuilder':
        """public static com.google.common.cache.CacheBuilder<java.lang.Object, java.lang.Object> com.google.common.cache.CacheBuilder.from(com.google.common.cache.CacheBuilderSpec)"""
        return CacheBuilder._wrap(_CacheBuilder.from(spec))

    @overload
    def expireAfterWrite(self, duration: 'Duration') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterWrite(java.time.Duration)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).expireAfterWrite(duration))

    @overload
    def maximumWeight(self, maximumWeight: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.maximumWeight(long)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).maximumWeight(_long.valueOf(maximumWeight)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def refreshAfterWrite(self, duration: int, unit: 'TimeUnit') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.refreshAfterWrite(long,java.util.concurrent.TimeUnit)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).refreshAfterWrite(_long.valueOf(duration), unit))

    @overload
    def recordStats(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.recordStats()"""
        return 'CacheBuilder'._wrap(super(CacheBuilder, self).recordStats())

    @overload
    def expireAfterWrite(self, duration: int, unit: 'TimeUnit') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterWrite(long,java.util.concurrent.TimeUnit)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).expireAfterWrite(_long.valueOf(duration), unit))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def concurrencyLevel(self, concurrencyLevel: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.concurrencyLevel(int)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).concurrencyLevel(_int.valueOf(concurrencyLevel)))

    @overload
    def removalListener(self, listener: 'RemovalListener') -> 'CacheBuilder':
        """public <K1 extends K,V1 extends V> com.google.common.cache.CacheBuilder<K1, V1> com.google.common.cache.CacheBuilder.removalListener(com.google.common.cache.RemovalListener<? super K1, ? super V1>)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).removalListener(listener))

    @staticmethod
    @overload
    def newBuilder() -> 'CacheBuilder':
        """public static com.google.common.cache.CacheBuilder<java.lang.Object, java.lang.Object> com.google.common.cache.CacheBuilder.newBuilder()"""
        return CacheBuilder._wrap(_CacheBuilder.newBuilder())

    @overload
    def ticker(self, ticker: 'Ticker') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.ticker(com.google.common.base.Ticker)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).ticker(ticker))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def weakKeys(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.weakKeys()"""
        return 'CacheBuilder'._wrap(super(CacheBuilder, self).weakKeys())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def expireAfterAccess(self, duration: 'Duration') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterAccess(java.time.Duration)"""
        return 'CacheBuilder'._wrap(super(_CacheBuilder, self).expireAfterAccess(duration))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.Cache
import com.google.common.cache.Cache as _Cache
_Cache = _Cache
import java.lang.Iterable as Iterable
import java.util.concurrent.Callable as Callable
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class Cache():
    """com.google.common.cache.Cache"""
 
    @staticmethod
    def _wrap(java_value: _Cache) -> 'Cache':
        return Cache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cache):
        """
        Dynamic initializer for Cache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invalidate(self, key: object):
        """public abstract void com.google.common.cache.Cache.invalidate(java.lang.Object)"""
        pass

    @abstractmethod
    def stats(self, ):
        """public abstract com.google.common.cache.CacheStats com.google.common.cache.Cache.stats()"""
        pass

    @abstractmethod
    def invalidateAll(self, keys: 'Iterable'):
        """public abstract void com.google.common.cache.Cache.invalidateAll(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @abstractmethod
    def get(self, key: object, loader: 'Callable'):
        """public abstract V com.google.common.cache.Cache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.Cache.asMap()"""
        pass

    @abstractmethod
    def cleanUp(self, ):
        """public abstract void com.google.common.cache.Cache.cleanUp()"""
        pass

    @abstractmethod
    def putAll(self, m: 'Map'):
        """public abstract void com.google.common.cache.Cache.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def invalidateAll(self, ):
        """public abstract void com.google.common.cache.Cache.invalidateAll()"""
        pass

    @abstractmethod
    def put(self, key: object, value: object):
        """public abstract void com.google.common.cache.Cache.put(K,V)"""
        pass

    @abstractmethod
    def getAllPresent(self, keys: 'Iterable'):
        """public abstract com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.Cache.getAllPresent(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract long com.google.common.cache.Cache.size()"""
        pass 
 
 
# CLASS: com.google.common.cache.RemovalListeners
import com.google.common.cache.RemovalListeners as _RemovalListeners
_RemovalListeners = _RemovalListeners
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.RemovalListener as _RemovalListener
_RemovalListener = _RemovalListener
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemovalListeners():
    """com.google.common.cache.RemovalListeners"""
 
    @staticmethod
    def _wrap(java_value: _RemovalListeners) -> 'RemovalListeners':
        return RemovalListeners(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemovalListeners):
        """
        Dynamic initializer for RemovalListeners.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemovalListeners__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemovalListeners__wrapper":
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

    @staticmethod
    @overload
    def asynchronous(listener: 'RemovalListener', executor: 'Executor') -> 'RemovalListener':
        """public static <K,V> com.google.common.cache.RemovalListener<K, V> com.google.common.cache.RemovalListeners.asynchronous(com.google.common.cache.RemovalListener<K, V>,java.util.concurrent.Executor)"""
        return RemovalListener._wrap(_RemovalListeners.asynchronous(listener, executor))

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
 
 
# CLASS: com.google.common.cache.CacheLoader$UnsupportedLoadingOperationException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import com.google.common.cache.CacheLoader as _CacheLoader_UnsupportedLoadingOperationException
_UnsupportedLoadingOperationException = _CacheLoader_UnsupportedLoadingOperationException.UnsupportedLoadingOperationException
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsupportedLoadingOperationException():
    """com.google.common.cache.CacheLoader.UnsupportedLoadingOperationException"""
 
    @staticmethod
    def _wrap(java_value: _UnsupportedLoadingOperationException) -> 'UnsupportedLoadingOperationException':
        return UnsupportedLoadingOperationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsupportedLoadingOperationException):
        """
        Dynamic initializer for UnsupportedLoadingOperationException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsupportedLoadingOperationException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsupportedLoadingOperationException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.CacheBuilderSpec
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.cache.CacheBuilderSpec as _CacheBuilderSpec
_CacheBuilderSpec = _CacheBuilderSpec
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CacheBuilderSpec():
    """com.google.common.cache.CacheBuilderSpec"""
 
    @staticmethod
    def _wrap(java_value: _CacheBuilderSpec) -> 'CacheBuilderSpec':
        return CacheBuilderSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CacheBuilderSpec):
        """
        Dynamic initializer for CacheBuilderSpec.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CacheBuilderSpec__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CacheBuilderSpec__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.cache.CacheBuilderSpec.equals(java.lang.Object)"""
        return bool._wrap(super(_CacheBuilderSpec, self).equals(obj))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.cache.CacheBuilderSpec.hashCode()"""
        return int._wrap(super(CacheBuilderSpec, self).hashCode())

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

    @staticmethod
    @overload
    def parse(cacheBuilderSpecification: str) -> 'CacheBuilderSpec':
        """public static com.google.common.cache.CacheBuilderSpec com.google.common.cache.CacheBuilderSpec.parse(java.lang.String)"""
        return CacheBuilderSpec._wrap(_CacheBuilderSpec.parse(cacheBuilderSpecification))

    @overload
    def toParsableString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheBuilderSpec.toParsableString()"""
        return str._wrap(super(CacheBuilderSpec, self).toParsableString())

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
    def disableCaching() -> 'CacheBuilderSpec':
        """public static com.google.common.cache.CacheBuilderSpec com.google.common.cache.CacheBuilderSpec.disableCaching()"""
        return CacheBuilderSpec._wrap(_CacheBuilderSpec.disableCaching())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheBuilderSpec.toString()"""
        return str._wrap(super(CacheBuilderSpec, self).toString()) 
 
 
# CLASS: com.google.common.cache.AbstractCache$StatsCounter
import com.google.common.cache.AbstractCache as _AbstractCache_StatsCounter
_StatsCounter = _AbstractCache_StatsCounter.StatsCounter
from abc import abstractmethod, ABC
 
class StatsCounter():
    """com.google.common.cache.AbstractCache.StatsCounter"""
 
    @staticmethod
    def _wrap(java_value: _StatsCounter) -> 'StatsCounter':
        return StatsCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StatsCounter):
        """
        Dynamic initializer for StatsCounter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StatsCounter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StatsCounter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def recordLoadException(self, loadTime: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordLoadException(long)"""
        pass

    @abstractmethod
    def recordLoadSuccess(self, loadTime: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordLoadSuccess(long)"""
        pass

    @abstractmethod
    def recordEviction(self, ):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordEviction()"""
        pass

    @abstractmethod
    def recordHits(self, count: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordHits(int)"""
        pass

    @abstractmethod
    def snapshot(self, ):
        """public abstract com.google.common.cache.CacheStats com.google.common.cache.AbstractCache$StatsCounter.snapshot()"""
        pass

    @abstractmethod
    def recordMisses(self, count: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordMisses(int)"""
        pass 
 
 
# CLASS: com.google.common.cache.AbstractCache
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.cache.Cache as _Cache
_Cache = _Cache
import java.lang.Integer as _int
import com.google.common.cache.AbstractCache as _AbstractCache
_AbstractCache = _AbstractCache
import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.Callable as Callable
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractCache():
    """com.google.common.cache.AbstractCache"""
 
    @staticmethod
    def _wrap(java_value: _AbstractCache) -> 'AbstractCache':
        return AbstractCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractCache):
        """
        Dynamic initializer for AbstractCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.AbstractCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractCache, self).putAll(m)

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.AbstractCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_AbstractCache, self).getAllPresent(keys))

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.AbstractCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_AbstractCache, self).get(key, valueLoader))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.AbstractCache.invalidateAll()"""
        super(AbstractCache, self).invalidateAll()

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
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.AbstractCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_AbstractCache, self).invalidateAll(keys)

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.AbstractCache.stats()"""
        return 'CacheStats'._wrap(super(AbstractCache, self).stats())

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
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.AbstractCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(AbstractCache, self).asMap())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.AbstractCache.invalidate(java.lang.Object)"""
        super(_AbstractCache, self).invalidate(key)

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
    def size(self) -> int:
        """public long com.google.common.cache.AbstractCache.size()"""
        return int._wrap(super(AbstractCache, self).size())

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.AbstractCache.put(K,V)"""
        super(_AbstractCache, self).put(key, value)

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.AbstractCache.cleanUp()"""
        super(AbstractCache, self).cleanUp()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.RemovalListener
import com.google.common.cache.RemovalListener as _RemovalListener
_RemovalListener = _RemovalListener
from abc import abstractmethod, ABC
 
class RemovalListener():
    """com.google.common.cache.RemovalListener"""
 
    @staticmethod
    def _wrap(java_value: _RemovalListener) -> 'RemovalListener':
        return RemovalListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemovalListener):
        """
        Dynamic initializer for RemovalListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemovalListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemovalListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRemoval(self, notification: 'RemovalNotification'):
        """public abstract void com.google.common.cache.RemovalListener.onRemoval(com.google.common.cache.RemovalNotification<K, V>)"""
        pass 
 
 
# CLASS: com.google.common.cache.CacheStats
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CacheStats():
    """com.google.common.cache.CacheStats"""
 
    @staticmethod
    def _wrap(java_value: _CacheStats) -> 'CacheStats':
        return CacheStats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CacheStats):
        """
        Dynamic initializer for CacheStats.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CacheStats__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CacheStats__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def evictionCount(self) -> int:
        """public long com.google.common.cache.CacheStats.evictionCount()"""
        return int._wrap(super(CacheStats, self).evictionCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheStats.toString()"""
        return str._wrap(super(CacheStats, self).toString())

    @overload
    def loadSuccessCount(self) -> int:
        """public long com.google.common.cache.CacheStats.loadSuccessCount()"""
        return int._wrap(super(CacheStats, self).loadSuccessCount())

    @overload
    def minus(self, other: 'CacheStats') -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.CacheStats.minus(com.google.common.cache.CacheStats)"""
        return 'CacheStats'._wrap(super(_CacheStats, self).minus(other))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def hitCount(self) -> int:
        """public long com.google.common.cache.CacheStats.hitCount()"""
        return int._wrap(super(CacheStats, self).hitCount())

    @overload
    def missRate(self) -> float:
        """public double com.google.common.cache.CacheStats.missRate()"""
        return float._wrap(super(CacheStats, self).missRate())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.cache.CacheStats.hashCode()"""
        return int._wrap(super(CacheStats, self).hashCode())

    @overload
    def averageLoadPenalty(self) -> float:
        """public double com.google.common.cache.CacheStats.averageLoadPenalty()"""
        return float._wrap(super(CacheStats, self).averageLoadPenalty())

    @overload
    def hitRate(self) -> float:
        """public double com.google.common.cache.CacheStats.hitRate()"""
        return float._wrap(super(CacheStats, self).hitRate())

    @overload
    def __init__(self, hitCount: int, missCount: int, loadSuccessCount: int, loadExceptionCount: int, totalLoadTime: int, evictionCount: int):
        """public com.google.common.cache.CacheStats(long,long,long,long,long,long)"""
        val = _CacheStats(_long.valueOf(hitCount), _long.valueOf(missCount), _long.valueOf(loadSuccessCount), _long.valueOf(loadExceptionCount), _long.valueOf(totalLoadTime), _long.valueOf(evictionCount))
        self.__wrapper = val

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.cache.CacheStats.equals(java.lang.Object)"""
        return bool._wrap(super(_CacheStats, self).equals(object))

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
    def totalLoadTime(self) -> int:
        """public long com.google.common.cache.CacheStats.totalLoadTime()"""
        return int._wrap(super(CacheStats, self).totalLoadTime())

    @overload
    def plus(self, other: 'CacheStats') -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.CacheStats.plus(com.google.common.cache.CacheStats)"""
        return 'CacheStats'._wrap(super(_CacheStats, self).plus(other))

    @overload
    def loadCount(self) -> int:
        """public long com.google.common.cache.CacheStats.loadCount()"""
        return int._wrap(super(CacheStats, self).loadCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def loadExceptionRate(self) -> float:
        """public double com.google.common.cache.CacheStats.loadExceptionRate()"""
        return float._wrap(super(CacheStats, self).loadExceptionRate())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def missCount(self) -> int:
        """public long com.google.common.cache.CacheStats.missCount()"""
        return int._wrap(super(CacheStats, self).missCount())

    @overload
    def requestCount(self) -> int:
        """public long com.google.common.cache.CacheStats.requestCount()"""
        return int._wrap(super(CacheStats, self).requestCount())

    @overload
    def loadExceptionCount(self) -> int:
        """public long com.google.common.cache.CacheStats.loadExceptionCount()"""
        return int._wrap(super(CacheStats, self).loadExceptionCount()) 
 
 
# CLASS: com.google.common.cache.AbstractCache$SimpleStatsCounter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import java.lang.String as _String
_String = _String
import com.google.common.cache.AbstractCache as _AbstractCache_SimpleStatsCounter
_SimpleStatsCounter = _AbstractCache_SimpleStatsCounter.SimpleStatsCounter
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleStatsCounter():
    """com.google.common.cache.AbstractCache.SimpleStatsCounter"""
 
    @staticmethod
    def _wrap(java_value: _SimpleStatsCounter) -> 'SimpleStatsCounter':
        return SimpleStatsCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleStatsCounter):
        """
        Dynamic initializer for SimpleStatsCounter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleStatsCounter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleStatsCounter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def recordLoadException(self, loadTime: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordLoadException(long)"""
        super(_SimpleStatsCounter, self).recordLoadException(_long.valueOf(loadTime))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def recordLoadSuccess(self, loadTime: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordLoadSuccess(long)"""
        super(_SimpleStatsCounter, self).recordLoadSuccess(_long.valueOf(loadTime))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def recordHits(self, count: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordHits(int)"""
        super(_SimpleStatsCounter, self).recordHits(_int.valueOf(count))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def recordMisses(self, count: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordMisses(int)"""
        super(_SimpleStatsCounter, self).recordMisses(_int.valueOf(count))

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
    def __init__(self):
        """public com.google.common.cache.AbstractCache$SimpleStatsCounter()"""
        val = _SimpleStatsCounter()
        self.__wrapper = val

    @overload
    def incrementBy(self, other: 'StatsCounter'):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.incrementBy(com.google.common.cache.AbstractCache$StatsCounter)"""
        super(_SimpleStatsCounter, self).incrementBy(other)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.common.cache.AbstractCache$SimpleStatsCounter()"""
        val = _SimpleStatsCounter()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def snapshot(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.AbstractCache$SimpleStatsCounter.snapshot()"""
        return 'CacheStats'._wrap(super(SimpleStatsCounter, self).snapshot())

    @override
    @overload
    def recordEviction(self):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordEviction()"""
        super(SimpleStatsCounter, self).recordEviction()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.RemovalCause
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.RemovalCause as _RemovalCause
_RemovalCause = _RemovalCause
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemovalCause():
    """com.google.common.cache.RemovalCause"""
 
    @staticmethod
    def _wrap(java_value: _RemovalCause) -> 'RemovalCause':
        return RemovalCause(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemovalCause):
        """
        Dynamic initializer for RemovalCause.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemovalCause__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemovalCause__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(name: str) -> 'RemovalCause':
        """public static com.google.common.cache.RemovalCause com.google.common.cache.RemovalCause.valueOf(java.lang.String)"""
        return RemovalCause._wrap(_RemovalCause.valueOf(name))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['RemovalCause']:
        """public static com.google.common.cache.RemovalCause[] com.google.common.cache.RemovalCause.values()"""
        return List[RemovalCause]._wrap(_RemovalCause.values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.cache.CacheLoader
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
try:
    from pygcommon.util import concurrent
except ImportError:
    concurrent = _import_once("pygcommon.util.concurrent")

import java.lang.Iterable as Iterable
import java.util.concurrent.Executor as Executor
import com.google.common.cache.CacheLoader as _CacheLoader
_CacheLoader = _CacheLoader
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CacheLoader():
    """com.google.common.cache.CacheLoader"""
 
    @staticmethod
    def _wrap(java_value: _CacheLoader) -> 'CacheLoader':
        return CacheLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CacheLoader):
        """
        Dynamic initializer for CacheLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CacheLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CacheLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def from(supplier: 'Supplier') -> 'CacheLoader':
        """public static <V> com.google.common.cache.CacheLoader<java.lang.Object, V> com.google.common.cache.CacheLoader.from(com.google.common.base.Supplier<V>)"""
        return CacheLoader._wrap(_CacheLoader.from(supplier))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def reload(self, key: object, oldValue: object) -> 'concurrent.ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<V> com.google.common.cache.CacheLoader.reload(K,V) throws java.lang.Exception"""
        return 'concurrent.ListenableFuture'._wrap(super(_CacheLoader, self).reload(key, oldValue))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def load(self, key: object):
        """public abstract V com.google.common.cache.CacheLoader.load(K) throws java.lang.Exception"""
        pass

    @staticmethod
    @overload
    def from(function: 'Function') -> 'CacheLoader':
        """public static <K,V> com.google.common.cache.CacheLoader<K, V> com.google.common.cache.CacheLoader.from(com.google.common.base.Function<K, V>)"""
        return CacheLoader._wrap(_CacheLoader.from(function))

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
    def loadAll(self, keys: 'Iterable') -> 'Map':
        """public java.util.Map<K, V> com.google.common.cache.CacheLoader.loadAll(java.lang.Iterable<? extends K>) throws java.lang.Exception"""
        return 'Map'._wrap(super(_CacheLoader, self).loadAll(keys))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def asyncReloading(loader: 'CacheLoader', executor: 'Executor') -> 'CacheLoader':
        """public static <K,V> com.google.common.cache.CacheLoader<K, V> com.google.common.cache.CacheLoader.asyncReloading(com.google.common.cache.CacheLoader<K, V>,java.util.concurrent.Executor)"""
        return CacheLoader._wrap(_CacheLoader.asyncReloading(loader, executor))

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
 
 
# CLASS: com.google.common.cache.AbstractLoadingCache
from pyquantum_helper import import_once as _import_once
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
from abc import abstractmethod, ABC
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.cache.Cache as _Cache
_Cache = _Cache
import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.Callable as Callable
from builtins import bool
import com.google.common.cache.LoadingCache as _LoadingCache
_LoadingCache = _LoadingCache
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.cache.AbstractCache as _AbstractCache
_AbstractCache = _AbstractCache
import com.google.common.cache.AbstractLoadingCache as _AbstractLoadingCache
_AbstractLoadingCache = _AbstractLoadingCache
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractLoadingCache():
    """com.google.common.cache.AbstractLoadingCache"""
 
    @staticmethod
    def _wrap(java_value: _AbstractLoadingCache) -> 'AbstractLoadingCache':
        return AbstractLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractLoadingCache):
        """
        Dynamic initializer for AbstractLoadingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractLoadingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractLoadingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.AbstractCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_AbstractCache, self).getAllPresent(keys))

    @overload
    def apply(self, key: object) -> object:
        """public final V com.google.common.cache.AbstractLoadingCache.apply(K)"""
        return object._wrap(super(_AbstractLoadingCache, self).apply(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.AbstractCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_AbstractCache, self).get(key, valueLoader))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.AbstractCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_AbstractCache, self).invalidateAll(keys)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.AbstractCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(AbstractCache, self).asMap())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.AbstractCache.invalidate(java.lang.Object)"""
        super(_AbstractCache, self).invalidate(key)

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.AbstractLoadingCache.refresh(K)"""
        super(_AbstractLoadingCache, self).refresh(key)

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.AbstractLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'._wrap(super(_AbstractLoadingCache, self).getAll(keys))

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.AbstractCache.size()"""
        return int._wrap(super(AbstractCache, self).size())

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.AbstractCache.put(K,V)"""
        super(_AbstractCache, self).put(key, value)

    @abstractmethod
    def get(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        pass

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.AbstractCache.cleanUp()"""
        super(AbstractCache, self).cleanUp()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.AbstractCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractCache, self).putAll(m)

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.AbstractCache.invalidateAll()"""
        super(AbstractCache, self).invalidateAll()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.AbstractLoadingCache.getUnchecked(K)"""
        return object._wrap(super(_AbstractLoadingCache, self).getUnchecked(key))

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.AbstractCache.stats()"""
        return 'CacheStats'._wrap(super(AbstractCache, self).stats())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.RemovalNotification
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.cache.RemovalCause as _RemovalCause
_RemovalCause = _RemovalCause
import java.lang.String as _String
_String = _String
from builtins import object
import com.google.common.cache.RemovalNotification as _RemovalNotification
_RemovalNotification = _RemovalNotification
import java.lang.Integer as _int
import java.util.AbstractMap as _AbstractMap_SimpleImmutableEntry
_SimpleImmutableEntry = _AbstractMap_SimpleImmutableEntry.SimpleImmutableEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemovalNotification():
    """com.google.common.cache.RemovalNotification"""
 
    @staticmethod
    def _wrap(java_value: _RemovalNotification) -> 'RemovalNotification':
        return RemovalNotification(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemovalNotification):
        """
        Dynamic initializer for RemovalNotification.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemovalNotification__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemovalNotification__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap$SimpleImmutableEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).equals(arg0))

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
        """public K java.util.AbstractMap$SimpleImmutableEntry.getKey()"""
        return object._wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).getKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap$SimpleImmutableEntry.hashCode()"""
        return int._wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).hashCode())

    @overload
    def wasEvicted(self) -> bool:
        """public boolean com.google.common.cache.RemovalNotification.wasEvicted()"""
        return bool._wrap(super(RemovalNotification, self).wasEvicted())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V java.util.AbstractMap$SimpleImmutableEntry.setValue(V)"""
        return object._wrap(super(_SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).setValue(arg0))

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

    @staticmethod
    @overload
    def create(key: object, value: object, cause: 'RemovalCause') -> 'RemovalNotification':
        """public static <K,V> com.google.common.cache.RemovalNotification<K, V> com.google.common.cache.RemovalNotification.create(K,V,com.google.common.cache.RemovalCause)"""
        return RemovalNotification._wrap(_RemovalNotification.create(key, value, cause))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractMap$SimpleImmutableEntry.toString()"""
        return str._wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).toString())

    @overload
    def getCause(self) -> 'RemovalCause':
        """public com.google.common.cache.RemovalCause com.google.common.cache.RemovalNotification.getCause()"""
        return 'RemovalCause'._wrap(super(RemovalNotification, self).getCause())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> object:
        """public V java.util.AbstractMap$SimpleImmutableEntry.getValue()"""
        return object._wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).getValue()) 
 
 
# CLASS: com.google.common.cache.ForwardingLoadingCache
from pyquantum_helper import import_once as _import_once
import com.google.common.cache.ForwardingLoadingCache as _ForwardingLoadingCache
_ForwardingLoadingCache = _ForwardingLoadingCache
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.concurrent.ConcurrentMap as ConcurrentMap
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.cache.CacheStats as _CacheStats
_CacheStats = _CacheStats
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.cache.ForwardingCache as _ForwardingCache
_ForwardingCache = _ForwardingCache
import java.lang.Integer as _int
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForwardingLoadingCache():
    """com.google.common.cache.ForwardingLoadingCache"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingLoadingCache) -> 'ForwardingLoadingCache':
        return ForwardingLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingLoadingCache):
        """
        Dynamic initializer for ForwardingLoadingCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingLoadingCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingLoadingCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.getUnchecked(K)"""
        return object._wrap(super(_ForwardingLoadingCache, self).getUnchecked(key))

    @overload
    def apply(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.apply(K)"""
        return object._wrap(super(_ForwardingLoadingCache, self).apply(key))

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'._wrap(super(ForwardingCache, self).asMap())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'._wrap(super(ForwardingCache, self).stats())

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingLoadingCache, self).getAll(keys))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(_ForwardingCache, self).put(key, value)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'._wrap(super(_ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.ForwardingLoadingCache.refresh(K)"""
        super(_ForwardingLoadingCache, self).refresh(key)

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_ForwardingCache, self).putAll(m)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int._wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(_ForwardingCache, self).invalidateAll(keys)

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingLoadingCache, self).get(key))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(_ForwardingCache, self).invalidate(key)

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object._wrap(super(_ForwardingCache, self).getIfPresent(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingCache, self).get(key, valueLoader))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())