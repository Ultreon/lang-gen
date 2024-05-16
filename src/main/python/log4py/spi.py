from __future__ import annotations
from overload import overload


 
import org.apache.logging.log4j.spi.LoggerRegistry as __LoggerRegistry_ConcurrentMapFactory
__ConcurrentMapFactory = __LoggerRegistry_ConcurrentMapFactory.ConcurrentMapFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ConcurrentMapFactory(__MapFactory, MapFactory):
    """org.apache.logging.log4j.spi.LoggerRegistry.ConcurrentMapFactory"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentMapFactory) -> 'ConcurrentMapFactory':
        return ConcurrentMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentMapFactory):
        """
        Dynamic initializer for ConcurrentMapFactory.
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
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        super(__ConcurrentMapFactory, self).putIfAbsent(innerMap, name, logger)

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory()"""
        val = __ConcurrentMapFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def createInnerMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.createInnerMap()"""
        return 'Map'.__wrap(super(ConcurrentMapFactory, self).createInnerMap())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory()"""
        val = __ConcurrentMapFactory()
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

    @override
    @overload
    def createOuterMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.createOuterMap()"""
        return 'Map'.__wrap(super(ConcurrentMapFactory, self).createOuterMap())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory
import org.apache.logging.log4j.spi.LoggerRegistry as __LoggerRegistry_ConcurrentMapFactory
__ConcurrentMapFactory = __LoggerRegistry_ConcurrentMapFactory.ConcurrentMapFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ConcurrentMapFactory(__MapFactory, MapFactory):
    """org.apache.logging.log4j.spi.LoggerRegistry.ConcurrentMapFactory"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentMapFactory) -> 'ConcurrentMapFactory':
        return ConcurrentMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentMapFactory):
        """
        Dynamic initializer for ConcurrentMapFactory.
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
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        super(__ConcurrentMapFactory, self).putIfAbsent(innerMap, name, logger)

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory()"""
        val = __ConcurrentMapFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def createInnerMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.createInnerMap()"""
        return 'Map'.__wrap(super(ConcurrentMapFactory, self).createInnerMap())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory()"""
        val = __ConcurrentMapFactory()
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

    @override
    @overload
    def createOuterMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.createOuterMap()"""
        return 'Map'.__wrap(super(ConcurrentMapFactory, self).createOuterMap())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory 
 
 
