from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import java.util.Collection as Collection
import dev.ultreon.quantum.tags.NamedTag as __NamedTag
__NamedTag = __NamedTag
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NamedTag():
    """dev.ultreon.quantum.tags.NamedTag"""
 
    @staticmethod
    def __wrap(java_value: __NamedTag) -> 'NamedTag':
        return NamedTag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NamedTag):
        """
        Dynamic initializer for NamedTag.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.tags.NamedTag.hashCode()"""
        return int.__wrap(super(NamedTag, self).hashCode())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Registry'):
        """public dev.ultreon.quantum.tags.NamedTag(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.registry.Registry<T>)"""
        val = __NamedTag(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.equals(java.lang.Object)"""
        return bool.__wrap(super(__NamedTag, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.tags.NamedTag.toString()"""
        return str.__wrap(super(NamedTag, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.tags.NamedTag.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__NamedTag, self).reload(arg0)

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
    def getName(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.tags.NamedTag.getName()"""
        return 'util.Identifier'.__wrap(super(NamedTag, self).getName())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.contains(T)"""
        return bool.__wrap(super(__NamedTag, self).contains(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getValues(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.quantum.tags.NamedTag.getValues()"""
        return 'Collection'.__wrap(super(NamedTag, self).getValues())

 
 
 
# CLASS: dev.ultreon.quantum.tags.NamedTag
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import java.util.Collection as Collection
import dev.ultreon.quantum.tags.NamedTag as __NamedTag
__NamedTag = __NamedTag
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NamedTag():
    """dev.ultreon.quantum.tags.NamedTag"""
 
    @staticmethod
    def __wrap(java_value: __NamedTag) -> 'NamedTag':
        return NamedTag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NamedTag):
        """
        Dynamic initializer for NamedTag.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.tags.NamedTag.hashCode()"""
        return int.__wrap(super(NamedTag, self).hashCode())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Registry'):
        """public dev.ultreon.quantum.tags.NamedTag(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.registry.Registry<T>)"""
        val = __NamedTag(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.equals(java.lang.Object)"""
        return bool.__wrap(super(__NamedTag, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.tags.NamedTag.toString()"""
        return str.__wrap(super(NamedTag, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.tags.NamedTag.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__NamedTag, self).reload(arg0)

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
    def getName(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.tags.NamedTag.getName()"""
        return 'util.Identifier'.__wrap(super(NamedTag, self).getName())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.contains(T)"""
        return bool.__wrap(super(__NamedTag, self).contains(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getValues(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.quantum.tags.NamedTag.getValues()"""
        return 'Collection'.__wrap(super(NamedTag, self).getValues())

 
 
 
# CLASS: dev.ultreon.quantum.tags.NamedTag