from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.registry.Registry as _Registry
_Registry = _Registry
import dev.ultreon.quantum.registry.Registry as _Registry_Builder
_Builder = _Registry_Builder.Builder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.registry.Registry.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
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
    def doNotSync(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.doNotSync()"""
        return 'Builder'._wrap(super(Builder, self).doNotSync())

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

    @overload
    def build(self) -> 'Registry':
        """public dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry$Builder.build()"""
        return 'Registry'._wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Identifier', *arg1: object):
        """public dev.ultreon.quantum.registry.Registry$Builder(dev.ultreon.quantum.util.Identifier,T...)"""
        val = _Builder(arg0, arg1)
        self.__wrapper = val

    @overload
    def allowOverride(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.allowOverride()"""
        return 'Builder'._wrap(super(Builder, self).allowOverride())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.registry.Registry$Builder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.registry.Registry as _Registry
_Registry = _Registry
import dev.ultreon.quantum.registry.Registry as _Registry_Builder
_Builder = _Registry_Builder.Builder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.registry.Registry.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
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
    def doNotSync(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.doNotSync()"""
        return 'Builder'._wrap(super(Builder, self).doNotSync())

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

    @overload
    def build(self) -> 'Registry':
        """public dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry$Builder.build()"""
        return 'Registry'._wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Identifier', *arg1: object):
        """public dev.ultreon.quantum.registry.Registry$Builder(dev.ultreon.quantum.util.Identifier,T...)"""
        val = _Builder(arg0, arg1)
        self.__wrapper = val

    @overload
    def allowOverride(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.allowOverride()"""
        return 'Builder'._wrap(super(Builder, self).allowOverride())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.registry.Registry$Builder 
 
 
# CLASS: dev.ultreon.quantum.registry.Registry
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.libs.commons.v0.Logger as _Logger
_Logger = _Logger
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import dev.ultreon.quantum.registry.AbstractRegistry as _AbstractRegistry
_AbstractRegistry = _AbstractRegistry
import org.reactivestreams.Subscriber as Subscriber
import java.util.Optional as _Optional
_Optional = _Optional
try:
    from pyquantum import tags
except ImportError:
    tags = _import_once("pyquantum.tags")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.registry.RegistryKey as _RegistryKey
_RegistryKey = _RegistryKey
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import java.util.Optional as Optional
import dev.ultreon.quantum.registry.Registry as _Registry
_Registry = _Registry
import dev.ultreon.quantum.registry.Registry as _Registry_Builder
_Builder = _Registry_Builder.Builder
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.tags.NamedTag as _NamedTag
_NamedTag = _NamedTag
import java.lang.Long as _long
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Registry():
    """dev.ultreon.quantum.registry.Registry"""
 
    @staticmethod
    def _wrap(java_value: _Registry) -> 'Registry':
        return Registry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Registry):
        """
        Dynamic initializer for Registry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Registry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Registry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def subscribe(self, arg0: 'Subscriber'):
        """public void dev.ultreon.quantum.registry.Registry.subscribe(org.reactivestreams.Subscriber<? super dev.ultreon.quantum.registry.Registry<T>>)"""
        super(_Registry, self).subscribe(arg0)

    @staticmethod
    @overload
    def builder(arg0: 'Identifier', *arg1: object) -> 'Builder':
        """public static <T> dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry.builder(dev.ultreon.quantum.util.Identifier,T...)"""
        return Builder._wrap(_Registry.builder(arg0, arg1))

    @overload
    def getId(self, arg0: object) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.Registry.getId(T)"""
        return 'util.Identifier'._wrap(super(_Registry, self).getId(arg0))

    @overload
    def unsubscribe(self, arg0: 'Subscriber'):
        """public void dev.ultreon.quantum.registry.Registry.unsubscribe(org.reactivestreams.Subscriber<? super dev.ultreon.quantum.registry.Registry<T>>)"""
        super(_Registry, self).unsubscribe(arg0)

    @overload
    def byId(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.registry.Registry.byId(int)"""
        return object._wrap(super(_Registry, self).byId(_int.valueOf(arg0)))

    @overload
    def createTag(self, arg0: 'Identifier') -> 'tags.NamedTag':
        """public dev.ultreon.quantum.tags.NamedTag<T> dev.ultreon.quantum.registry.Registry.createTag(dev.ultreon.quantum.util.Identifier)"""
        return 'tags.NamedTag'._wrap(super(_Registry, self).createTag(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'RegistryKey') -> object:
        """public T dev.ultreon.quantum.registry.Registry.get(dev.ultreon.quantum.registry.RegistryKey<T>)"""
        return object._wrap(super(_Registry, self).get(arg0))

    @overload
    def contains(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.contains(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_Registry, self).contains(arg0))

    @overload
    def dumpRegistry(self):
        """public void dev.ultreon.quantum.registry.Registry.dumpRegistry()"""
        super(Registry, self).dumpRegistry()

    @overload
    def getRawId(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.registry.Registry.getRawId(T)"""
        return int._wrap(super(_Registry, self).getRawId(arg0))

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
    def getDumpLogger() -> 'v0.Logger':
        """public static dev.ultreon.libs.commons.v0.Logger dev.ultreon.quantum.registry.Registry.getDumpLogger()"""
        return v0.Logger._wrap(_Registry.getDumpLogger())

    @overload
    def key(self) -> 'RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>> dev.ultreon.quantum.registry.Registry.key()"""
        return 'RegistryKey'._wrap(super(Registry, self).key())

        @staticmethod
        @overload
        def freeze():
            """public static void dev.ultreon.quantum.registry.Registry.freeze()"""
            _Registry.freeze()

    @override
    @overload
    def values(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.registry.Registry.values()"""
        return 'List'._wrap(super(Registry, self).values())

    @overload
    def isSyncDisabled(self) -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.isSyncDisabled()"""
        return bool._wrap(super(Registry, self).isSyncDisabled())

    @staticmethod
    @overload
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry.create(dev.ultreon.quantum.util.Identifier,T...)"""
        return Registry._wrap(_Registry.create(arg0, arg1))

    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.Registry.id()"""
        return 'util.Identifier'._wrap(super(Registry, self).id())

    @override
    @overload
    def keys(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.registry.RegistryKey<T>> dev.ultreon.quantum.registry.Registry.keys()"""
        return 'List'._wrap(super(Registry, self).keys())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getTag(self, arg0: 'Identifier') -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.tags.NamedTag<T>> dev.ultreon.quantum.registry.Registry.getTag(dev.ultreon.quantum.util.Identifier)"""
        return 'Optional'._wrap(super(_Registry, self).getTag(arg0))

    @overload
    def isOverrideAllowed(self) -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.isOverrideAllowed()"""
        return bool._wrap(super(Registry, self).isOverrideAllowed())

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.isFrozen()"""
        return bool._wrap(super(Registry, self).isFrozen())

    @overload
    def ids(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.registry.Registry.ids()"""
        return 'List'._wrap(super(Registry, self).ids())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def register(self, arg0: 'RegistryKey', arg1: object):
        """public void dev.ultreon.quantum.registry.Registry.register(dev.ultreon.quantum.registry.RegistryKey<T>,T)"""
        super(_Registry, self).register(arg0, arg1)

        @staticmethod
        @overload
        def dump():
            """public static void dev.ultreon.quantum.registry.Registry.dump()"""
            _Registry.dump()

    @override
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.quantum.registry.RegistryKey<T>, T>> dev.ultreon.quantum.registry.Registry.entries()"""
        return 'Set'._wrap(super(Registry, self).entries())

    @overload
    def publish(self):
        """public void dev.ultreon.quantum.registry.Registry.publish()"""
        super(Registry, self).publish()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def builder(arg0: str, *arg1: object) -> 'Builder':
        """public static <T> dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry.builder(java.lang.String,T...)"""
        return Builder._wrap(_Registry.builder(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> 'RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.Registry.getKey(T)"""
        return 'RegistryKey'._wrap(super(_Registry, self).getKey(arg0))

    @overload
    def register(self, arg0: 'Identifier', arg1: object):
        """public void dev.ultreon.quantum.registry.Registry.register(dev.ultreon.quantum.util.Identifier,T)"""
        super(_Registry, self).register(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: 'Identifier') -> object:
        """public T dev.ultreon.quantum.registry.Registry.get(dev.ultreon.quantum.util.Identifier)"""
        return object._wrap(super(_Registry, self).get(arg0))

    @staticmethod
    @overload
    def getRegistries() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.Registry.getRegistries()"""
        return Collection._wrap(_Registry.getRegistries())

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.quantum.registry.Registry.getType()"""
        return 'type.Class'._wrap(super(Registry, self).getType())

    @staticmethod
    @overload
    def setDumpLogger(arg0: 'Logger'):
        """public static void dev.ultreon.quantum.registry.Registry.setDumpLogger(dev.ultreon.libs.commons.v0.Logger)"""
        _Registry.setDumpLogger(arg0)

    @staticmethod
    @overload
    def getRegistry(arg0: 'RegistryKey') -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry.getRegistry(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>)"""
        return Registry._wrap(_Registry.getRegistry(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def random(self) -> object:
        """public V dev.ultreon.quantum.registry.AbstractRegistry.random()"""
        return object._wrap(super(AbstractRegistry, self).random())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


Registry.REGISTRY = Registry._wrap(_REGISTRY.REGISTRY) 
 
 
# CLASS: dev.ultreon.quantum.registry.DeferRegistry
import groovy.lang.Closure as Closure
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.quantum.registry.DeferredElement as _DeferredElement
_DeferredElement = _DeferredElement
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.registry.DeferRegistry as _DeferRegistry
_DeferRegistry = _DeferRegistry
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferRegistry():
    """dev.ultreon.quantum.registry.DeferRegistry"""
 
    @staticmethod
    def _wrap(java_value: _DeferRegistry) -> 'DeferRegistry':
        return DeferRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeferRegistry):
        """
        Dynamic initializer for DeferRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeferRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeferRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: str, arg1: 'Registry') -> 'DeferRegistry':
        """public static <T> dev.ultreon.quantum.registry.DeferRegistry<T> dev.ultreon.quantum.registry.DeferRegistry.of(java.lang.String,dev.ultreon.quantum.registry.Registry<T>)"""
        return DeferRegistry._wrap(_DeferRegistry.of(arg0, arg1))

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

    @overload
    def register(self):
        """public void dev.ultreon.quantum.registry.DeferRegistry.register()"""
        super(DeferRegistry, self).register()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def defer(self, arg0: str, arg1: 'Supplier') -> 'DeferredElement':
        """public <C extends T> dev.ultreon.quantum.registry.DeferredElement<C> dev.ultreon.quantum.registry.DeferRegistry.defer(java.lang.String,java.util.function.Supplier<C>)"""
        return 'DeferredElement'._wrap(super(_DeferRegistry, self).defer(arg0, arg1))

    @overload
    def defer(self, arg0: str, arg1: 'Closure') -> 'DeferredElement':
        """public <C extends T> dev.ultreon.quantum.registry.DeferredElement<C> dev.ultreon.quantum.registry.DeferRegistry.defer(java.lang.String,groovy.lang.Closure<C>)"""
        return 'DeferredElement'._wrap(super(_DeferRegistry, self).defer(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.registry.CustomKeyRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.registry.CustomKeyRegistry as _CustomKeyRegistry
_CustomKeyRegistry = _CustomKeyRegistry
import java.lang.Integer as _int
import dev.ultreon.quantum.text.TextKey as _TextKey
_TextKey = _TextKey
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CustomKeyRegistry():
    """dev.ultreon.quantum.registry.CustomKeyRegistry"""
 
    @staticmethod
    def _wrap(java_value: _CustomKeyRegistry) -> 'CustomKeyRegistry':
        return CustomKeyRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CustomKeyRegistry):
        """
        Dynamic initializer for CustomKeyRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CustomKeyRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CustomKeyRegistry__wrapper":
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

    @staticmethod
    @overload
    def get(arg0: 'Identifier') -> 'text.TextKey':
        """public static dev.ultreon.quantum.text.TextKey dev.ultreon.quantum.registry.CustomKeyRegistry.get(dev.ultreon.quantum.util.Identifier)"""
        return text.TextKey._wrap(_CustomKeyRegistry.get(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.CustomKeyRegistry()"""
        val = _CustomKeyRegistry()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.CustomKeyRegistry()"""
        val = _CustomKeyRegistry()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.registry.RegistryKeys
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.registry.RegistryKeys as _RegistryKeys
_RegistryKeys = _RegistryKeys
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegistryKeys():
    """dev.ultreon.quantum.registry.RegistryKeys"""
 
    @staticmethod
    def _wrap(java_value: _RegistryKeys) -> 'RegistryKeys':
        return RegistryKeys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegistryKeys):
        """
        Dynamic initializer for RegistryKeys.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegistryKeys__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegistryKeys__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.SoundEvent>> dev.ultreon.quantum.registry.RegistryKeys.SOUND_EVENT
    SOUND_EVENT: 'RegistryKey' = _wrap(_RegistryKey.SOUND_EVENT)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.EntityType<?>>> dev.ultreon.quantum.registry.RegistryKeys.ENTITY_TYPE
    ENTITY_TYPE: 'RegistryKey' = _wrap(_RegistryKey.ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.particles.ParticleType>> dev.ultreon.quantum.registry.RegistryKeys.PARTICLE_TYPE
    PARTICLE_TYPE: 'RegistryKey' = _wrap(_RegistryKey.PARTICLE_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.weather.Weather>> dev.ultreon.quantum.registry.RegistryKeys.WEATHER
    WEATHER: 'RegistryKey' = _wrap(_RegistryKey.WEATHER)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.Block>> dev.ultreon.quantum.registry.RegistryKeys.BLOCK
    BLOCK: 'RegistryKey' = _wrap(_RegistryKey.BLOCK)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.recipe.RecipeType<?>>> dev.ultreon.quantum.registry.RegistryKeys.RECIPE_TYPE
    RECIPE_TYPE: 'RegistryKey' = _wrap(_RegistryKey.RECIPE_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.damagesource.DamageSource>> dev.ultreon.quantum.registry.RegistryKeys.DAMAGE_SOURCE
    DAMAGE_SOURCE: 'RegistryKey' = _wrap(_RegistryKey.DAMAGE_SOURCE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.menu.MenuType<?>>> dev.ultreon.quantum.registry.RegistryKeys.MENU_TYPE
    MENU_TYPE: 'RegistryKey' = _wrap(_RegistryKey.MENU_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.entity.BlockEntityType<?>>> dev.ultreon.quantum.registry.RegistryKeys.BLOCK_ENTITY_TYPE
    BLOCK_ENTITY_TYPE: 'RegistryKey' = _wrap(_RegistryKey.BLOCK_ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.item.Item>> dev.ultreon.quantum.registry.RegistryKeys.ITEM
    ITEM: 'RegistryKey' = _wrap(_RegistryKey.ITEM)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.Biome>> dev.ultreon.quantum.registry.RegistryKeys.BIOME
    BIOME: 'RegistryKey' = _wrap(_RegistryKey.BIOME)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.gen.noise.NoiseConfig>> dev.ultreon.quantum.registry.RegistryKeys.NOISE_SETTINGS
    NOISE_SETTINGS: 'RegistryKey' = _wrap(_RegistryKey.NOISE_SETTINGS)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.Attribute>> dev.ultreon.quantum.registry.RegistryKeys.ATTRIBUTE
    ATTRIBUTE: 'RegistryKey' = _wrap(_RegistryKey.ATTRIBUTE)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.RegistryKeys()"""
        val = _RegistryKeys()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.RegistryKeys()"""
        val = _RegistryKeys()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.registry.Registries
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.registry.Registries as _Registries
_Registries = _Registries
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.registry.Registry as _Registry
_Registry = _Registry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Registries():
    """dev.ultreon.quantum.registry.Registries"""
 
    @staticmethod
    def _wrap(java_value: _Registries) -> 'Registries':
        return Registries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Registries):
        """
        Dynamic initializer for Registries.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Registries__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Registries__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.gen.noise.NoiseConfig> dev.ultreon.quantum.registry.Registries.NOISE_SETTINGS
    NOISE_SETTINGS: 'Registry' = _wrap(_Registry.NOISE_SETTINGS)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.particles.ParticleType> dev.ultreon.quantum.registry.Registries.PARTICLE_TYPES
    PARTICLE_TYPES: 'Registry' = _wrap(_Registry.PARTICLE_TYPES)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.SoundEvent> dev.ultreon.quantum.registry.Registries.SOUND_EVENT
    SOUND_EVENT: 'Registry' = _wrap(_Registry.SOUND_EVENT)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.Attribute> dev.ultreon.quantum.registry.Registries.ATTRIBUTE
    ATTRIBUTE: 'Registry' = _wrap(_Registry.ATTRIBUTE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.Biome> dev.ultreon.quantum.registry.Registries.BIOME
    BIOME: 'Registry' = _wrap(_Registry.BIOME)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.recipe.RecipeType<?>> dev.ultreon.quantum.registry.Registries.RECIPE_TYPE
    RECIPE_TYPE: 'Registry' = _wrap(_Registry.RECIPE_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.menu.MenuType<?>> dev.ultreon.quantum.registry.Registries.MENU_TYPE
    MENU_TYPE: 'Registry' = _wrap(_Registry.MENU_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.weather.Weather> dev.ultreon.quantum.registry.Registries.WEATHER
    WEATHER: 'Registry' = _wrap(_Registry.WEATHER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.entity.BlockEntityType<?>> dev.ultreon.quantum.registry.Registries.BLOCK_ENTITY_TYPE
    BLOCK_ENTITY_TYPE: 'Registry' = _wrap(_Registry.BLOCK_ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.EntityType<?>> dev.ultreon.quantum.registry.Registries.ENTITY_TYPE
    ENTITY_TYPE: 'Registry' = _wrap(_Registry.ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.Registries.REGISTRY
    REGISTRY: 'Registry' = _wrap(_Registry.REGISTRY)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.registry.Registries.BLOCK
    BLOCK: 'Registry' = _wrap(_Registry.BLOCK)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.damagesource.DamageSource> dev.ultreon.quantum.registry.Registries.DAMAGE_SOURCE
    DAMAGE_SOURCE: 'Registry' = _wrap(_Registry.DAMAGE_SOURCE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.item.Item> dev.ultreon.quantum.registry.Registries.ITEM
    ITEM: 'Registry' = _wrap(_Registry.ITEM)


        @staticmethod
        @overload
        def nopInit():
            """public static void dev.ultreon.quantum.registry.Registries.nopInit()"""
            _Registries.nopInit()

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
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registries.create(dev.ultreon.quantum.util.Identifier,T...)"""
        return Registry._wrap(_Registries.create(arg0, arg1))

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

    @staticmethod
    @overload
    def create(arg0: 'RegistryKey', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registries.create(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>,T...)"""
        return Registry._wrap(_Registries.create(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.Registries()"""
        val = _Registries()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.Registries()"""
        val = _Registries()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.registry.AbstractRegistry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.registry.AbstractRegistry as _AbstractRegistry
_AbstractRegistry = _AbstractRegistry
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractRegistry():
    """dev.ultreon.quantum.registry.AbstractRegistry"""
 
    @staticmethod
    def _wrap(java_value: _AbstractRegistry) -> 'AbstractRegistry':
        return AbstractRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractRegistry):
        """
        Dynamic initializer for AbstractRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def random(self) -> object:
        """public V dev.ultreon.quantum.registry.AbstractRegistry.random()"""
        return object._wrap(super(AbstractRegistry, self).random())

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

    @abstractmethod
    def values(self, ):
        """public abstract java.util.List<V> dev.ultreon.quantum.registry.AbstractRegistry.values()"""
        pass

    @abstractmethod
    def register(self, arg0: object, arg1: object):
        """public abstract void dev.ultreon.quantum.registry.AbstractRegistry.register(K,V)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V dev.ultreon.quantum.registry.AbstractRegistry.get(K)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.quantum.registry.AbstractRegistry.entries() throws java.lang.IllegalAccessException"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract java.util.List<K> dev.ultreon.quantum.registry.AbstractRegistry.keys()"""
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
 
 
# CLASS: dev.ultreon.quantum.registry.RegistryKey
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.registry.RegistryKey as _RegistryKey
_RegistryKey = _RegistryKey
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegistryKey():
    """dev.ultreon.quantum.registry.RegistryKey"""
 
    @staticmethod
    def _wrap(java_value: _RegistryKey) -> 'RegistryKey':
        return RegistryKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegistryKey):
        """
        Dynamic initializer for RegistryKey.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegistryKey__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegistryKey__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def registry(arg0: 'Registry') -> 'RegistryKey':
        """public static <T extends dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.RegistryKey.registry(T)"""
        return RegistryKey._wrap(_RegistryKey.registry(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.registry.RegistryKey.toString()"""
        return str._wrap(super(RegistryKey, self).toString())

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
        """public boolean dev.ultreon.quantum.registry.RegistryKey.equals(java.lang.Object)"""
        return bool._wrap(super(_RegistryKey, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.registry.RegistryKey.hashCode()"""
        return int._wrap(super(RegistryKey, self).hashCode())

    @overload
    def parent(self) -> 'RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>> dev.ultreon.quantum.registry.RegistryKey.parent()"""
        return 'RegistryKey'._wrap(super(RegistryKey, self).parent())

    @staticmethod
    @overload
    def of(arg0: 'RegistryKey', arg1: 'Identifier') -> 'RegistryKey':
        """public static <T> dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.RegistryKey.of(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>,dev.ultreon.quantum.util.Identifier)"""
        return RegistryKey._wrap(_RegistryKey.of(arg0, arg1))

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
    def __init__(self, arg0: 'RegistryKey', arg1: 'Identifier'):
        """public dev.ultreon.quantum.registry.RegistryKey(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>,dev.ultreon.quantum.util.Identifier)"""
        val = _RegistryKey(arg0, arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def registry(arg0: 'Identifier') -> 'RegistryKey':
        """public static <T extends dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.RegistryKey.registry(dev.ultreon.quantum.util.Identifier)"""
        return RegistryKey._wrap(_RegistryKey.registry(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def element(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.RegistryKey.element()"""
        return 'util.Identifier'._wrap(super(RegistryKey, self).element())


RegistryKey.ROOT = RegistryKey._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.registry.RawIdMap
import dev.ultreon.quantum.registry.RawIdMap as _RawIdMap
_RawIdMap = _RawIdMap
from abc import abstractmethod, ABC
 
class RawIdMap():
    """dev.ultreon.quantum.registry.RawIdMap"""
 
    @staticmethod
    def _wrap(java_value: _RawIdMap) -> 'RawIdMap':
        return RawIdMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RawIdMap):
        """
        Dynamic initializer for RawIdMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RawIdMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RawIdMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def byId(self, arg0: int):
        """public abstract T dev.ultreon.quantum.registry.RawIdMap.byId(int)"""
        pass

    @abstractmethod
    def getRawId(self, arg0: object):
        """public abstract int dev.ultreon.quantum.registry.RawIdMap.getRawId(T)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.registry.CommandRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import dev.ultreon.quantum.registry.CommandRegistry as _CommandRegistry
_CommandRegistry = _CommandRegistry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandRegistry():
    """dev.ultreon.quantum.registry.CommandRegistry"""
 
    @staticmethod
    def _wrap(java_value: _CommandRegistry) -> 'CommandRegistry':
        return CommandRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandRegistry):
        """
        Dynamic initializer for CommandRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.CommandRegistry()"""
        val = _CommandRegistry()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getCommands() -> 'Stream':
        """public static java.util.stream.Stream<dev.ultreon.quantum.api.commands.Command> dev.ultreon.quantum.registry.CommandRegistry.getCommands()"""
        return Stream._wrap(_CommandRegistry.getCommands())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def register(arg0: 'Command'):
        """public static void dev.ultreon.quantum.registry.CommandRegistry.register(dev.ultreon.quantum.api.commands.Command)"""
        _CommandRegistry.register(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getCommandNames() -> 'Stream':
        """public static java.util.stream.Stream<java.lang.String> dev.ultreon.quantum.registry.CommandRegistry.getCommandNames()"""
        return Stream._wrap(_CommandRegistry.getCommandNames())

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
    def get(arg0: str) -> 'commands.Command':
        """public static dev.ultreon.quantum.api.commands.Command dev.ultreon.quantum.registry.CommandRegistry.get(java.lang.String)"""
        return commands.Command._wrap(_CommandRegistry.get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.CommandRegistry()"""
        val = _CommandRegistry()
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
 
 
# CLASS: dev.ultreon.quantum.registry.DeferredElement
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.registry.DeferredElement as _DeferredElement
_DeferredElement = _DeferredElement
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferredElement():
    """dev.ultreon.quantum.registry.DeferredElement"""
 
    @staticmethod
    def _wrap(java_value: _DeferredElement) -> 'DeferredElement':
        return DeferredElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeferredElement):
        """
        Dynamic initializer for DeferredElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeferredElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeferredElement__wrapper":
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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.DeferredElement.id()"""
        return 'util.Identifier'._wrap(super(DeferredElement, self).id())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def register(self):
        """public void dev.ultreon.quantum.registry.DeferredElement.register()"""
        super(DeferredElement, self).register()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Registry', arg1: 'Supplier', arg2: 'Identifier'):
        """public dev.ultreon.quantum.registry.DeferredElement(dev.ultreon.quantum.registry.Registry<? super T>,java.util.function.Supplier<T>,dev.ultreon.quantum.util.Identifier)"""
        val = _DeferredElement(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.registry.DeferredElement.get()"""
        return object._wrap(super(DeferredElement, self).get())

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