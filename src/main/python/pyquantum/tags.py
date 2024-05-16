from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import dev.ultreon.quantum.tags.NamedTag as _NamedTag
_NamedTag = _NamedTag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NamedTag():
    """dev.ultreon.quantum.tags.NamedTag"""
 
    @staticmethod
    def _wrap(java_value: _NamedTag) -> 'NamedTag':
        return NamedTag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NamedTag):
        """
        Dynamic initializer for NamedTag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NamedTag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NamedTag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getValues(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.quantum.tags.NamedTag.getValues()"""
        return 'Collection'._wrap(super(NamedTag, self).getValues())

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
        """public java.lang.String dev.ultreon.quantum.tags.NamedTag.toString()"""
        return str._wrap(super(NamedTag, self).toString())

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
    def getName(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.tags.NamedTag.getName()"""
        return 'util.Identifier'._wrap(super(NamedTag, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.equals(java.lang.Object)"""
        return bool._wrap(super(_NamedTag, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.tags.NamedTag.hashCode()"""
        return int._wrap(super(NamedTag, self).hashCode())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.contains(T)"""
        return bool._wrap(super(_NamedTag, self).contains(arg0))

    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.tags.NamedTag.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_NamedTag, self).reload(arg0)

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Registry'):
        """public dev.ultreon.quantum.tags.NamedTag(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.registry.Registry<T>)"""
        val = _NamedTag(arg0, arg1)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.tags.NamedTag
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import dev.ultreon.quantum.tags.NamedTag as _NamedTag
_NamedTag = _NamedTag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NamedTag():
    """dev.ultreon.quantum.tags.NamedTag"""
 
    @staticmethod
    def _wrap(java_value: _NamedTag) -> 'NamedTag':
        return NamedTag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NamedTag):
        """
        Dynamic initializer for NamedTag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NamedTag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NamedTag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getValues(self) -> 'Collection':
        """public java.util.Collection<T> dev.ultreon.quantum.tags.NamedTag.getValues()"""
        return 'Collection'._wrap(super(NamedTag, self).getValues())

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
        """public java.lang.String dev.ultreon.quantum.tags.NamedTag.toString()"""
        return str._wrap(super(NamedTag, self).toString())

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
    def getName(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.tags.NamedTag.getName()"""
        return 'util.Identifier'._wrap(super(NamedTag, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.equals(java.lang.Object)"""
        return bool._wrap(super(_NamedTag, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.tags.NamedTag.hashCode()"""
        return int._wrap(super(NamedTag, self).hashCode())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.tags.NamedTag.contains(T)"""
        return bool._wrap(super(_NamedTag, self).contains(arg0))

    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.tags.NamedTag.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_NamedTag, self).reload(arg0)

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Registry'):
        """public dev.ultreon.quantum.tags.NamedTag(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.registry.Registry<T>)"""
        val = _NamedTag(arg0, arg1)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.tags.NamedTag