from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.resources.ResourceCategory as __ResourceCategory
__ResourceCategory = __ResourceCategory
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as __StaticResource
__StaticResource = __StaticResource
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.resources.android.DeferredResourcePackage as __DeferredResourcePackage
__DeferredResourcePackage = __DeferredResourcePackage
import dev.ultreon.quantum.resources.ResourcePackage as __ResourcePackage
__ResourcePackage = __ResourcePackage
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class DeferredResourcePackage():
    """dev.ultreon.quantum.resources.android.DeferredResourcePackage"""
 
    @staticmethod
    def __wrap(java_value: __DeferredResourcePackage) -> 'DeferredResourcePackage':
        return DeferredResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeferredResourcePackage):
        """
        Dynamic initializer for DeferredResourcePackage.
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
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourcePackage.mapEntries()"""
        return 'Map'.__wrap(super(resources.ResourcePackage, self).mapEntries())

    @overload
    def hasCategory(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.hasCategory(java.lang.String)"""
        return bool.__wrap(super(__resources.ResourcePackage, self).hasCategory(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.android.DeferredResourcePackage.has(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__DeferredResourcePackage, self).has(arg0))

    @overload
    def getCategory(self, arg0: str) -> 'resources.ResourceCategory':
        """public dev.ultreon.quantum.resources.ResourceCategory dev.ultreon.quantum.resources.ResourcePackage.getCategory(java.lang.String)"""
        return 'resources.ResourceCategory'.__wrap(super(__resources.ResourcePackage, self).getCategory(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourcePackage.close()"""
        super(resources.ResourcePackage, self).close()

    @override
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourcePackage.entries()"""
        return 'Set'.__wrap(super(resources.ResourcePackage, self).entries())

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
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.quantum.resources.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = __DeferredResourcePackage(arg0, arg1)
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

    @override
    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourcePackage.getCategories()"""
        return 'List'.__wrap(super(resources.ResourcePackage, self).getCategories())

    @overload
    def get(self, arg0: 'Identifier') -> 'resources.StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.android.DeferredResourcePackage.get(dev.ultreon.quantum.util.Identifier)"""
        return 'resources.StaticResource'.__wrap(super(__DeferredResourcePackage, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.resources.android.DeferredResourcePackage
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.resources.ResourceCategory as __ResourceCategory
__ResourceCategory = __ResourceCategory
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as __StaticResource
__StaticResource = __StaticResource
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.resources.android.DeferredResourcePackage as __DeferredResourcePackage
__DeferredResourcePackage = __DeferredResourcePackage
import dev.ultreon.quantum.resources.ResourcePackage as __ResourcePackage
__ResourcePackage = __ResourcePackage
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class DeferredResourcePackage():
    """dev.ultreon.quantum.resources.android.DeferredResourcePackage"""
 
    @staticmethod
    def __wrap(java_value: __DeferredResourcePackage) -> 'DeferredResourcePackage':
        return DeferredResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeferredResourcePackage):
        """
        Dynamic initializer for DeferredResourcePackage.
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
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourcePackage.mapEntries()"""
        return 'Map'.__wrap(super(resources.ResourcePackage, self).mapEntries())

    @overload
    def hasCategory(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.hasCategory(java.lang.String)"""
        return bool.__wrap(super(__resources.ResourcePackage, self).hasCategory(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.android.DeferredResourcePackage.has(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__DeferredResourcePackage, self).has(arg0))

    @overload
    def getCategory(self, arg0: str) -> 'resources.ResourceCategory':
        """public dev.ultreon.quantum.resources.ResourceCategory dev.ultreon.quantum.resources.ResourcePackage.getCategory(java.lang.String)"""
        return 'resources.ResourceCategory'.__wrap(super(__resources.ResourcePackage, self).getCategory(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourcePackage.close()"""
        super(resources.ResourcePackage, self).close()

    @override
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourcePackage.entries()"""
        return 'Set'.__wrap(super(resources.ResourcePackage, self).entries())

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
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.quantum.resources.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = __DeferredResourcePackage(arg0, arg1)
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

    @override
    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourcePackage.getCategories()"""
        return 'List'.__wrap(super(resources.ResourcePackage, self).getCategories())

    @overload
    def get(self, arg0: 'Identifier') -> 'resources.StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.android.DeferredResourcePackage.get(dev.ultreon.quantum.util.Identifier)"""
        return 'resources.StaticResource'.__wrap(super(__DeferredResourcePackage, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.resources.android.DeferredResourcePackage