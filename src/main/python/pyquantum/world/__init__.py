from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class BlockPos():
    """dev.ultreon.quantum.world.BlockPos"""
 
    @staticmethod
    def __wrap(java_value: __BlockPos) -> 'BlockPos':
        return BlockPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockPos):
        """
        Dynamic initializer for BlockPos.
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
        """public int dev.ultreon.quantum.world.BlockPos.hashCode()"""
        return int.__wrap(super(BlockPos, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.BlockPos.equals(java.lang.Object)"""
        return bool.__wrap(super(__BlockPos, self).equals(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.BlockPos(double,double,double)"""
        val = __BlockPos(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.x()"""
        return int.__wrap(super(BlockPos, self).x())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.BlockPos.toString()"""
        return str.__wrap(super(BlockPos, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def offset(self, arg0: 'ChunkPos') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.ChunkPos)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(arg0))

    @overload
    def vec(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.BlockPos.vec()"""
        return 'vector.Vec3i'.__wrap(super(BlockPos, self).vec())

    @overload
    def y(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.y()"""
        return int.__wrap(super(BlockPos, self).y())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def below(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.below()"""
        return 'BlockPos'.__wrap(super(BlockPos, self).below())

    @overload
    def above(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.above()"""
        return 'BlockPos'.__wrap(super(BlockPos, self).above())

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
    def __init__(self, arg0: 'Vec3i'):
        """public dev.ultreon.quantum.world.BlockPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        val = __BlockPos(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.world.BlockPos(int,int,int)"""
        val = __BlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = __BlockPos()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.z()"""
        return int.__wrap(super(BlockPos, self).z())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = __BlockPos()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def offset(self, arg0: 'CubicDirection') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(arg0))

    @overload
    def offset(self, arg0: 'CubicDirection', arg1: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection,int)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(arg0, __int.valueOf(arg1)))

    @overload
    def offset(self, arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(int,int,int)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

 
 
 
# CLASS: dev.ultreon.quantum.world.BlockPos
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class BlockPos():
    """dev.ultreon.quantum.world.BlockPos"""
 
    @staticmethod
    def __wrap(java_value: __BlockPos) -> 'BlockPos':
        return BlockPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockPos):
        """
        Dynamic initializer for BlockPos.
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
        """public int dev.ultreon.quantum.world.BlockPos.hashCode()"""
        return int.__wrap(super(BlockPos, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.BlockPos.equals(java.lang.Object)"""
        return bool.__wrap(super(__BlockPos, self).equals(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.BlockPos(double,double,double)"""
        val = __BlockPos(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.x()"""
        return int.__wrap(super(BlockPos, self).x())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.BlockPos.toString()"""
        return str.__wrap(super(BlockPos, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def offset(self, arg0: 'ChunkPos') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.ChunkPos)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(arg0))

    @overload
    def vec(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.BlockPos.vec()"""
        return 'vector.Vec3i'.__wrap(super(BlockPos, self).vec())

    @overload
    def y(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.y()"""
        return int.__wrap(super(BlockPos, self).y())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def below(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.below()"""
        return 'BlockPos'.__wrap(super(BlockPos, self).below())

    @overload
    def above(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.above()"""
        return 'BlockPos'.__wrap(super(BlockPos, self).above())

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
    def __init__(self, arg0: 'Vec3i'):
        """public dev.ultreon.quantum.world.BlockPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        val = __BlockPos(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.world.BlockPos(int,int,int)"""
        val = __BlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = __BlockPos()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.z()"""
        return int.__wrap(super(BlockPos, self).z())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = __BlockPos()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def offset(self, arg0: 'CubicDirection') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(arg0))

    @overload
    def offset(self, arg0: 'CubicDirection', arg1: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection,int)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(arg0, __int.valueOf(arg1)))

    @overload
    def offset(self, arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(int,int,int)"""
        return 'BlockPos'.__wrap(super(__BlockPos, self).offset(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

 
 
 
# CLASS: dev.ultreon.quantum.world.BlockPos 
 
 
# CLASS: dev.ultreon.quantum.world.SoundEvent
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.SoundEvent as __SoundEvent
__SoundEvent = __SoundEvent
from builtins import float
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SoundEvent():
    """dev.ultreon.quantum.world.SoundEvent"""
 
    @staticmethod
    def __wrap(java_value: __SoundEvent) -> 'SoundEvent':
        return SoundEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SoundEvent):
        """
        Dynamic initializer for SoundEvent.
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

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.world.SoundEvent(float)"""
        val = __SoundEvent(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRange(self) -> float:
        """public float dev.ultreon.quantum.world.SoundEvent.getRange()"""
        return float.__wrap(super(SoundEvent, self).getRange())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.SoundEvent.getId()"""
        return 'util.Identifier'.__wrap(super(SoundEvent, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.CubicDirection
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.CubicDirection as __CubicDirection
__CubicDirection = __CubicDirection
import dev.ultreon.quantum.util.Axis as __Axis
__Axis = __Axis
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.math.Quaternion as __Quaternion
__Quaternion = __Quaternion
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class CubicDirection():
    """dev.ultreon.quantum.world.CubicDirection"""
 
    @staticmethod
    def __wrap(java_value: __CubicDirection) -> 'CubicDirection':
        return CubicDirection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CubicDirection):
        """
        Dynamic initializer for CubicDirection.
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
 
    # public static final dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.DOWN
    DOWN: 'CubicDirection' = __wrap(__CubicDirection.DOWN)

    # public static final dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.NORTH
    NORTH: 'CubicDirection' = __wrap(__CubicDirection.NORTH)

    # public static final dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.UP
    UP: 'CubicDirection' = __wrap(__CubicDirection.UP)

    # public static final dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.WEST
    WEST: 'CubicDirection' = __wrap(__CubicDirection.WEST)

    # public static final dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.SOUTH
    SOUTH: 'CubicDirection' = __wrap(__CubicDirection.SOUTH)

    # public static final dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.EAST
    EAST: 'CubicDirection' = __wrap(__CubicDirection.EAST)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @overload
    def rotateY(self, arg0: int) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.rotateY(int)"""
        return 'CubicDirection'.__wrap(super(__CubicDirection, self).rotateY(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CubicDirection':
        """public static dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.valueOf(java.lang.String)"""
        return CubicDirection.__wrap(__CubicDirection.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def values() -> List['CubicDirection']:
        """public static dev.ultreon.quantum.world.CubicDirection[] dev.ultreon.quantum.world.CubicDirection.values()"""
        return List[CubicDirection].__wrap(__CubicDirection.values())

    @staticmethod
    @overload
    def fromVec3d(arg0: 'Vec3d') -> 'CubicDirection':
        """public static dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.fromVec3d(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return CubicDirection.__wrap(__CubicDirection.fromVec3d(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.world.CubicDirection.getIndex()"""
        return int.__wrap(super(CubicDirection, self).getIndex())

    @overload
    def getClockwise(self) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.getClockwise()"""
        return 'CubicDirection'.__wrap(super(CubicDirection, self).getClockwise())

    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.world.CubicDirection.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(CubicDirection, self).getDisplayName())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @overload
    def getCounterClockwise(self) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.getCounterClockwise()"""
        return 'CubicDirection'.__wrap(super(CubicDirection, self).getCounterClockwise())

    @overload
    def getNormal(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.world.CubicDirection.getNormal()"""
        return 'math.Vector3'.__wrap(super(CubicDirection, self).getNormal())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def ofNormal(arg0: 'Vec3f') -> 'CubicDirection':
        """public static dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.ofNormal(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return CubicDirection.__wrap(__CubicDirection.ofNormal(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAxis(self) -> 'util.Axis':
        """public dev.ultreon.quantum.util.Axis dev.ultreon.quantum.world.CubicDirection.getAxis()"""
        return 'util.Axis'.__wrap(super(CubicDirection, self).getAxis())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @overload
    def getHorizontalRotation(self) -> 'math.Quaternion':
        """public com.badlogic.gdx.math.Quaternion dev.ultreon.quantum.world.CubicDirection.getHorizontalRotation()"""
        return 'math.Quaternion'.__wrap(super(CubicDirection, self).getHorizontalRotation())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @overload
    def getOpposite(self) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.getOpposite()"""
        return 'CubicDirection'.__wrap(super(CubicDirection, self).getOpposite())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getOffset(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.CubicDirection.getOffset()"""
        return 'BlockPos'.__wrap(super(CubicDirection, self).getOffset())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.world.Chunk$Status
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.world.Chunk as __Chunk_Status
__Status = __Chunk_Status.Status
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Status():
    """dev.ultreon.quantum.world.Chunk.Status"""
 
    @staticmethod
    def __wrap(java_value: __Status) -> 'Status':
        return Status(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Status):
        """
        Dynamic initializer for Status.
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
 
    # public static final dev.ultreon.quantum.world.Chunk$Status dev.ultreon.quantum.world.Chunk$Status.FAILED
    FAILED: 'Status' = __wrap(__Status.FAILED)

    # public static final dev.ultreon.quantum.world.Chunk$Status dev.ultreon.quantum.world.Chunk$Status.UNLOADED
    UNLOADED: 'Status' = __wrap(__Status.UNLOADED)

    # public static final dev.ultreon.quantum.world.Chunk$Status dev.ultreon.quantum.world.Chunk$Status.SUCCESS
    SUCCESS: 'Status' = __wrap(__Status.SUCCESS)

    # public static final dev.ultreon.quantum.world.Chunk$Status dev.ultreon.quantum.world.Chunk$Status.SKIP
    SKIP: 'Status' = __wrap(__Status.SKIP)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Status':
        """public static dev.ultreon.quantum.world.Chunk$Status dev.ultreon.quantum.world.Chunk$Status.valueOf(java.lang.String)"""
        return Status.__wrap(__Status.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['Status']:
        """public static dev.ultreon.quantum.world.Chunk$Status[] dev.ultreon.quantum.world.Chunk$Status.values()"""
        return List[Status].__wrap(__Status.values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.world.BuilderChunk
from pyquantum_helper import import_once as __import_once__
import java.lang.Thread as Thread
import dev.ultreon.quantum.world.Chunk as __Chunk
__Chunk = __Chunk
try:
    from pyquantum.world.gen import biome
except ImportError:
    biome = __import_once__("pyquantum.world.gen.biome")

try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

try:
    from pyquantum.world import gen
except ImportError:
    gen = __import_once__("pyquantum.world.gen")

from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator
__BiomeGenerator = __BiomeGenerator
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import java.util.Collection as Collection
try:
    from pyquantum import collection
except ImportError:
    collection = __import_once__("pyquantum.collection")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.world.LightMap as __LightMap
__LightMap = __LightMap
import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.quantum.world.ServerChunk as __ServerChunk
__ServerChunk = __ServerChunk
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.lang.Float as __float
import dev.ultreon.quantum.world.gen.TreeData as __TreeData
__TreeData = __TreeData
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.BuilderChunk as __BuilderChunk
__BuilderChunk = __BuilderChunk
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class BuilderChunk():
    """dev.ultreon.quantum.world.BuilderChunk"""
 
    @staticmethod
    def __wrap(java_value: __BuilderChunk) -> 'BuilderChunk':
        return BuilderChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BuilderChunk):
        """
        Dynamic initializer for BuilderChunk.
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
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'.__wrap(super(Chunk, self).getOffset())

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'Biome'.__wrap(super(__Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def build(self) -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.BuilderChunk.build()"""
        return 'ServerChunk'.__wrap(super(BuilderChunk, self).build())

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int.__wrap(super(__Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRNG(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.world.BuilderChunk.getRNG()"""
        return 'rng.RNG'.__wrap(super(BuilderChunk, self).getRNG())

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(arg0))

    @overload
    def getBiomeCenters(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3i> dev.ultreon.quantum.world.BuilderChunk.getBiomeCenters()"""
        return 'List'.__wrap(super(BuilderChunk, self).getBiomeCenters())

    @override
    @overload
    def getPos(self) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'ChunkPos'.__wrap(super(Chunk, self).getPos())

    @override
    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(__Chunk, self).setTreeData(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int.__wrap(super(__Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block.__wrap(__Chunk.decodeBlock(arg0))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'BreakResult'.__wrap(super(__Chunk, self).continueBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'Thread', arg2: 'ChunkPos', arg3: 'Region'):
        """public dev.ultreon.quantum.world.BuilderChunk(dev.ultreon.quantum.world.ServerWorld,java.lang.Thread,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ServerWorld$Region)"""
        val = __BuilderChunk(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool.__wrap(super(Chunk, self).isReady())

    @override
    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.BuilderChunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__BuilderChunk, self).setFast(arg0, arg1)

    @property
    def biomeStorage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).biomeStorage())

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float.__wrap(super(__Chunk, self).getBrightness(__int.valueOf(arg0)))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(__Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(arg0))

    @overload
    def isOnBuilderThread(self) -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.isOnBuilderThread()"""
        return bool.__wrap(super(BuilderChunk, self).isOnBuilderThread())

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.BuilderChunk.getFast(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__BuilderChunk, self).getFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool.__wrap(super(Chunk, self).isActive())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int.__wrap(super(Chunk, self).hashCode())

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool.__wrap(super(Chunk, self).isDisposed())

    @override
    @overload
    def getWorld(self) -> 'ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.world.BuilderChunk.getWorld()"""
        return 'ServerWorld'.__wrap(super(BuilderChunk, self).getWorld())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(__Chunk, self).stopBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__Chunk, self).getBlockLight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(__Chunk, self).removeBlockEntity(arg0)

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__Chunk, self).getSunlight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'.__wrap(super(Chunk, self).getBreaking())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.BuilderChunk.getHighest(int,int)"""
        return int.__wrap(super(__BuilderChunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Chunk, self).getBlockLight(arg0))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties.__wrap(__Chunk.loadBlock(arg0))

    @overload
    def getBiomeGenerator(self, arg0: int, arg1: int) -> 'biome.BiomeGenerator':
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator dev.ultreon.quantum.world.BuilderChunk.getBiomeGenerator(int,int)"""
        return 'biome.BiomeGenerator'.__wrap(super(__BuilderChunk, self).getBiomeGenerator(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'Biome'.__wrap(super(__Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(arg0))

    @override
    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.world.Chunk.onUpdated()"""
        super(Chunk, self).onUpdated()

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Chunk, self).getSunlight(arg0))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__BuilderChunk, self).setFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @property
    def treeData(self) -> TreeData:
        return TreeData.__wrap(super(__Chunk).treeData())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.Chunk.dispose()"""
        super(Chunk, self).dispose()

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).getFast(arg0))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int.__wrap(super(__Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @property
    def storage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).storage())

    @override
    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.BuilderChunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__BuilderChunk, self).set(arg0, arg1)

    @override
    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'.__wrap(super(Chunk, self).getBlockEntities())

    @overload
    def setBiomeGenerator(self, arg0: int, arg1: int, arg2: 'BiomeGenerator'):
        """public void dev.ultreon.quantum.world.BuilderChunk.setBiomeGenerator(int,int,dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        super(__BuilderChunk, self).setBiomeGenerator(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str.__wrap(super(Chunk, self).toString())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__BuilderChunk, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def setBiomeCenters(self, arg0: 'List'):
        """public void dev.ultreon.quantum.world.BuilderChunk.setBiomeCenters(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3i>)"""
        super(__BuilderChunk, self).setBiomeCenters(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool.__wrap(super(__Chunk, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLightMap(self) -> 'LightMap':
        """public dev.ultreon.quantum.world.LightMap dev.ultreon.quantum.world.BuilderChunk.getLightMap()"""
        return 'LightMap'.__wrap(super(BuilderChunk, self).getLightMap())

    @override
    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(__Chunk, self).startBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def isOnInvalidThread(self) -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.isOnInvalidThread()"""
        return bool.__wrap(super(BuilderChunk, self).isOnInvalidThread()) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerChunk
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.Chunk as __Chunk
__Chunk = __Chunk
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

try:
    from pyquantum.world import gen
except ImportError:
    gen = __import_once__("pyquantum.world.gen")

from builtins import type
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import java.util.Collection as Collection
try:
    from pyquantum import collection
except ImportError:
    collection = __import_once__("pyquantum.collection")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.quantum.world.ServerChunk as __ServerChunk
__ServerChunk = __ServerChunk
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.lang.Float as __float
import dev.ultreon.quantum.world.gen.TreeData as __TreeData
__TreeData = __TreeData
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class ServerChunk():
    """dev.ultreon.quantum.world.ServerChunk"""
 
    @staticmethod
    def __wrap(java_value: __ServerChunk) -> 'ServerChunk':
        return ServerChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerChunk):
        """
        Dynamic initializer for ServerChunk.
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
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'.__wrap(super(Chunk, self).getOffset())

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'Biome'.__wrap(super(__Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int.__wrap(super(__Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(arg0))

    @overload
    def shouldSave(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerChunk.shouldSave()"""
        return bool.__wrap(super(ServerChunk, self).shouldSave())

    @override
    @overload
    def getPos(self) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'ChunkPos'.__wrap(super(Chunk, self).getPos())

    @override
    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(__Chunk, self).setTreeData(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int.__wrap(super(__Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Chunk, self).setFast(arg0, arg1)

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block.__wrap(__Chunk.decodeBlock(arg0))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'BreakResult'.__wrap(super(__Chunk, self).continueBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.world.ServerChunk.load(dev.ultreon.ubo.types.MapType)"""
        super(__ServerChunk, self).load(arg0)

    @override
    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool.__wrap(super(Chunk, self).isReady())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Chunk, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @property
    def biomeStorage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).biomeStorage())

    @override
    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Chunk, self).set(arg0, arg1)

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float.__wrap(super(__Chunk, self).getBrightness(__int.valueOf(arg0)))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(__Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool.__wrap(super(Chunk, self).isActive())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int.__wrap(super(Chunk, self).hashCode())

    @staticmethod
    @overload
    def load(arg0: 'ServerWorld', arg1: 'ChunkPos', arg2: 'MapType', arg3: 'Region') -> 'ServerChunk':
        """public static dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerChunk.load(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.ubo.types.MapType,dev.ultreon.quantum.world.ServerWorld$Region)"""
        return ServerChunk.__wrap(__ServerChunk.load(arg0, arg1, arg2, arg3))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool.__wrap(super(Chunk, self).isDisposed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'ChunkPos', arg2: 'Storage', arg3: 'Storage', arg4: 'Region'):
        """public dev.ultreon.quantum.world.ServerChunk(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,dev.ultreon.quantum.world.ServerWorld$Region)"""
        val = __ServerChunk(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(__Chunk, self).stopBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__Chunk, self).getBlockLight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(__Chunk, self).removeBlockEntity(arg0)

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).getFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__Chunk, self).getSunlight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'.__wrap(super(Chunk, self).getBreaking())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int)"""
        return int.__wrap(super(__Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Chunk, self).getBlockLight(arg0))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties.__wrap(__Chunk.loadBlock(arg0))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__ServerChunk, self).setFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'Biome'.__wrap(super(__Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(arg0))

    @override
    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.world.Chunk.onUpdated()"""
        super(Chunk, self).onUpdated()

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Chunk, self).getSunlight(arg0))

    @property
    def treeData(self) -> TreeData:
        return TreeData.__wrap(super(__Chunk).treeData())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.Chunk.dispose()"""
        super(Chunk, self).dispose()

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).getFast(arg0))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int.__wrap(super(__Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @property
    def storage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).storage())

    @override
    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'.__wrap(super(Chunk, self).getBlockEntities())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str.__wrap(super(Chunk, self).toString())

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.ServerChunk.save()"""
        return 'types.MapType'.__wrap(super(ServerChunk, self).save())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool.__wrap(super(__Chunk, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(__Chunk, self).startBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getWorld(self) -> 'ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.world.ServerChunk.getWorld()"""
        return 'ServerWorld'.__wrap(super(ServerChunk, self).getWorld())

    @overload
    def isOriginal(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerChunk.isOriginal()"""
        return bool.__wrap(super(ServerChunk, self).isOriginal()) 
 
 
# CLASS: dev.ultreon.quantum.world.TerrainNoise
from builtins import str
import dev.ultreon.quantum.world.TerrainNoise as __TerrainNoise
__TerrainNoise = __TerrainNoise
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TerrainNoise():
    """dev.ultreon.quantum.world.TerrainNoise"""
 
    @staticmethod
    def __wrap(java_value: __TerrainNoise) -> 'TerrainNoise':
        return TerrainNoise(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TerrainNoise):
        """
        Dynamic initializer for TerrainNoise.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def evaluateNoise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double,double)"""
        return float.__wrap(super(__TerrainNoise, self).evaluateNoise(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double,double,double,double)"""
        return float.__wrap(super(__TerrainNoise, self).evaluateNoise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double,double,double)"""
        return float.__wrap(super(__TerrainNoise, self).evaluateNoise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

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
    def evaluateNoise(self, arg0: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double)"""
        return float.__wrap(super(__TerrainNoise, self).evaluateNoise(__double.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.TerrainNoise(long)"""
        val = __TerrainNoise(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld$RegionStorage
from builtins import str
import java.io.DataOutputStream as DataOutputStream
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld_RegionStorage
__RegionStorage = __ServerWorld_RegionStorage.RegionStorage
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld_Region
__Region = __ServerWorld_Region.Region
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.io.DataInputStream as DataInputStream
from builtins import int
 
class RegionStorage():
    """dev.ultreon.quantum.world.ServerWorld.RegionStorage"""
 
    @staticmethod
    def __wrap(java_value: __RegionStorage) -> 'RegionStorage':
        return RegionStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegionStorage):
        """
        Dynamic initializer for RegionStorage.
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
    def save(self, arg0: 'Region', arg1: 'DataOutputStream', arg2: bool):
        """public void dev.ultreon.quantum.world.ServerWorld$RegionStorage.save(dev.ultreon.quantum.world.ServerWorld$Region,java.io.DataOutputStream,boolean) throws java.io.IOException"""
        super(__RegionStorage, self).save(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getRegionAt(self, arg0: 'ChunkPos') -> 'Region':
        """public dev.ultreon.quantum.world.ServerWorld$Region dev.ultreon.quantum.world.ServerWorld$RegionStorage.getRegionAt(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Region'.__wrap(super(__RegionStorage, self).getRegionAt(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.ServerWorld$RegionStorage()"""
        val = __RegionStorage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'ServerWorld', arg1: 'DataInputStream') -> 'Region':
        """public dev.ultreon.quantum.world.ServerWorld$Region dev.ultreon.quantum.world.ServerWorld$RegionStorage.load(dev.ultreon.quantum.world.ServerWorld,java.io.DataInputStream) throws java.io.IOException"""
        return 'Region'.__wrap(super(__RegionStorage, self).load(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getChunkCount(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RegionStorage.getChunkCount()"""
        return int.__wrap(super(RegionStorage, self).getChunkCount())

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

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.ServerWorld$RegionStorage.dispose()"""
        super(RegionStorage, self).dispose()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.ServerWorld$RegionStorage()"""
        val = __RegionStorage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.World
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.util.EntityHitResult as __EntityHitResult
__EntityHitResult = __EntityHitResult
import java.util.function.Predicate as Predicate
import java.util.UUID as UUID
import dev.ultreon.quantum.world.Chunk as __Chunk
__Chunk = __Chunk
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import java.util.Collection as Collection
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.Double as __double
from builtins import bool
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
from builtins import float
import dev.ultreon.quantum.world.DimensionInfo as __DimensionInfo
__DimensionInfo = __DimensionInfo
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.world import particles
except ImportError:
    particles = __import_once__("pyquantum.world.particles")

import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.World as __World
__World = __World
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import dev.ultreon.quantum.util.BlockHitResult as __BlockHitResult
__BlockHitResult = __BlockHitResult
import java.lang.Object as __object
import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Integer as __int
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class World(ABC):
    """dev.ultreon.quantum.world.World"""
 
    @staticmethod
    def __wrap(java_value: __World) -> 'World':
        return World(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __World):
        """
        Dynamic initializer for World.
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
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.World.OVERWORLD
    OVERWORLD: 'util.Identifier' = __wrap(__util.Identifier.OVERWORLD)


    @overload
    def getEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.world.World.getEntity(int)"""
        return 'entity.Entity'.__wrap(super(__World, self).getEntity(__int.valueOf(arg0)))

    @overload
    def isOutOfWorldBounds(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(dev.ultreon.quantum.world.BlockPos)"""
        return bool.__wrap(super(__World, self).isOutOfWorldBounds(arg0))

    @abstractmethod
    def getLoadedChunks(self, ):
        """public abstract java.util.Collection<? extends dev.ultreon.quantum.world.Chunk> dev.ultreon.quantum.world.World.getLoadedChunks()"""
        pass

    @overload
    def updateChunk(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunk(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).updateChunk(arg0)

    @overload
    def collide(self, arg0: 'BoundingBox', arg1: bool) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.BoundingBox> dev.ultreon.quantum.world.World.collide(dev.ultreon.quantum.util.BoundingBox,boolean)"""
        return 'List'.__wrap(super(__World, self).collide(arg0, __boolean.valueOf(arg1)))

    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__World, self).openMenu(arg0)

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float) -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def fillCrashInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.world.World.fillCrashInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(__World, self).fillCrashInfo(arg0)

    @overload
    def isServerSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isServerSide()"""
        return bool.__wrap(super(World, self).isServerSide())

    @overload
    def startBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.startBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__World, self).startBreaking(arg0, arg1)

    @overload
    def spawn(self, arg0: 'Entity') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T)"""
        return 'entity.Entity'.__wrap(super(__World, self).spawn(arg0))

    @overload
    def despawn(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.world.World.despawn(dev.ultreon.quantum.entity.Entity)"""
        super(__World, self).despawn(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChunk(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunk(int,int)"""
        return 'Chunk'.__wrap(super(__World, self).getChunk(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__World, self).setColumn(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def updateNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).updateNeighbours(arg0)

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3i') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @overload
    def intersectEntities(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.world.World.intersectEntities(dev.ultreon.quantum.util.BoundingBox)"""
        return bool.__wrap(super(__World, self).intersectEntities(arg0))

    @overload
    def stopBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.stopBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__World, self).stopBreaking(arg0, arg1)

    @overload
    def entitiesWithinDst(self, arg0: 'Entity', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.entitiesWithinDst(dev.ultreon.quantum.entity.Entity,int)"""
        return 'List'.__wrap(super(__World, self).entitiesWithinDst(arg0, __int.valueOf(arg1)))

    @overload
    def collideEntities(self, arg0: 'Entity', arg1: 'BoundingBox') -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.collideEntities(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.util.BoundingBox)"""
        return 'List'.__wrap(super(__World, self).collideEntities(arg0, arg1))

    @overload
    def isSpawnChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isSpawnChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__World, self).isSpawnChunk(arg0))

    @overload
    def spawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.world.World.spawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(__World, self).spawnParticles(arg0, arg1, arg2, __int.valueOf(arg3))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Predicate') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.util.function.Predicate<dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toChunkPos(arg0: int, arg1: int, arg2: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(int,int,int)"""
        return ChunkPos.__wrap(__World.toChunkPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__World, self).set(arg0, arg1))

    @overload
    def getSeed(self) -> int:
        """public long dev.ultreon.quantum.world.World.getSeed()"""
        return int.__wrap(super(World, self).getSeed())

    @overload
    def getChunksLoaded(self) -> int:
        """public int dev.ultreon.quantum.world.World.getChunksLoaded()"""
        return int.__wrap(super(World, self).getChunksLoaded())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isChunkInvalidated(self, arg0: 'Chunk') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isChunkInvalidated(dev.ultreon.quantum.world.Chunk)"""
        return bool.__wrap(super(__World, self).isChunkInvalidated(arg0))

    @overload
    def getChunksAround(self, arg0: 'Vec3d') -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.World.getChunksAround(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'List'.__wrap(super(__World, self).getChunksAround(arg0))

    @overload
    def getBreakProgress(self, arg0: 'BlockPos') -> float:
        """public float dev.ultreon.quantum.world.World.getBreakProgress(dev.ultreon.quantum.world.BlockPos)"""
        return float.__wrap(super(__World, self).getBreakProgress(arg0))

    @overload
    def destroyBlock(self, arg0: 'BlockPos', arg1: 'Player') -> bool:
        """public boolean dev.ultreon.quantum.world.World.destroyBlock(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        return bool.__wrap(super(__World, self).destroyBlock(arg0, arg1))

    @staticmethod
    @overload
    def toChunkPos(arg0: 'BlockPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(dev.ultreon.quantum.world.BlockPos)"""
        return ChunkPos.__wrap(__World.toChunkPos(arg0))

    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__World, self).setColumn(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Class') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def isOutOfWorldBounds(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(int,int,int)"""
        return bool.__wrap(super(__World, self).isOutOfWorldBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setBlockEntity(self, arg0: 'BlockPos', arg1: 'BlockEntity'):
        """public void dev.ultreon.quantum.world.World.setBlockEntity(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntity)"""
        super(__World, self).setBlockEntity(arg0, arg1)

    @overload
    def onChunkUpdated(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.onChunkUpdated(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).onChunkUpdated(arg0)

    @overload
    def getChunkAt(self, arg0: int, arg1: int, arg2: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(int,int,int)"""
        return 'Chunk'.__wrap(super(__World, self).getChunkAt(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getEntitiesByClass(self, arg0: 'Class') -> 'Collection':
        """public <T extends dev.ultreon.quantum.entity.Entity> java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntitiesByClass(java.lang.Class<T>)"""
        return 'Collection'.__wrap(super(__World, self).getEntitiesByClass(arg0))

    @abstractmethod
    def getChunk(self, arg0: 'ChunkPos'):
        """public abstract dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        pass

    @overload
    def isAlwaysLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isAlwaysLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__World, self).isAlwaysLoaded(arg0))

    @overload
    def rayCast(self, arg0: 'Ray', arg1: float) -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.BlockHitResult'.__wrap(super(__World, self).rayCast(arg0, __float.valueOf(arg1)))

    @overload
    def setSpawnPoint(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.world.World.setSpawnPoint(int,int)"""
        super(__World, self).setSpawnPoint(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.World.getHighest(int,int)"""
        return int.__wrap(super(__World, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getUID(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.world.World.getUID()"""
        return 'UUID'.__wrap(super(World, self).getUID())

    @abstractmethod
    def getTotalChunks(self, ):
        """public abstract int dev.ultreon.quantum.world.World.getTotalChunks()"""
        pass

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int)"""
        return BlockPos.__wrap(__World.toLocalBlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @abstractmethod
    def isClientSide(self, ):
        """public abstract boolean dev.ultreon.quantum.world.World.isClientSide()"""
        pass

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'EntityType') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def rayCast(self, arg0: 'Ray') -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray)"""
        return 'util.BlockHitResult'.__wrap(super(__World, self).rayCast(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vector3') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(com.badlogic.gdx.math.Vector3)"""
        return ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: 'BlockPos') -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return BlockPos.__wrap(__World.toLocalBlockPos(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def toChunkVec(arg0: int, arg1: int, arg2: int) -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(int,int,int)"""
        return vector.Vec2i.__wrap(__World.toChunkVec(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'LongType'):
        """public dev.ultreon.quantum.world.World(dev.ultreon.ubo.types.LongType)"""
        val = __World(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__World, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def rayCastEntity(self, arg0: 'Ray') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3d') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.world.World.playSound(dev.ultreon.quantum.world.SoundEvent,double,double,double)"""
        super(__World, self).playSound(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__World, self).drop(arg0, arg1)

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__World, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntities()"""
        return 'Collection'.__wrap(super(World, self).getEntities())

    @overload
    def despawn(self, arg0: int):
        """public void dev.ultreon.quantum.world.World.despawn(int)"""
        super(__World, self).despawn(__int.valueOf(arg0))

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool.__wrap(super(__World, self).set(arg0, arg1, __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def continueBreaking(self, arg0: 'BlockPos', arg1: float, arg2: 'Player') -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.World.continueBreaking(dev.ultreon.quantum.world.BlockPos,float,dev.ultreon.quantum.entity.player.Player)"""
        return 'BreakResult'.__wrap(super(__World, self).continueBreaking(arg0, __float.valueOf(arg1), arg2))

    @overload
    def spawn(self, arg0: 'Entity', arg1: 'MapType') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T,dev.ultreon.ubo.types.MapType)"""
        return 'entity.Entity'.__wrap(super(__World, self).spawn(arg0, arg1))

    @overload
    def unloadChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.unloadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__World, self).unloadChunk(arg0))

    @overload
    def getBiome(self, arg0: 'BlockPos') -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.World.getBiome(dev.ultreon.quantum.world.BlockPos)"""
        return 'Biome'.__wrap(super(__World, self).getBiome(arg0))

    @overload
    def closeMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.closeMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__World, self).closeMenu(arg0)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.World.dispose()"""
        super(World, self).dispose()

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int, arg3: 'Vec3i') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return vector.Vec3i.__wrap(__World.toLocalBlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def updateChunkAndNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunkAndNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).updateChunkAndNeighbours(arg0)

    @overload
    def getSpawnPoint(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.getSpawnPoint()"""
        return 'BlockPos'.__wrap(super(World, self).getSpawnPoint())

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: 'ChunkPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return ChunkPos.__wrap(__World.toLocalChunkPos(arg0))

    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__World, self).drop(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getChunkAt(self, arg0: 'BlockPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(dev.ultreon.quantum.world.BlockPos)"""
        return 'Chunk'.__wrap(super(__World, self).getChunkAt(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool.__wrap(super(__World, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: int, arg1: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(int,int)"""
        return ChunkPos.__wrap(__World.toLocalChunkPos(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'BlockProperties') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.world.World.set(int,int,int,int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'CompletableFuture'.__wrap(super(__World, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.World.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__World, self).getBlockEntity(arg0))

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__World, self).get(arg0))

    @staticmethod
    @overload
    def toChunkVec(arg0: 'BlockPos') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(dev.ultreon.quantum.world.BlockPos)"""
        return vector.Vec2i.__wrap(__World.toChunkVec(arg0))

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isDisposed()"""
        return bool.__wrap(super(World, self).isDisposed())

    @overload
    def getDimension(self) -> 'DimensionInfo':
        """public dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.World.getDimension()"""
        return 'DimensionInfo'.__wrap(super(World, self).getDimension()) 
 
 
# CLASS: dev.ultreon.quantum.world.Biome
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum.world.gen import biome
except ImportError:
    biome = __import_once__("pyquantum.world.gen.biome")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator
__BiomeGenerator = __BiomeGenerator
from builtins import float
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import dev.ultreon.quantum.world.Biome as __Biome_Builder
__Builder = __Biome_Builder.Builder
import dev.ultreon.quantum.world.gen.noise.NoiseConfig as __NoiseConfig
__NoiseConfig = __NoiseConfig
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class Biome(ABC):
    """dev.ultreon.quantum.world.Biome"""
 
    @staticmethod
    def __wrap(java_value: __Biome) -> 'Biome':
        return Biome(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Biome):
        """
        Dynamic initializer for Biome.
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
    def isOcean(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Biome.isOcean()"""
        return bool.__wrap(super(Biome, self).isOcean())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getSettings(self) -> 'noise.NoiseConfig':
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.Biome.getSettings()"""
        return 'noise.NoiseConfig'.__wrap(super(Biome, self).getSettings())

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Biome':
        """public static dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Biome.load(dev.ultreon.ubo.types.MapType)"""
        return Biome.__wrap(__Biome.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def doesNotGenerate(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Biome.doesNotGenerate()"""
        return bool.__wrap(super(Biome, self).doesNotGenerate())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome.builder()"""
        return Builder.__wrap(__Biome.builder())

    @overload
    def getTemperatureEnd(self) -> float:
        """public float dev.ultreon.quantum.world.Biome.getTemperatureEnd()"""
        return float.__wrap(super(Biome, self).getTemperatureEnd())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def create(self, arg0: 'ServerWorld', arg1: int) -> 'biome.BiomeGenerator':
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator dev.ultreon.quantum.world.Biome.create(dev.ultreon.quantum.world.ServerWorld,long)"""
        return 'biome.BiomeGenerator'.__wrap(super(__Biome, self).create(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.Biome.save()"""
        return 'types.MapType'.__wrap(super(Biome, self).save())

    @overload
    def getTemperatureStart(self) -> float:
        """public float dev.ultreon.quantum.world.Biome.getTemperatureStart()"""
        return float.__wrap(super(Biome, self).getTemperatureStart())

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

    @overload
    def buildLayers(self):
        """public final void dev.ultreon.quantum.world.Biome.buildLayers()"""
        super(Biome, self).buildLayers() 
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.util.EntityHitResult as __EntityHitResult
__EntityHitResult = __EntityHitResult
import java.util.function.Predicate as Predicate
import java.util.UUID as UUID
import dev.ultreon.quantum.world.Chunk as __Chunk
__Chunk = __Chunk
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.quantum.world.gen.TerrainGenerator as __TerrainGenerator
__TerrainGenerator = __TerrainGenerator
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import java.util.Collection as Collection
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
import java.lang.Double as __double
from builtins import bool
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
from builtins import float
import dev.ultreon.quantum.world.DimensionInfo as __DimensionInfo
__DimensionInfo = __DimensionInfo
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.world import particles
except ImportError:
    particles = __import_once__("pyquantum.world.particles")

import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
import java.lang.Boolean as __boolean
try:
    from pyquantum.world import gen
except ImportError:
    gen = __import_once__("pyquantum.world.gen")

from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import dev.ultreon.quantum.world.World as __World
__World = __World
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import dev.ultreon.quantum.util.BlockHitResult as __BlockHitResult
__BlockHitResult = __BlockHitResult
import java.lang.Object as __object
import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.quantum.world.ServerChunk as __ServerChunk
__ServerChunk = __ServerChunk
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

import java.util.List as List
 
class ServerWorld():
    """dev.ultreon.quantum.world.ServerWorld"""
 
    @staticmethod
    def __wrap(java_value: __ServerWorld) -> 'ServerWorld':
        return ServerWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerWorld):
        """
        Dynamic initializer for ServerWorld.
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
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.World.OVERWORLD
    OVERWORLD: 'util.Identifier' = __wrap(__util.Identifier.OVERWORLD)


    @overload
    def getEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.world.World.getEntity(int)"""
        return 'entity.Entity'.__wrap(super(__World, self).getEntity(__int.valueOf(arg0)))

    @overload
    def isLoaded(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.isLoaded(dev.ultreon.quantum.world.BlockPos)"""
        return bool.__wrap(super(__ServerWorld, self).isLoaded(arg0))

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__World, self).drop(arg0, arg1, arg2)

    @overload
    def isOutOfWorldBounds(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(dev.ultreon.quantum.world.BlockPos)"""
        return bool.__wrap(super(__World, self).isOutOfWorldBounds(arg0))

    @overload
    def loadChunkNow(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld.loadChunkNow(int,int)"""
        return 'Chunk'.__wrap(super(__ServerWorld, self).loadChunkNow(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getPlayTime(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getPlayTime()"""
        return int.__wrap(super(ServerWorld, self).getPlayTime())

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float) -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setSpawnPoint(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.world.World.setSpawnPoint(int,int)"""
        super(__World, self).setSpawnPoint(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getChunkLoads() -> int:
        """public static long dev.ultreon.quantum.world.ServerWorld.getChunkLoads()"""
        return int.__wrap(__ServerWorld.getChunkLoads())

    @overload
    def saveRegion(self, arg0: 'Region'):
        """public void dev.ultreon.quantum.world.ServerWorld.saveRegion(dev.ultreon.quantum.world.ServerWorld$Region)"""
        super(__ServerWorld, self).saveRegion(arg0)

    @override
    @overload
    def getUID(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.world.World.getUID()"""
        return 'UUID'.__wrap(super(World, self).getUID())

    @overload
    def unloadChunk(self, arg0: 'ChunkPos', arg1: bool, arg2: bool) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.unloadChunk(dev.ultreon.quantum.world.ChunkPos,boolean,boolean)"""
        return bool.__wrap(super(__ServerWorld, self).unloadChunk(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def refreshChunks(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.world.ServerWorld.refreshChunks(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__ServerWorld, self).refreshChunks(arg0)

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3i') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @overload
    def doRefresh(self, arg0: 'ChunkRefresher'):
        """public void dev.ultreon.quantum.world.ServerWorld.doRefresh(dev.ultreon.quantum.world.ChunkRefresher)"""
        super(__ServerWorld, self).doRefresh(arg0)

    @overload
    def intersectEntities(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.world.World.intersectEntities(dev.ultreon.quantum.util.BoundingBox)"""
        return bool.__wrap(super(__World, self).intersectEntities(arg0))

    @overload
    def entitiesWithinDst(self, arg0: 'Entity', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.entitiesWithinDst(dev.ultreon.quantum.entity.Entity,int)"""
        return 'List'.__wrap(super(__World, self).entitiesWithinDst(arg0, __int.valueOf(arg1)))

    @overload
    def collideEntities(self, arg0: 'Entity', arg1: 'BoundingBox') -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.collideEntities(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.util.BoundingBox)"""
        return 'List'.__wrap(super(__World, self).collideEntities(arg0, arg1))

    @overload
    def spawn(self, arg0: 'Entity', arg1: 'MapType') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.ServerWorld.spawn(T,dev.ultreon.ubo.types.MapType)"""
        return 'entity.Entity'.__wrap(super(__ServerWorld, self).spawn(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toChunkPos(arg0: int, arg1: int, arg2: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(int,int,int)"""
        return ChunkPos.__wrap(__World.toChunkPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def regenerateChunk(self, arg0: 'ChunkPos'):
        """public void dev.ultreon.quantum.world.ServerWorld.regenerateChunk(dev.ultreon.quantum.world.ChunkPos)"""
        super(__ServerWorld, self).regenerateChunk(arg0)

    @overload
    def sendAllTrackingExcept(self, arg0: int, arg1: int, arg2: int, arg3: 'Packet', arg4: 'ServerPlayer'):
        """public void dev.ultreon.quantum.world.ServerWorld.sendAllTrackingExcept(int,int,int,dev.ultreon.quantum.network.packets.Packet<? extends dev.ultreon.quantum.network.client.ClientPacketHandler>,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__ServerWorld, self).sendAllTrackingExcept(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4)

    @overload
    def isChunkInvalidated(self, arg0: 'Chunk') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isChunkInvalidated(dev.ultreon.quantum.world.Chunk)"""
        return bool.__wrap(super(__World, self).isChunkInvalidated(arg0))

    @overload
    def getChunksAround(self, arg0: 'Vec3d') -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.World.getChunksAround(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'List'.__wrap(super(__World, self).getChunksAround(arg0))

    @overload
    def getBreakProgress(self, arg0: 'BlockPos') -> float:
        """public float dev.ultreon.quantum.world.World.getBreakProgress(dev.ultreon.quantum.world.BlockPos)"""
        return float.__wrap(super(__World, self).getBreakProgress(arg0))

    @overload
    def sync(self, arg0: 'Vec3i'):
        """public void dev.ultreon.quantum.world.ServerWorld.sync(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        super(__ServerWorld, self).sync(arg0)

    @staticmethod
    @overload
    def toChunkPos(arg0: 'BlockPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(dev.ultreon.quantum.world.BlockPos)"""
        return ChunkPos.__wrap(__World.toChunkPos(arg0))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Class') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def getEntitiesByClass(self, arg0: 'Class') -> 'Collection':
        """public <T extends dev.ultreon.quantum.entity.Entity> java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntitiesByClass(java.lang.Class<T>)"""
        return 'Collection'.__wrap(super(__World, self).getEntitiesByClass(arg0))

    @overload
    def isAlwaysLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isAlwaysLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__World, self).isAlwaysLoaded(arg0))

    @overload
    def rayCast(self, arg0: 'Ray', arg1: float) -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.BlockHitResult'.__wrap(super(__World, self).rayCast(arg0, __float.valueOf(arg1)))

    @overload
    def getChunk(self, arg0: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'.__wrap(super(__ServerWorld, self).getChunk(arg0))

    @overload
    def save(self, arg0: bool):
        """public synchronized void dev.ultreon.quantum.world.ServerWorld.save(boolean) throws java.io.IOException"""
        super(__ServerWorld, self).save(__boolean.valueOf(arg0))

    @overload
    def load(self):
        """public void dev.ultreon.quantum.world.ServerWorld.load() throws java.io.IOException"""
        super(ServerWorld, self).load()

    @override
    @overload
    def despawn(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.world.World.despawn(dev.ultreon.quantum.entity.Entity)"""
        super(__World, self).despawn(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vector3') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(com.badlogic.gdx.math.Vector3)"""
        return ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @overload
    def spawn(self, arg0: 'Entity') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.ServerWorld.spawn(T)"""
        return 'entity.Entity'.__wrap(super(__ServerWorld, self).spawn(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rayCastEntity(self, arg0: 'Ray') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.ServerWorld.dispose()"""
        super(ServerWorld, self).dispose()

    @overload
    def doRefreshNow(self, arg0: 'ChunkRefresher'):
        """public void dev.ultreon.quantum.world.ServerWorld.doRefreshNow(dev.ultreon.quantum.world.ChunkRefresher)"""
        super(__ServerWorld, self).doRefreshNow(arg0)

    @overload
    def getStorage(self) -> 'WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.world.ServerWorld.getStorage()"""
        return 'WorldStorage'.__wrap(super(ServerWorld, self).getStorage())

    @overload
    def prepareSpawn(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.world.ServerWorld.prepareSpawn(dev.ultreon.quantum.entity.player.Player)"""
        super(__ServerWorld, self).prepareSpawn(arg0)

    @overload
    def getTerrainGenerator(self) -> 'gen.TerrainGenerator':
        """public dev.ultreon.quantum.world.gen.TerrainGenerator dev.ultreon.quantum.world.ServerWorld.getTerrainGenerator()"""
        return 'gen.TerrainGenerator'.__wrap(super(ServerWorld, self).getTerrainGenerator())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__World, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getSeed(self) -> int:
        """public long dev.ultreon.quantum.world.World.getSeed()"""
        return int.__wrap(super(World, self).getSeed())

    @overload
    def loadChunk(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld.loadChunk(int,int)"""
        return 'Chunk'.__wrap(super(__ServerWorld, self).loadChunk(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getChunksToLoad(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getChunksToLoad()"""
        return int.__wrap(super(ServerWorld, self).getChunksToLoad())

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool.__wrap(super(__World, self).set(arg0, arg1, __int.valueOf(arg2)))

    @override
    @overload
    def updateChunkAndNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunkAndNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).updateChunkAndNeighbours(arg0)

    @override
    @overload
    def getLoadedChunks(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.world.ServerChunk> dev.ultreon.quantum.world.ServerWorld.getLoadedChunks()"""
        return 'Collection'.__wrap(super(ServerWorld, self).getLoadedChunks())

    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getRenderDistance()"""
        return int.__wrap(super(ServerWorld, self).getRenderDistance())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__ServerWorld, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool.__wrap(super(__ServerWorld, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4)))

    @overload
    def loadChunk(self, arg0: int, arg1: int, arg2: bool) -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld.loadChunk(int,int,boolean)"""
        return 'ServerChunk'.__wrap(super(__ServerWorld, self).loadChunk(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__World, self).drop(arg0, arg1)

    @override
    @overload
    def startBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.startBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__World, self).startBreaking(arg0, arg1)

    @override
    @overload
    def getSpawnPoint(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.ServerWorld.getSpawnPoint()"""
        return 'BlockPos'.__wrap(super(ServerWorld, self).getSpawnPoint())

    @override
    @overload
    def stopBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.stopBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__World, self).stopBreaking(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getPlayersWithinRange(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.world.ServerWorld.getPlayersWithinRange(double,double,double,float)"""
        return 'List'.__wrap(super(__ServerWorld, self).getPlayersWithinRange(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def loadChunkNow(self, arg0: int, arg1: int, arg2: bool) -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld.loadChunkNow(int,int,boolean)"""
        return 'ServerChunk'.__wrap(super(__ServerWorld, self).loadChunkNow(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: int, arg1: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(int,int)"""
        return ChunkPos.__wrap(__World.toLocalChunkPos(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__World, self).setColumn(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'BlockProperties') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.world.World.set(int,int,int,int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'CompletableFuture'.__wrap(super(__World, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.World.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__World, self).getBlockEntity(arg0))

    @overload
    def continueBreaking(self, arg0: 'BlockPos', arg1: float, arg2: 'Player') -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.ServerWorld.continueBreaking(dev.ultreon.quantum.world.BlockPos,float,dev.ultreon.quantum.entity.player.Player)"""
        return 'BreakResult'.__wrap(super(__ServerWorld, self).continueBreaking(arg0, __float.valueOf(arg1), arg2))

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__World, self).get(arg0))

    @override
    @overload
    def getEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntities()"""
        return 'Collection'.__wrap(super(World, self).getEntities())

    @override
    @overload
    def fillCrashInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.world.World.fillCrashInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(__World, self).fillCrashInfo(arg0)

    @overload
    def unloadChunk(self, arg0: 'ChunkPos', arg1: bool) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.unloadChunk(dev.ultreon.quantum.world.ChunkPos,boolean)"""
        return bool.__wrap(super(__ServerWorld, self).unloadChunk(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def despawn(self, arg0: int):
        """public void dev.ultreon.quantum.world.World.despawn(int)"""
        super(__World, self).despawn(__int.valueOf(arg0))

    @override
    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.world.ServerWorld.playSound(dev.ultreon.quantum.world.SoundEvent,double,double,double)"""
        super(__ServerWorld, self).playSound(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @overload
    def collide(self, arg0: 'BoundingBox', arg1: bool) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.BoundingBox> dev.ultreon.quantum.world.World.collide(dev.ultreon.quantum.util.BoundingBox,boolean)"""
        return 'List'.__wrap(super(__World, self).collide(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def getTotalChunks(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getTotalChunks()"""
        return int.__wrap(super(ServerWorld, self).getTotalChunks())

    @override
    @overload
    def closeMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.closeMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__World, self).closeMenu(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__World, self).openMenu(arg0)

    @overload
    def getChunk(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunk(int,int)"""
        return 'Chunk'.__wrap(super(__World, self).getChunk(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'WorldStorage', arg2: 'MapType'):
        """public dev.ultreon.quantum.world.ServerWorld(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.world.WorldStorage,dev.ultreon.ubo.types.MapType)"""
        val = __ServerWorld(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getDimension(self) -> 'DimensionInfo':
        """public dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.World.getDimension()"""
        return 'DimensionInfo'.__wrap(super(World, self).getDimension())

    @override
    @overload
    def getChunksLoaded(self) -> int:
        """public int dev.ultreon.quantum.world.World.getChunksLoaded()"""
        return int.__wrap(super(World, self).getChunksLoaded())

    @overload
    def isSpawnChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isSpawnChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__World, self).isSpawnChunk(arg0))

    @overload
    def refreshChunks(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.world.ServerWorld.refreshChunks(float,float)"""
        super(__ServerWorld, self).refreshChunks(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Predicate') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.util.function.Predicate<dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__World, self).set(arg0, arg1))

    @overload
    def setupSpawn(self):
        """public void dev.ultreon.quantum.world.ServerWorld.setupSpawn()"""
        super(ServerWorld, self).setupSpawn()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def recordOutOfBounds(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.ServerWorld.recordOutOfBounds(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__ServerWorld, self).recordOutOfBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def setBlockEntity(self, arg0: 'BlockPos', arg1: 'BlockEntity'):
        """public void dev.ultreon.quantum.world.ServerWorld.setBlockEntity(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntity)"""
        super(__ServerWorld, self).setBlockEntity(arg0, arg1)

    @overload
    def destroyBlock(self, arg0: 'BlockPos', arg1: 'Player') -> bool:
        """public boolean dev.ultreon.quantum.world.World.destroyBlock(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        return bool.__wrap(super(__World, self).destroyBlock(arg0, arg1))

    @overload
    def isOutOfWorldBounds(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(int,int,int)"""
        return bool.__wrap(super(__World, self).isOutOfWorldBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getChunkAt(self, arg0: int, arg1: int, arg2: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(int,int,int)"""
        return 'Chunk'.__wrap(super(__World, self).getChunkAt(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def sendAllTracking(self, arg0: int, arg1: int, arg2: int, arg3: 'Packet'):
        """public void dev.ultreon.quantum.world.ServerWorld.sendAllTracking(int,int,int,dev.ultreon.quantum.network.packets.Packet<? extends dev.ultreon.quantum.network.client.ClientPacketHandler>)"""
        super(__ServerWorld, self).sendAllTracking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.World.getHighest(int,int)"""
        return int.__wrap(super(__World, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def isServerSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isServerSide()"""
        return bool.__wrap(super(World, self).isServerSide())

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int)"""
        return BlockPos.__wrap(__World.toLocalBlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'EntityType') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'util.EntityHitResult'.__wrap(super(__World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def rayCast(self, arg0: 'Ray') -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray)"""
        return 'util.BlockHitResult'.__wrap(super(__World, self).rayCast(arg0))

    @override
    @overload
    def updateNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).updateNeighbours(arg0)

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: 'BlockPos') -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return BlockPos.__wrap(__World.toLocalBlockPos(arg0))

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.world.ServerWorld.getServer()"""
        return 'server.QuantumServer'.__wrap(super(ServerWorld, self).getServer())

    @staticmethod
    @overload
    def toChunkVec(arg0: int, arg1: int, arg2: int) -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(int,int,int)"""
        return vector.Vec2i.__wrap(__World.toChunkVec(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3d') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @override
    @overload
    def isClientSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.isClientSide()"""
        return bool.__wrap(super(ServerWorld, self).isClientSide())

    @overload
    def saveRegion(self, arg0: 'Region', arg1: bool):
        """public void dev.ultreon.quantum.world.ServerWorld.saveRegion(dev.ultreon.quantum.world.ServerWorld$Region,boolean)"""
        super(__ServerWorld, self).saveRegion(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def onChunkUpdated(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.onChunkUpdated(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).onChunkUpdated(arg0)

    @overload
    def sync(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.ServerWorld.sync(dev.ultreon.quantum.world.BlockPos)"""
        super(__ServerWorld, self).sync(arg0)

    @overload
    def saveAsync(self, arg0: bool) -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Boolean> dev.ultreon.quantum.world.ServerWorld.saveAsync(boolean)"""
        return 'CompletableFuture'.__wrap(super(__ServerWorld, self).saveAsync(__boolean.valueOf(arg0)))

    @override
    @overload
    def spawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.world.ServerWorld.spawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(__ServerWorld, self).spawnParticles(arg0, arg1, arg2, __int.valueOf(arg3))

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__World, self).setColumn(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def unloadChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.unloadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__World, self).unloadChunk(arg0))

    @overload
    def getBiome(self, arg0: 'BlockPos') -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.World.getBiome(dev.ultreon.quantum.world.BlockPos)"""
        return 'Biome'.__wrap(super(__World, self).getBiome(arg0))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int, arg3: 'Vec3i') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return vector.Vec3i.__wrap(__World.toLocalBlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def getChunkUnloads() -> int:
        """public static long dev.ultreon.quantum.world.ServerWorld.getChunkUnloads()"""
        return int.__wrap(__ServerWorld.getChunkUnloads())

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: 'ChunkPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return ChunkPos.__wrap(__World.toLocalChunkPos(arg0))

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.world.ServerWorld.tick()"""
        super(ServerWorld, self).tick()

    @overload
    def isLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.isLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__ServerWorld, self).isLoaded(arg0))

    @overload
    def getChunkAt(self, arg0: 'BlockPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(dev.ultreon.quantum.world.BlockPos)"""
        return 'Chunk'.__wrap(super(__World, self).getChunkAt(arg0))

    @overload
    def refreshChunks(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.world.ServerWorld.refreshChunks(dev.ultreon.quantum.entity.player.Player)"""
        super(__ServerWorld, self).refreshChunks(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getChunkSaves() -> int:
        """public static long dev.ultreon.quantum.world.ServerWorld.getChunkSaves()"""
        return int.__wrap(__ServerWorld.getChunkSaves())

    @overload
    def loadChunk(self, arg0: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld.loadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'.__wrap(super(__ServerWorld, self).loadChunk(arg0))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isDisposed()"""
        return bool.__wrap(super(World, self).isDisposed())

    @override
    @overload
    def updateChunk(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunk(dev.ultreon.quantum.world.Chunk)"""
        super(__World, self).updateChunk(arg0)

    @staticmethod
    @overload
    def toChunkVec(arg0: 'BlockPos') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(dev.ultreon.quantum.world.BlockPos)"""
        return vector.Vec2i.__wrap(__World.toChunkVec(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.IllegalChunkStateException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.world.IllegalChunkStateException as __IllegalChunkStateException
__IllegalChunkStateException = __IllegalChunkStateException
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IllegalChunkStateException():
    """dev.ultreon.quantum.world.IllegalChunkStateException"""
 
    @staticmethod
    def __wrap(java_value: __IllegalChunkStateException) -> 'IllegalChunkStateException':
        return IllegalChunkStateException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IllegalChunkStateException):
        """
        Dynamic initializer for IllegalChunkStateException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.world.IllegalChunkStateException(java.lang.String)"""
        val = __IllegalChunkStateException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.world.UseResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class UseResult():
    """dev.ultreon.quantum.world.UseResult"""
 
    @staticmethod
    def __wrap(java_value: __UseResult) -> 'UseResult':
        return UseResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UseResult):
        """
        Dynamic initializer for UseResult.
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
 
    # public static final dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.world.UseResult.ALLOW
    ALLOW: 'UseResult' = __wrap(__UseResult.ALLOW)

    # public static final dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.world.UseResult.DENY
    DENY: 'UseResult' = __wrap(__UseResult.DENY)

    # public static final dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.world.UseResult.SKIP
    SKIP: 'UseResult' = __wrap(__UseResult.SKIP)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'UseResult':
        """public static dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.world.UseResult.valueOf(java.lang.String)"""
        return UseResult.__wrap(__UseResult.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['UseResult']:
        """public static dev.ultreon.quantum.world.UseResult[] dev.ultreon.quantum.world.UseResult.values()"""
        return List[UseResult].__wrap(__UseResult.values()) 
 
 
# CLASS: dev.ultreon.quantum.world.RegionPos
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.world.RegionPos as __RegionPos
__RegionPos = __RegionPos
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegionPos():
    """dev.ultreon.quantum.world.RegionPos"""
 
    @staticmethod
    def __wrap(java_value: __RegionPos) -> 'RegionPos':
        return RegionPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegionPos):
        """
        Dynamic initializer for RegionPos.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.RegionPos.hashCode()"""
        return int.__wrap(super(RegionPos, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.RegionPos.toString()"""
        return str.__wrap(super(RegionPos, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.RegionPos.equals(java.lang.Object)"""
        return bool.__wrap(super(__RegionPos, self).equals(arg0))

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
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.RegionPos.z()"""
        return int.__wrap(super(RegionPos, self).z())

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.RegionPos.x()"""
        return int.__wrap(super(RegionPos, self).x())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.world.RegionPos(int,int)"""
        val = __RegionPos(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.Location
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class Location():
    """dev.ultreon.quantum.world.Location"""
 
    @staticmethod
    def __wrap(java_value: __Location) -> 'Location':
        return Location(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Location):
        """
        Dynamic initializer for Location.
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

    @property
    def world(self) -> Identifier:
        return Identifier.__wrap(super(__Location).world())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.Location(double,double,double)"""
        val = __Location(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'World', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.world.Location(dev.ultreon.quantum.world.World,double,double,double,float,float)"""
        val = __Location(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @property
    def world(self, value: 'util.Identifier'):
        super(__Location).world(value)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getSeverWorld(self) -> 'ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.world.Location.getSeverWorld()"""
        return 'ServerWorld'.__wrap(super(Location, self).getSeverWorld())

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

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public dev.ultreon.quantum.world.Location(double,double,double,float,float)"""
        val = __Location(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBlockPos(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.Location.getBlockPos()"""
        return 'BlockPos'.__wrap(super(Location, self).getBlockPos())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.quantum.world.Location(dev.ultreon.quantum.world.ServerWorld,double,double,double)"""
        val = __Location(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cpy(self) -> 'Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.world.Location.cpy()"""
        return 'Location'.__wrap(super(Location, self).cpy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.world.Location(dev.ultreon.quantum.util.Identifier,double,double,double,float,float)"""
        val = __Location(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.BreakResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class BreakResult():
    """dev.ultreon.quantum.world.BreakResult"""
 
    @staticmethod
    def __wrap(java_value: __BreakResult) -> 'BreakResult':
        return BreakResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BreakResult):
        """
        Dynamic initializer for BreakResult.
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
 
    # public static final dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.BreakResult.BROKEN
    BROKEN: 'BreakResult' = __wrap(__BreakResult.BROKEN)

    # public static final dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.BreakResult.CONTINUE
    CONTINUE: 'BreakResult' = __wrap(__BreakResult.CONTINUE)

    # public static final dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.BreakResult.FAILED
    FAILED: 'BreakResult' = __wrap(__BreakResult.FAILED)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['BreakResult']:
        """public static dev.ultreon.quantum.world.BreakResult[] dev.ultreon.quantum.world.BreakResult.values()"""
        return List[BreakResult].__wrap(__BreakResult.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BreakResult':
        """public static dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.BreakResult.valueOf(java.lang.String)"""
        return BreakResult.__wrap(__BreakResult.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld$RecordedChange
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld_RecordedChange
__RecordedChange = __ServerWorld_RecordedChange.RecordedChange
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class RecordedChange():
    """dev.ultreon.quantum.world.ServerWorld.RecordedChange"""
 
    @staticmethod
    def __wrap(java_value: __RecordedChange) -> 'RecordedChange':
        return RecordedChange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecordedChange):
        """
        Dynamic initializer for RecordedChange.
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
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.x()"""
        return int.__wrap(super(RecordedChange, self).x())

    @overload
    def block(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.ServerWorld$RecordedChange.block()"""
        return 'state.BlockProperties'.__wrap(super(RecordedChange, self).block())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.ServerWorld$RecordedChange.toString()"""
        return str.__wrap(super(RecordedChange, self).toString())

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
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.ServerWorld$RecordedChange.save()"""
        return 'types.MapType'.__wrap(super(RecordedChange, self).save())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.z()"""
        return int.__wrap(super(RecordedChange, self).z())

    @overload
    def y(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.y()"""
        return int.__wrap(super(RecordedChange, self).y())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$RecordedChange.equals(java.lang.Object)"""
        return bool.__wrap(super(__RecordedChange, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public dev.ultreon.quantum.world.ServerWorld$RecordedChange(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        val = __RecordedChange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.hashCode()"""
        return int.__wrap(super(RecordedChange, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.HeightMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.HeightMap as __HeightMap
__HeightMap = __HeightMap
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeightMap():
    """dev.ultreon.quantum.world.HeightMap"""
 
    @staticmethod
    def __wrap(java_value: __HeightMap) -> 'HeightMap':
        return HeightMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeightMap):
        """
        Dynamic initializer for HeightMap.
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
    def set(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.HeightMap.set(int,int,short)"""
        super(__HeightMap, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2))

    @overload
    def get(self, arg0: int, arg1: int) -> int:
        """public short dev.ultreon.quantum.world.HeightMap.get(int,int)"""
        return int.__wrap(super(__HeightMap, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def getMap(self) -> List[int]:
        """public short[] dev.ultreon.quantum.world.HeightMap.getMap()"""
        return List[int].__wrap(super(HeightMap, self).getMap())

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
    def save(self) -> List[int]:
        """public short[] dev.ultreon.quantum.world.HeightMap.save()"""
        return List[int].__wrap(super(HeightMap, self).save())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.HeightMap(int)"""
        val = __HeightMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def load(self, arg0: 'short'):
        """public void dev.ultreon.quantum.world.HeightMap.load(short[])"""
        super(__HeightMap, self).load(arg0)

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.world.HeightMap.getWidth()"""
        return int.__wrap(super(HeightMap, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.Biome$Builder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum.world import gen
except ImportError:
    gen = __import_once__("pyquantum.world.gen")

from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import it.unimi.dsi.fastutil.longs.Long2ReferenceFunction as Long2ReferenceFunction
import dev.ultreon.quantum.world.Biome as __Biome_Builder
__Builder = __Biome_Builder.Builder
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyquantum.world.gen import layer
except ImportError:
    layer = __import_once__("pyquantum.world.gen.layer")

from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.world.Biome.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def layer(self, arg0: 'TerrainLayer') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.layer(dev.ultreon.quantum.world.gen.layer.TerrainLayer)"""
        return 'Builder'.__wrap(super(__Builder, self).layer(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def temperatureEnd(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.temperatureEnd(float)"""
        return 'Builder'.__wrap(super(__Builder, self).temperatureEnd(__float.valueOf(arg0)))

    @overload
    def domainWarping(self, arg0: 'Long2ReferenceFunction') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.domainWarping(it.unimi.dsi.fastutil.longs.Long2ReferenceFunction<dev.ultreon.quantum.world.gen.noise.DomainWarping>)"""
        return 'Builder'.__wrap(super(__Builder, self).domainWarping(arg0))

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
    def doesNotGenerate(self) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.doesNotGenerate()"""
        return 'Builder'.__wrap(super(Builder, self).doesNotGenerate())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def feature(self, arg0: 'WorldGenFeature') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.feature(dev.ultreon.quantum.world.gen.WorldGenFeature)"""
        return 'Builder'.__wrap(super(__Builder, self).feature(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def ocean(self) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.ocean()"""
        return 'Builder'.__wrap(super(Builder, self).ocean())

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

    @overload
    def noise(self, arg0: 'NoiseConfig') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.noise(dev.ultreon.quantum.world.gen.noise.NoiseConfig)"""
        return 'Builder'.__wrap(super(__Builder, self).noise(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def build(self) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Biome$Builder.build()"""
        return 'Biome'.__wrap(super(Builder, self).build())

    @overload
    def temperatureStart(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.temperatureStart(float)"""
        return 'Builder'.__wrap(super(__Builder, self).temperatureStart(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.WorldSaveInfo
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.WorldSaveInfo as __WorldSaveInfo
__WorldSaveInfo = __WorldSaveInfo
from builtins import str
import dev.ultreon.quantum.util.GameMode as __GameMode
__GameMode = __GameMode
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.libs.datetime.v0.DateTime as __DateTime
__DateTime = __DateTime
import java.util.Optional as Optional
try:
    from pycorelibs.datetime import v0
except ImportError:
    v0 = __import_once__("pycorelibs.datetime.v0")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class WorldSaveInfo():
    """dev.ultreon.quantum.world.WorldSaveInfo"""
 
    @staticmethod
    def __wrap(java_value: __WorldSaveInfo) -> 'WorldSaveInfo':
        return WorldSaveInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldSaveInfo):
        """
        Dynamic initializer for WorldSaveInfo.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldSaveInfo.equals(java.lang.Object)"""
        return bool.__wrap(super(__WorldSaveInfo, self).equals(arg0))

    @overload
    def seed(self) -> int:
        """public long dev.ultreon.quantum.world.WorldSaveInfo.seed()"""
        return int.__wrap(super(WorldSaveInfo, self).seed())

    @overload
    def gamemode(self) -> 'util.GameMode':
        """public dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.world.WorldSaveInfo.gamemode()"""
        return 'util.GameMode'.__wrap(super(WorldSaveInfo, self).gamemode())

    @overload
    def generatorVersion(self) -> int:
        """public int dev.ultreon.quantum.world.WorldSaveInfo.generatorVersion()"""
        return int.__wrap(super(WorldSaveInfo, self).generatorVersion())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.WorldSaveInfo.toString()"""
        return str.__wrap(super(WorldSaveInfo, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.WorldSaveInfo.hashCode()"""
        return int.__wrap(super(WorldSaveInfo, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.WorldSaveInfo.name()"""
        return str.__wrap(super(WorldSaveInfo, self).name())

    @overload
    def setName(self, arg0: str):
        """public void dev.ultreon.quantum.world.WorldSaveInfo.setName(java.lang.String)"""
        super(__WorldSaveInfo, self).setName(arg0)

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
    def save(self, arg0: 'WorldStorage'):
        """public void dev.ultreon.quantum.world.WorldSaveInfo.save(dev.ultreon.quantum.world.WorldStorage) throws java.io.IOException"""
        super(__WorldSaveInfo, self).save(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def fromMap(arg0: 'MapType') -> 'WorldSaveInfo':
        """public static dev.ultreon.quantum.world.WorldSaveInfo dev.ultreon.quantum.world.WorldSaveInfo.fromMap(dev.ultreon.ubo.types.MapType)"""
        return WorldSaveInfo.__wrap(__WorldSaveInfo.fromMap(arg0))

    @overload
    def picture(self, arg0: 'WorldStorage') -> 'Optional':
        """public java.util.Optional<com.badlogic.gdx.graphics.Texture> dev.ultreon.quantum.world.WorldSaveInfo.picture(dev.ultreon.quantum.world.WorldStorage)"""
        return 'Optional'.__wrap(super(__WorldSaveInfo, self).picture(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'GameMode', arg3: 'GameMode', arg4: str, arg5: 'DateTime'):
        """public dev.ultreon.quantum.world.WorldSaveInfo(long,int,dev.ultreon.quantum.util.GameMode,dev.ultreon.quantum.util.GameMode,java.lang.String,dev.ultreon.libs.datetime.v0.DateTime)"""
        val = __WorldSaveInfo(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def lastPlayedInMode(self) -> 'util.GameMode':
        """public dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.world.WorldSaveInfo.lastPlayedInMode()"""
        return 'util.GameMode'.__wrap(super(WorldSaveInfo, self).lastPlayedInMode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def lastSave(self) -> 'v0.DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.quantum.world.WorldSaveInfo.lastSave()"""
        return 'v0.DateTime'.__wrap(super(WorldSaveInfo, self).lastSave()) 
 
 
# CLASS: dev.ultreon.quantum.world.DimensionInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.DimensionInfo as __DimensionInfo
__DimensionInfo = __DimensionInfo
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DimensionInfo():
    """dev.ultreon.quantum.world.DimensionInfo"""
 
    @staticmethod
    def __wrap(java_value: __DimensionInfo) -> 'DimensionInfo':
        return DimensionInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DimensionInfo):
        """
        Dynamic initializer for DimensionInfo.
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
 
    # public static final dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.DimensionInfo.OVERWORLD
    OVERWORLD: 'DimensionInfo' = __wrap(__DimensionInfo.OVERWORLD)


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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.DimensionInfo.equals(java.lang.Object)"""
        return bool.__wrap(super(__DimensionInfo, self).equals(arg0))

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.DimensionInfo.getId()"""
        return 'util.Identifier'.__wrap(super(DimensionInfo, self).getId())

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
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.world.DimensionInfo(dev.ultreon.quantum.util.Identifier)"""
        val = __DimensionInfo(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.world.DimensionInfo.getName()"""
        return 'text.TextObject'.__wrap(super(DimensionInfo, self).getName())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.DimensionInfo.hashCode()"""
        return int.__wrap(super(DimensionInfo, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.ChunkRefresher
from builtins import str
import dev.ultreon.quantum.world.ChunkRefresher as __ChunkRefresher
__ChunkRefresher = __ChunkRefresher
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
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
 
class ChunkRefresher():
    """dev.ultreon.quantum.world.ChunkRefresher"""
 
    @staticmethod
    def __wrap(java_value: __ChunkRefresher) -> 'ChunkRefresher':
        return ChunkRefresher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkRefresher):
        """
        Dynamic initializer for ChunkRefresher.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addLoading(self, arg0: 'Collection'):
        """public void dev.ultreon.quantum.world.ChunkRefresher.addLoading(java.util.Collection<dev.ultreon.quantum.world.ChunkPos>)"""
        super(__ChunkRefresher, self).addLoading(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ChunkRefresher.isFrozen()"""
        return bool.__wrap(super(ChunkRefresher, self).isFrozen())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addUnloading(self, arg0: 'Collection'):
        """public void dev.ultreon.quantum.world.ChunkRefresher.addUnloading(java.util.Collection<dev.ultreon.quantum.world.ChunkPos>)"""
        super(__ChunkRefresher, self).addUnloading(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def freeze(self):
        """public void dev.ultreon.quantum.world.ChunkRefresher.freeze()"""
        super(ChunkRefresher, self).freeze()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.ChunkRefresher()"""
        val = __ChunkRefresher()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.ChunkRefresher()"""
        val = __ChunkRefresher()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.Chunk
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.Chunk as __Chunk
__Chunk = __Chunk
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

try:
    from pyquantum.world import gen
except ImportError:
    gen = __import_once__("pyquantum.world.gen")

from builtins import type
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import java.util.Collection as Collection
try:
    from pyquantum import collection
except ImportError:
    collection = __import_once__("pyquantum.collection")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.lang.Float as __float
import dev.ultreon.quantum.world.gen.TreeData as __TreeData
__TreeData = __TreeData
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class Chunk(ABC):
    """dev.ultreon.quantum.world.Chunk"""
 
    @staticmethod
    def __wrap(java_value: __Chunk) -> 'Chunk':
        return Chunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Chunk):
        """
        Dynamic initializer for Chunk.
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
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'.__wrap(super(Chunk, self).getOffset())

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'Biome'.__wrap(super(__Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(__Chunk, self).setTreeData(arg0)

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int.__wrap(super(__Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Chunk, self).setFast(arg0, arg1)

    @overload
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int.__wrap(super(__Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block.__wrap(__Chunk.decodeBlock(arg0))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'BreakResult'.__wrap(super(__Chunk, self).continueBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'.__wrap(super(Chunk, self).getBreaking())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Chunk, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool.__wrap(super(Chunk, self).isActive())

    @property
    def biomeStorage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).biomeStorage())

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float.__wrap(super(__Chunk, self).getBrightness(__int.valueOf(arg0)))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(__Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__Chunk, self).getBlockEntity(arg0))

    @overload
    def getWorld(self) -> 'World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.world.Chunk.getWorld()"""
        return 'World'.__wrap(super(Chunk, self).getWorld())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'.__wrap(super(Chunk, self).getBlockEntities())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int.__wrap(super(Chunk, self).hashCode())

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool.__wrap(super(Chunk, self).isDisposed())

    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.world.Chunk.onUpdated()"""
        super(Chunk, self).onUpdated()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__Chunk, self).getBlockLight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).getFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__Chunk, self).getSunlight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPos(self) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'ChunkPos'.__wrap(super(Chunk, self).getPos())

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int)"""
        return int.__wrap(super(__Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Chunk, self).getBlockLight(arg0))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties.__wrap(__Chunk.loadBlock(arg0))

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'Biome'.__wrap(super(__Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).get(arg0))

    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(__Chunk, self).removeBlockEntity(arg0)

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Chunk, self).getSunlight(arg0))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Chunk, self).setFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @property
    def treeData(self) -> TreeData:
        return TreeData.__wrap(super(__Chunk).treeData())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.Chunk.dispose()"""
        super(Chunk, self).dispose()

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__Chunk, self).getFast(arg0))

    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Chunk, self).set(arg0, arg1)

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int.__wrap(super(__Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @property
    def storage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).storage())

    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(__Chunk, self).stopBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool.__wrap(super(Chunk, self).isReady())

    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(__Chunk, self).startBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str.__wrap(super(Chunk, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool.__wrap(super(__Chunk, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass()) 
 
 
# CLASS: dev.ultreon.quantum.world.ChunkAccess
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import dev.ultreon.quantum.world.ChunkAccess as __ChunkAccess
__ChunkAccess = __ChunkAccess
from abc import abstractmethod, ABC
 
class ChunkAccess(ABC):
    """dev.ultreon.quantum.world.ChunkAccess"""
 
    @staticmethod
    def __wrap(java_value: __ChunkAccess) -> 'ChunkAccess':
        return ChunkAccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkAccess):
        """
        Dynamic initializer for ChunkAccess.
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
 
    @abstractmethod
    def getOffset(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.ChunkAccess.getOffset()"""
        pass

    @abstractmethod
    def getFast(self, arg0: int, arg1: int, arg2: int):
        """public abstract dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.ChunkAccess.getFast(int,int,int)"""
        pass

    @abstractmethod
    def getHighest(self, arg0: int, arg1: int):
        """public abstract int dev.ultreon.quantum.world.ChunkAccess.getHighest(int,int)"""
        pass

    @abstractmethod
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public abstract boolean dev.ultreon.quantum.world.ChunkAccess.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        pass

    @abstractmethod
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public abstract boolean dev.ultreon.quantum.world.ChunkAccess.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        pass

    @abstractmethod
    def get(self, arg0: int, arg1: int, arg2: int):
        """public abstract dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.ChunkAccess.get(int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.world.LightMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.LightMap as __LightMap
__LightMap = __LightMap
from typing import List
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
 
class LightMap():
    """dev.ultreon.quantum.world.LightMap"""
 
    @staticmethod
    def __wrap(java_value: __LightMap) -> 'LightMap':
        return LightMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LightMap):
        """
        Dynamic initializer for LightMap.
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
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.LightMap.getSunlight(int,int,int)"""
        return int.__wrap(super(__LightMap, self).getSunlight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def save(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.world.LightMap.save()"""
        return List[int].__wrap(super(LightMap, self).save())

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.LightMap.getBlockLight(int,int,int)"""
        return int.__wrap(super(__LightMap, self).getBlockLight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setBlockLight(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.world.LightMap.setBlockLight(int,int,int,int)"""
        super(__LightMap, self).setBlockLight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.LightMap(int)"""
        val = __LightMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSunlight(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.world.LightMap.setSunlight(int,int,int,int)"""
        super(__LightMap, self).setSunlight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def load(self, arg0: bytes):
        """public void dev.ultreon.quantum.world.LightMap.load(byte[])"""
        super(__LightMap, self).load(bytes)

    @overload
    def __init__(self, arg0: bytes):
        """public dev.ultreon.quantum.world.LightMap(byte[])"""
        val = __LightMap(bytes)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.world.LightMap.getData()"""
        return List[int].__wrap(super(LightMap, self).getData()) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld$Region
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import dev.ultreon.quantum.world.Chunk as __Chunk
__Chunk = __Chunk
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld_Region
__Region = __ServerWorld_Region.Region
import dev.ultreon.quantum.world.ServerChunk as __ServerChunk
__ServerChunk = __ServerChunk
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.RegionPos as __RegionPos
__RegionPos = __RegionPos
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class Region():
    """dev.ultreon.quantum.world.ServerWorld.Region"""
 
    @staticmethod
    def __wrap(java_value: __Region) -> 'Region':
        return Region(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Region):
        """
        Dynamic initializer for Region.
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
    def generateChunk(self, arg0: 'ChunkPos', arg1: 'ChunkPos'):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.generateChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        super(__Region, self).generateChunk(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def trySet(self, arg0: 'Supplier') -> 'util.Result':
        """public <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.world.ServerWorld$Region.trySet(com.google.common.base.Supplier<T>)"""
        return 'util.Result'.__wrap(super(__Region, self).trySet(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$Region.isEmpty()"""
        return bool.__wrap(super(Region, self).isEmpty())

    @overload
    def getChunkCount(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$Region.getChunkCount()"""
        return int.__wrap(super(Region, self).getChunkCount())

    @overload
    def generateChunkNow(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.generateChunkNow(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'.__wrap(super(__Region, self).generateChunkNow(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getActiveChunks(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.ServerWorld$Region.getActiveChunks()"""
        return 'Set'.__wrap(super(Region, self).getActiveChunks())

    @overload
    def deactivate(self, arg0: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.deactivate(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'.__wrap(super(__Region, self).deactivate(arg0))

    @overload
    def putChunk(self, arg0: 'ChunkPos', arg1: 'ServerChunk') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.putChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ServerChunk)"""
        return 'Chunk'.__wrap(super(__Region, self).putChunk(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def openChunkNow(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.openChunkNow(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'.__wrap(super(__Region, self).openChunkNow(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPos(self) -> 'RegionPos':
        """public dev.ultreon.quantum.world.RegionPos dev.ultreon.quantum.world.ServerWorld$Region.getPos()"""
        return 'RegionPos'.__wrap(super(Region, self).getPos())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def markDirty(self):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.markDirty()"""
        super(Region, self).markDirty()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.dispose()"""
        super(Region, self).dispose()

    @overload
    def writeUnlock(self):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.writeUnlock()"""
        super(Region, self).writeUnlock()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def activate(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.activate(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'.__wrap(super(__Region, self).activate(arg0, arg1))

    @overload
    def pos(self) -> 'RegionPos':
        """public dev.ultreon.quantum.world.RegionPos dev.ultreon.quantum.world.ServerWorld$Region.pos()"""
        return 'RegionPos'.__wrap(super(Region, self).pos())

    @overload
    def isDirty(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$Region.isDirty()"""
        return bool.__wrap(super(Region, self).isDirty())

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'RegionPos'):
        """public dev.ultreon.quantum.world.ServerWorld$Region(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.RegionPos)"""
        val = __Region(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def writeLock(self):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.writeLock()"""
        super(Region, self).writeLock()

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'RegionPos', arg2: 'Map'):
        """public dev.ultreon.quantum.world.ServerWorld$Region(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.RegionPos,java.util.Map<dev.ultreon.quantum.world.ChunkPos, dev.ultreon.quantum.world.ServerChunk>)"""
        val = __Region(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getActiveChunk(self, arg0: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.getActiveChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'.__wrap(super(__Region, self).getActiveChunk(arg0))

    @overload
    def getChunks(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.world.ServerChunk> dev.ultreon.quantum.world.ServerWorld$Region.getChunks()"""
        return 'Collection'.__wrap(super(Region, self).getChunks())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def openChunk(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.openChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'.__wrap(super(__Region, self).openChunk(arg0, arg1))

    @overload
    def hasActiveChunks(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$Region.hasActiveChunks()"""
        return bool.__wrap(super(Region, self).hasActiveChunks())

    @overload
    def getChunk(self, arg0: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'.__wrap(super(__Region, self).getChunk(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.SeededSupplier
import dev.ultreon.quantum.world.SeededSupplier as __SeededSupplier
__SeededSupplier = __SeededSupplier
from abc import abstractmethod, ABC
 
class SeededSupplier(ABC):
    """dev.ultreon.quantum.world.SeededSupplier"""
 
    @staticmethod
    def __wrap(java_value: __SeededSupplier) -> 'SeededSupplier':
        return SeededSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SeededSupplier):
        """
        Dynamic initializer for SeededSupplier.
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
 
    @abstractmethod
    def get(self, arg0: int):
        """public abstract T dev.ultreon.quantum.world.SeededSupplier.get(long)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.world.WorldStorage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.WorldSaveInfo as __WorldSaveInfo
__WorldSaveInfo = __WorldSaveInfo
from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.io.File as __File
__File = __File
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class WorldStorage():
    """dev.ultreon.quantum.world.WorldStorage"""
 
    @staticmethod
    def __wrap(java_value: __WorldStorage) -> 'WorldStorage':
        return WorldStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldStorage):
        """
        Dynamic initializer for WorldStorage.
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
    def createWorld(self):
        """public void dev.ultreon.quantum.world.WorldStorage.createWorld() throws java.io.IOException"""
        super(WorldStorage, self).createWorld()

    @staticmethod
    @overload
    def createFolderName() -> str:
        """public static <V,K> java.lang.String dev.ultreon.quantum.world.WorldStorage.createFolderName()"""
        return str.__wrap(__WorldStorage.createFolderName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def regionFile(self, arg0: 'RegionPos') -> 'File':
        """public java.io.File dev.ultreon.quantum.world.WorldStorage.regionFile(dev.ultreon.quantum.world.RegionPos)"""
        return 'File'.__wrap(super(__WorldStorage, self).regionFile(arg0))

    @staticmethod
    @overload
    def hashSHA256(arg0: bytes) -> List[int]:
        """public static byte[] dev.ultreon.quantum.world.WorldStorage.hashSHA256(byte[])"""
        return List[int].__wrap(__WorldStorage.hashSHA256(bytes))

    @overload
    def read(self, arg0: str, *arg1: 'types.DataType') -> 'types.DataType':
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.quantum.world.WorldStorage.read(java.lang.String,T...) throws java.io.IOException"""
        return 'types.DataType'.__wrap(super(__WorldStorage, self).read(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'File'):
        """public dev.ultreon.quantum.world.WorldStorage(java.io.File)"""
        val = __WorldStorage(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.WorldStorage.getName()"""
        return str.__wrap(super(WorldStorage, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.world.WorldStorage(java.lang.String)"""
        val = __WorldStorage(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def delete(self) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.delete() throws java.io.IOException"""
        return bool.__wrap(super(WorldStorage, self).delete())

    @overload
    def createDir(self, arg0: str):
        """public void dev.ultreon.quantum.world.WorldStorage.createDir(java.lang.String) throws java.io.IOException"""
        super(__WorldStorage, self).createDir(arg0)

    @overload
    def regionExists(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.regionExists(int,int) throws java.io.IOException"""
        return bool.__wrap(super(__WorldStorage, self).regionExists(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def write(self, arg0: 'DataType', arg1: str):
        """public void dev.ultreon.quantum.world.WorldStorage.write(dev.ultreon.ubo.types.DataType<?>,java.lang.String) throws java.io.IOException"""
        super(__WorldStorage, self).write(arg0, arg1)

    @overload
    def getSHA256Name(self) -> str:
        """public <V,K> java.lang.String dev.ultreon.quantum.world.WorldStorage.getSHA256Name()"""
        return str.__wrap(super(WorldStorage, self).getSHA256Name())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def hasInfo(self) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.hasInfo()"""
        return bool.__wrap(super(WorldStorage, self).hasInfo())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def exists(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.exists(java.lang.String)"""
        return bool.__wrap(super(__WorldStorage, self).exists(arg0))

    @overload
    def getDirectory(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.world.WorldStorage.getDirectory()"""
        return 'Path'.__wrap(super(WorldStorage, self).getDirectory())

    @overload
    def regionFile(self, arg0: int, arg1: int) -> 'File':
        """public java.io.File dev.ultreon.quantum.world.WorldStorage.regionFile(int,int)"""
        return 'File'.__wrap(super(__WorldStorage, self).regionFile(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def loadInfo(self) -> 'WorldSaveInfo':
        """public dev.ultreon.quantum.world.WorldSaveInfo dev.ultreon.quantum.world.WorldStorage.loadInfo()"""
        return 'WorldSaveInfo'.__wrap(super(WorldStorage, self).loadInfo())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def saveInfo(self, arg0: 'WorldSaveInfo'):
        """public void dev.ultreon.quantum.world.WorldStorage.saveInfo(dev.ultreon.quantum.world.WorldSaveInfo) throws java.io.IOException"""
        super(__WorldStorage, self).saveInfo(arg0)

    @overload
    def __init__(self, arg0: 'Path'):
        """public dev.ultreon.quantum.world.WorldStorage(java.nio.file.Path)"""
        val = __WorldStorage(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.ChunkPos
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.world.RegionPos as __RegionPos
__RegionPos = __RegionPos
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as __Vec2d
__Vec2d = __Vec2d
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ChunkPos():
    """dev.ultreon.quantum.world.ChunkPos"""
 
    @staticmethod
    def __wrap(java_value: __ChunkPos) -> 'ChunkPos':
        return ChunkPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkPos):
        """
        Dynamic initializer for ChunkPos.
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
    def compareTo(self, arg0: 'ChunkPos') -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.compareTo(dev.ultreon.quantum.world.ChunkPos)"""
        return int.__wrap(super(__ChunkPos, self).compareTo(arg0))

    @staticmethod
    @overload
    def parse(arg0: str) -> 'RegionPos':
        """public static dev.ultreon.quantum.world.RegionPos dev.ultreon.quantum.world.ChunkPos.parse(java.lang.String)"""
        return RegionPos.__wrap(__ChunkPos.parse(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.x()"""
        return int.__wrap(super(ChunkPos, self).x())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.ChunkPos.equals(java.lang.Object)"""
        return bool.__wrap(super(__ChunkPos, self).equals(arg0))

    @overload
    def vec(self) -> 'vector.Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.quantum.world.ChunkPos.vec()"""
        return 'vector.Vec2d'.__wrap(super(ChunkPos, self).vec())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.hashCode()"""
        return int.__wrap(super(ChunkPos, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.ChunkPos.toString()"""
        return str.__wrap(super(ChunkPos, self).toString())

    @overload
    def offset(self, arg0: int, arg1: int) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.ChunkPos.offset(int,int)"""
        return 'ChunkPos'.__wrap(super(__ChunkPos, self).offset(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.world.ChunkPos(int,int)"""
        val = __ChunkPos(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChunkOrigin(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.world.ChunkPos.getChunkOrigin()"""
        return 'vector.Vec3d'.__wrap(super(ChunkPos, self).getChunkOrigin())

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.z()"""
        return int.__wrap(super(ChunkPos, self).z()) 
 
 
# CLASS: dev.ultreon.quantum.world.BlockFlags
from builtins import str
import java.lang.Long as __long
import dev.ultreon.quantum.world.BlockFlags as __BlockFlags
__BlockFlags = __BlockFlags
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockFlags():
    """dev.ultreon.quantum.world.BlockFlags"""
 
    @staticmethod
    def __wrap(java_value: __BlockFlags) -> 'BlockFlags':
        return BlockFlags(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockFlags):
        """
        Dynamic initializer for BlockFlags.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.BlockFlags()"""
        val = __BlockFlags()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.BlockFlags()"""
        val = __BlockFlags()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))