# CLASS: org.apache.logging.log4j.spi.DefaultThreadContextMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
from builtins import object
import org.apache.logging.log4j.spi.DefaultThreadContextMap as __DefaultThreadContextMap
__DefaultThreadContextMap = __DefaultThreadContextMap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class DefaultThreadContextMap(__ThreadContextMap, ThreadContextMap, log4py.__ReadOnlyStringMap, util.ReadOnlyStringMap):
    """org.apache.logging.log4j.spi.DefaultThreadContextMap"""
 
    @staticmethod
    def __wrap(java_value: __DefaultThreadContextMap) -> 'DefaultThreadContextMap':
        return DefaultThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultThreadContextMap):
        """
        Dynamic initializer for DefaultThreadContextMap.
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
    def putAll(self, m: 'Map'):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(__DefaultThreadContextMap, self).putAll(m)

    @override
    @overload
    def getImmutableMapOrNull(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextMap.getImmutableMapOrNull()"""
        return 'Map'.__wrap(super(DefaultThreadContextMap, self).getImmutableMapOrNull())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextMap.toString()"""
        return str.__wrap(super(DefaultThreadContextMap, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextMap.hashCode()"""
        return int.__wrap(super(DefaultThreadContextMap, self).hashCode())

    @overload
    def getValue(self, key: str) -> object:
        """public <V> V org.apache.logging.log4j.spi.DefaultThreadContextMap.getValue(java.lang.String)"""
        return object.__wrap(super(__DefaultThreadContextMap, self).getValue(key))

    @overload
    def __init__(self, useMap: bool):
        """public org.apache.logging.log4j.spi.DefaultThreadContextMap(boolean)"""
        val = __DefaultThreadContextMap(__boolean.valueOf(useMap))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getCopy(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextMap.getCopy()"""
        return 'Map'.__wrap(super(DefaultThreadContextMap, self).getCopy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def remove(self, key: str):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.remove(java.lang.String)"""
        super(__DefaultThreadContextMap, self).remove(key)

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <V,S> void org.apache.logging.log4j.spi.DefaultThreadContextMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        super(__DefaultThreadContextMap, self).forEach(action, state)

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextMap.containsKey(java.lang.String)"""
        return bool.__wrap(super(__DefaultThreadContextMap, self).containsKey(key))

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__DefaultThreadContextMap, self).equals(obj))

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextMap.toMap()"""
        return 'Map'.__wrap(super(DefaultThreadContextMap, self).toMap())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.DefaultThreadContextMap()"""
        val = __DefaultThreadContextMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <V> void org.apache.logging.log4j.spi.DefaultThreadContextMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        super(__DefaultThreadContextMap, self).forEach(action)

    @override
    @overload
    def put(self, key: str, value: str):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.put(java.lang.String,java.lang.String)"""
        super(__DefaultThreadContextMap, self).put(key, value)

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextMap.get(java.lang.String)"""
        return str.__wrap(super(__DefaultThreadContextMap, self).get(key))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextMap.isEmpty()"""
        return bool.__wrap(super(DefaultThreadContextMap, self).isEmpty())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextMap.size()"""
        return int.__wrap(super(DefaultThreadContextMap, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.clear()"""
        super(DefaultThreadContextMap, self).clear()

    @overload
    def removeAll(self, keys: 'Iterable'):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.removeAll(java.lang.Iterable<java.lang.String>)"""
        super(__DefaultThreadContextMap, self).removeAll(keys)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.DefaultThreadContextMap()"""
        val = __DefaultThreadContextMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.spi.StandardLevel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.spi.StandardLevel as __StandardLevel
__StandardLevel = __StandardLevel
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class StandardLevel(__Enum, Enum):
    """org.apache.logging.log4j.spi.StandardLevel"""
 
    @staticmethod
    def __wrap(java_value: __StandardLevel) -> 'StandardLevel':
        return StandardLevel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StandardLevel):
        """
        Dynamic initializer for StandardLevel.
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
 
    @staticmethod
    @overload
    def values() -> List['StandardLevel']:
        """public static org.apache.logging.log4j.spi.StandardLevel[] org.apache.logging.log4j.spi.StandardLevel.values()"""
        return List[StandardLevel].__wrap(__StandardLevel.values())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def getStandardLevel(intLevel: int) -> 'StandardLevel':
        """public static org.apache.logging.log4j.spi.StandardLevel org.apache.logging.log4j.spi.StandardLevel.getStandardLevel(int)"""
        return StandardLevel.__wrap(__StandardLevel.getStandardLevel(__int.valueOf(intLevel)))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @overload
    def intLevel(self) -> int:
        """public int org.apache.logging.log4j.spi.StandardLevel.intLevel()"""
        return int.__wrap(super(StandardLevel, self).intLevel())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'StandardLevel':
        """public static org.apache.logging.log4j.spi.StandardLevel org.apache.logging.log4j.spi.StandardLevel.valueOf(java.lang.String)"""
        return StandardLevel.__wrap(__StandardLevel.valueOf(name))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: org.apache.logging.log4j.spi.NoOpThreadContextMap
import org.apache.logging.log4j.spi.NoOpThreadContextMap as __NoOpThreadContextMap
__NoOpThreadContextMap = __NoOpThreadContextMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class NoOpThreadContextMap(__ThreadContextMap, ThreadContextMap):
    """org.apache.logging.log4j.spi.NoOpThreadContextMap"""
 
    @staticmethod
    def __wrap(java_value: __NoOpThreadContextMap) -> 'NoOpThreadContextMap':
        return NoOpThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoOpThreadContextMap):
        """
        Dynamic initializer for NoOpThreadContextMap.
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
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.NoOpThreadContextMap.containsKey(java.lang.String)"""
        return bool.__wrap(super(__NoOpThreadContextMap, self).containsKey(key))

    @override
    @overload
    def put(self, key: str, value: str):
        """public void org.apache.logging.log4j.spi.NoOpThreadContextMap.put(java.lang.String,java.lang.String)"""
        super(__NoOpThreadContextMap, self).put(key, value)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self, key: str):
        """public void org.apache.logging.log4j.spi.NoOpThreadContextMap.remove(java.lang.String)"""
        super(__NoOpThreadContextMap, self).remove(key)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.NoOpThreadContextMap()"""
        val = __NoOpThreadContextMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.NoOpThreadContextMap.get(java.lang.String)"""
        return str.__wrap(super(__NoOpThreadContextMap, self).get(key))

    @override
    @overload
    def getImmutableMapOrNull(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.NoOpThreadContextMap.getImmutableMapOrNull()"""
        return 'Map'.__wrap(super(NoOpThreadContextMap, self).getImmutableMapOrNull())

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
    def getCopy(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.NoOpThreadContextMap.getCopy()"""
        return 'Map'.__wrap(super(NoOpThreadContextMap, self).getCopy())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.NoOpThreadContextMap.isEmpty()"""
        return bool.__wrap(super(NoOpThreadContextMap, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.NoOpThreadContextMap.clear()"""
        super(NoOpThreadContextMap, self).clear()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.NoOpThreadContextMap()"""
        val = __NoOpThreadContextMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerAdapter
import java.io.Closeable as __Closeable
__Closeable = __Closeable
import org.apache.logging.log4j.spi.LoggerAdapter as __LoggerAdapter
__LoggerAdapter = __LoggerAdapter
from abc import abstractmethod, ABC
 
class LoggerAdapter(ABC, __Closeable, Closeable):
    """org.apache.logging.log4j.spi.LoggerAdapter"""
 
    @staticmethod
    def __wrap(java_value: __LoggerAdapter) -> 'LoggerAdapter':
        return LoggerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerAdapter):
        """
        Dynamic initializer for LoggerAdapter.
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
 
    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def getLogger(self, name: str):
        """public abstract L org.apache.logging.log4j.spi.LoggerAdapter.getLogger(java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$MapFactory
import org.apache.logging.log4j.spi.LoggerRegistry as __LoggerRegistry_MapFactory
__MapFactory = __LoggerRegistry_MapFactory.MapFactory
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class MapFactory(ABC):
    """org.apache.logging.log4j.spi.LoggerRegistry.MapFactory"""
 
    @staticmethod
    def __wrap(java_value: __MapFactory) -> 'MapFactory':
        return MapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapFactory):
        """
        Dynamic initializer for MapFactory.
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
 
    @abstractmethod
    def createOuterMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$MapFactory.createOuterMap()"""
        pass

    @abstractmethod
    def createInnerMap(self, ):
        """public abstract java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$MapFactory.createInnerMap()"""
        pass

    @abstractmethod
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public abstract void org.apache.logging.log4j.spi.LoggerRegistry$MapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextFactory
import java.lang.Boolean as __boolean
import java.net.URI as URI
import java.lang.String as __string
import java.lang.ClassLoader as ClassLoader
from abc import abstractmethod, ABC
from builtins import bool
import org.apache.logging.log4j.spi.LoggerContextFactory as __LoggerContextFactory
__LoggerContextFactory = __LoggerContextFactory
 
class LoggerContextFactory(ABC):
    """org.apache.logging.log4j.spi.LoggerContextFactory"""
 
    @staticmethod
    def __wrap(java_value: __LoggerContextFactory) -> 'LoggerContextFactory':
        return LoggerContextFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerContextFactory):
        """
        Dynamic initializer for LoggerContextFactory.
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
 
    @abstractmethod
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool, configLocation: 'URI', name: str):
        """public abstract org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.spi.LoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean,java.net.URI,java.lang.String)"""
        pass

    @overload
    def hasContext(self, fqcn: str, loader: 'ClassLoader', currentContext: bool) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContextFactory.hasContext(java.lang.String,java.lang.ClassLoader,boolean)"""
        return bool.__wrap(super(__LoggerContextFactory, self).hasContext(fqcn, loader, __boolean.valueOf(currentContext)))

    @abstractmethod
    def removeContext(self, context: 'LoggerContext'):
        """public abstract void org.apache.logging.log4j.spi.LoggerContextFactory.removeContext(org.apache.logging.log4j.spi.LoggerContext)"""
        pass

    @abstractmethod
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool):
        """public abstract org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.spi.LoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean)"""
        pass

    @overload
    def shutdown(self, fqcn: str, loader: 'ClassLoader', currentContext: bool, allContexts: bool):
        """public default void org.apache.logging.log4j.spi.LoggerContextFactory.shutdown(java.lang.String,java.lang.ClassLoader,boolean,boolean)"""
        super(__LoggerContextFactory, self).shutdown(fqcn, loader, __boolean.valueOf(currentContext), __boolean.valueOf(allContexts))

    @overload
    def isClassLoaderDependent(self) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContextFactory.isClassLoaderDependent()"""
        return bool.__wrap(super(LoggerContextFactory, self).isClassLoaderDependent()) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextShutdownAware
import org.apache.logging.log4j.spi.LoggerContextShutdownAware as __LoggerContextShutdownAware
__LoggerContextShutdownAware = __LoggerContextShutdownAware
from abc import abstractmethod, ABC
 
class LoggerContextShutdownAware(ABC):
    """org.apache.logging.log4j.spi.LoggerContextShutdownAware"""
 
    @staticmethod
    def __wrap(java_value: __LoggerContextShutdownAware) -> 'LoggerContextShutdownAware':
        return LoggerContextShutdownAware(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerContextShutdownAware):
        """
        Dynamic initializer for LoggerContextShutdownAware.
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
 
    @abstractmethod
    def contextShutdown(self, loggerContext: 'LoggerContext'):
        """public abstract void org.apache.logging.log4j.spi.LoggerContextShutdownAware.contextShutdown(org.apache.logging.log4j.spi.LoggerContext)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap as __ThreadContextMap
__ThreadContextMap = __ThreadContextMap
from abc import abstractmethod, ABC
 
class ThreadContextMap(ABC):
    """org.apache.logging.log4j.spi.ThreadContextMap"""
 
    @staticmethod
    def __wrap(java_value: __ThreadContextMap) -> 'ThreadContextMap':
        return ThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadContextMap):
        """
        Dynamic initializer for ThreadContextMap.
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
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextMapFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.spi.ThreadContextMap as __ThreadContextMap
__ThreadContextMap = __ThreadContextMap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.spi.ThreadContextMapFactory as __ThreadContextMapFactory
__ThreadContextMapFactory = __ThreadContextMapFactory
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ThreadContextMapFactory():
    """org.apache.logging.log4j.spi.ThreadContextMapFactory"""
 
    @staticmethod
    def __wrap(java_value: __ThreadContextMapFactory) -> 'ThreadContextMapFactory':
        return ThreadContextMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadContextMapFactory):
        """
        Dynamic initializer for ThreadContextMapFactory.
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

    @staticmethod
    @overload
    def createThreadContextMap() -> 'ThreadContextMap':
        """public static org.apache.logging.log4j.spi.ThreadContextMap org.apache.logging.log4j.spi.ThreadContextMapFactory.createThreadContextMap()"""
        return ThreadContextMap.__wrap(__ThreadContextMapFactory.createThreadContextMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

        @staticmethod
        @overload
        def init():
            """public static void org.apache.logging.log4j.spi.ThreadContextMapFactory.init()"""
            __ThreadContextMapFactory.init()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.spi.AbstractLogger
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.message.EntryMessage as __EntryMessage
__EntryMessage = __EntryMessage
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
import org.apache.logging.log4j.message.FlowMessageFactory as __FlowMessageFactory
__FlowMessageFactory = __FlowMessageFactory
from abc import abstractmethod, ABC
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.apache.logging.log4j.spi.AbstractLogger as __AbstractLogger
__AbstractLogger = __AbstractLogger
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

from builtins import bool
from builtins import str
import org.apache.logging.log4j.Logger as __Logger
__Logger = __Logger
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import org.apache.logging.log4j.spi.ExtendedLogger as __ExtendedLogger
__ExtendedLogger = __ExtendedLogger
import java.lang.StackTraceElement as StackTraceElement
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import int
 
class AbstractLogger(ABC, __ExtendedLogger, ExtendedLogger, __LocationAwareLogger, LocationAwareLogger, __Serializable, Serializable):
    """org.apache.logging.log4j.spi.AbstractLogger"""
 
    @staticmethod
    def __wrap(java_value: __AbstractLogger) -> 'AbstractLogger':
        return AbstractLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractLogger):
        """
        Dynamic initializer for AbstractLogger.
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
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.AbstractLogger()"""
        val = __AbstractLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(__AbstractLogger, self).trace(message)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(__AbstractLogger, self).error(message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isDebugEnabled(marker))

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).error(message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atTrace())

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).trace(message, paramSuppliers)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atFatal())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'.__wrap(super(AbstractLogger, self).getFlowMessageFactory())

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).fatal(message)

    @abstractmethod
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).printf(level, format, params)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).warn(message, paramSuppliers)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).trace(marker, message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message)

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.AbstractLogger()"""
        val = __AbstractLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).log(level, message, params)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atError())

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(message, params)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, messageSupplier, throwable)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isErrorEnabled(marker))

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(__AbstractLogger, self).catching(throwable)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(__AbstractLogger, self).entry(params)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).debug(marker, message, paramSuppliers)

    @overload
    def __init__(self, name: str, messageFactory: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.AbstractLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        val = __AbstractLogger(name, messageFactory)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int.__wrap(__AbstractLogger.getRecursionDepth())

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isEnabled(level, marker))

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.spi.AbstractLogger(java.lang.String)"""
        val = __AbstractLogger(name)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(message, params)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(__AbstractLogger, self).log(level, message)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(AbstractLogger, self).entry()

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool.__wrap(super(__AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atInfo())

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(messageSupplier, throwable)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isFatalEnabled(marker))

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'.__wrap(super(__AbstractLogger, self).throwing(throwable))

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isWarnEnabled(marker))

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(messageSupplier, throwable)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(result))

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).warn(marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).trace(message)

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object.__wrap(super(__AbstractLogger, self).exit(result))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(format, params))

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0)

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).error(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isErrorEnabled())

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).error(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(message, params)

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(AbstractLogger, self).exit()

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(__AbstractLogger, self).fatal(message)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isWarnEnabled())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(__AbstractLogger, self).catching(level, throwable)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atWarn())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).fatal(marker, message, params)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        __AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'.__wrap(super(AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'.__wrap(super(__AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'.__wrap(super(AbstractLogger, self).traceEntry())

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str.__wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(__AbstractLogger, self).fatal(message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(message, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(__AbstractLogger, self).error(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).always())

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(__AbstractLogger, self).error(message)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(AbstractLogger, self).traceExit()

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(message, params)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @abstractmethod
    def getLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.Logger.getLevel()"""
        pass

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(__AbstractLogger, self).trace(message)

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'.__wrap(super(__AbstractLogger, self).atLevel(level))

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atDebug())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(__AbstractLogger, self).trace(message)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(__AbstractLogger, self).traceExit(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).error(marker, message) 
 
 
# CLASS: org.apache.logging.log4j.spi.ExtendedLoggerWrapper
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.message.EntryMessage as __EntryMessage
__EntryMessage = __EntryMessage
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
import org.apache.logging.log4j.message.FlowMessageFactory as __FlowMessageFactory
__FlowMessageFactory = __FlowMessageFactory
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.apache.logging.log4j.spi.AbstractLogger as __AbstractLogger
__AbstractLogger = __AbstractLogger
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import java.lang.StackTraceElement as StackTraceElement
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import org.apache.logging.log4j.spi.ExtendedLoggerWrapper as __ExtendedLoggerWrapper
__ExtendedLoggerWrapper = __ExtendedLoggerWrapper
import org.apache.logging.log4j.Level as __Level
__Level = __Level
from builtins import int
 
