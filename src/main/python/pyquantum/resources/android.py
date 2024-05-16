from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as _StaticResource
_StaticResource = _StaticResource
import java.lang.String as _string
import dev.ultreon.quantum.resources.android.DeferredResourcePackage as _DeferredResourcePackage
_DeferredResourcePackage = _DeferredResourcePackage
import java.util.Set as Set
import dev.ultreon.quantum.resources.ResourceCategory as _ResourceCategory
_ResourceCategory = _ResourceCategory
import java.lang.Integer as _int
import dev.ultreon.quantum.resources.ResourcePackage as _ResourcePackage
_ResourcePackage = _ResourcePackage
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferredResourcePackage():
    """dev.ultreon.quantum.resources.android.DeferredResourcePackage"""
 
    @staticmethod
    def _wrap(java_value: _DeferredResourcePackage) -> 'DeferredResourcePackage':
        return DeferredResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeferredResourcePackage):
        """
        Dynamic initializer for DeferredResourcePackage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeferredResourcePackage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeferredResourcePackage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.android.DeferredResourcePackage.has(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_DeferredResourcePackage, self).has(arg0))

    @overload
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.quantum.resources.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = _DeferredResourcePackage(arg0, arg1)
        self.__wrapper = val

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
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourcePackage.mapEntries()"""
        return 'Map'._wrap(super(resources.ResourcePackage, self).mapEntries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourcePackage.close()"""
        super(resources.ResourcePackage, self).close()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def hasCategory(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.hasCategory(java.lang.String)"""
        return bool._wrap(super(_resources.ResourcePackage, self).hasCategory(arg0))

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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourcePackage.entries()"""
        return 'Set'._wrap(super(resources.ResourcePackage, self).entries())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getCategory(self, arg0: str) -> 'resources.ResourceCategory':
        """public dev.ultreon.quantum.resources.ResourceCategory dev.ultreon.quantum.resources.ResourcePackage.getCategory(java.lang.String)"""
        return 'resources.ResourceCategory'._wrap(super(_resources.ResourcePackage, self).getCategory(arg0))

    @override
    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourcePackage.getCategories()"""
        return 'List'._wrap(super(resources.ResourcePackage, self).getCategories())

    @overload
    def get(self, arg0: 'Identifier') -> 'resources.StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.android.DeferredResourcePackage.get(dev.ultreon.quantum.util.Identifier)"""
        return 'resources.StaticResource'._wrap(super(_DeferredResourcePackage, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.resources.android.DeferredResourcePackage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as _StaticResource
_StaticResource = _StaticResource
import java.lang.String as _string
import dev.ultreon.quantum.resources.android.DeferredResourcePackage as _DeferredResourcePackage
_DeferredResourcePackage = _DeferredResourcePackage
import java.util.Set as Set
import dev.ultreon.quantum.resources.ResourceCategory as _ResourceCategory
_ResourceCategory = _ResourceCategory
import java.lang.Integer as _int
import dev.ultreon.quantum.resources.ResourcePackage as _ResourcePackage
_ResourcePackage = _ResourcePackage
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferredResourcePackage():
    """dev.ultreon.quantum.resources.android.DeferredResourcePackage"""
 
    @staticmethod
    def _wrap(java_value: _DeferredResourcePackage) -> 'DeferredResourcePackage':
        return DeferredResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeferredResourcePackage):
        """
        Dynamic initializer for DeferredResourcePackage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeferredResourcePackage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeferredResourcePackage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.android.DeferredResourcePackage.has(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_DeferredResourcePackage, self).has(arg0))

    @overload
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.quantum.resources.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = _DeferredResourcePackage(arg0, arg1)
        self.__wrapper = val

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
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourcePackage.mapEntries()"""
        return 'Map'._wrap(super(resources.ResourcePackage, self).mapEntries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourcePackage.close()"""
        super(resources.ResourcePackage, self).close()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def hasCategory(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.hasCategory(java.lang.String)"""
        return bool._wrap(super(_resources.ResourcePackage, self).hasCategory(arg0))

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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourcePackage.entries()"""
        return 'Set'._wrap(super(resources.ResourcePackage, self).entries())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getCategory(self, arg0: str) -> 'resources.ResourceCategory':
        """public dev.ultreon.quantum.resources.ResourceCategory dev.ultreon.quantum.resources.ResourcePackage.getCategory(java.lang.String)"""
        return 'resources.ResourceCategory'._wrap(super(_resources.ResourcePackage, self).getCategory(arg0))

    @override
    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourcePackage.getCategories()"""
        return 'List'._wrap(super(resources.ResourcePackage, self).getCategories())

    @overload
    def get(self, arg0: 'Identifier') -> 'resources.StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.android.DeferredResourcePackage.get(dev.ultreon.quantum.util.Identifier)"""
        return 'resources.StaticResource'._wrap(super(_DeferredResourcePackage, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.resources.android.DeferredResourcePackage