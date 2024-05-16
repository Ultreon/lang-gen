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
try:
    from pycorelibs.resources import v0
except ImportError:
    v0 = _import_once("pycorelibs.resources.v0")

import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.resources.v0.android.DeferredResourcePackage as _DeferredResourcePackage
_DeferredResourcePackage = _DeferredResourcePackage
import dev.ultreon.libs.resources.v0.Resource as _Resource
_Resource = _Resource
import dev.ultreon.libs.resources.v0.ResourcePackage as _ResourcePackage
_ResourcePackage = _ResourcePackage
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferredResourcePackage():
    """dev.ultreon.libs.resources.v0.android.DeferredResourcePackage"""
 
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
 
    @override
    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource> dev.ultreon.libs.resources.v0.ResourcePackage.mapEntries()"""
        return 'Map'._wrap(super(v0.ResourcePackage, self).mapEntries())

    @overload
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.libs.resources.v0.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = _DeferredResourcePackage(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.has(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool._wrap(super(_DeferredResourcePackage, self).has(arg0))

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

    @overload
    def get(self, arg0: 'Identifier') -> 'v0.Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.get(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'v0.Resource'._wrap(super(_DeferredResourcePackage, self).get(arg0))

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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.resources.v0.ResourcePackage.entries()"""
        return 'Set'._wrap(super(v0.ResourcePackage, self).entries())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.android.DeferredResourcePackage
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
try:
    from pycorelibs.resources import v0
except ImportError:
    v0 = _import_once("pycorelibs.resources.v0")

import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.resources.v0.android.DeferredResourcePackage as _DeferredResourcePackage
_DeferredResourcePackage = _DeferredResourcePackage
import dev.ultreon.libs.resources.v0.Resource as _Resource
_Resource = _Resource
import dev.ultreon.libs.resources.v0.ResourcePackage as _ResourcePackage
_ResourcePackage = _ResourcePackage
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferredResourcePackage():
    """dev.ultreon.libs.resources.v0.android.DeferredResourcePackage"""
 
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
 
    @override
    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource> dev.ultreon.libs.resources.v0.ResourcePackage.mapEntries()"""
        return 'Map'._wrap(super(v0.ResourcePackage, self).mapEntries())

    @overload
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.libs.resources.v0.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = _DeferredResourcePackage(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.has(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool._wrap(super(_DeferredResourcePackage, self).has(arg0))

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

    @overload
    def get(self, arg0: 'Identifier') -> 'v0.Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.get(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'v0.Resource'._wrap(super(_DeferredResourcePackage, self).get(arg0))

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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.resources.v0.ResourcePackage.entries()"""
        return 'Set'._wrap(super(v0.ResourcePackage, self).entries())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.android.DeferredResourcePackage