from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.registry.Registry as __Registry_Builder
__Builder = __Registry_Builder.Builder
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.registry.Registry as __Registry
__Registry = __Registry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.registry.Registry.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def doNotSync(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.doNotSync()"""
        return 'Builder'.__wrap(super(Builder, self).doNotSync())

    @overload
    def allowOverride(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.allowOverride()"""
        return 'Builder'.__wrap(super(Builder, self).allowOverride())

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

    @overload
    def build(self) -> 'Registry':
        """public dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry$Builder.build()"""
        return 'Registry'.__wrap(super(Builder, self).build())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Identifier', *arg1: object):
        """public dev.ultreon.quantum.registry.Registry$Builder(dev.ultreon.quantum.util.Identifier,T...)"""
        val = __Builder(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.registry.Registry$Builder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.registry.Registry as __Registry_Builder
__Builder = __Registry_Builder.Builder
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.registry.Registry as __Registry
__Registry = __Registry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.registry.Registry.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def doNotSync(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.doNotSync()"""
        return 'Builder'.__wrap(super(Builder, self).doNotSync())

    @overload
    def allowOverride(self) -> 'Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry$Builder.allowOverride()"""
        return 'Builder'.__wrap(super(Builder, self).allowOverride())

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

    @overload
    def build(self) -> 'Registry':
        """public dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry$Builder.build()"""
        return 'Registry'.__wrap(super(Builder, self).build())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Identifier', *arg1: object):
        """public dev.ultreon.quantum.registry.Registry$Builder(dev.ultreon.quantum.util.Identifier,T...)"""
        val = __Builder(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.registry.Registry$Builder 
 
 
# CLASS: dev.ultreon.quantum.registry.Registry
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.registry.Registry as __Registry_Builder
__Builder = __Registry_Builder.Builder
from builtins import type
import dev.ultreon.quantum.registry.RegistryKey as __RegistryKey
__RegistryKey = __RegistryKey
import java.util.Collection as Collection
import dev.ultreon.quantum.registry.AbstractRegistry as __AbstractRegistry
__AbstractRegistry = __AbstractRegistry
import dev.ultreon.libs.commons.v0.Logger as __Logger
__Logger = __Logger
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.registry.Registry as __Registry
__Registry = __Registry
import java.lang.String as __string
import org.reactivestreams.Subscriber as Subscriber
try:
    from pyquantum import tags
except ImportError:
    tags = __import_once__("pyquantum.tags")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.util.Optional as __Optional
__Optional = __Optional
from builtins import object
import dev.ultreon.quantum.tags.NamedTag as __NamedTag
__NamedTag = __NamedTag
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.util.Optional as Optional
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class Registry():
    """dev.ultreon.quantum.registry.Registry"""
 
    @staticmethod
    def __wrap(java_value: __Registry) -> 'Registry':
        return Registry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Registry):
        """
        Dynamic initializer for Registry.
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
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.Registry.REGISTRY
    REGISTRY: 'Registry' = __wrap(__Registry.REGISTRY)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getRegistry(arg0: 'RegistryKey') -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry.getRegistry(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>)"""
        return Registry.__wrap(__Registry.getRegistry(arg0))

    @override
    @overload
    def keys(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.registry.RegistryKey<T>> dev.ultreon.quantum.registry.Registry.keys()"""
        return 'List'.__wrap(super(Registry, self).keys())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def subscribe(self, arg0: 'Subscriber'):
        """public void dev.ultreon.quantum.registry.Registry.subscribe(org.reactivestreams.Subscriber<? super dev.ultreon.quantum.registry.Registry<T>>)"""
        super(__Registry, self).subscribe(arg0)

    @staticmethod
    @overload
    def getDumpLogger() -> 'v0.Logger':
        """public static dev.ultreon.libs.commons.v0.Logger dev.ultreon.quantum.registry.Registry.getDumpLogger()"""
        return v0.Logger.__wrap(__Registry.getDumpLogger())

    @overload
    def register(self, arg0: 'Identifier', arg1: object):
        """public void dev.ultreon.quantum.registry.Registry.register(dev.ultreon.quantum.util.Identifier,T)"""
        super(__Registry, self).register(arg0, arg1)

    @overload
    def getKey(self, arg0: object) -> 'RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.Registry.getKey(T)"""
        return 'RegistryKey'.__wrap(super(__Registry, self).getKey(arg0))

    @overload
    def getTag(self, arg0: 'Identifier') -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.tags.NamedTag<T>> dev.ultreon.quantum.registry.Registry.getTag(dev.ultreon.quantum.util.Identifier)"""
        return 'Optional'.__wrap(super(__Registry, self).getTag(arg0))

    @overload
    def dumpRegistry(self):
        """public void dev.ultreon.quantum.registry.Registry.dumpRegistry()"""
        super(Registry, self).dumpRegistry()

    @overload
    def createTag(self, arg0: 'Identifier') -> 'tags.NamedTag':
        """public dev.ultreon.quantum.tags.NamedTag<T> dev.ultreon.quantum.registry.Registry.createTag(dev.ultreon.quantum.util.Identifier)"""
        return 'tags.NamedTag'.__wrap(super(__Registry, self).createTag(arg0))

    @override
    @overload
    def random(self) -> object:
        """public V dev.ultreon.quantum.registry.AbstractRegistry.random()"""
        return object.__wrap(super(AbstractRegistry, self).random())

    @overload
    def getRawId(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.registry.Registry.getRawId(T)"""
        return int.__wrap(super(__Registry, self).getRawId(arg0))

    @overload
    def byId(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.registry.Registry.byId(int)"""
        return object.__wrap(super(__Registry, self).byId(__int.valueOf(arg0)))

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.isFrozen()"""
        return bool.__wrap(super(Registry, self).isFrozen())

    @overload
    def isOverrideAllowed(self) -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.isOverrideAllowed()"""
        return bool.__wrap(super(Registry, self).isOverrideAllowed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.quantum.registry.Registry.getType()"""
        return 'type.Class'.__wrap(super(Registry, self).getType())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

        @staticmethod
        @overload
        def freeze():
            """public static void dev.ultreon.quantum.registry.Registry.freeze()"""
            __Registry.freeze()

    @overload
    def register(self, arg0: 'RegistryKey', arg1: object):
        """public void dev.ultreon.quantum.registry.Registry.register(dev.ultreon.quantum.registry.RegistryKey<T>,T)"""
        super(__Registry, self).register(arg0, arg1)

    @overload
    def contains(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.contains(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__Registry, self).contains(arg0))

    @overload
    def key(self) -> 'RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>> dev.ultreon.quantum.registry.Registry.key()"""
        return 'RegistryKey'.__wrap(super(Registry, self).key())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def setDumpLogger(arg0: 'Logger'):
        """public static void dev.ultreon.quantum.registry.Registry.setDumpLogger(dev.ultreon.libs.commons.v0.Logger)"""
        __Registry.setDumpLogger(arg0)

    @staticmethod
    @overload
    def builder(arg0: str, *arg1: object) -> 'Builder':
        """public static <T> dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry.builder(java.lang.String,T...)"""
        return Builder.__wrap(__Registry.builder(arg0, arg1))

    @staticmethod
    @overload
    def builder(arg0: 'Identifier', *arg1: object) -> 'Builder':
        """public static <T> dev.ultreon.quantum.registry.Registry$Builder<T> dev.ultreon.quantum.registry.Registry.builder(dev.ultreon.quantum.util.Identifier,T...)"""
        return Builder.__wrap(__Registry.builder(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def values(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.registry.Registry.values()"""
        return 'List'.__wrap(super(Registry, self).values())

        @staticmethod
        @overload
        def dump():
            """public static void dev.ultreon.quantum.registry.Registry.dump()"""
            __Registry.dump()

    @override
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.quantum.registry.RegistryKey<T>, T>> dev.ultreon.quantum.registry.Registry.entries()"""
        return 'Set'.__wrap(super(Registry, self).entries())

    @overload
    def unsubscribe(self, arg0: 'Subscriber'):
        """public void dev.ultreon.quantum.registry.Registry.unsubscribe(org.reactivestreams.Subscriber<? super dev.ultreon.quantum.registry.Registry<T>>)"""
        super(__Registry, self).unsubscribe(arg0)

    @overload
    def isSyncDisabled(self) -> bool:
        """public boolean dev.ultreon.quantum.registry.Registry.isSyncDisabled()"""
        return bool.__wrap(super(Registry, self).isSyncDisabled())

    @overload
    def publish(self):
        """public void dev.ultreon.quantum.registry.Registry.publish()"""
        super(Registry, self).publish()

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
    def get(self, arg0: 'RegistryKey') -> object:
        """public T dev.ultreon.quantum.registry.Registry.get(dev.ultreon.quantum.registry.RegistryKey<T>)"""
        return object.__wrap(super(__Registry, self).get(arg0))

    @overload
    def ids(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.registry.Registry.ids()"""
        return 'List'.__wrap(super(Registry, self).ids())

    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.Registry.id()"""
        return 'util.Identifier'.__wrap(super(Registry, self).id())

    @overload
    def get(self, arg0: 'Identifier') -> object:
        """public T dev.ultreon.quantum.registry.Registry.get(dev.ultreon.quantum.util.Identifier)"""
        return object.__wrap(super(__Registry, self).get(arg0))

    @overload
    def getId(self, arg0: object) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.Registry.getId(T)"""
        return 'util.Identifier'.__wrap(super(__Registry, self).getId(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registry.create(dev.ultreon.quantum.util.Identifier,T...)"""
        return Registry.__wrap(__Registry.create(arg0, arg1))

    @staticmethod
    @overload
    def getRegistries() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.Registry.getRegistries()"""
        return Collection.__wrap(__Registry.getRegistries()) 
 
 
# CLASS: dev.ultreon.quantum.registry.DeferRegistry
import groovy.lang.Closure as Closure
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.registry.DeferredElement as __DeferredElement
__DeferredElement = __DeferredElement
import dev.ultreon.quantum.registry.DeferRegistry as __DeferRegistry
__DeferRegistry = __DeferRegistry
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
 
class DeferRegistry():
    """dev.ultreon.quantum.registry.DeferRegistry"""
 
    @staticmethod
    def __wrap(java_value: __DeferRegistry) -> 'DeferRegistry':
        return DeferRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeferRegistry):
        """
        Dynamic initializer for DeferRegistry.
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
    def defer(self, arg0: str, arg1: 'Closure') -> 'DeferredElement':
        """public <C extends T> dev.ultreon.quantum.registry.DeferredElement<C> dev.ultreon.quantum.registry.DeferRegistry.defer(java.lang.String,groovy.lang.Closure<C>)"""
        return 'DeferredElement'.__wrap(super(__DeferRegistry, self).defer(arg0, arg1))

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
    def defer(self, arg0: str, arg1: 'Supplier') -> 'DeferredElement':
        """public <C extends T> dev.ultreon.quantum.registry.DeferredElement<C> dev.ultreon.quantum.registry.DeferRegistry.defer(java.lang.String,java.util.function.Supplier<C>)"""
        return 'DeferredElement'.__wrap(super(__DeferRegistry, self).defer(arg0, arg1))

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

    @staticmethod
    @overload
    def of(arg0: str, arg1: 'Registry') -> 'DeferRegistry':
        """public static <T> dev.ultreon.quantum.registry.DeferRegistry<T> dev.ultreon.quantum.registry.DeferRegistry.of(java.lang.String,dev.ultreon.quantum.registry.Registry<T>)"""
        return DeferRegistry.__wrap(__DeferRegistry.of(arg0, arg1))

    @overload
    def register(self):
        """public void dev.ultreon.quantum.registry.DeferRegistry.register()"""
        super(DeferRegistry, self).register()

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
 
 
# CLASS: dev.ultreon.quantum.registry.CustomKeyRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.registry.CustomKeyRegistry as __CustomKeyRegistry
__CustomKeyRegistry = __CustomKeyRegistry
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.text.TextKey as __TextKey
__TextKey = __TextKey
from builtins import int
 
class CustomKeyRegistry():
    """dev.ultreon.quantum.registry.CustomKeyRegistry"""
 
    @staticmethod
    def __wrap(java_value: __CustomKeyRegistry) -> 'CustomKeyRegistry':
        return CustomKeyRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CustomKeyRegistry):
        """
        Dynamic initializer for CustomKeyRegistry.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.CustomKeyRegistry()"""
        val = __CustomKeyRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.CustomKeyRegistry()"""
        val = __CustomKeyRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def get(arg0: 'Identifier') -> 'text.TextKey':
        """public static dev.ultreon.quantum.text.TextKey dev.ultreon.quantum.registry.CustomKeyRegistry.get(dev.ultreon.quantum.util.Identifier)"""
        return text.TextKey.__wrap(__CustomKeyRegistry.get(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.registry.RegistryKeys
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.registry.RegistryKeys as __RegistryKeys
__RegistryKeys = __RegistryKeys
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegistryKeys():
    """dev.ultreon.quantum.registry.RegistryKeys"""
 
    @staticmethod
    def __wrap(java_value: __RegistryKeys) -> 'RegistryKeys':
        return RegistryKeys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistryKeys):
        """
        Dynamic initializer for RegistryKeys.
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
 
    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.gen.noise.NoiseConfig>> dev.ultreon.quantum.registry.RegistryKeys.NOISE_SETTINGS
    NOISE_SETTINGS: 'RegistryKey' = __wrap(__RegistryKey.NOISE_SETTINGS)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.Block>> dev.ultreon.quantum.registry.RegistryKeys.BLOCK
    BLOCK: 'RegistryKey' = __wrap(__RegistryKey.BLOCK)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.weather.Weather>> dev.ultreon.quantum.registry.RegistryKeys.WEATHER
    WEATHER: 'RegistryKey' = __wrap(__RegistryKey.WEATHER)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.recipe.RecipeType<?>>> dev.ultreon.quantum.registry.RegistryKeys.RECIPE_TYPE
    RECIPE_TYPE: 'RegistryKey' = __wrap(__RegistryKey.RECIPE_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.item.Item>> dev.ultreon.quantum.registry.RegistryKeys.ITEM
    ITEM: 'RegistryKey' = __wrap(__RegistryKey.ITEM)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.EntityType<?>>> dev.ultreon.quantum.registry.RegistryKeys.ENTITY_TYPE
    ENTITY_TYPE: 'RegistryKey' = __wrap(__RegistryKey.ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.Attribute>> dev.ultreon.quantum.registry.RegistryKeys.ATTRIBUTE
    ATTRIBUTE: 'RegistryKey' = __wrap(__RegistryKey.ATTRIBUTE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.Biome>> dev.ultreon.quantum.registry.RegistryKeys.BIOME
    BIOME: 'RegistryKey' = __wrap(__RegistryKey.BIOME)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.menu.MenuType<?>>> dev.ultreon.quantum.registry.RegistryKeys.MENU_TYPE
    MENU_TYPE: 'RegistryKey' = __wrap(__RegistryKey.MENU_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.entity.BlockEntityType<?>>> dev.ultreon.quantum.registry.RegistryKeys.BLOCK_ENTITY_TYPE
    BLOCK_ENTITY_TYPE: 'RegistryKey' = __wrap(__RegistryKey.BLOCK_ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.particles.ParticleType>> dev.ultreon.quantum.registry.RegistryKeys.PARTICLE_TYPE
    PARTICLE_TYPE: 'RegistryKey' = __wrap(__RegistryKey.PARTICLE_TYPE)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.SoundEvent>> dev.ultreon.quantum.registry.RegistryKeys.SOUND_EVENT
    SOUND_EVENT: 'RegistryKey' = __wrap(__RegistryKey.SOUND_EVENT)

    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.damagesource.DamageSource>> dev.ultreon.quantum.registry.RegistryKeys.DAMAGE_SOURCE
    DAMAGE_SOURCE: 'RegistryKey' = __wrap(__RegistryKey.DAMAGE_SOURCE)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.RegistryKeys()"""
        val = __RegistryKeys()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.RegistryKeys()"""
        val = __RegistryKeys()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.registry.Registries
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.registry.Registry as __Registry
__Registry = __Registry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.registry.Registries as __Registries
__Registries = __Registries
from builtins import int
 
class Registries():
    """dev.ultreon.quantum.registry.Registries"""
 
    @staticmethod
    def __wrap(java_value: __Registries) -> 'Registries':
        return Registries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Registries):
        """
        Dynamic initializer for Registries.
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
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.damagesource.DamageSource> dev.ultreon.quantum.registry.Registries.DAMAGE_SOURCE
    DAMAGE_SOURCE: 'Registry' = __wrap(__Registry.DAMAGE_SOURCE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.SoundEvent> dev.ultreon.quantum.registry.Registries.SOUND_EVENT
    SOUND_EVENT: 'Registry' = __wrap(__Registry.SOUND_EVENT)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.entity.BlockEntityType<?>> dev.ultreon.quantum.registry.Registries.BLOCK_ENTITY_TYPE
    BLOCK_ENTITY_TYPE: 'Registry' = __wrap(__Registry.BLOCK_ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.registry.Registries.BLOCK
    BLOCK: 'Registry' = __wrap(__Registry.BLOCK)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.particles.ParticleType> dev.ultreon.quantum.registry.Registries.PARTICLE_TYPES
    PARTICLE_TYPES: 'Registry' = __wrap(__Registry.PARTICLE_TYPES)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.item.Item> dev.ultreon.quantum.registry.Registries.ITEM
    ITEM: 'Registry' = __wrap(__Registry.ITEM)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.Registries.REGISTRY
    REGISTRY: 'Registry' = __wrap(__Registry.REGISTRY)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.gen.noise.NoiseConfig> dev.ultreon.quantum.registry.Registries.NOISE_SETTINGS
    NOISE_SETTINGS: 'Registry' = __wrap(__Registry.NOISE_SETTINGS)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.menu.MenuType<?>> dev.ultreon.quantum.registry.Registries.MENU_TYPE
    MENU_TYPE: 'Registry' = __wrap(__Registry.MENU_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.Attribute> dev.ultreon.quantum.registry.Registries.ATTRIBUTE
    ATTRIBUTE: 'Registry' = __wrap(__Registry.ATTRIBUTE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.world.Biome> dev.ultreon.quantum.registry.Registries.BIOME
    BIOME: 'Registry' = __wrap(__Registry.BIOME)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.weather.Weather> dev.ultreon.quantum.registry.Registries.WEATHER
    WEATHER: 'Registry' = __wrap(__Registry.WEATHER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.entity.EntityType<?>> dev.ultreon.quantum.registry.Registries.ENTITY_TYPE
    ENTITY_TYPE: 'Registry' = __wrap(__Registry.ENTITY_TYPE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.recipe.RecipeType<?>> dev.ultreon.quantum.registry.Registries.RECIPE_TYPE
    RECIPE_TYPE: 'Registry' = __wrap(__Registry.RECIPE_TYPE)


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

    @staticmethod
    @overload
    def create(arg0: 'RegistryKey', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registries.create(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>,T...)"""
        return Registry.__wrap(__Registries.create(arg0, arg1))

        @staticmethod
        @overload
        def nopInit():
            """public static void dev.ultreon.quantum.registry.Registries.nopInit()"""
            __Registries.nopInit()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.Registries()"""
        val = __Registries()
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.Registries()"""
        val = __Registries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.quantum.registry.Registry<T> dev.ultreon.quantum.registry.Registries.create(dev.ultreon.quantum.util.Identifier,T...)"""
        return Registry.__wrap(__Registries.create(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.registry.AbstractRegistry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.registry.AbstractRegistry as __AbstractRegistry
__AbstractRegistry = __AbstractRegistry
from abc import abstractmethod, ABC
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
 
class AbstractRegistry(ABC):
    """dev.ultreon.quantum.registry.AbstractRegistry"""
 
    @staticmethod
    def __wrap(java_value: __AbstractRegistry) -> 'AbstractRegistry':
        return AbstractRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractRegistry):
        """
        Dynamic initializer for AbstractRegistry.
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

    @overload
    def random(self) -> object:
        """public V dev.ultreon.quantum.registry.AbstractRegistry.random()"""
        return object.__wrap(super(AbstractRegistry, self).random())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.registry.RegistryKey
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.registry.RegistryKey as __RegistryKey
__RegistryKey = __RegistryKey
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegistryKey():
    """dev.ultreon.quantum.registry.RegistryKey"""
 
    @staticmethod
    def __wrap(java_value: __RegistryKey) -> 'RegistryKey':
        return RegistryKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistryKey):
        """
        Dynamic initializer for RegistryKey.
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
 
    # public static final dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.registry.Registry<?>>> dev.ultreon.quantum.registry.RegistryKey.ROOT
    ROOT: 'RegistryKey' = __wrap(__RegistryKey.ROOT)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def element(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.RegistryKey.element()"""
        return 'util.Identifier'.__wrap(super(RegistryKey, self).element())

    @overload
    def parent(self) -> 'RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>> dev.ultreon.quantum.registry.RegistryKey.parent()"""
        return 'RegistryKey'.__wrap(super(RegistryKey, self).parent())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.registry.RegistryKey.equals(java.lang.Object)"""
        return bool.__wrap(super(__RegistryKey, self).equals(arg0))

    @staticmethod
    @overload
    def registry(arg0: 'Identifier') -> 'RegistryKey':
        """public static <T extends dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.RegistryKey.registry(dev.ultreon.quantum.util.Identifier)"""
        return RegistryKey.__wrap(__RegistryKey.registry(arg0))

    @overload
    def __init__(self, arg0: 'RegistryKey', arg1: 'Identifier'):
        """public dev.ultreon.quantum.registry.RegistryKey(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>,dev.ultreon.quantum.util.Identifier)"""
        val = __RegistryKey(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def of(arg0: 'RegistryKey', arg1: 'Identifier') -> 'RegistryKey':
        """public static <T> dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.RegistryKey.of(dev.ultreon.quantum.registry.RegistryKey<dev.ultreon.quantum.registry.Registry<T>>,dev.ultreon.quantum.util.Identifier)"""
        return RegistryKey.__wrap(__RegistryKey.of(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def registry(arg0: 'Registry') -> 'RegistryKey':
        """public static <T extends dev.ultreon.quantum.registry.Registry<?>> dev.ultreon.quantum.registry.RegistryKey<T> dev.ultreon.quantum.registry.RegistryKey.registry(T)"""
        return RegistryKey.__wrap(__RegistryKey.registry(arg0))

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
        """public int dev.ultreon.quantum.registry.RegistryKey.hashCode()"""
        return int.__wrap(super(RegistryKey, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.registry.RegistryKey.toString()"""
        return str.__wrap(super(RegistryKey, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.registry.RawIdMap
import dev.ultreon.quantum.registry.RawIdMap as __RawIdMap
__RawIdMap = __RawIdMap
from abc import abstractmethod, ABC
 
class RawIdMap(ABC):
    """dev.ultreon.quantum.registry.RawIdMap"""
 
    @staticmethod
    def __wrap(java_value: __RawIdMap) -> 'RawIdMap':
        return RawIdMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RawIdMap):
        """
        Dynamic initializer for RawIdMap.
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
    def byId(self, arg0: int):
        """public abstract T dev.ultreon.quantum.registry.RawIdMap.byId(int)"""
        pass

    @abstractmethod
    def getRawId(self, arg0: object):
        """public abstract int dev.ultreon.quantum.registry.RawIdMap.getRawId(T)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.registry.CommandRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.registry.CommandRegistry as __CommandRegistry
__CommandRegistry = __CommandRegistry
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
from builtins import int
 
class CommandRegistry():
    """dev.ultreon.quantum.registry.CommandRegistry"""
 
    @staticmethod
    def __wrap(java_value: __CommandRegistry) -> 'CommandRegistry':
        return CommandRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandRegistry):
        """
        Dynamic initializer for CommandRegistry.
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

    @staticmethod
    @overload
    def get(arg0: str) -> 'commands.Command':
        """public static dev.ultreon.quantum.api.commands.Command dev.ultreon.quantum.registry.CommandRegistry.get(java.lang.String)"""
        return commands.Command.__wrap(__CommandRegistry.get(arg0))

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
    def getCommands() -> 'Stream':
        """public static java.util.stream.Stream<dev.ultreon.quantum.api.commands.Command> dev.ultreon.quantum.registry.CommandRegistry.getCommands()"""
        return Stream.__wrap(__CommandRegistry.getCommands())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getCommandNames() -> 'Stream':
        """public static java.util.stream.Stream<java.lang.String> dev.ultreon.quantum.registry.CommandRegistry.getCommandNames()"""
        return Stream.__wrap(__CommandRegistry.getCommandNames())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.CommandRegistry()"""
        val = __CommandRegistry()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.CommandRegistry()"""
        val = __CommandRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def register(arg0: 'Command'):
        """public static void dev.ultreon.quantum.registry.CommandRegistry.register(dev.ultreon.quantum.api.commands.Command)"""
        __CommandRegistry.register(arg0) 
 
 
# CLASS: dev.ultreon.quantum.registry.DeferredElement
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.registry.DeferredElement as __DeferredElement
__DeferredElement = __DeferredElement
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DeferredElement():
    """dev.ultreon.quantum.registry.DeferredElement"""
 
    @staticmethod
    def __wrap(java_value: __DeferredElement) -> 'DeferredElement':
        return DeferredElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeferredElement):
        """
        Dynamic initializer for DeferredElement.
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
    def get(self) -> object:
        """public T dev.ultreon.quantum.registry.DeferredElement.get()"""
        return object.__wrap(super(DeferredElement, self).get())

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
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.registry.DeferredElement.id()"""
        return 'util.Identifier'.__wrap(super(DeferredElement, self).id())

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
    def register(self):
        """public void dev.ultreon.quantum.registry.DeferredElement.register()"""
        super(DeferredElement, self).register()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Registry', arg1: 'Supplier', arg2: 'Identifier'):
        """public dev.ultreon.quantum.registry.DeferredElement(dev.ultreon.quantum.registry.Registry<? super T>,java.util.function.Supplier<T>,dev.ultreon.quantum.util.Identifier)"""
        val = __DeferredElement(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))