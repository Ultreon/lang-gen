from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.keyvalue.DefaultKeyValue as _DefaultKeyValue
_DefaultKeyValue = _DefaultKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as _AbstractKeyValue
_AbstractKeyValue = _AbstractKeyValue
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultKeyValue():
    """org.apache.commons.collections4.keyvalue.DefaultKeyValue"""
 
    @staticmethod
    def _wrap(java_value: _DefaultKeyValue) -> 'DefaultKeyValue':
        return DefaultKeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultKeyValue):
        """
        Dynamic initializer for DefaultKeyValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultKeyValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultKeyValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = _DefaultKeyValue(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = _DefaultKeyValue(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.DefaultKeyValue.equals(java.lang.Object)"""
        return bool._wrap(super(_DefaultKeyValue, self).equals(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.DefaultKeyValue.setValue(V)"""
        return object._wrap(super(_DefaultKeyValue, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str._wrap(super(AbstractKeyValue, self).toString())

    @overload
    def setKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.keyvalue.DefaultKeyValue.setKey(K)"""
        return object._wrap(super(_DefaultKeyValue, self).setKey(arg0))

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
    def toMapEntry(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.keyvalue.DefaultKeyValue.toMapEntry()"""
        return 'Entry.Map$Entry'._wrap(super(DefaultKeyValue, self).toMapEntry())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object._wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = _DefaultKeyValue()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.DefaultKeyValue.hashCode()"""
        return int._wrap(super(DefaultKeyValue, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = _DefaultKeyValue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(K,V)"""
        val = _DefaultKeyValue(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object._wrap(super(AbstractKeyValue, self).getKey())

 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.DefaultKeyValue
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.keyvalue.DefaultKeyValue as _DefaultKeyValue
_DefaultKeyValue = _DefaultKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as _AbstractKeyValue
_AbstractKeyValue = _AbstractKeyValue
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultKeyValue():
    """org.apache.commons.collections4.keyvalue.DefaultKeyValue"""
 
    @staticmethod
    def _wrap(java_value: _DefaultKeyValue) -> 'DefaultKeyValue':
        return DefaultKeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultKeyValue):
        """
        Dynamic initializer for DefaultKeyValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultKeyValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultKeyValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = _DefaultKeyValue(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = _DefaultKeyValue(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.DefaultKeyValue.equals(java.lang.Object)"""
        return bool._wrap(super(_DefaultKeyValue, self).equals(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.DefaultKeyValue.setValue(V)"""
        return object._wrap(super(_DefaultKeyValue, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str._wrap(super(AbstractKeyValue, self).toString())

    @overload
    def setKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.keyvalue.DefaultKeyValue.setKey(K)"""
        return object._wrap(super(_DefaultKeyValue, self).setKey(arg0))

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
    def toMapEntry(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.keyvalue.DefaultKeyValue.toMapEntry()"""
        return 'Entry.Map$Entry'._wrap(super(DefaultKeyValue, self).toMapEntry())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object._wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = _DefaultKeyValue()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.DefaultKeyValue.hashCode()"""
        return int._wrap(super(DefaultKeyValue, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue()"""
        val = _DefaultKeyValue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.DefaultKeyValue(K,V)"""
        val = _DefaultKeyValue(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object._wrap(super(AbstractKeyValue, self).getKey())

 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.DefaultKeyValue 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry
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
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as _AbstractKeyValue
_AbstractKeyValue = _AbstractKeyValue
import org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry as _UnmodifiableMapEntry
_UnmodifiableMapEntry = _UnmodifiableMapEntry
import org.apache.commons.collections4.keyvalue.AbstractMapEntry as _AbstractMapEntry
_AbstractMapEntry = _AbstractMapEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableMapEntry():
    """org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableMapEntry) -> 'UnmodifiableMapEntry':
        return UnmodifiableMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableMapEntry):
        """
        Dynamic initializer for UnmodifiableMapEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableMapEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableMapEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = _UnmodifiableMapEntry(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str._wrap(super(AbstractKeyValue, self).toString())

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
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = _UnmodifiableMapEntry(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry(K,V)"""
        val = _UnmodifiableMapEntry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object._wrap(super(AbstractKeyValue, self).getValue())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapEntry, self).equals(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object._wrap(super(AbstractKeyValue, self).getKey())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.UnmodifiableMapEntry.setValue(V)"""
        return object._wrap(super(_UnmodifiableMapEntry, self).setValue(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntry.hashCode()"""
        return int._wrap(super(AbstractMapEntry, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.DefaultMapEntry
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
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as _AbstractKeyValue
_AbstractKeyValue = _AbstractKeyValue
import org.apache.commons.collections4.keyvalue.DefaultMapEntry as _DefaultMapEntry
_DefaultMapEntry = _DefaultMapEntry
import org.apache.commons.collections4.keyvalue.AbstractMapEntry as _AbstractMapEntry
_AbstractMapEntry = _AbstractMapEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultMapEntry():
    """org.apache.commons.collections4.keyvalue.DefaultMapEntry"""
 
    @staticmethod
    def _wrap(java_value: _DefaultMapEntry) -> 'DefaultMapEntry':
        return DefaultMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultMapEntry):
        """
        Dynamic initializer for DefaultMapEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultMapEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultMapEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntry.setValue(V)"""
        return object._wrap(super(_AbstractMapEntry, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str._wrap(super(AbstractKeyValue, self).toString())

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
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.DefaultMapEntry(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = _DefaultMapEntry(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object._wrap(super(AbstractKeyValue, self).getValue())

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
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.keyvalue.DefaultMapEntry(org.apache.commons.collections4.KeyValue<? extends K, ? extends V>)"""
        val = _DefaultMapEntry(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.DefaultMapEntry(K,V)"""
        val = _DefaultMapEntry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapEntry, self).equals(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object._wrap(super(AbstractKeyValue, self).getKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntry.hashCode()"""
        return int._wrap(super(AbstractMapEntry, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Map.Entry as Entry
import org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator as _AbstractMapEntryDecorator
_AbstractMapEntryDecorator = _AbstractMapEntryDecorator
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMapEntryDecorator():
    """org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMapEntryDecorator) -> 'AbstractMapEntryDecorator':
        return AbstractMapEntryDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMapEntryDecorator):
        """
        Dynamic initializer for AbstractMapEntryDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMapEntryDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMapEntryDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator(java.util.Map$Entry<K, V>)"""
        val = _AbstractMapEntryDecorator(arg0)
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getValue()"""
        return object._wrap(super(AbstractMapEntryDecorator, self).getValue())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapEntryDecorator, self).equals(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getKey()"""
        return object._wrap(super(AbstractMapEntryDecorator, self).getKey())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.toString()"""
        return str._wrap(super(AbstractMapEntryDecorator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.setValue(V)"""
        return object._wrap(super(_AbstractMapEntryDecorator, self).setValue(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.hashCode()"""
        return int._wrap(super(AbstractMapEntryDecorator, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.TiedMapEntry
from builtins import str
import org.apache.commons.collections4.keyvalue.TiedMapEntry as _TiedMapEntry
_TiedMapEntry = _TiedMapEntry
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiedMapEntry():
    """org.apache.commons.collections4.keyvalue.TiedMapEntry"""
 
    @staticmethod
    def _wrap(java_value: _TiedMapEntry) -> 'TiedMapEntry':
        return TiedMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiedMapEntry):
        """
        Dynamic initializer for TiedMapEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiedMapEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiedMapEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.TiedMapEntry.getKey()"""
        return object._wrap(super(TiedMapEntry, self).getKey())

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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.TiedMapEntry.setValue(V)"""
        return object._wrap(super(_TiedMapEntry, self).setValue(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.TiedMapEntry.getValue()"""
        return object._wrap(super(TiedMapEntry, self).getValue())

    @overload
    def __init__(self, arg0: 'Map', arg1: object):
        """public org.apache.commons.collections4.keyvalue.TiedMapEntry(java.util.Map<K, V>,K)"""
        val = _TiedMapEntry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.TiedMapEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_TiedMapEntry, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.TiedMapEntry.toString()"""
        return str._wrap(super(TiedMapEntry, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.TiedMapEntry.hashCode()"""
        return int._wrap(super(TiedMapEntry, self).hashCode())

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
 
 
# CLASS: org.apache.commons.collections4.keyvalue.MultiKey
from builtins import str
import org.apache.commons.collections4.keyvalue.MultiKey as _MultiKey
_MultiKey = _MultiKey
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiKey():
    """org.apache.commons.collections4.keyvalue.MultiKey"""
 
    @staticmethod
    def _wrap(java_value: _MultiKey) -> 'MultiKey':
        return MultiKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiKey):
        """
        Dynamic initializer for MultiKey.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiKey__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiKey__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.MultiKey.hashCode()"""
        return int._wrap(super(MultiKey, self).hashCode())

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
    def getKeys(self) -> List[object]:
        """public K[] org.apache.commons.collections4.keyvalue.MultiKey.getKeys()"""
        return List[object]._wrap(super(MultiKey, self).getKeys())

    @overload
    def __init__(self, arg0: 'Object'):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K[])"""
        val = _MultiKey(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K,K)"""
        val = _MultiKey(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K,K,K,K)"""
        val = _MultiKey(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def getKey(self, arg0: int) -> object:
        """public K org.apache.commons.collections4.keyvalue.MultiKey.getKey(int)"""
        return object._wrap(super(_MultiKey, self).getKey(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K,K,K)"""
        val = _MultiKey(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.MultiKey.toString()"""
        return str._wrap(super(MultiKey, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.MultiKey.equals(java.lang.Object)"""
        return bool._wrap(super(_MultiKey, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K,K)"""
        val = _MultiKey(arg0, arg1)
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.MultiKey.size()"""
        return int._wrap(super(MultiKey, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Object', arg1: bool):
        """public org.apache.commons.collections4.keyvalue.MultiKey(K[],boolean)"""
        val = _MultiKey(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.AbstractMapEntry
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
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as _AbstractKeyValue
_AbstractKeyValue = _AbstractKeyValue
import org.apache.commons.collections4.keyvalue.AbstractMapEntry as _AbstractMapEntry
_AbstractMapEntry = _AbstractMapEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMapEntry():
    """org.apache.commons.collections4.keyvalue.AbstractMapEntry"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMapEntry) -> 'AbstractMapEntry':
        return AbstractMapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMapEntry):
        """
        Dynamic initializer for AbstractMapEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMapEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMapEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntry.setValue(V)"""
        return object._wrap(super(_AbstractMapEntry, self).setValue(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object._wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str._wrap(super(AbstractKeyValue, self).toString())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapEntry, self).equals(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object._wrap(super(AbstractKeyValue, self).getKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntry.hashCode()"""
        return int._wrap(super(AbstractMapEntry, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.keyvalue.AbstractKeyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
import org.apache.commons.collections4.keyvalue.AbstractKeyValue as _AbstractKeyValue
_AbstractKeyValue = _AbstractKeyValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractKeyValue():
    """org.apache.commons.collections4.keyvalue.AbstractKeyValue"""
 
    @staticmethod
    def _wrap(java_value: _AbstractKeyValue) -> 'AbstractKeyValue':
        return AbstractKeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractKeyValue):
        """
        Dynamic initializer for AbstractKeyValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractKeyValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractKeyValue__wrapper":
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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractKeyValue.getValue()"""
        return object._wrap(super(AbstractKeyValue, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractKeyValue.toString()"""
        return str._wrap(super(AbstractKeyValue, self).toString())

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractKeyValue.getKey()"""
        return object._wrap(super(AbstractKeyValue, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())