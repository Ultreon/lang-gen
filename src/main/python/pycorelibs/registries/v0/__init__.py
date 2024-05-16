from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
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
import java.util.Set as _Set
_Set = _Set
import dev.ultreon.libs.commons.v0.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.libs.registries.v0.Registry as _Registry
_Registry = _Registry
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Registry():
    """dev.ultreon.libs.registries.v0.Registry"""
 
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
 
    @overload
    def getValue(self, arg0: 'Identifier') -> object:
        """public T dev.ultreon.libs.registries.v0.Registry.getValue(dev.ultreon.libs.commons.v0.Identifier)"""
        return object._wrap(super(_Registry, self).getValue(arg0))

    @staticmethod
    @overload
    def getRegistries() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.libs.registries.v0.Registry<?>> dev.ultreon.libs.registries.v0.Registry.getRegistries()"""
        return Collection._wrap(_Registry.getRegistries())

    @overload
    def getKey(self, arg0: object) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.Registry.getKey(T)"""
        return 'v0.Identifier'._wrap(super(_Registry, self).getKey(arg0))

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.libs.registries.v0.Registry.isFrozen()"""
        return bool._wrap(super(Registry, self).isFrozen())

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
    def contains(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.registries.v0.Registry.contains(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool._wrap(super(_Registry, self).contains(arg0))

        @staticmethod
        @overload
        def dump():
            """public static void dev.ultreon.libs.registries.v0.Registry.dump()"""
            _Registry.dump()

    @overload
    def keys(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.registries.v0.Registry.keys()"""
        return 'Set'._wrap(super(Registry, self).keys())

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.libs.commons.v0.Identifier, T>> dev.ultreon.libs.registries.v0.Registry.entries()"""
        return 'Set'._wrap(super(Registry, self).entries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

        @staticmethod
        @overload
        def freeze():
            """public static void dev.ultreon.libs.registries.v0.Registry.freeze()"""
            _Registry.freeze()

    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.libs.registries.v0.Registry.values()"""
        return 'Collection'._wrap(super(Registry, self).values())

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
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.libs.registries.v0.Registry<T> dev.ultreon.libs.registries.v0.Registry.create(dev.ultreon.libs.commons.v0.Identifier,T...)"""
        return Registry._wrap(_Registry.create(arg0, arg1))

    @overload
    def dumpRegistry(self):
        """public void dev.ultreon.libs.registries.v0.Registry.dumpRegistry()"""
        super(Registry, self).dumpRegistry()

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
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.libs.registries.v0.Registry.getType()"""
        return 'type.Class'._wrap(super(Registry, self).getType())

    @overload
    def id(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.Registry.id()"""
        return 'v0.Identifier'._wrap(super(Registry, self).id())

    @overload
    def register(self, arg0: 'Identifier', arg1: object):
        """public void dev.ultreon.libs.registries.v0.Registry.register(dev.ultreon.libs.commons.v0.Identifier,T)"""
        super(_Registry, self).register(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.Registry
from pyquantum_helper import import_once as _import_once
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
import java.util.Set as _Set
_Set = _Set
import dev.ultreon.libs.commons.v0.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.libs.registries.v0.Registry as _Registry
_Registry = _Registry
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Registry():
    """dev.ultreon.libs.registries.v0.Registry"""
 
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
 
    @overload
    def getValue(self, arg0: 'Identifier') -> object:
        """public T dev.ultreon.libs.registries.v0.Registry.getValue(dev.ultreon.libs.commons.v0.Identifier)"""
        return object._wrap(super(_Registry, self).getValue(arg0))

    @staticmethod
    @overload
    def getRegistries() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.libs.registries.v0.Registry<?>> dev.ultreon.libs.registries.v0.Registry.getRegistries()"""
        return Collection._wrap(_Registry.getRegistries())

    @overload
    def getKey(self, arg0: object) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.Registry.getKey(T)"""
        return 'v0.Identifier'._wrap(super(_Registry, self).getKey(arg0))

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.libs.registries.v0.Registry.isFrozen()"""
        return bool._wrap(super(Registry, self).isFrozen())

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
    def contains(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.registries.v0.Registry.contains(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool._wrap(super(_Registry, self).contains(arg0))

        @staticmethod
        @overload
        def dump():
            """public static void dev.ultreon.libs.registries.v0.Registry.dump()"""
            _Registry.dump()

    @overload
    def keys(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.registries.v0.Registry.keys()"""
        return 'Set'._wrap(super(Registry, self).keys())

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.libs.commons.v0.Identifier, T>> dev.ultreon.libs.registries.v0.Registry.entries()"""
        return 'Set'._wrap(super(Registry, self).entries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

        @staticmethod
        @overload
        def freeze():
            """public static void dev.ultreon.libs.registries.v0.Registry.freeze()"""
            _Registry.freeze()

    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.libs.registries.v0.Registry.values()"""
        return 'Collection'._wrap(super(Registry, self).values())

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
    def create(arg0: 'Identifier', *arg1: object) -> 'Registry':
        """public static <T> dev.ultreon.libs.registries.v0.Registry<T> dev.ultreon.libs.registries.v0.Registry.create(dev.ultreon.libs.commons.v0.Identifier,T...)"""
        return Registry._wrap(_Registry.create(arg0, arg1))

    @overload
    def dumpRegistry(self):
        """public void dev.ultreon.libs.registries.v0.Registry.dumpRegistry()"""
        super(Registry, self).dumpRegistry()

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
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.libs.registries.v0.Registry.getType()"""
        return 'type.Class'._wrap(super(Registry, self).getType())

    @overload
    def id(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.Registry.id()"""
        return 'v0.Identifier'._wrap(super(Registry, self).id())

    @overload
    def register(self, arg0: 'Identifier', arg1: object):
        """public void dev.ultreon.libs.registries.v0.Registry.register(dev.ultreon.libs.commons.v0.Identifier,T)"""
        super(_Registry, self).register(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.Registry 
 
 
# CLASS: dev.ultreon.libs.registries.v0.DelayedRegister
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
import java.lang.Integer as _int
import dev.ultreon.libs.registries.v0.DelayedRegister as _DelayedRegister
_DelayedRegister = _DelayedRegister
import dev.ultreon.libs.registries.v0.RegistrySupplier as _RegistrySupplier
_RegistrySupplier = _RegistrySupplier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DelayedRegister():
    """dev.ultreon.libs.registries.v0.DelayedRegister"""
 
    @staticmethod
    def _wrap(java_value: _DelayedRegister) -> 'DelayedRegister':
        return DelayedRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DelayedRegister):
        """
        Dynamic initializer for DelayedRegister.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DelayedRegister__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DelayedRegister__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def register(self):
        """public void dev.ultreon.libs.registries.v0.DelayedRegister.register()"""
        super(DelayedRegister, self).register()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: str, arg1: 'Registry') -> 'DelayedRegister':
        """public static <T> dev.ultreon.libs.registries.v0.DelayedRegister<T> dev.ultreon.libs.registries.v0.DelayedRegister.create(java.lang.String,dev.ultreon.libs.registries.v0.Registry<T>)"""
        return DelayedRegister._wrap(_DelayedRegister.create(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def register(self, arg0: str, arg1: 'Supplier') -> 'RegistrySupplier':
        """public <C extends T> dev.ultreon.libs.registries.v0.RegistrySupplier<C> dev.ultreon.libs.registries.v0.DelayedRegister.register(java.lang.String,java.util.function.Supplier<C>)"""
        return 'RegistrySupplier'._wrap(super(_DelayedRegister, self).register(arg0, arg1))

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
 
 
# CLASS: dev.ultreon.libs.registries.v0.RegistrySupplier
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
import dev.ultreon.libs.commons.v0.Identifier as _Identifier
_Identifier = _Identifier
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.registries.v0.RegistrySupplier as _RegistrySupplier
_RegistrySupplier = _RegistrySupplier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegistrySupplier():
    """dev.ultreon.libs.registries.v0.RegistrySupplier"""
 
    @staticmethod
    def _wrap(java_value: _RegistrySupplier) -> 'RegistrySupplier':
        return RegistrySupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegistrySupplier):
        """
        Dynamic initializer for RegistrySupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegistrySupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegistrySupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def id(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.registries.v0.RegistrySupplier.id()"""
        return 'v0.Identifier'._wrap(super(RegistrySupplier, self).id())

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
    def register(self):
        """public void dev.ultreon.libs.registries.v0.RegistrySupplier.register()"""
        super(RegistrySupplier, self).register()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Registry', arg1: 'Supplier', arg2: 'Identifier'):
        """public dev.ultreon.libs.registries.v0.RegistrySupplier(dev.ultreon.libs.registries.v0.Registry<? super T>,java.util.function.Supplier<T>,dev.ultreon.libs.commons.v0.Identifier)"""
        val = _RegistrySupplier(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.libs.registries.v0.RegistrySupplier.get()"""
        return object._wrap(super(RegistrySupplier, self).get())

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
 
 
# CLASS: dev.ultreon.libs.registries.v0.ObjectInit
import java.util.function.Supplier as Supplier
from builtins import str
import dev.ultreon.libs.registries.v0.ObjectInit as _ObjectInit
_ObjectInit = _ObjectInit
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.libs.registries.v0.RegistrySupplier as _RegistrySupplier
_RegistrySupplier = _RegistrySupplier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectInit():
    """dev.ultreon.libs.registries.v0.ObjectInit"""
 
    @staticmethod
    def _wrap(java_value: _ObjectInit) -> 'ObjectInit':
        return ObjectInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectInit):
        """
        Dynamic initializer for ObjectInit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectInit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectInit__wrapper":
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

    @overload
    def __init__(self, arg0: str, arg1: 'Registry'):
        """public dev.ultreon.libs.registries.v0.ObjectInit(java.lang.String,dev.ultreon.libs.registries.v0.Registry<T>)"""
        val = _ObjectInit(arg0, arg1)
        self.__wrapper = val

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
    def register(self, arg0: str, arg1: 'Supplier') -> 'RegistrySupplier':
        """public <C extends T> dev.ultreon.libs.registries.v0.RegistrySupplier<C> dev.ultreon.libs.registries.v0.ObjectInit.register(java.lang.String,java.util.function.Supplier<C>)"""
        return 'RegistrySupplier'._wrap(super(_ObjectInit, self).register(arg0, arg1))

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
 
 
# CLASS: dev.ultreon.libs.registries.v0.AbstractRegistry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.registries.v0.AbstractRegistry as _AbstractRegistry
_AbstractRegistry = _AbstractRegistry
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractRegistry():
    """dev.ultreon.libs.registries.v0.AbstractRegistry"""
 
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
 
    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.libs.registries.v0.AbstractRegistry.entries() throws java.lang.IllegalAccessException"""
        pass

    @abstractmethod
    def register(self, arg0: object, arg1: object):
        """public abstract void dev.ultreon.libs.registries.v0.AbstractRegistry.register(K,V)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def __init__(self):
        """public dev.ultreon.libs.registries.v0.AbstractRegistry() throws java.lang.IllegalStateException"""
        val = _AbstractRegistry()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V dev.ultreon.libs.registries.v0.AbstractRegistry.get(K)"""
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.registries.v0.AbstractRegistry() throws java.lang.IllegalStateException"""
        val = _AbstractRegistry()
        self.__wrapper = val

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