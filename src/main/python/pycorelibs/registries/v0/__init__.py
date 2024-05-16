from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import dev.ultreon.libs.registries.v0.RegistrySupplier as __RegistrySupplier
__RegistrySupplier = __RegistrySupplier
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegistrySupplier(__Supplier, Supplier):
    """dev.ultreon.libs.registries.v0.RegistrySupplier"""
 
    @staticmethod
    def __wrap(java_value: __RegistrySupplier) -> 'RegistrySupplier':
        return RegistrySupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistrySupplier):
        """
        Dynamic initializer for RegistrySupplier.
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
    def __init__(self, arg0: 'Registry', arg1: 'Supplier', arg2: 'Identifier'):
        """public dev.ultreon.libs.registries.v0.RegistrySupplier(dev.ultreon.libs.registries.v0.Registry<? super T>,java.util.function.Supplier<T>,dev.ultreon.libs.commons.v0.Identifier)"""
        val = __RegistrySupplier(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def register(self):
        """public void dev.ultreon.libs.registries.v0.RegistrySupplier.register()"""
        super(RegistrySupplier, self).register()

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
    def get(self) -> object:
        """public T dev.ultreon.libs.registries.v0.RegistrySupplier.get()"""
        return object.__wrap(super(RegistrySupplier, self).get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def id(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.RegistrySupplier.id()"""
        return 'v0.Identifier'.__wrap(super(RegistrySupplier, self).id())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.RegistrySupplier
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import dev.ultreon.libs.registries.v0.RegistrySupplier as __RegistrySupplier
__RegistrySupplier = __RegistrySupplier
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegistrySupplier(__Supplier, Supplier):
    """dev.ultreon.libs.registries.v0.RegistrySupplier"""
 
    @staticmethod
    def __wrap(java_value: __RegistrySupplier) -> 'RegistrySupplier':
        return RegistrySupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistrySupplier):
        """
        Dynamic initializer for RegistrySupplier.
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
    def __init__(self, arg0: 'Registry', arg1: 'Supplier', arg2: 'Identifier'):
        """public dev.ultreon.libs.registries.v0.RegistrySupplier(dev.ultreon.libs.registries.v0.Registry<? super T>,java.util.function.Supplier<T>,dev.ultreon.libs.commons.v0.Identifier)"""
        val = __RegistrySupplier(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def register(self):
        """public void dev.ultreon.libs.registries.v0.RegistrySupplier.register()"""
        super(RegistrySupplier, self).register()

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
    def get(self) -> object:
        """public T dev.ultreon.libs.registries.v0.RegistrySupplier.get()"""
        return object.__wrap(super(RegistrySupplier, self).get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def id(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.RegistrySupplier.id()"""
        return 'v0.Identifier'.__wrap(super(RegistrySupplier, self).id())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.RegistrySupplier 
 
 
# CLASS: dev.ultreon.libs.registries.v0.ObjectInit
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.registries.v0.ObjectInit as __ObjectInit
__ObjectInit = __ObjectInit
import java.lang.Long as __long
import dev.ultreon.libs.registries.v0.RegistrySupplier as __RegistrySupplier
__RegistrySupplier = __RegistrySupplier
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
 
