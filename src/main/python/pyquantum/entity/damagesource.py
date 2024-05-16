from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
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
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.entity.damagesource.DamageSource as __DamageSource
__DamageSource = __DamageSource
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DamageSource():
    """dev.ultreon.quantum.entity.damagesource.DamageSource"""
 
    @staticmethod
    def __wrap(java_value: __DamageSource) -> 'DamageSource':
        return DamageSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DamageSource):
        """
        Dynamic initializer for DamageSource.
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
 
    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.FALLING
    FALLING: 'DamageSource' = __wrap(__DamageSource.FALLING)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.PLAYER
    PLAYER: 'DamageSource' = __wrap(__DamageSource.PLAYER)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.VOID
    VOID: 'DamageSource' = __wrap(__DamageSource.VOID)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.HUNGER
    HUNGER: 'DamageSource' = __wrap(__DamageSource.HUNGER)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.KILL
    KILL: 'DamageSource' = __wrap(__DamageSource.KILL)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.NOTHING
    NOTHING: 'DamageSource' = __wrap(__DamageSource.NOTHING)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def byPassInvincibility(self, arg0: bool) -> 'DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility(boolean)"""
        return 'DamageSource'.__wrap(super(__DamageSource, self).byPassInvincibility(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = __DamageSource()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = __DamageSource()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDescription(self, arg0: 'Entity') -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.damagesource.DamageSource.getDescription(dev.ultreon.quantum.entity.Entity)"""
        return 'text.TextObject'.__wrap(super(__DamageSource, self).getDescription(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getType(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.entity.damagesource.DamageSource.getType()"""
        return 'util.Identifier'.__wrap(super(DamageSource, self).getType())

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
    def byPassInvincibility(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility()"""
        return bool.__wrap(super(DamageSource, self).byPassInvincibility())

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

 
 
 
# CLASS: dev.ultreon.quantum.entity.damagesource.DamageSource
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
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
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.entity.damagesource.DamageSource as __DamageSource
__DamageSource = __DamageSource
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DamageSource():
    """dev.ultreon.quantum.entity.damagesource.DamageSource"""
 
    @staticmethod
    def __wrap(java_value: __DamageSource) -> 'DamageSource':
        return DamageSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DamageSource):
        """
        Dynamic initializer for DamageSource.
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
 
    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.FALLING
    FALLING: 'DamageSource' = __wrap(__DamageSource.FALLING)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.PLAYER
    PLAYER: 'DamageSource' = __wrap(__DamageSource.PLAYER)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.VOID
    VOID: 'DamageSource' = __wrap(__DamageSource.VOID)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.HUNGER
    HUNGER: 'DamageSource' = __wrap(__DamageSource.HUNGER)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.KILL
    KILL: 'DamageSource' = __wrap(__DamageSource.KILL)

    # public static final dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.NOTHING
    NOTHING: 'DamageSource' = __wrap(__DamageSource.NOTHING)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def byPassInvincibility(self, arg0: bool) -> 'DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility(boolean)"""
        return 'DamageSource'.__wrap(super(__DamageSource, self).byPassInvincibility(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = __DamageSource()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.damagesource.DamageSource()"""
        val = __DamageSource()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDescription(self, arg0: 'Entity') -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.damagesource.DamageSource.getDescription(dev.ultreon.quantum.entity.Entity)"""
        return 'text.TextObject'.__wrap(super(__DamageSource, self).getDescription(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getType(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.entity.damagesource.DamageSource.getType()"""
        return 'util.Identifier'.__wrap(super(DamageSource, self).getType())

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
    def byPassInvincibility(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.damagesource.DamageSource.byPassInvincibility()"""
        return bool.__wrap(super(DamageSource, self).byPassInvincibility())

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

 
 
 
# CLASS: dev.ultreon.quantum.entity.damagesource.DamageSource