class ExtendedLoggerWrapper(__AbstractLogger, AbstractLogger):
    """org.apache.logging.log4j.spi.ExtendedLoggerWrapper"""
 
    @staticmethod
    def __wrap(java_value: __ExtendedLoggerWrapper) -> 'ExtendedLoggerWrapper':
        return ExtendedLoggerWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExtendedLoggerWrapper):
        """
        Dynamic initializer for ExtendedLoggerWrapper.
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
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(__AbstractLogger, self).trace(message)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(__AbstractLogger, self).error(message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isDebugEnabled(marker))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public void org.apache.logging.log4j.spi.ExtendedLoggerWrapper.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__ExtendedLoggerWrapper, self).logMessage(fqcn, level, marker, message, t)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).error(message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atTrace())

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).debug(marker, message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).trace(message, paramSuppliers)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atFatal())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1))

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'.__wrap(super(AbstractLogger, self).getFlowMessageFactory())

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message))

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).fatal(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).printf(level, format, params)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).warn(message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).trace(marker, message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message)

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).log(level, message, params)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atError())

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def getLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.spi.ExtendedLoggerWrapper.getLevel()"""
        return 'log4py.Level'.__wrap(super(ExtendedLoggerWrapper, self).getLevel())

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(message, params)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, messageSupplier, throwable)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isErrorEnabled(marker))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, params))

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(__AbstractLogger, self).catching(throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(__AbstractLogger, self).entry(params)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).debug(marker, message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int.__wrap(__AbstractLogger.getRecursionDepth())

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isEnabled(level, marker))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(message, params)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(AbstractLogger, self).entry()

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool.__wrap(super(__AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atInfo())

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(messageSupplier, throwable)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isFatalEnabled(marker))

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'.__wrap(super(__AbstractLogger, self).throwing(throwable))

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isWarnEnabled(marker))

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(messageSupplier, throwable)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(result))

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).warn(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).warn(marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).trace(message)

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object.__wrap(super(__AbstractLogger, self).exit(result))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'.__wrap(super(__AbstractLogger, self).traceEntry(format, params))

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(__AbstractLogger, self).debug(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3))

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0)

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).error(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isErrorEnabled())

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).info(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__AbstractLogger, self).error(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(message, params)

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(AbstractLogger, self).exit()

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(__AbstractLogger, self).fatal(message)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool.__wrap(super(AbstractLogger, self).isWarnEnabled())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(__AbstractLogger, self).catching(level, throwable)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atWarn())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).fatal(marker, message, params)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        __AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'.__wrap(super(AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'.__wrap(super(__AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'.__wrap(super(AbstractLogger, self).traceEntry())

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).info(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str.__wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(__AbstractLogger, self).fatal(message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(message, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(__AbstractLogger, self).error(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).always())

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(__AbstractLogger, self).error(message)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(AbstractLogger, self).traceExit()

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(marker, message, p0, p1)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(message, params)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def __init__(self, logger: 'ExtendedLogger', name: str, messageFactory: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.ExtendedLoggerWrapper(org.apache.logging.log4j.spi.ExtendedLogger,java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        val = __ExtendedLoggerWrapper(logger, name, messageFactory)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(__AbstractLogger, self).trace(message)

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object.__wrap(super(__AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'.__wrap(super(__AbstractLogger, self).atLevel(level))

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'.__wrap(super(AbstractLogger, self).atDebug())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(__AbstractLogger, self).trace(message)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(__AbstractLogger, self).traceExit(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(__AbstractLogger, self).fatal(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2))

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__AbstractLogger, self).error(marker, message) 
 
 
# CLASS: org.apache.logging.log4j.spi.Provider
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.net.URL as URL
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.net.URL as __URL
__URL = __URL
import java.lang.Integer as Integer
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import org.apache.logging.log4j.spi.Provider as __Provider
__Provider = __Provider
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Provider():
    """org.apache.logging.log4j.spi.Provider"""
 
    @staticmethod
    def __wrap(java_value: __Provider) -> 'Provider':
        return Provider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Provider):
        """
        Dynamic initializer for Provider.
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
    def getThreadContextMap(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.getThreadContextMap()"""
        return str.__wrap(super(Provider, self).getThreadContextMap())

    @overload
    def __init__(self, priority: 'Integer', versions: str, loggerContextFactoryClass: 'Class'):
        """public org.apache.logging.log4j.spi.Provider(java.lang.Integer,java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.spi.LoggerContextFactory>)"""
        val = __Provider(priority, versions, loggerContextFactoryClass)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPriority(self) -> 'Integer':
        """public java.lang.Integer org.apache.logging.log4j.spi.Provider.getPriority()"""
        return __transform(super(Provider, self).getPriority()).'Integer'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.Provider.equals(java.lang.Object)"""
        return bool.__wrap(super(__Provider, self).equals(o))

    @overload
    def getUrl(self) -> 'URL':
        """public java.net.URL org.apache.logging.log4j.spi.Provider.getUrl()"""
        return 'URL'.__wrap(super(Provider, self).getUrl())

    @overload
    def getClassName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.getClassName()"""
        return str.__wrap(super(Provider, self).getClassName())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, props: 'Properties', url: 'URL', classLoader: 'ClassLoader'):
        """public org.apache.logging.log4j.spi.Provider(java.util.Properties,java.net.URL,java.lang.ClassLoader)"""
        val = __Provider(props, url, classLoader)
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

    @overload
    def loadLoggerContextFactory(self) -> 'type.Class':
        """public java.lang.Class<? extends org.apache.logging.log4j.spi.LoggerContextFactory> org.apache.logging.log4j.spi.Provider.loadLoggerContextFactory()"""
        return 'type.Class'.__wrap(super(Provider, self).loadLoggerContextFactory())

    @overload
    def __init__(self, priority: 'Integer', versions: str, loggerContextFactoryClass: 'Class', threadContextMapClass: 'Class'):
        """public org.apache.logging.log4j.spi.Provider(java.lang.Integer,java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.spi.LoggerContextFactory>,java.lang.Class<? extends org.apache.logging.log4j.spi.ThreadContextMap>)"""
        val = __Provider(priority, versions, loggerContextFactoryClass, threadContextMapClass)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.toString()"""
        return str.__wrap(super(Provider, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.Provider.hashCode()"""
        return int.__wrap(super(Provider, self).hashCode())

    @overload
    def loadThreadContextMap(self) -> 'type.Class':
        """public java.lang.Class<? extends org.apache.logging.log4j.spi.ThreadContextMap> org.apache.logging.log4j.spi.Provider.loadThreadContextMap()"""
        return 'type.Class'.__wrap(super(Provider, self).loadThreadContextMap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVersions(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.getVersions()"""
        return str.__wrap(super(Provider, self).getVersions()) 
 
 
# CLASS: org.apache.logging.log4j.spi.MutableThreadContextStack
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
from builtins import type
import org.apache.logging.log4j.spi.MutableThreadContextStack as __MutableThreadContextStack
__MutableThreadContextStack = __MutableThreadContextStack
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.apache.logging.log4j.spi.ThreadContextStack as __ThreadContextStack
__ThreadContextStack = __ThreadContextStack
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

from builtins import bool
from builtins import str
import org.apache.logging.log4j.ThreadContext as __ThreadContext_ContextStack
__ContextStack = __ThreadContext_ContextStack.ContextStack
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MutableThreadContextStack(__ThreadContextStack, ThreadContextStack, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.spi.MutableThreadContextStack"""
 
    @staticmethod
    def __wrap(java_value: __MutableThreadContextStack) -> 'MutableThreadContextStack':
        return MutableThreadContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableThreadContextStack):
        """
        Dynamic initializer for MutableThreadContextStack.
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
    def clear(self):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.clear()"""
        super(MutableThreadContextStack, self).clear()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.MutableThreadContextStack()"""
        val = __MutableThreadContextStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.String> org.apache.logging.log4j.spi.MutableThreadContextStack.iterator()"""
        return 'Iterator'.__wrap(super(MutableThreadContextStack, self).iterator())

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
    def __init__(self, list: 'List'):
        """public org.apache.logging.log4j.spi.MutableThreadContextStack(java.util.List<java.lang.String>)"""
        val = __MutableThreadContextStack(list)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isFrozen(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.isFrozen()"""
        return bool.__wrap(super(MutableThreadContextStack, self).isFrozen())

    @override
    @overload
    def push(self, message: str):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.push(java.lang.String)"""
        super(__MutableThreadContextStack, self).push(message)

    @overload
    def toArray(self, ts: 'Object') -> List[object]:
        """public <T> T[] org.apache.logging.log4j.spi.MutableThreadContextStack.toArray(T[])"""
        return List[object].__wrap(super(__MutableThreadContextStack, self).toArray(ts))

    @override
    @overload
    def getDepth(self) -> int:
        """public int org.apache.logging.log4j.spi.MutableThreadContextStack.getDepth()"""
        return int.__wrap(super(MutableThreadContextStack, self).getDepth())

    @override
    @overload
    def pop(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.MutableThreadContextStack.pop()"""
        return str.__wrap(super(MutableThreadContextStack, self).pop())

    @overload
    def retainAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).retainAll(objects))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.MutableThreadContextStack.hashCode()"""
        return int.__wrap(super(MutableThreadContextStack, self).hashCode())

    @overload
    def remove(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.remove(java.lang.Object)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).remove(o))

    @overload
    def freeze(self):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.freeze()"""
        super(MutableThreadContextStack, self).freeze()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.spi.MutableThreadContextStack.toArray()"""
        return List[object].__wrap(super(MutableThreadContextStack, self).toArray())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.isEmpty()"""
        return bool.__wrap(super(MutableThreadContextStack, self).isEmpty())

    @override
    @overload
    def peek(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.MutableThreadContextStack.peek()"""
        return str.__wrap(super(MutableThreadContextStack, self).peek())

    @overload
    def add(self, s: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.add(java.lang.String)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).add(s))

    @overload
    def contains(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.contains(java.lang.Object)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).contains(o))

    @overload
    def addAll(self, strings: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.addAll(java.util.Collection<? extends java.lang.String>)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).addAll(strings))

    @overload
    def removeAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).removeAll(objects))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.spi.MutableThreadContextStack.size()"""
        return int.__wrap(super(MutableThreadContextStack, self).size())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.MutableThreadContextStack.toString()"""
        return str.__wrap(super(MutableThreadContextStack, self).toString())

    @override
    @overload
    def trim(self, depth: int):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.trim(int)"""
        super(__MutableThreadContextStack, self).trim(__int.valueOf(depth))

    @overload
    def containsAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).containsAll(objects))

    @override
    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.String> org.apache.logging.log4j.spi.MutableThreadContextStack.asList()"""
        return 'List'.__wrap(super(MutableThreadContextStack, self).asList())

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
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.equals(java.lang.Object)"""
        return bool.__wrap(super(__MutableThreadContextStack, self).equals(obj))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.MutableThreadContextStack()"""
        val = __MutableThreadContextStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def copy(self) -> 'ThreadContextStack':
        """public org.apache.logging.log4j.spi.ThreadContextStack org.apache.logging.log4j.spi.MutableThreadContextStack.copy()"""
        return 'ThreadContextStack'.__wrap(super(MutableThreadContextStack, self).copy())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.formatTo(java.lang.StringBuilder)"""
        super(__MutableThreadContextStack, self).formatTo(buffer)

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getImmutableStackOrNull(self) -> 'log4py.ThreadContext$ContextStack':
        """public org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.spi.MutableThreadContextStack.getImmutableStackOrNull()"""
        return 'log4py.ThreadContext$ContextStack'.__wrap(super(MutableThreadContextStack, self).getImmutableStackOrNull()) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextShutdownEnabled
import org.apache.logging.log4j.spi.LoggerContextShutdownEnabled as __LoggerContextShutdownEnabled
__LoggerContextShutdownEnabled = __LoggerContextShutdownEnabled
from abc import abstractmethod, ABC
 
class LoggerContextShutdownEnabled(ABC):
    """org.apache.logging.log4j.spi.LoggerContextShutdownEnabled"""
 
    @staticmethod
    def __wrap(java_value: __LoggerContextShutdownEnabled) -> 'LoggerContextShutdownEnabled':
        return LoggerContextShutdownEnabled(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerContextShutdownEnabled):
        """
        Dynamic initializer for LoggerContextShutdownEnabled.
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
 
    @abstractmethod
    def getListeners(self, ):
        """public abstract java.util.List<org.apache.logging.log4j.spi.LoggerContextShutdownAware> org.apache.logging.log4j.spi.LoggerContextShutdownEnabled.getListeners()"""
        pass

    @abstractmethod
    def addShutdownListener(self, listener: 'LoggerContextShutdownAware'):
        """public abstract void org.apache.logging.log4j.spi.LoggerContextShutdownEnabled.addShutdownListener(org.apache.logging.log4j.spi.LoggerContextShutdownAware)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.MessageFactory2Adapter
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.spi.MessageFactory2Adapter as __MessageFactory2Adapter
__MessageFactory2Adapter = __MessageFactory2Adapter
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MessageFactory2Adapter(log4py.__MessageFactory2, message.MessageFactory2):
    """org.apache.logging.log4j.spi.MessageFactory2Adapter"""
 
    @staticmethod
    def __wrap(java_value: __MessageFactory2Adapter) -> 'MessageFactory2Adapter':
        return MessageFactory2Adapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageFactory2Adapter):
        """
        Dynamic initializer for MessageFactory2Adapter.
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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, wrapped: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.MessageFactory2Adapter(org.apache.logging.log4j.message.MessageFactory)"""
        val = __MessageFactory2Adapter(wrapped)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1))

    @overload
    def newMessage(self, message: str, *params: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object...)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, params))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getOriginal(self) -> 'message.MessageFactory':
        """public org.apache.logging.log4j.message.MessageFactory org.apache.logging.log4j.spi.MessageFactory2Adapter.getOriginal()"""
        return 'message.MessageFactory'.__wrap(super(MessageFactory2Adapter, self).getOriginal())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def newMessage(self, charSequence: 'CharSequence') -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.CharSequence)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(charSequence))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.Object)"""
        return 'message.Message'.__wrap(super(__MessageFactory2Adapter, self).newMessage(message)) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextKey
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import org.apache.logging.log4j.spi.LoggerContextKey as __LoggerContextKey
__LoggerContextKey = __LoggerContextKey
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoggerContextKey():
    """org.apache.logging.log4j.spi.LoggerContextKey"""
 
    @staticmethod
    def __wrap(java_value: __LoggerContextKey) -> 'LoggerContextKey':
        return LoggerContextKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerContextKey):
        """
        Dynamic initializer for LoggerContextKey.
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
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerContextKey()"""
        val = __LoggerContextKey()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(name: str, messageFactoryClass: 'Class') -> str:
        """public static java.lang.String org.apache.logging.log4j.spi.LoggerContextKey.create(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        return str.__wrap(__LoggerContextKey.create(name, messageFactoryClass))

    @staticmethod
    @overload
    def create(name: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.spi.LoggerContextKey.create(java.lang.String)"""
        return str.__wrap(__LoggerContextKey.create(name))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerContextKey()"""
        val = __LoggerContextKey()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(name: str, messageFactory: 'MessageFactory') -> str:
        """public static java.lang.String org.apache.logging.log4j.spi.LoggerContextKey.create(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return str.__wrap(__LoggerContextKey.create(name, messageFactory))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.spi.AbstractLoggerAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import org.apache.logging.log4j.spi.AbstractLoggerAdapter as __AbstractLoggerAdapter
__AbstractLoggerAdapter = __AbstractLoggerAdapter
from builtins import object
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class AbstractLoggerAdapter(ABC, __LoggerAdapter, LoggerAdapter, __LoggerContextShutdownAware, LoggerContextShutdownAware):
    """org.apache.logging.log4j.spi.AbstractLoggerAdapter"""
 
    @staticmethod
    def __wrap(java_value: __AbstractLoggerAdapter) -> 'AbstractLoggerAdapter':
        return AbstractLoggerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractLoggerAdapter):
        """
        Dynamic initializer for AbstractLoggerAdapter.
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
    def getLoggersInContext(self, context: 'LoggerContext') -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<java.lang.String, L> org.apache.logging.log4j.spi.AbstractLoggerAdapter.getLoggersInContext(org.apache.logging.log4j.spi.LoggerContext)"""
        return 'ConcurrentMap'.__wrap(super(__AbstractLoggerAdapter, self).getLoggersInContext(context))

    @overload
    def getLogger(self, name: str) -> object:
        """public L org.apache.logging.log4j.spi.AbstractLoggerAdapter.getLogger(java.lang.String)"""
        return object.__wrap(super(__AbstractLoggerAdapter, self).getLogger(name))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLoggerContexts(self) -> 'Set':
        """public java.util.Set<org.apache.logging.log4j.spi.LoggerContext> org.apache.logging.log4j.spi.AbstractLoggerAdapter.getLoggerContexts()"""
        return 'Set'.__wrap(super(AbstractLoggerAdapter, self).getLoggerContexts())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.AbstractLoggerAdapter()"""
        val = __AbstractLoggerAdapter()
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
    def close(self):
        """public void org.apache.logging.log4j.spi.AbstractLoggerAdapter.close()"""
        super(AbstractLoggerAdapter, self).close()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.AbstractLoggerAdapter()"""
        val = __AbstractLoggerAdapter()
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

    @override
    @overload
    def contextShutdown(self, loggerContext: 'LoggerContext'):
        """public void org.apache.logging.log4j.spi.AbstractLoggerAdapter.contextShutdown(org.apache.logging.log4j.spi.LoggerContext)"""
        super(__AbstractLoggerAdapter, self).contextShutdown(loggerContext)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextMap2