class ObjectInit(ABC):
    """dev.ultreon.libs.registries.v0.ObjectInit"""
 
    @staticmethod
    def __wrap(java_value: __ObjectInit) -> 'ObjectInit':
        return ObjectInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectInit):
        """
        Dynamic initializer for ObjectInit.
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

    @overload
    def __init__(self, arg0: str, arg1: 'Registry'):
        """public dev.ultreon.libs.registries.v0.ObjectInit(java.lang.String,dev.ultreon.libs.registries.v0.Registry<T>)"""
        val = __ObjectInit(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def register(self, arg0: str, arg1: 'Supplier') -> 'RegistrySupplier':
        """public <C extends T> dev.ultreon.libs.registries.v0.RegistrySupplier<C> dev.ultreon.libs.registries.v0.ObjectInit.register(java.lang.String,java.util.function.Supplier<C>)"""
        return 'RegistrySupplier'.__wrap(super(__ObjectInit, self).register(arg0, arg1))

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
 
 
# CLASS: dev.ultreon.libs.registries.v0.DelayedRegister
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.registries.v0.DelayedRegister as __DelayedRegister
__DelayedRegister = __DelayedRegister
from builtins import type
import java.lang.Long as __long
import dev.ultreon.libs.registries.v0.RegistrySupplier as __RegistrySupplier
__RegistrySupplier = __RegistrySupplier
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
 
class DelayedRegister():
    """dev.ultreon.libs.registries.v0.DelayedRegister"""
 
    @staticmethod
    def __wrap(java_value: __DelayedRegister) -> 'DelayedRegister':
        return DelayedRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DelayedRegister):
        """
        Dynamic initializer for DelayedRegister.
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
    def register(self):
        """public void dev.ultreon.libs.registries.v0.DelayedRegister.register()"""
        super(DelayedRegister, self).register()

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
    def register(self, arg0: str, arg1: 'Supplier') -> 'RegistrySupplier':
        """public <C extends T> dev.ultreon.libs.registries.v0.RegistrySupplier<C> dev.ultreon.libs.registries.v0.DelayedRegister.register(java.lang.String,java.util.function.Supplier<C>)"""
        return 'RegistrySupplier'.__wrap(super(__DelayedRegister, self).register(arg0, arg1))

    @staticmethod
    @overload
    def create(arg0: str, arg1: 'Registry') -> 'DelayedRegister':
        """public static <T> dev.ultreon.libs.registries.v0.DelayedRegister<T> dev.ultreon.libs.registries.v0.DelayedRegister.create(java.lang.String,dev.ultreon.libs.registries.v0.Registry<T>)"""
        return DelayedRegister.__wrap(__DelayedRegister.create(arg0, arg1))

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
 
 
# CLASS: dev.ultreon.libs.registries.v0.AbstractRegistry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.registries.v0.AbstractRegistry as __AbstractRegistry
__AbstractRegistry = __AbstractRegistry
from abc import abstractmethod, ABC
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
    """dev.ultreon.libs.registries.v0.AbstractRegistry"""
 
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

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.libs.registries.v0.AbstractRegistry.entries() throws java.lang.IllegalAccessException"""
        pass

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.registries.v0.AbstractRegistry() throws java.lang.IllegalStateException"""
        val = __AbstractRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def register(self, arg0: object, arg1: object):
        """public abstract void dev.ultreon.libs.registries.v0.AbstractRegistry.register(K,V)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.registries.v0.AbstractRegistry() throws java.lang.IllegalStateException"""
        val = __AbstractRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def keys(self, ):
        """public abstract java.util.Set<K> dev.ultreon.libs.registries.v0.AbstractRegistry.keys()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> dev.ultreon.libs.registries.v0.AbstractRegistry.values()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V dev.ultreon.libs.registries.v0.AbstractRegistry.get(K)"""
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.registries.v0.Registry
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.libs.registries.v0.Registry as __Registry
__Registry = __Registry
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
from builtins import object
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Registry():
    """dev.ultreon.libs.registries.v0.Registry"""
 
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
 
    @overload
    def register(self, arg0: 'Identifier', arg1: object):
        """public void dev.ultreon.libs.registries.v0.Registry.register(dev.ultreon.libs.commons.v0.Identifier,T)"""
        super(__Registry, self).register(arg0, arg1)

    @overload
    def keys(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.registries.v0.Registry.keys()"""
        return 'Set'.__wrap(super(Registry, self).keys())

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
        def freeze():
            """public static void dev.ultreon.libs.registries.v0.Registry.freeze()"""
            __Registry.freeze()

    @overload
    def id(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.Registry.id()"""
        return 'v0.Identifier'.__wrap(super(Registry, self).id())

        @staticmethod
        @overload
        def dump():
            """public static void dev.ultreon.libs.registries.v0.Registry.dump()"""
            __Registry.dump()

    @overload
    def contains(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.registries.v0.Registry.contains(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool.__wrap(super(__Registry, self).contains(arg0))

    @overload
    def getKey(self, arg0: object) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.Registry.getKey(T)"""
        return 'v0.Identifier'.__wrap(super(__Registry, self).getKey(arg0))

    @overload
    def getValue(self, arg0: 'Identifier') -> object:
        """public T dev.ultreon.libs.registries.v0.Registry.getValue(dev.ultreon.libs.commons.v0.Identifier)"""
        return object.__wrap(super(__Registry, self).getValue(arg0))

    @staticmethod
    @overload
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.libs.registries.v0.Registry<T> dev.ultreon.libs.registries.v0.Registry.create(dev.ultreon.libs.commons.v0.Identifier,T...)"""
        return Registry.__wrap(__Registry.create(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.libs.registries.v0.Registry.values()"""
        return 'Collection'.__wrap(super(Registry, self).values())

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.libs.registries.v0.Registry.isFrozen()"""
        return bool.__wrap(super(Registry, self).isFrozen())

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
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.libs.registries.v0.Registry.getType()"""
        return 'type.Class'.__wrap(super(Registry, self).getType())

    @overload
    def dumpRegistry(self):
        """public void dev.ultreon.libs.registries.v0.Registry.dumpRegistry()"""
        super(Registry, self).dumpRegistry()

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

    @staticmethod
    @overload
    def getRegistries() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.libs.registries.v0.Registry<?>> dev.ultreon.libs.registries.v0.Registry.getRegistries()"""
        return Collection.__wrap(__Registry.getRegistries())

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.libs.commons.v0.Identifier, T>> dev.ultreon.libs.registries.v0.Registry.entries()"""
        return 'Set'.__wrap(super(Registry, self).entries())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))