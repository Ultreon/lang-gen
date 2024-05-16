from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DamageSource():
    """dev.ultreon.quantum.entity.damagesource.DamageSource"""
 
    @staticmethod
    def _wrap(java_value: _DamageSource) -> 'DamageSource':
        return DamageSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DamageSource):
        """
        Dynamic initializer for DamageSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DamageSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DamageSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDescription(self, arg0: 'Entity') -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.damagesource.DamageSource.getDescription(dev.ultreon.quantum.entity.Entity)"""
        return 'text.TextObject'._wrap(super(_DamageSource, self).getDescription(arg0))

    @overload
    def getType(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.entity.damagesource.DamageSource.getType()"""
        return 'util.Identifier'._wrap(super(DamageSource, self).getType())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = _DamageSource()
        self.__wrapper = val

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
    def byPassInvincibility(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility()"""
        return bool._wrap(super(DamageSource, self).byPassInvincibility())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = _DamageSource()
        self.__wrapper = val

    @overload
    def byPassInvincibility(self, arg0: bool) -> 'DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility(boolean)"""
        return 'DamageSource'._wrap(super(_DamageSource, self).byPassInvincibility(_boolean.valueOf(arg0)))

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


DamageSource.VOID = DamageSource._wrap(_VOID.VOID)

DamageSource.NOTHING = DamageSource._wrap(_NOTHING.NOTHING)

DamageSource.FALLING = DamageSource._wrap(_FALLING.FALLING)

DamageSource.HUNGER = DamageSource._wrap(_HUNGER.HUNGER)

DamageSource.KILL = DamageSource._wrap(_KILL.KILL)

DamageSource.PLAYER = DamageSource._wrap(_PLAYER.PLAYER)

 
 
 
# CLASS: dev.ultreon.quantum.entity.damagesource.DamageSource
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DamageSource():
    """dev.ultreon.quantum.entity.damagesource.DamageSource"""
 
    @staticmethod
    def _wrap(java_value: _DamageSource) -> 'DamageSource':
        return DamageSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DamageSource):
        """
        Dynamic initializer for DamageSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DamageSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DamageSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDescription(self, arg0: 'Entity') -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.damagesource.DamageSource.getDescription(dev.ultreon.quantum.entity.Entity)"""
        return 'text.TextObject'._wrap(super(_DamageSource, self).getDescription(arg0))

    @overload
    def getType(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.entity.damagesource.DamageSource.getType()"""
        return 'util.Identifier'._wrap(super(DamageSource, self).getType())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = _DamageSource()
        self.__wrapper = val

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
    def byPassInvincibility(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility()"""
        return bool._wrap(super(DamageSource, self).byPassInvincibility())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = _DamageSource()
        self.__wrapper = val

    @overload
    def byPassInvincibility(self, arg0: bool) -> 'DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility(boolean)"""
        return 'DamageSource'._wrap(super(_DamageSource, self).byPassInvincibility(_boolean.valueOf(arg0)))

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


DamageSource.VOID = DamageSource._wrap(_VOID.VOID)

DamageSource.NOTHING = DamageSource._wrap(_NOTHING.NOTHING)

DamageSource.FALLING = DamageSource._wrap(_FALLING.FALLING)

DamageSource.HUNGER = DamageSource._wrap(_HUNGER.HUNGER)

DamageSource.KILL = DamageSource._wrap(_KILL.KILL)

DamageSource.PLAYER = DamageSource._wrap(_PLAYER.PLAYER)

 
 
 
# CLASS: dev.ultreon.quantum.entity.damagesource.DamageSource