import org.apache.logging.log4j.spi.ThreadContextMap as __ThreadContextMap
__ThreadContextMap = __ThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap2 as __ThreadContextMap2
__ThreadContextMap2 = __ThreadContextMap2
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class ThreadContextMap2(ABC, __ThreadContextMap, ThreadContextMap):
    """org.apache.logging.log4j.spi.ThreadContextMap2"""
 
    @staticmethod
    def __wrap(java_value: __ThreadContextMap2) -> 'ThreadContextMap2':
        return ThreadContextMap2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadContextMap2):
        """
        Dynamic initializer for ThreadContextMap2.
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
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ThreadContextMap2.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def putAll(self, map: 'Map'):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap2.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.CleanableThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap as __ThreadContextMap
__ThreadContextMap = __ThreadContextMap
import org.apache.logging.log4j.spi.CleanableThreadContextMap as __CleanableThreadContextMap
__CleanableThreadContextMap = __CleanableThreadContextMap
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.spi.ThreadContextMap2 as __ThreadContextMap2
__ThreadContextMap2 = __ThreadContextMap2
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class CleanableThreadContextMap(ABC, __ThreadContextMap2, ThreadContextMap2):
    """org.apache.logging.log4j.spi.CleanableThreadContextMap"""
 
    @staticmethod
    def __wrap(java_value: __CleanableThreadContextMap) -> 'CleanableThreadContextMap':
        return CleanableThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CleanableThreadContextMap):
        """
        Dynamic initializer for CleanableThreadContextMap.
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
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ThreadContextMap2.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def putAll(self, map: 'Map'):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap2.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def removeAll(self, keys: 'Iterable'):
        """public abstract void org.apache.logging.log4j.spi.CleanableThreadContextMap.removeAll(java.lang.Iterable<java.lang.String>)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContext
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.spi.LoggerRegistry as __LoggerRegistry
__LoggerRegistry = __LoggerRegistry
import java.lang.Object as __object
from builtins import type
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.spi.LoggerContext as __LoggerContext
__LoggerContext = __LoggerContext
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from abc import abstractmethod, ABC
import org.apache.logging.log4j.spi.ExtendedLogger as __ExtendedLogger
__ExtendedLogger = __ExtendedLogger
from builtins import object
from builtins import bool
 
class LoggerContext(ABC):
    """org.apache.logging.log4j.spi.LoggerContext"""
 
    @staticmethod
    def __wrap(java_value: __LoggerContext) -> 'LoggerContext':
        return LoggerContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerContext):
        """
        Dynamic initializer for LoggerContext.
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
 
    @abstractmethod
    def getLogger(self, name: str):
        """public abstract org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.String)"""
        pass

    @abstractmethod
    def hasLogger(self, name: str):
        """public abstract boolean org.apache.logging.log4j.spi.LoggerContext.hasLogger(java.lang.String)"""
        pass

    @overload
    def getLogger(self, cls: 'Class') -> 'ExtendedLogger':
        """public default org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.Class<?>)"""
        return 'ExtendedLogger'.__wrap(super(__LoggerContext, self).getLogger(cls))

    @abstractmethod
    def hasLogger(self, name: str, messageFactoryClass: 'Class'):
        """public abstract boolean org.apache.logging.log4j.spi.LoggerContext.hasLogger(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        pass

    @overload
    def getLogger(self, cls: 'Class', messageFactory: 'MessageFactory') -> 'ExtendedLogger':
        """public default org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.Class<?>,org.apache.logging.log4j.message.MessageFactory)"""
        return 'ExtendedLogger'.__wrap(super(__LoggerContext, self).getLogger(cls, messageFactory))

    @abstractmethod
    def hasLogger(self, name: str, messageFactory: 'MessageFactory'):
        """public abstract boolean org.apache.logging.log4j.spi.LoggerContext.hasLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        pass

    @overload
    def getLoggerRegistry(self) -> 'LoggerRegistry':
        """public default org.apache.logging.log4j.spi.LoggerRegistry<? extends org.apache.logging.log4j.Logger> org.apache.logging.log4j.spi.LoggerContext.getLoggerRegistry()"""
        return 'LoggerRegistry'.__wrap(super(LoggerContext, self).getLoggerRegistry())

    @overload
    def putObjectIfAbsent(self, key: str, value: object) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.putObjectIfAbsent(java.lang.String,java.lang.Object)"""
        return object.__wrap(super(__LoggerContext, self).putObjectIfAbsent(key, value))

    @overload
    def getObject(self, key: str) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.getObject(java.lang.String)"""
        return object.__wrap(super(__LoggerContext, self).getObject(key))

    @abstractmethod
    def getLogger(self, name: str, messageFactory: 'MessageFactory'):
        """public abstract org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        pass

    @abstractmethod
    def getExternalContext(self, ):
        """public abstract java.lang.Object org.apache.logging.log4j.spi.LoggerContext.getExternalContext()"""
        pass

    @overload
    def putObject(self, key: str, value: object) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.putObject(java.lang.String,java.lang.Object)"""
        return object.__wrap(super(__LoggerContext, self).putObject(key, value))

    @overload
    def removeObject(self, key: str, value: object) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContext.removeObject(java.lang.String,java.lang.Object)"""
        return bool.__wrap(super(__LoggerContext, self).removeObject(key, value))

    @overload
    def removeObject(self, key: str) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.removeObject(java.lang.String)"""
        return object.__wrap(super(__LoggerContext, self).removeObject(key)) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import org.apache.logging.log4j.spi.ExtendedLogger as __ExtendedLogger
