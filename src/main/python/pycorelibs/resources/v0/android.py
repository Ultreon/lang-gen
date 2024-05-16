from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.resources.v0.Resource as __Resource
__Resource = __Resource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.libs.resources.v0.android.DeferredResourcePackage as __DeferredResourcePackage
__DeferredResourcePackage = __DeferredResourcePackage
try:
    from pycorelibs.resources import v0
except ImportError:
    v0 = __import_once__("pycorelibs.resources.v0")

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
import java.lang.String as __string
import dev.ultreon.libs.resources.v0.ResourcePackage as __ResourcePackage
__ResourcePackage = __ResourcePackage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class DeferredResourcePackage(resources.__ResourcePackage, v0.ResourcePackage):
    """dev.ultreon.libs.resources.v0.android.DeferredResourcePackage"""
 
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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.resources.v0.ResourcePackage.entries()"""
        return 'Set'.__wrap(super(v0.ResourcePackage, self).entries())

    @overload
    def get(self, arg0: 'Identifier') -> 'v0.Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.get(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'v0.Resource'.__wrap(super(__DeferredResourcePackage, self).get(arg0))

    @override
    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource> dev.ultreon.libs.resources.v0.ResourcePackage.mapEntries()"""
        return 'Map'.__wrap(super(v0.ResourcePackage, self).mapEntries())

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
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.has(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool.__wrap(super(__DeferredResourcePackage, self).has(arg0))

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
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.libs.resources.v0.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = __DeferredResourcePackage(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.android.DeferredResourcePackage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.resources.v0.Resource as __Resource
__Resource = __Resource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.libs.resources.v0.android.DeferredResourcePackage as __DeferredResourcePackage
__DeferredResourcePackage = __DeferredResourcePackage
try:
    from pycorelibs.resources import v0
except ImportError:
    v0 = __import_once__("pycorelibs.resources.v0")

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
import java.lang.String as __string
import dev.ultreon.libs.resources.v0.ResourcePackage as __ResourcePackage
__ResourcePackage = __ResourcePackage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class DeferredResourcePackage(resources.__ResourcePackage, v0.ResourcePackage):
    """dev.ultreon.libs.resources.v0.android.DeferredResourcePackage"""
 
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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.resources.v0.ResourcePackage.entries()"""
        return 'Set'.__wrap(super(v0.ResourcePackage, self).entries())

    @overload
    def get(self, arg0: 'Identifier') -> 'v0.Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.get(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'v0.Resource'.__wrap(super(__DeferredResourcePackage, self).get(arg0))

    @override
    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource> dev.ultreon.libs.resources.v0.ResourcePackage.mapEntries()"""
        return 'Map'.__wrap(super(v0.ResourcePackage, self).mapEntries())

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
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.resources.v0.android.DeferredResourcePackage.has(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool.__wrap(super(__DeferredResourcePackage, self).has(arg0))

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
    def __init__(self, arg0: 'Class', arg1: str):
        """public dev.ultreon.libs.resources.v0.android.DeferredResourcePackage(java.lang.Class<?>,java.lang.String)"""
        val = __DeferredResourcePackage(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.android.DeferredResourcePackage