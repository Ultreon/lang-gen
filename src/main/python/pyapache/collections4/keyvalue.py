from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.keyvalue.DefaultKeyValue as __DefaultKeyValue
__DefaultKeyValue = __DefaultKeyValue
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as __AbstractKeyValue
__AbstractKeyValue = __AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Map.Entry as Entry
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
 
class DefaultKeyValue():
    """org.apache.commons.collections4.keyvalue.DefaultKeyValue"""
 
    @staticmethod
    def __wrap(java_value: __DefaultKeyValue) -> 'DefaultKeyValue':
        return DefaultKeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultKeyValue):
        """
        Dynamic initializer for DefaultKeyValue.
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
    def __init__(self, ):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = __DefaultKeyValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object.__wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object.__wrap(super(AbstractKeyValue, self).getKey())

    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = __DefaultKeyValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str.__wrap(super(AbstractKeyValue, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.DefaultKeyValue.equals(java.lang.Object)"""
        return bool.__wrap(super(__DefaultKeyValue, self).equals(arg0))

    @overload
    def setKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.keyvalue.DefaultKeyValue.setKey(K)"""
        return object.__wrap(super(__DefaultKeyValue, self).setKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = __DefaultKeyValue(arg0)
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
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(K,V)"""
        val = __DefaultKeyValue(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.DefaultKeyValue.hashCode()"""
        return int.__wrap(super(DefaultKeyValue, self).hashCode())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.DefaultKeyValue.setValue(V)"""
        return object.__wrap(super(__DefaultKeyValue, self).setValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toMapEntry(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.keyvalue.DefaultKeyValue.toMapEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(DefaultKeyValue, self).toMapEntry())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = __DefaultKeyValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.DefaultKeyValue
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.keyvalue.DefaultKeyValue as __DefaultKeyValue
__DefaultKeyValue = __DefaultKeyValue
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as __AbstractKeyValue
__AbstractKeyValue = __AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Map.Entry as Entry
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
 
class DefaultKeyValue():
    """org.apache.commons.collections4.keyvalue.DefaultKeyValue"""
 
    @staticmethod
    def __wrap(java_value: __DefaultKeyValue) -> 'DefaultKeyValue':
        return DefaultKeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultKeyValue):
        """
        Dynamic initializer for DefaultKeyValue.
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
    def __init__(self, ):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = __DefaultKeyValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object.__wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object.__wrap(super(AbstractKeyValue, self).getKey())

    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = __DefaultKeyValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str.__wrap(super(AbstractKeyValue, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.DefaultKeyValue.equals(java.lang.Object)"""
        return bool.__wrap(super(__DefaultKeyValue, self).equals(arg0))

    @overload
    def setKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.keyvalue.DefaultKeyValue.setKey(K)"""
        return object.__wrap(super(__DefaultKeyValue, self).setKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = __DefaultKeyValue(arg0)
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
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(K,V)"""
        val = __DefaultKeyValue(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.DefaultKeyValue.hashCode()"""
        return int.__wrap(super(DefaultKeyValue, self).hashCode())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.DefaultKeyValue.setValue(V)"""
        return object.__wrap(super(__DefaultKeyValue, self).setValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toMapEntry(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.keyvalue.DefaultKeyValue.toMapEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(DefaultKeyValue, self).toMapEntry())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = __DefaultKeyValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.DefaultKeyValue 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as __AbstractKeyValue
__AbstractKeyValue = __AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry as __UnmodifiableMapEntry
__UnmodifiableMapEntry = __UnmodifiableMapEntry
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.keyvalue.AbstractMapEntry as __AbstractMapEntry
__AbstractMapEntry = __AbstractMapEntry
from builtins import int
 
class UnmodifiableMapEntry():
    """org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableMapEntry) -> 'UnmodifiableMapEntry':
        return UnmodifiableMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableMapEntry):
        """
        Dynamic initializer for UnmodifiableMapEntry.
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
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object.__wrap(super(AbstractKeyValue, self).getValue())

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = __UnmodifiableMapEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntry.hashCode()"""
        return int.__wrap(super(AbstractMapEntry, self).hashCode())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry.setValue(V)"""
        return object.__wrap(super(__UnmodifiableMapEntry, self).setValue(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object.__wrap(super(AbstractKeyValue, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str.__wrap(super(AbstractKeyValue, self).toString())

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
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = __UnmodifiableMapEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry(K,V)"""
        val = __UnmodifiableMapEntry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapEntry, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.AbstractKeyValue
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as __AbstractKeyValue
__AbstractKeyValue = __AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
 
class AbstractKeyValue(ABC):
    """org.apache.commons.collections4.keyvalue.AbstractKeyValue"""
 
    @staticmethod
    def __wrap(java_value: __AbstractKeyValue) -> 'AbstractKeyValue':
        return AbstractKeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractKeyValue):
        """
        Dynamic initializer for AbstractKeyValue.
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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object.__wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object.__wrap(super(AbstractKeyValue, self).getKey())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str.__wrap(super(AbstractKeyValue, self).toString())

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
 
 
# CLASS: org.apache.commons.collections4.keyvalue.MultiKey
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.keyvalue.MultiKey as __MultiKey
__MultiKey = __MultiKey
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MultiKey():
    """org.apache.commons.collections4.keyvalue.MultiKey"""
 
    @staticmethod
    def __wrap(java_value: __MultiKey) -> 'MultiKey':
        return MultiKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiKey):
        """
        Dynamic initializer for MultiKey.
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
    def getKey(self, arg0: int) -> object:
        """public K org.apache.commons.collections4.keyvalue.MultiKey.getKey(int)"""
        return object.__wrap(super(__MultiKey, self).getKey(__int.valueOf(arg0)))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.MultiKey.size()"""
        return int.__wrap(super(MultiKey, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.MultiKey.equals(java.lang.Object)"""
        return bool.__wrap(super(__MultiKey, self).equals(arg0))

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.MultiKey.toString()"""
        return str.__wrap(super(MultiKey, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.MultiKey.hashCode()"""
        return int.__wrap(super(MultiKey, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K)"""
        val = __MultiKey(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K,K,K)"""
        val = __MultiKey(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getKeys(self) -> List[object]:
        """public K[] org.apache.commons.collections4.keyvalue.MultiKey.getKeys()"""
        return List[object].__wrap(super(MultiKey, self).getKeys())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Object', arg1: bool):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K[],boolean)"""
        val = __MultiKey(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K,K,K,K)"""
        val = __MultiKey(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K,K)"""
        val = __MultiKey(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Object'):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K[])"""
        val = __MultiKey(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.DefaultMapEntry
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as __AbstractKeyValue
__AbstractKeyValue = __AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.keyvalue.DefaultMapEntry as __DefaultMapEntry
__DefaultMapEntry = __DefaultMapEntry
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.keyvalue.AbstractMapEntry as __AbstractMapEntry
__AbstractMapEntry = __AbstractMapEntry
from builtins import int
 
class DefaultMapEntry():
    """org.apache.commons.collections4.keyvalue.DefaultMapEntry"""
 
    @staticmethod
    def __wrap(java_value: __DefaultMapEntry) -> 'DefaultMapEntry':
        return DefaultMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultMapEntry):
        """
        Dynamic initializer for DefaultMapEntry.
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
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object.__wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntry.hashCode()"""
        return int.__wrap(super(AbstractMapEntry, self).hashCode())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object.__wrap(super(AbstractKeyValue, self).getKey())

    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.DefaultMapEntry(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = __DefaultMapEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str.__wrap(super(AbstractKeyValue, self).toString())

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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntry.setValue(V)"""
        return object.__wrap(super(__AbstractMapEntry, self).setValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.DefaultMapEntry(K,V)"""
        val = __DefaultMapEntry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapEntry, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.DefaultMapEntry(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = __DefaultMapEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.TiedMapEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.keyvalue.TiedMapEntry as __TiedMapEntry
__TiedMapEntry = __TiedMapEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class TiedMapEntry():
    """org.apache.commons.collections4.keyvalue.TiedMapEntry"""
 
    @staticmethod
    def __wrap(java_value: __TiedMapEntry) -> 'TiedMapEntry':
        return TiedMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiedMapEntry):
        """
        Dynamic initializer for TiedMapEntry.
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
        """public K org.apache.commons.collections4.keyvalue.TiedMapEntry.getKey()"""
        return object.__wrap(super(TiedMapEntry, self).getKey())

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
    def __init__(self, arg0: 'Map', arg1: object):
        """public org.apache.commons.collections4.keyvalue.TiedMapEntry(java.util.Map<K, V>,K)"""
        val = __TiedMapEntry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.TiedMapEntry.setValue(V)"""
        return object.__wrap(super(__TiedMapEntry, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.TiedMapEntry.toString()"""
        return str.__wrap(super(TiedMapEntry, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.TiedMapEntry.getValue()"""
        return object.__wrap(super(TiedMapEntry, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.TiedMapEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__TiedMapEntry, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.TiedMapEntry.hashCode()"""
        return int.__wrap(super(TiedMapEntry, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.AbstractMapEntry
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as __AbstractKeyValue
__AbstractKeyValue = __AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
import org.apache.commons.collections4.keyvalue.AbstractMapEntry as __AbstractMapEntry
__AbstractMapEntry = __AbstractMapEntry
from builtins import int
 
class AbstractMapEntry(ABC):
    """org.apache.commons.collections4.keyvalue.AbstractMapEntry"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMapEntry) -> 'AbstractMapEntry':
        return AbstractMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMapEntry):
        """
        Dynamic initializer for AbstractMapEntry.
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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object.__wrap(super(AbstractKeyValue, self).getValue())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntry.setValue(V)"""
        return object.__wrap(super(__AbstractMapEntry, self).setValue(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntry.hashCode()"""
        return int.__wrap(super(AbstractMapEntry, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object.__wrap(super(AbstractKeyValue, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapEntry, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str.__wrap(super(AbstractKeyValue, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator as __AbstractMapEntryDecorator
__AbstractMapEntryDecorator = __AbstractMapEntryDecorator
from builtins import object
import java.lang.Long as __long
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractMapEntryDecorator(ABC):
    """org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMapEntryDecorator) -> 'AbstractMapEntryDecorator':
        return AbstractMapEntryDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMapEntryDecorator):
        """
        Dynamic initializer for AbstractMapEntryDecorator.
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
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator(java.util.Map$Entry<K, V>)"""
        val = __AbstractMapEntryDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.toString()"""
        return str.__wrap(super(AbstractMapEntryDecorator, self).toString())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.setValue(V)"""
        return object.__wrap(super(__AbstractMapEntryDecorator, self).setValue(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapEntryDecorator, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getKey()"""
        return object.__wrap(super(AbstractMapEntryDecorator, self).getKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapEntryDecorator, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getValue()"""
        return object.__wrap(super(AbstractMapEntryDecorator, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()