__ExtendedLogger = __ExtendedLogger
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import org.apache.logging.log4j.spi.LoggerRegistry as __LoggerRegistry
__LoggerRegistry = __LoggerRegistry
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoggerRegistry():
    """org.apache.logging.log4j.spi.LoggerRegistry"""
 
    @staticmethod
    def __wrap(java_value: __LoggerRegistry) -> 'LoggerRegistry':
        return LoggerRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerRegistry):
        """
        Dynamic initializer for LoggerRegistry.
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
    def hasLogger(self, name: str, messageFactory: 'MessageFactory') -> bool:
        """public boolean org.apache.logging.log4j.spi.LoggerRegistry.hasLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return bool.__wrap(super(__LoggerRegistry, self).hasLogger(name, messageFactory))

    @overload
    def hasLogger(self, name: str, messageFactoryClass: 'Class') -> bool:
        """public boolean org.apache.logging.log4j.spi.LoggerRegistry.hasLogger(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        return bool.__wrap(super(__LoggerRegistry, self).hasLogger(name, messageFactoryClass))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLogger(self, name: str) -> 'ExtendedLogger':
        """public T org.apache.logging.log4j.spi.LoggerRegistry.getLogger(java.lang.String)"""
        return 'ExtendedLogger'.__wrap(super(__LoggerRegistry, self).getLogger(name))

    @overload
    def getLoggers(self, destination: 'Collection') -> 'Collection':
        """public java.util.Collection<T> org.apache.logging.log4j.spi.LoggerRegistry.getLoggers(java.util.Collection<T>)"""
        return 'Collection'.__wrap(super(__LoggerRegistry, self).getLoggers(destination))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def putIfAbsent(self, name: str, messageFactory: 'MessageFactory', logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry.putIfAbsent(java.lang.String,org.apache.logging.log4j.message.MessageFactory,T)"""
        super(__LoggerRegistry, self).putIfAbsent(name, messageFactory, logger)

    @overload
    def hasLogger(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.LoggerRegistry.hasLogger(java.lang.String)"""
        return bool.__wrap(super(__LoggerRegistry, self).hasLogger(name))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getLogger(self, name: str, messageFactory: 'MessageFactory') -> 'ExtendedLogger':
        """public T org.apache.logging.log4j.spi.LoggerRegistry.getLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return 'ExtendedLogger'.__wrap(super(__LoggerRegistry, self).getLogger(name, messageFactory))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerRegistry()"""
        val = __LoggerRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry()"""
        val = __LoggerRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getLoggers(self) -> 'Collection':
        """public java.util.Collection<T> org.apache.logging.log4j.spi.LoggerRegistry.getLoggers()"""
        return 'Collection'.__wrap(super(LoggerRegistry, self).getLoggers())

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

    @overload
    def __init__(self, factory: 'MapFactory'):
        """public org.apache.logging.log4j.spi.LoggerRegistry(org.apache.logging.log4j.spi.LoggerRegistry$MapFactory<T>)"""
        val = __LoggerRegistry(factory)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.logging.log4j.spi.LoggerRegistry as __LoggerRegistry_WeakMapFactory
__WeakMapFactory = __LoggerRegistry_WeakMapFactory.WeakMapFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class WeakMapFactory(__MapFactory, MapFactory):
    """org.apache.logging.log4j.spi.LoggerRegistry.WeakMapFactory"""
 
    @staticmethod
    def __wrap(java_value: __WeakMapFactory) -> 'WeakMapFactory':
        return WeakMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WeakMapFactory):
        """
        Dynamic initializer for WeakMapFactory.
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
    def createInnerMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory.createInnerMap()"""
        return 'Map'.__wrap(super(WeakMapFactory, self).createInnerMap())

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
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        super(__WeakMapFactory, self).putIfAbsent(innerMap, name, logger)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def createOuterMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory.createOuterMap()"""
        return 'Map'.__wrap(super(WeakMapFactory, self).createOuterMap())

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
        """public org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory()"""
        val = __WeakMapFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory()"""
        val = __WeakMapFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.spi.DefaultThreadContextStack
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import java.lang.Boolean as __boolean
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.apache.logging.log4j.spi.ThreadContextStack as __ThreadContextStack
__ThreadContextStack = __ThreadContextStack
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

from builtins import bool
from builtins import str
import org.apache.logging.log4j.ThreadContext as __ThreadContext_ContextStack
__ContextStack = __ThreadContext_ContextStack.ContextStack
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import org.apache.logging.log4j.spi.DefaultThreadContextStack as __DefaultThreadContextStack
__DefaultThreadContextStack = __DefaultThreadContextStack
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class DefaultThreadContextStack(__ThreadContextStack, ThreadContextStack, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.spi.DefaultThreadContextStack"""
 
    @staticmethod
    def __wrap(java_value: __DefaultThreadContextStack) -> 'DefaultThreadContextStack':
        return DefaultThreadContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultThreadContextStack):
        """
        Dynamic initializer for DefaultThreadContextStack.
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
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextStack.hashCode()"""
        return int.__wrap(super(DefaultThreadContextStack, self).hashCode())

    @overload
    def add(self, s: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.add(java.lang.String)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).add(s))

    @override
    @overload
    def peek(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextStack.peek()"""
        return str.__wrap(super(DefaultThreadContextStack, self).peek())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.formatTo(java.lang.StringBuilder)"""
        super(__DefaultThreadContextStack, self).formatTo(buffer)

    @override
    @overload
    def getDepth(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextStack.getDepth()"""
        return int.__wrap(super(DefaultThreadContextStack, self).getDepth())

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
    def remove(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.remove(java.lang.Object)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).remove(o))

    @override
    @overload
    def pop(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextStack.pop()"""
        return str.__wrap(super(DefaultThreadContextStack, self).pop())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextStack.size()"""
        return int.__wrap(super(DefaultThreadContextStack, self).size())

    @override
    @overload
    def copy(self) -> 'ThreadContextStack':
        """public org.apache.logging.log4j.spi.ThreadContextStack org.apache.logging.log4j.spi.DefaultThreadContextStack.copy()"""
        return 'ThreadContextStack'.__wrap(super(DefaultThreadContextStack, self).copy())

    @override
    @overload
    def getImmutableStackOrNull(self) -> 'log4py.ThreadContext$ContextStack':
        """public org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.spi.DefaultThreadContextStack.getImmutableStackOrNull()"""
        return 'log4py.ThreadContext$ContextStack'.__wrap(super(DefaultThreadContextStack, self).getImmutableStackOrNull())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).retainAll(objects))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, useStack: bool):
        """public org.apache.logging.log4j.spi.DefaultThreadContextStack(boolean)"""
        val = __DefaultThreadContextStack(__boolean.valueOf(useStack))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.equals(java.lang.Object)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).equals(obj))

    @override
    @overload
    def push(self, message: str):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.push(java.lang.String)"""
        super(__DefaultThreadContextStack, self).push(message)

    @overload
    def containsAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).containsAll(objects))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.spi.DefaultThreadContextStack.toArray()"""
        return List[object].__wrap(super(DefaultThreadContextStack, self).toArray())

    @overload
    def contains(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.contains(java.lang.Object)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).contains(o))

    @overload
    def removeAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).removeAll(objects))

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.clear()"""
        super(DefaultThreadContextStack, self).clear()

    @overload
    def toArray(self, ts: 'Object') -> List[object]:
        """public <T> T[] org.apache.logging.log4j.spi.DefaultThreadContextStack.toArray(T[])"""
        return List[object].__wrap(super(__DefaultThreadContextStack, self).toArray(ts))

    @overload
    def addAll(self, strings: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.addAll(java.util.Collection<? extends java.lang.String>)"""
        return bool.__wrap(super(__DefaultThreadContextStack, self).addAll(strings))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.isEmpty()"""
        return bool.__wrap(super(DefaultThreadContextStack, self).isEmpty())

    @override
    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextStack.asList()"""
        return 'List'.__wrap(super(DefaultThreadContextStack, self).asList())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextStack.toString()"""
        return str.__wrap(super(DefaultThreadContextStack, self).toString())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def trim(self, depth: int):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.trim(int)"""
        super(__DefaultThreadContextStack, self).trim(__int.valueOf(depth))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextStack.iterator()"""
        return 'Iterator'.__wrap(super(DefaultThreadContextStack, self).iterator()) 
 
 
# CLASS: org.apache.logging.log4j.spi.ExtendedLogger
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.Logger as __Logger
__Logger = __Logger
import java.lang.CharSequence as CharSequence
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
import java.lang.String as __string
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

import java.lang.Throwable as Throwable
import org.apache.logging.log4j.spi.ExtendedLogger as __ExtendedLogger
__ExtendedLogger = __ExtendedLogger
from abc import abstractmethod, ABC
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import java.lang.StackTraceElement as StackTraceElement
 
class ExtendedLogger(ABC, log4py.__Logger, log4py.Logger):
    """org.apache.logging.log4j.spi.ExtendedLogger"""
 
    @staticmethod
    def __wrap(java_value: __ExtendedLogger) -> 'ExtendedLogger':
        return ExtendedLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExtendedLogger):
        """
        Dynamic initializer for ExtendedLogger.
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
 
    @abstractmethod
    def error(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def exit(self, ):
        """public abstract void org.apache.logging.log4j.Logger.exit()"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isInfoEnabled()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.always()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).always())

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'EntryMessage'):
        """public abstract void org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceEntry(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def warn(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public default void org.apache.logging.log4j.Logger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__log4py.Logger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'Message', result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atWarn()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).atWarn())

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getMessageFactory(self, ):
        """public abstract <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.Logger.getMessageFactory()"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level'):
        """public abstract boolean org.apache.logging.log4j.Logger.isEnabled(org.apache.logging.log4j.Level)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def throwing(self, level: 'Level', throwable: 'Throwable'):
        """public abstract <T extends java.lang.Throwable> T org.apache.logging.log4j.Logger.throwing(org.apache.logging.log4j.Level,T)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def error(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.Object,java.lang.Throwable)"""
        pass

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atDebug()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).atDebug())

    @abstractmethod
    def info(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isErrorEnabled()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        pass

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atFatal()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).atFatal())

    @abstractmethod
    def trace(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atInfo()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).atInfo())

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isWarnEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def traceEntry(self, *paramSuppliers: 'util.Supplier'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def trace(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceEntry(self, format: str, *params: object):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isDebugEnabled()"""
        pass

    @abstractmethod
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atTrace()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).atTrace())

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def printf(self, level: 'Level', format: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.Logger.getName()"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def throwing(self, throwable: 'Throwable'):
        """public abstract <T extends java.lang.Throwable> T org.apache.logging.log4j.Logger.throwing(T)"""
        pass

    @abstractmethod
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def catching(self, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.catching(java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def entry(self, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.entry(java.lang.Object...)"""
        pass

    @abstractmethod
    def traceExit(self, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(R)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String)"""
        pass

    @abstractmethod
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'EntryMessage', result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getFlowMessageFactory(self, ):
        """public abstract org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.Logger.getFlowMessageFactory()"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', msgSupplier: 'MessageSupplier', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'.__wrap(super(__log4py.Logger, self).atLevel(level))

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isTraceEnabled()"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isFatalEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isFatalEnabled()"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def traceEntry(self, ):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry()"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, ):
        """public abstract void org.apache.logging.log4j.Logger.traceExit()"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isFatalEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atError()"""
        return 'log4py.LogBuilder'.__wrap(super(log4py.Logger, self).atError())

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def exit(self, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.exit(R)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def info(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def info(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def traceExit(self, format: str, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(java.lang.String,R)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def entry(self, ):
        """public abstract void org.apache.logging.log4j.Logger.entry()"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.Logger.getLevel()"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', msgSupplier: 'Supplier', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def trace(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.Terminable
from abc import abstractmethod, ABC
import org.apache.logging.log4j.spi.Terminable as __Terminable
__Terminable = __Terminable
 
class Terminable(ABC):
    """org.apache.logging.log4j.spi.Terminable"""
 
    @staticmethod
    def __wrap(java_value: __Terminable) -> 'Terminable':
        return Terminable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Terminable):
        """
        Dynamic initializer for Terminable.
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
 
    @abstractmethod
    def terminate(self, ):
        """public abstract void org.apache.logging.log4j.spi.Terminable.terminate()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ReadOnlyThreadContextMap
import org.apache.logging.log4j.spi.ReadOnlyThreadContextMap as __ReadOnlyThreadContextMap
__ReadOnlyThreadContextMap = __ReadOnlyThreadContextMap
from abc import abstractmethod, ABC
 
class ReadOnlyThreadContextMap(ABC):
    """org.apache.logging.log4j.spi.ReadOnlyThreadContextMap"""
 
    @staticmethod
    def __wrap(java_value: __ReadOnlyThreadContextMap) -> 'ReadOnlyThreadContextMap':
        return ReadOnlyThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReadOnlyThreadContextMap):
        """
        Dynamic initializer for ReadOnlyThreadContextMap.
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
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.clear()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.getImmutableMapOrNull()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.CopyOnWrite
import org.apache.logging.log4j.spi.CopyOnWrite as __CopyOnWrite
__CopyOnWrite = __CopyOnWrite
 
class CopyOnWrite(ABC):
    """org.apache.logging.log4j.spi.CopyOnWrite"""
 
    @staticmethod
    def __wrap(java_value: __CopyOnWrite) -> 'CopyOnWrite':
        return CopyOnWrite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CopyOnWrite):
        """
        Dynamic initializer for CopyOnWrite.
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
 
 
# CLASS: org.apache.logging.log4j.spi.LocationAwareLogger
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.spi.LocationAwareLogger as __LocationAwareLogger
__LocationAwareLogger = __LocationAwareLogger
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

import java.lang.Throwable as Throwable
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from abc import abstractmethod, ABC
import java.lang.StackTraceElement as StackTraceElement
 
class LocationAwareLogger(ABC):
    """org.apache.logging.log4j.spi.LocationAwareLogger"""
 
    @staticmethod
    def __wrap(java_value: __LocationAwareLogger) -> 'LocationAwareLogger':
        return LocationAwareLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LocationAwareLogger):
        """
        Dynamic initializer for LocationAwareLogger.
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
 
    @abstractmethod
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.LocationAwareLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ObjectThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap as __ThreadContextMap
__ThreadContextMap = __ThreadContextMap
import org.apache.logging.log4j.spi.CleanableThreadContextMap as __CleanableThreadContextMap
__CleanableThreadContextMap = __CleanableThreadContextMap
import org.apache.logging.log4j.spi.ObjectThreadContextMap as __ObjectThreadContextMap
__ObjectThreadContextMap = __ObjectThreadContextMap
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.spi.ThreadContextMap2 as __ThreadContextMap2
__ThreadContextMap2 = __ThreadContextMap2
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class ObjectThreadContextMap(ABC, __CleanableThreadContextMap, CleanableThreadContextMap):
    """org.apache.logging.log4j.spi.ObjectThreadContextMap"""
 
    @staticmethod
    def __wrap(java_value: __ObjectThreadContextMap) -> 'ObjectThreadContextMap':
        return ObjectThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectThreadContextMap):
        """
        Dynamic initializer for ObjectThreadContextMap.
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
 
    @abstractmethod
    def putValue(self, key: str, value: object):
        """public abstract <V> void org.apache.logging.log4j.spi.ObjectThreadContextMap.putValue(java.lang.String,V)"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def putAll(self, map: 'Map'):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap2.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def putAllValues(self, values: 'Map'):
        """public abstract <V> void org.apache.logging.log4j.spi.ObjectThreadContextMap.putAllValues(java.util.Map<java.lang.String, V>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ThreadContextMap2.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.spi.ObjectThreadContextMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def removeAll(self, keys: 'Iterable'):
        """public abstract void org.apache.logging.log4j.spi.CleanableThreadContextMap.removeAll(java.lang.Iterable<java.lang.String>)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextStack
import java.util.function.Predicate as Predicate
import org.apache.logging.log4j.ThreadContext as __ThreadContext_ContextStack
__ContextStack = __ThreadContext_ContextStack.ContextStack
import java.util.function.IntFunction as IntFunction
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import org.apache.logging.log4j.spi.ThreadContextStack as __ThreadContextStack
__ThreadContextStack = __ThreadContextStack
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ThreadContextStack(ABC, log4py.__ThreadContext_ContextStack, log4py.ThreadContext$ContextStack):
    """org.apache.logging.log4j.spi.ThreadContextStack"""
 
    @staticmethod
    def __wrap(java_value: __ThreadContextStack) -> 'ThreadContextStack':
        return ThreadContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadContextStack):
        """
        Dynamic initializer for ThreadContextStack.
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
 
    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def copy(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.copy()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean java.util.Collection.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.containsAll(java.util.Collection<?>)"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @abstractmethod
    def pop(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.pop()"""
        pass

    @abstractmethod
    def peek(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.peek()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @abstractmethod
    def asList(self, ):
        """public abstract java.util.List<java.lang.String> org.apache.logging.log4j.ThreadContext$ContextStack.asList()"""
        pass

    @abstractmethod
    def trim(self, depth: int):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.trim(int)"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def push(self, message: str):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.push(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int org.apache.logging.log4j.ThreadContext$ContextStack.getDepth()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @abstractmethod
    def getImmutableStackOrNull(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.getImmutableStackOrNull()"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))