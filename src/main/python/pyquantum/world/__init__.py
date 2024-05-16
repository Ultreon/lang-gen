from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.Integer as _int
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import java.lang.Class as _Class
_Class = _Class
 
class BlockPos():
    """dev.ultreon.quantum.world.BlockPos"""
 
    @staticmethod
    def _wrap(java_value: _BlockPos) -> 'BlockPos':
        return BlockPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockPos):
        """
        Dynamic initializer for BlockPos.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockPos__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockPos__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def offset(self, arg0: 'ChunkPos') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.ChunkPos)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(arg0))

    @overload
    def offset(self, arg0: 'CubicDirection', arg1: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection,int)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def offset(self, arg0: 'CubicDirection') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(arg0))

    @overload
    def below(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.below()"""
        return 'BlockPos'._wrap(super(BlockPos, self).below())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.BlockPos.toString()"""
        return str._wrap(super(BlockPos, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.x()"""
        return int._wrap(super(BlockPos, self).x())

    @overload
    def offset(self, arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(int,int,int)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def vec(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.BlockPos.vec()"""
        return 'vector.Vec3i'._wrap(super(BlockPos, self).vec())

    @overload
    def above(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.above()"""
        return 'BlockPos'._wrap(super(BlockPos, self).above())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Vec3i'):
        """public dev.ultreon.quantum.world.BlockPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        val = _BlockPos(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = _BlockPos()
        self.__wrapper = val

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.z()"""
        return int._wrap(super(BlockPos, self).z())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def y(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.y()"""
        return int._wrap(super(BlockPos, self).y())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.world.BlockPos(int,int,int)"""
        val = _BlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.BlockPos.equals(java.lang.Object)"""
        return bool._wrap(super(_BlockPos, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.BlockPos(double,double,double)"""
        val = _BlockPos(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = _BlockPos()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.hashCode()"""
        return int._wrap(super(BlockPos, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.world.BlockPos
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.Integer as _int
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import java.lang.Class as _Class
_Class = _Class
 
class BlockPos():
    """dev.ultreon.quantum.world.BlockPos"""
 
    @staticmethod
    def _wrap(java_value: _BlockPos) -> 'BlockPos':
        return BlockPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockPos):
        """
        Dynamic initializer for BlockPos.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockPos__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockPos__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def offset(self, arg0: 'ChunkPos') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.ChunkPos)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(arg0))

    @overload
    def offset(self, arg0: 'CubicDirection', arg1: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection,int)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def offset(self, arg0: 'CubicDirection') -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(dev.ultreon.quantum.world.CubicDirection)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(arg0))

    @overload
    def below(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.below()"""
        return 'BlockPos'._wrap(super(BlockPos, self).below())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.BlockPos.toString()"""
        return str._wrap(super(BlockPos, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.x()"""
        return int._wrap(super(BlockPos, self).x())

    @overload
    def offset(self, arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.offset(int,int,int)"""
        return 'BlockPos'._wrap(super(_BlockPos, self).offset(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def vec(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.BlockPos.vec()"""
        return 'vector.Vec3i'._wrap(super(BlockPos, self).vec())

    @overload
    def above(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.BlockPos.above()"""
        return 'BlockPos'._wrap(super(BlockPos, self).above())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Vec3i'):
        """public dev.ultreon.quantum.world.BlockPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        val = _BlockPos(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = _BlockPos()
        self.__wrapper = val

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.z()"""
        return int._wrap(super(BlockPos, self).z())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def y(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.y()"""
        return int._wrap(super(BlockPos, self).y())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.world.BlockPos(int,int,int)"""
        val = _BlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.BlockPos.equals(java.lang.Object)"""
        return bool._wrap(super(_BlockPos, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.BlockPos(double,double,double)"""
        val = _BlockPos(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.BlockPos()"""
        val = _BlockPos()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.BlockPos.hashCode()"""
        return int._wrap(super(BlockPos, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.world.BlockPos 
 
 
# CLASS: dev.ultreon.quantum.world.SoundEvent
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import dev.ultreon.quantum.world.SoundEvent as _SoundEvent
_SoundEvent = _SoundEvent
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoundEvent():
    """dev.ultreon.quantum.world.SoundEvent"""
 
    @staticmethod
    def _wrap(java_value: _SoundEvent) -> 'SoundEvent':
        return SoundEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoundEvent):
        """
        Dynamic initializer for SoundEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoundEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoundEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.SoundEvent.getId()"""
        return 'util.Identifier'._wrap(super(SoundEvent, self).getId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.world.SoundEvent(float)"""
        val = _SoundEvent(_float.valueOf(arg0))
        self.__wrapper = val

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
    def getRange(self) -> float:
        """public float dev.ultreon.quantum.world.SoundEvent.getRange()"""
        return float._wrap(super(SoundEvent, self).getRange())

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
 
 
# CLASS: dev.ultreon.quantum.world.CubicDirection
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.math.Quaternion as _Quaternion
_Quaternion = _Quaternion
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.util.Optional as _Optional
_Optional = _Optional
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.util.Axis as _Axis
_Axis = _Axis
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.quantum.world.CubicDirection as _CubicDirection
_CubicDirection = _CubicDirection
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Enum as Enum
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as Optional
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubicDirection():
    """dev.ultreon.quantum.world.CubicDirection"""
 
    @staticmethod
    def _wrap(java_value: _CubicDirection) -> 'CubicDirection':
        return CubicDirection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubicDirection):
        """
        Dynamic initializer for CubicDirection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubicDirection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubicDirection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getNormal(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.world.CubicDirection.getNormal()"""
        return 'math.Vector3'._wrap(super(CubicDirection, self).getNormal())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CubicDirection':
        """public static dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.valueOf(java.lang.String)"""
        return CubicDirection._wrap(_CubicDirection.valueOf(arg0))

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.world.CubicDirection.getIndex()"""
        return int._wrap(super(CubicDirection, self).getIndex())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def fromVec3d(arg0: 'Vec3d') -> 'CubicDirection':
        """public static dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.fromVec3d(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return CubicDirection._wrap(_CubicDirection.fromVec3d(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCounterClockwise(self) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.getCounterClockwise()"""
        return 'CubicDirection'._wrap(super(CubicDirection, self).getCounterClockwise())

    @overload
    def getAxis(self) -> 'util.Axis':
        """public dev.ultreon.quantum.util.Axis dev.ultreon.quantum.world.CubicDirection.getAxis()"""
        return 'util.Axis'._wrap(super(CubicDirection, self).getAxis())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getOffset(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.CubicDirection.getOffset()"""
        return 'BlockPos'._wrap(super(CubicDirection, self).getOffset())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def ofNormal(arg0: 'Vec3f') -> 'CubicDirection':
        """public static dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.ofNormal(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return CubicDirection._wrap(_CubicDirection.ofNormal(arg0))

    @overload
    def rotateY(self, arg0: int) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.rotateY(int)"""
        return 'CubicDirection'._wrap(super(_CubicDirection, self).rotateY(_int.valueOf(arg0)))

    @overload
    def getClockwise(self) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.getClockwise()"""
        return 'CubicDirection'._wrap(super(CubicDirection, self).getClockwise())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @overload
    def getOpposite(self) -> 'CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.world.CubicDirection.getOpposite()"""
        return 'CubicDirection'._wrap(super(CubicDirection, self).getOpposite())

    @staticmethod
    @overload
    def values() -> List['CubicDirection']:
        """public static dev.ultreon.quantum.world.CubicDirection[] dev.ultreon.quantum.world.CubicDirection.values()"""
        return List[CubicDirection]._wrap(_CubicDirection.values())

    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.world.CubicDirection.getDisplayName()"""
        return 'text.TextObject'._wrap(super(CubicDirection, self).getDisplayName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getHorizontalRotation(self) -> 'math.Quaternion':
        """public com.badlogic.gdx.math.Quaternion dev.ultreon.quantum.world.CubicDirection.getHorizontalRotation()"""
        return 'math.Quaternion'._wrap(super(CubicDirection, self).getHorizontalRotation())


CubicDirection.DOWN = CubicDirection._wrap(_DOWN.DOWN)

CubicDirection.EAST = CubicDirection._wrap(_EAST.EAST)

CubicDirection.SOUTH = CubicDirection._wrap(_SOUTH.SOUTH)

CubicDirection.WEST = CubicDirection._wrap(_WEST.WEST)

CubicDirection.UP = CubicDirection._wrap(_UP.UP)

CubicDirection.NORTH = CubicDirection._wrap(_NORTH.NORTH) 
 
 
# CLASS: dev.ultreon.quantum.world.Chunk$Status
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.Chunk as _Chunk_Status
_Status = _Chunk_Status.Status
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Status():
    """dev.ultreon.quantum.world.Chunk.Status"""
 
    @staticmethod
    def _wrap(java_value: _Status) -> 'Status':
        return Status(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Status):
        """
        Dynamic initializer for Status.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Status__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Status__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['Status']:
        """public static dev.ultreon.quantum.world.Chunk$Status[] dev.ultreon.quantum.world.Chunk$Status.values()"""
        return List[Status]._wrap(_Status.values())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Status':
        """public static dev.ultreon.quantum.world.Chunk$Status dev.ultreon.quantum.world.Chunk$Status.valueOf(java.lang.String)"""
        return Status._wrap(_Status.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Status.SKIP = Status._wrap(_SKIP.SKIP)

Status.SUCCESS = Status._wrap(_SUCCESS.SUCCESS)

Status.FAILED = Status._wrap(_FAILED.FAILED)

Status.UNLOADED = Status._wrap(_UNLOADED.UNLOADED) 
 
 
# CLASS: dev.ultreon.quantum.world.BuilderChunk
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import java.lang.Thread as Thread
try:
    from pyquantum.world.gen import biome
except ImportError:
    biome = _import_once("pyquantum.world.gen.biome")

try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
import dev.ultreon.quantum.world.ServerChunk as _ServerChunk
_ServerChunk = _ServerChunk
import java.util.Collection as Collection
try:
    from pyquantum import collection
except ImportError:
    collection = _import_once("pyquantum.collection")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.TreeData as _TreeData
_TreeData = _TreeData
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator
_BiomeGenerator = _BiomeGenerator
from builtins import bool
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
from builtins import str
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
import dev.ultreon.quantum.world.LightMap as _LightMap
_LightMap = _LightMap
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.BuilderChunk as _BuilderChunk
_BuilderChunk = _BuilderChunk
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.util.Collection as _Collection
_Collection = _Collection
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.rng.RNG as _RNG
_RNG = _RNG
import java.util.Map as Map
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
import java.lang.Long as _long
from builtins import int
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class BuilderChunk():
    """dev.ultreon.quantum.world.BuilderChunk"""
 
    @staticmethod
    def _wrap(java_value: _BuilderChunk) -> 'BuilderChunk':
        return BuilderChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BuilderChunk):
        """
        Dynamic initializer for BuilderChunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BuilderChunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BuilderChunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorld(self) -> 'ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.world.BuilderChunk.getWorld()"""
        return 'ServerWorld'._wrap(super(BuilderChunk, self).getWorld())

    @override
    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(_Chunk, self).startBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(_Chunk, self).setTreeData(arg0)

    @overload
    def getBiomeGenerator(self, arg0: int, arg1: int) -> 'biome.BiomeGenerator':
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator dev.ultreon.quantum.world.BuilderChunk.getBiomeGenerator(int,int)"""
        return 'biome.BiomeGenerator'._wrap(super(_BuilderChunk, self).getBiomeGenerator(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getLightMap(self) -> 'LightMap':
        """public dev.ultreon.quantum.world.LightMap dev.ultreon.quantum.world.BuilderChunk.getLightMap()"""
        return 'LightMap'._wrap(super(BuilderChunk, self).getLightMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_Chunk, self).getSunlight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_BuilderChunk, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool._wrap(super(Chunk, self).isReady())

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
    def getBiomeCenters(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3i> dev.ultreon.quantum.world.BuilderChunk.getBiomeCenters()"""
        return 'List'._wrap(super(BuilderChunk, self).getBiomeCenters())

    @override
    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'._wrap(super(Chunk, self).getBreaking())

    @overload
    def build(self) -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.BuilderChunk.build()"""
        return 'ServerChunk'._wrap(super(BuilderChunk, self).build())

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int._wrap(super(_Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'._wrap(super(Chunk, self).getBlockEntities())

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_Chunk, self).getBlockLight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(_Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties._wrap(_Chunk.loadBlock(arg0))

    @override
    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.BuilderChunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_BuilderChunk, self).setFast(arg0, arg1)

    @override
    @overload
    def getPos(self) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'ChunkPos'._wrap(super(Chunk, self).getPos())

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_BuilderChunk, self).setFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'Biome'._wrap(super(_Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(_Chunk, self).removeBlockEntity(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.BuilderChunk.getFast(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_BuilderChunk, self).getFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(arg0))

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Chunk, self).getSunlight(arg0))

    @overload
    def setBiomeGenerator(self, arg0: int, arg1: int, arg2: 'BiomeGenerator'):
        """public void dev.ultreon.quantum.world.BuilderChunk.setBiomeGenerator(int,int,dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        super(_BuilderChunk, self).setBiomeGenerator(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool._wrap(super(Chunk, self).isActive())

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Chunk, self).getBlockLight(arg0))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.BuilderChunk.getHighest(int,int)"""
        return int._wrap(super(_BuilderChunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(arg0))

    @overload
    def isOnBuilderThread(self) -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.isOnBuilderThread()"""
        return bool._wrap(super(BuilderChunk, self).isOnBuilderThread())

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(arg0))

    @overload
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.world.Chunk.onUpdated()"""
        super(Chunk, self).onUpdated()

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int._wrap(super(_Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.Chunk.dispose()"""
        super(Chunk, self).dispose()

    @property
    def storage(self) -> Storage:
        return Storage._wrap(super(_Chunk).storage())

    @override
    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.BuilderChunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_BuilderChunk, self).set(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str._wrap(super(Chunk, self).toString())

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block._wrap(_Chunk.decodeBlock(arg0))

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'Thread', arg2: 'ChunkPos', arg3: 'Region'):
        """public dev.ultreon.quantum.world.BuilderChunk(dev.ultreon.quantum.world.ServerWorld,java.lang.Thread,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ServerWorld$Region)"""
        val = _BuilderChunk(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @overload
    def setBiomeCenters(self, arg0: 'List'):
        """public void dev.ultreon.quantum.world.BuilderChunk.setBiomeCenters(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3i>)"""
        super(_BuilderChunk, self).setBiomeCenters(arg0)

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).getFast(arg0))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'BreakResult'._wrap(super(_Chunk, self).continueBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int._wrap(super(_Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getRNG(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.world.BuilderChunk.getRNG()"""
        return 'rng.RNG'._wrap(super(BuilderChunk, self).getRNG())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool._wrap(super(Chunk, self).isDisposed())

    @property
    def treeData(self) -> TreeData:
        return TreeData._wrap(super(_Chunk).treeData())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int._wrap(super(Chunk, self).hashCode())

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'._wrap(super(Chunk, self).getOffset())

    @overload
    def isOnInvalidThread(self) -> bool:
        """public boolean dev.ultreon.quantum.world.BuilderChunk.isOnInvalidThread()"""
        return bool._wrap(super(BuilderChunk, self).isOnInvalidThread())

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'Biome'._wrap(super(_Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(_Chunk, self).stopBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool._wrap(super(_Chunk, self).equals(arg0))

    @property
    def biomeStorage(self) -> Storage:
        return Storage._wrap(super(_Chunk).biomeStorage())

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float._wrap(super(_Chunk, self).getBrightness(_int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerChunk
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
import dev.ultreon.quantum.world.ServerChunk as _ServerChunk
_ServerChunk = _ServerChunk
import java.util.Collection as Collection
try:
    from pyquantum import collection
except ImportError:
    collection = _import_once("pyquantum.collection")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
import dev.ultreon.quantum.world.gen.TreeData as _TreeData
_TreeData = _TreeData
from builtins import bool
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
from builtins import str
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.util.Collection as _Collection
_Collection = _Collection
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.util.Map as Map
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerChunk():
    """dev.ultreon.quantum.world.ServerChunk"""
 
    @staticmethod
    def _wrap(java_value: _ServerChunk) -> 'ServerChunk':
        return ServerChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerChunk):
        """
        Dynamic initializer for ServerChunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerChunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerChunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(_Chunk, self).startBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(_Chunk, self).setTreeData(arg0)

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.world.ServerChunk.load(dev.ultreon.ubo.types.MapType)"""
        super(_ServerChunk, self).load(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_Chunk, self).getSunlight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool._wrap(super(Chunk, self).isReady())

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
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'._wrap(super(Chunk, self).getBreaking())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Chunk, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int._wrap(super(_Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'._wrap(super(Chunk, self).getBlockEntities())

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.ServerChunk.save()"""
        return 'types.MapType'._wrap(super(ServerChunk, self).save())

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_Chunk, self).getBlockLight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(_Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Chunk, self).setFast(arg0, arg1)

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties._wrap(_Chunk.loadBlock(arg0))

    @overload
    def isOriginal(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerChunk.isOriginal()"""
        return bool._wrap(super(ServerChunk, self).isOriginal())

    @override
    @overload
    def getPos(self) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'ChunkPos'._wrap(super(Chunk, self).getPos())

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int)"""
        return int._wrap(super(_Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'Biome'._wrap(super(_Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(_Chunk, self).removeBlockEntity(arg0)

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'ChunkPos', arg2: 'Storage', arg3: 'Storage', arg4: 'Region'):
        """public dev.ultreon.quantum.world.ServerChunk(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,dev.ultreon.quantum.world.ServerWorld$Region)"""
        val = _ServerChunk(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(arg0))

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Chunk, self).getSunlight(arg0))

    @override
    @overload
    def getWorld(self) -> 'ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.world.ServerChunk.getWorld()"""
        return 'ServerWorld'._wrap(super(ServerChunk, self).getWorld())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool._wrap(super(Chunk, self).isActive())

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).getFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Chunk, self).getBlockLight(arg0))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(arg0))

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(arg0))

    @overload
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.world.Chunk.onUpdated()"""
        super(Chunk, self).onUpdated()

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int._wrap(super(_Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Chunk, self).set(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.Chunk.dispose()"""
        super(Chunk, self).dispose()

    @property
    def storage(self) -> Storage:
        return Storage._wrap(super(_Chunk).storage())

    @staticmethod
    @overload
    def load(arg0: 'ServerWorld', arg1: 'ChunkPos', arg2: 'MapType', arg3: 'Region') -> 'ServerChunk':
        """public static dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerChunk.load(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.ubo.types.MapType,dev.ultreon.quantum.world.ServerWorld$Region)"""
        return ServerChunk._wrap(_ServerChunk.load(arg0, arg1, arg2, arg3))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_ServerChunk, self).setFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str._wrap(super(Chunk, self).toString())

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block._wrap(_Chunk.decodeBlock(arg0))

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).getFast(arg0))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'BreakResult'._wrap(super(_Chunk, self).continueBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int._wrap(super(_Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool._wrap(super(Chunk, self).isDisposed())

    @property
    def treeData(self) -> TreeData:
        return TreeData._wrap(super(_Chunk).treeData())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int._wrap(super(Chunk, self).hashCode())

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'._wrap(super(Chunk, self).getOffset())

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'Biome'._wrap(super(_Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(_Chunk, self).stopBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool._wrap(super(_Chunk, self).equals(arg0))

    @property
    def biomeStorage(self) -> Storage:
        return Storage._wrap(super(_Chunk).biomeStorage())

    @overload
    def shouldSave(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerChunk.shouldSave()"""
        return bool._wrap(super(ServerChunk, self).shouldSave())

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float._wrap(super(_Chunk, self).getBrightness(_int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.quantum.world.TerrainNoise
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.world.TerrainNoise as _TerrainNoise
_TerrainNoise = _TerrainNoise
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TerrainNoise():
    """dev.ultreon.quantum.world.TerrainNoise"""
 
    @staticmethod
    def _wrap(java_value: _TerrainNoise) -> 'TerrainNoise':
        return TerrainNoise(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TerrainNoise):
        """
        Dynamic initializer for TerrainNoise.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TerrainNoise__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TerrainNoise__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double,double,double)"""
        return float._wrap(super(_TerrainNoise, self).evaluateNoise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def evaluateNoise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double,double)"""
        return float._wrap(super(_TerrainNoise, self).evaluateNoise(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.TerrainNoise(long)"""
        val = _TerrainNoise(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def evaluateNoise(self, arg0: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double)"""
        return float._wrap(super(_TerrainNoise, self).evaluateNoise(_double.valueOf(arg0)))

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
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.quantum.world.TerrainNoise.evaluateNoise(double,double,double,double)"""
        return float._wrap(super(_TerrainNoise, self).evaluateNoise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

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
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld$RegionStorage
from builtins import str
import java.io.DataOutputStream as DataOutputStream
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld_RegionStorage
_RegionStorage = _ServerWorld_RegionStorage.RegionStorage
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld_Region
_Region = _ServerWorld_Region.Region
from builtins import bool
import java.io.DataInputStream as DataInputStream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegionStorage():
    """dev.ultreon.quantum.world.ServerWorld.RegionStorage"""
 
    @staticmethod
    def _wrap(java_value: _RegionStorage) -> 'RegionStorage':
        return RegionStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegionStorage):
        """
        Dynamic initializer for RegionStorage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegionStorage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegionStorage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.ServerWorld$RegionStorage()"""
        val = _RegionStorage()
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getChunkCount(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RegionStorage.getChunkCount()"""
        return int._wrap(super(RegionStorage, self).getChunkCount())

    @overload
    def getRegionAt(self, arg0: 'ChunkPos') -> 'Region':
        """public dev.ultreon.quantum.world.ServerWorld$Region dev.ultreon.quantum.world.ServerWorld$RegionStorage.getRegionAt(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Region'._wrap(super(_RegionStorage, self).getRegionAt(arg0))

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
    def load(self, arg0: 'ServerWorld', arg1: 'DataInputStream') -> 'Region':
        """public dev.ultreon.quantum.world.ServerWorld$Region dev.ultreon.quantum.world.ServerWorld$RegionStorage.load(dev.ultreon.quantum.world.ServerWorld,java.io.DataInputStream) throws java.io.IOException"""
        return 'Region'._wrap(super(_RegionStorage, self).load(arg0, arg1))

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.ServerWorld$RegionStorage.dispose()"""
        super(RegionStorage, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def save(self, arg0: 'Region', arg1: 'DataOutputStream', arg2: bool):
        """public void dev.ultreon.quantum.world.ServerWorld$RegionStorage.save(dev.ultreon.quantum.world.ServerWorld$Region,java.io.DataOutputStream,boolean) throws java.io.IOException"""
        super(_RegionStorage, self).save(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.ServerWorld$RegionStorage()"""
        val = _RegionStorage()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.World
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.util.function.Predicate as Predicate
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import java.util.Collection as Collection
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
import dev.ultreon.quantum.util.BlockHitResult as _BlockHitResult
_BlockHitResult = _BlockHitResult
from builtins import bool
import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
import java.lang.Object as _object
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.util.Collection as _Collection
_Collection = _Collection
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
try:
    from pyquantum.world import particles
except ImportError:
    particles = _import_once("pyquantum.world.particles")

import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import dev.ultreon.quantum.util.EntityHitResult as _EntityHitResult
_EntityHitResult = _EntityHitResult
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
import dev.ultreon.quantum.world.DimensionInfo as _DimensionInfo
_DimensionInfo = _DimensionInfo
import java.lang.Long as _long
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class World():
    """dev.ultreon.quantum.world.World"""
 
    @staticmethod
    def _wrap(java_value: _World) -> 'World':
        return World(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _World):
        """
        Dynamic initializer for World.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_World__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_World__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.World.OVERWORLD
    OVERWORLD: 'util.Identifier' = _wrap(_util.Identifier.OVERWORLD)


    @overload
    def updateChunkAndNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunkAndNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).updateChunkAndNeighbours(arg0)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_World, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def isChunkInvalidated(self, arg0: 'Chunk') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isChunkInvalidated(dev.ultreon.quantum.world.Chunk)"""
        return bool._wrap(super(_World, self).isChunkInvalidated(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vector3') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(com.badlogic.gdx.math.Vector3)"""
        return ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @abstractmethod
    def getLoadedChunks(self, ):
        """public abstract java.util.Collection<? extends dev.ultreon.quantum.world.Chunk> dev.ultreon.quantum.world.World.getLoadedChunks()"""
        pass

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'EntityType') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool._wrap(super(_World, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toChunkVec(arg0: int, arg1: int, arg2: int) -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(int,int,int)"""
        return vector.Vec2i._wrap(_World.toChunkVec(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def stopBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.stopBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_World, self).stopBreaking(arg0, arg1)

    @overload
    def getChunkAt(self, arg0: int, arg1: int, arg2: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(int,int,int)"""
        return 'Chunk'._wrap(super(_World, self).getChunkAt(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def updateNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).updateNeighbours(arg0)

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: 'BlockPos') -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return BlockPos._wrap(_World.toLocalBlockPos(arg0))

    @overload
    def destroyBlock(self, arg0: 'BlockPos', arg1: 'Player') -> bool:
        """public boolean dev.ultreon.quantum.world.World.destroyBlock(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        return bool._wrap(super(_World, self).destroyBlock(arg0, arg1))

    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_World, self).drop(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isOutOfWorldBounds(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(int,int,int)"""
        return bool._wrap(super(_World, self).isOutOfWorldBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_World, self).drop(arg0, arg1)

    @overload
    def isOutOfWorldBounds(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(dev.ultreon.quantum.world.BlockPos)"""
        return bool._wrap(super(_World, self).isOutOfWorldBounds(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isSpawnChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isSpawnChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_World, self).isSpawnChunk(arg0))

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: int, arg1: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(int,int)"""
        return ChunkPos._wrap(_World.toLocalChunkPos(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def updateChunk(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunk(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).updateChunk(arg0)

    @overload
    def collide(self, arg0: 'BoundingBox', arg1: bool) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.BoundingBox> dev.ultreon.quantum.world.World.collide(dev.ultreon.quantum.util.BoundingBox,boolean)"""
        return 'List'._wrap(super(_World, self).collide(arg0, _boolean.valueOf(arg1)))

    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.world.World.playSound(dev.ultreon.quantum.world.SoundEvent,double,double,double)"""
        super(_World, self).playSound(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @overload
    def fillCrashInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.world.World.fillCrashInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(_World, self).fillCrashInfo(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isAlwaysLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isAlwaysLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_World, self).isAlwaysLoaded(arg0))

    @overload
    def getChunksLoaded(self) -> int:
        """public int dev.ultreon.quantum.world.World.getChunksLoaded()"""
        return int._wrap(super(World, self).getChunksLoaded())

    @overload
    def getChunk(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunk(int,int)"""
        return 'Chunk'._wrap(super(_World, self).getChunk(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3d') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @overload
    def despawn(self, arg0: int):
        """public void dev.ultreon.quantum.world.World.despawn(int)"""
        super(_World, self).despawn(_int.valueOf(arg0))

    @overload
    def getDimension(self) -> 'DimensionInfo':
        """public dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.World.getDimension()"""
        return 'DimensionInfo'._wrap(super(World, self).getDimension())

    @overload
    def getChunksAround(self, arg0: 'Vec3d') -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.World.getChunksAround(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'List'._wrap(super(_World, self).getChunksAround(arg0))

    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_World, self).setColumn(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def rayCast(self, arg0: 'Ray') -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray)"""
        return 'util.BlockHitResult'._wrap(super(_World, self).rayCast(arg0))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.World.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_World, self).getBlockEntity(arg0))

    @overload
    def rayCast(self, arg0: 'Ray', arg1: float) -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.BlockHitResult'._wrap(super(_World, self).rayCast(arg0, _float.valueOf(arg1)))

    @overload
    def unloadChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.unloadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_World, self).unloadChunk(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getChunk(self, arg0: 'ChunkPos'):
        """public abstract dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        pass

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Class') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def getChunkAt(self, arg0: 'BlockPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(dev.ultreon.quantum.world.BlockPos)"""
        return 'Chunk'._wrap(super(_World, self).getChunkAt(arg0))

    @overload
    def closeMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.closeMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_World, self).closeMenu(arg0)

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int)"""
        return BlockPos._wrap(_World.toLocalBlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_World, self).setColumn(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'BlockProperties') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.world.World.set(int,int,int,int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'CompletableFuture'._wrap(super(_World, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6))

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_World, self).get(arg0))

    @overload
    def getEntitiesByClass(self, arg0: 'Class') -> 'Collection':
        """public <T extends dev.ultreon.quantum.entity.Entity> java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntitiesByClass(java.lang.Class<T>)"""
        return 'Collection'._wrap(super(_World, self).getEntitiesByClass(arg0))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.World.getHighest(int,int)"""
        return int._wrap(super(_World, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @abstractmethod
    def getTotalChunks(self, ):
        """public abstract int dev.ultreon.quantum.world.World.getTotalChunks()"""
        pass

    @abstractmethod
    def isClientSide(self, ):
        """public abstract boolean dev.ultreon.quantum.world.World.isClientSide()"""
        pass

    @overload
    def getEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntities()"""
        return 'Collection'._wrap(super(World, self).getEntities())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def intersectEntities(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.world.World.intersectEntities(dev.ultreon.quantum.util.BoundingBox)"""
        return bool._wrap(super(_World, self).intersectEntities(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setSpawnPoint(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.world.World.setSpawnPoint(int,int)"""
        super(_World, self).setSpawnPoint(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setBlockEntity(self, arg0: 'BlockPos', arg1: 'BlockEntity'):
        """public void dev.ultreon.quantum.world.World.setBlockEntity(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntity)"""
        super(_World, self).setBlockEntity(arg0, arg1)

    @overload
    def entitiesWithinDst(self, arg0: 'Entity', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.entitiesWithinDst(dev.ultreon.quantum.entity.Entity,int)"""
        return 'List'._wrap(super(_World, self).entitiesWithinDst(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toChunkVec(arg0: 'BlockPos') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(dev.ultreon.quantum.world.BlockPos)"""
        return vector.Vec2i._wrap(_World.toChunkVec(arg0))

    @overload
    def spawn(self, arg0: 'Entity', arg1: 'MapType') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T,dev.ultreon.ubo.types.MapType)"""
        return 'entity.Entity'._wrap(super(_World, self).spawn(arg0, arg1))

    @overload
    def __init__(self, arg0: 'LongType'):
        """public dev.ultreon.quantum.world.World(dev.ultreon.ubo.types.LongType)"""
        val = _World(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool._wrap(super(_World, self).set(arg0, arg1, _int.valueOf(arg2)))

    @overload
    def onChunkUpdated(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.onChunkUpdated(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).onChunkUpdated(arg0)

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: 'ChunkPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return ChunkPos._wrap(_World.toLocalChunkPos(arg0))

    @staticmethod
    @overload
    def toChunkPos(arg0: int, arg1: int, arg2: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(int,int,int)"""
        return ChunkPos._wrap(_World.toChunkPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toChunkPos(arg0: 'BlockPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(dev.ultreon.quantum.world.BlockPos)"""
        return ChunkPos._wrap(_World.toChunkPos(arg0))

    @overload
    def spawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.world.World.spawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(_World, self).spawnParticles(arg0, arg1, arg2, _int.valueOf(arg3))

    @overload
    def getUID(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.world.World.getUID()"""
        return 'UUID'._wrap(super(World, self).getUID())

    @overload
    def spawn(self, arg0: 'Entity') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T)"""
        return 'entity.Entity'._wrap(super(_World, self).spawn(arg0))

    @overload
    def getSpawnPoint(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.getSpawnPoint()"""
        return 'BlockPos'._wrap(super(World, self).getSpawnPoint())

    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_World, self).openMenu(arg0)

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float) -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1)))

    @overload
    def getEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.world.World.getEntity(int)"""
        return 'entity.Entity'._wrap(super(_World, self).getEntity(_int.valueOf(arg0)))

    @overload
    def isServerSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isServerSide()"""
        return bool._wrap(super(World, self).isServerSide())

    @overload
    def collideEntities(self, arg0: 'Entity', arg1: 'BoundingBox') -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.collideEntities(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.util.BoundingBox)"""
        return 'List'._wrap(super(_World, self).collideEntities(arg0, arg1))

    @overload
    def getBreakProgress(self, arg0: 'BlockPos') -> float:
        """public float dev.ultreon.quantum.world.World.getBreakProgress(dev.ultreon.quantum.world.BlockPos)"""
        return float._wrap(super(_World, self).getBreakProgress(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.World.dispose()"""
        super(World, self).dispose()

    @overload
    def getSeed(self) -> int:
        """public long dev.ultreon.quantum.world.World.getSeed()"""
        return int._wrap(super(World, self).getSeed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getBiome(self, arg0: 'BlockPos') -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.World.getBiome(dev.ultreon.quantum.world.BlockPos)"""
        return 'Biome'._wrap(super(_World, self).getBiome(arg0))

    @overload
    def despawn(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.world.World.despawn(dev.ultreon.quantum.entity.Entity)"""
        super(_World, self).despawn(arg0)

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Predicate') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.util.function.Predicate<dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_World, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def startBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.startBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_World, self).startBreaking(arg0, arg1)

    @overload
    def continueBreaking(self, arg0: 'BlockPos', arg1: float, arg2: 'Player') -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.World.continueBreaking(dev.ultreon.quantum.world.BlockPos,float,dev.ultreon.quantum.entity.player.Player)"""
        return 'BreakResult'._wrap(super(_World, self).continueBreaking(arg0, _float.valueOf(arg1), arg2))

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isDisposed()"""
        return bool._wrap(super(World, self).isDisposed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_World, self).set(arg0, arg1))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int, arg3: 'Vec3i') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return vector.Vec3i._wrap(_World.toLocalBlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def rayCastEntity(self, arg0: 'Ray') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3i') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return ChunkPos._wrap(_World.blockToChunkPos(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.Biome
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.world.gen.noise.NoiseConfig as _NoiseConfig
_NoiseConfig = _NoiseConfig
from pyquantum_helper import override
try:
    from pyquantum.world.gen import biome
except ImportError:
    biome = _import_once("pyquantum.world.gen.biome")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
import dev.ultreon.quantum.world.Biome as _Biome_Builder
_Builder = _Biome_Builder.Builder
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator
_BiomeGenerator = _BiomeGenerator
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Biome():
    """dev.ultreon.quantum.world.Biome"""
 
    @staticmethod
    def _wrap(java_value: _Biome) -> 'Biome':
        return Biome(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Biome):
        """
        Dynamic initializer for Biome.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Biome__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Biome__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome.builder()"""
        return Builder._wrap(_Biome.builder())

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
    def getTemperatureEnd(self) -> float:
        """public float dev.ultreon.quantum.world.Biome.getTemperatureEnd()"""
        return float._wrap(super(Biome, self).getTemperatureEnd())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def create(self, arg0: 'ServerWorld', arg1: int) -> 'biome.BiomeGenerator':
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator dev.ultreon.quantum.world.Biome.create(dev.ultreon.quantum.world.ServerWorld,long)"""
        return 'biome.BiomeGenerator'._wrap(super(_Biome, self).create(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Biome':
        """public static dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Biome.load(dev.ultreon.ubo.types.MapType)"""
        return Biome._wrap(_Biome.load(arg0))

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
    def getTemperatureStart(self) -> float:
        """public float dev.ultreon.quantum.world.Biome.getTemperatureStart()"""
        return float._wrap(super(Biome, self).getTemperatureStart())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isOcean(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Biome.isOcean()"""
        return bool._wrap(super(Biome, self).isOcean())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.Biome.save()"""
        return 'types.MapType'._wrap(super(Biome, self).save())

    @overload
    def doesNotGenerate(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Biome.doesNotGenerate()"""
        return bool._wrap(super(Biome, self).doesNotGenerate())

    @overload
    def buildLayers(self):
        """public final void dev.ultreon.quantum.world.Biome.buildLayers()"""
        super(Biome, self).buildLayers()

    @overload
    def getSettings(self) -> 'noise.NoiseConfig':
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.Biome.getSettings()"""
        return 'noise.NoiseConfig'._wrap(super(Biome, self).getSettings())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import java.util.UUID as UUID
import java.util.function.Predicate as Predicate
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import java.util.Collection as Collection
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.gen.TerrainGenerator as _TerrainGenerator
_TerrainGenerator = _TerrainGenerator
try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
import dev.ultreon.quantum.util.BlockHitResult as _BlockHitResult
_BlockHitResult = _BlockHitResult
from builtins import bool
import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
import java.lang.Object as _object
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.util.Collection as _Collection
_Collection = _Collection
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
try:
    from pyquantum.world import particles
except ImportError:
    particles = _import_once("pyquantum.world.particles")

import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

from builtins import type
import dev.ultreon.quantum.world.ServerChunk as _ServerChunk
_ServerChunk = _ServerChunk
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import dev.ultreon.quantum.util.EntityHitResult as _EntityHitResult
_EntityHitResult = _EntityHitResult
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
import dev.ultreon.quantum.world.DimensionInfo as _DimensionInfo
_DimensionInfo = _DimensionInfo
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.util.List as List
 
class ServerWorld():
    """dev.ultreon.quantum.world.ServerWorld"""
 
    @staticmethod
    def _wrap(java_value: _ServerWorld) -> 'ServerWorld':
        return ServerWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerWorld):
        """
        Dynamic initializer for ServerWorld.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerWorld__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerWorld__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.World.OVERWORLD
    OVERWORLD: 'util.Identifier' = _wrap(_util.Identifier.OVERWORLD)


    @override
    @overload
    def updateChunkAndNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunkAndNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).updateChunkAndNeighbours(arg0)

    @override
    @overload
    def onChunkUpdated(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.onChunkUpdated(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).onChunkUpdated(arg0)

    @overload
    def isChunkInvalidated(self, arg0: 'Chunk') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isChunkInvalidated(dev.ultreon.quantum.world.Chunk)"""
        return bool._wrap(super(_World, self).isChunkInvalidated(arg0))

    @override
    @overload
    def isServerSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isServerSide()"""
        return bool._wrap(super(World, self).isServerSide())

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'EntityType') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def despawn(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.world.World.despawn(dev.ultreon.quantum.entity.Entity)"""
        super(_World, self).despawn(arg0)

    @staticmethod
    @overload
    def toChunkVec(arg0: int, arg1: int, arg2: int) -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(int,int,int)"""
        return vector.Vec2i._wrap(_World.toChunkVec(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getChunkAt(self, arg0: int, arg1: int, arg2: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(int,int,int)"""
        return 'Chunk'._wrap(super(_World, self).getChunkAt(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isDisposed()"""
        return bool._wrap(super(World, self).isDisposed())

    @overload
    def loadChunkNow(self, arg0: int, arg1: int, arg2: bool) -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld.loadChunkNow(int,int,boolean)"""
        return 'ServerChunk'._wrap(super(_ServerWorld, self).loadChunkNow(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def isSpawnChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isSpawnChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_World, self).isSpawnChunk(arg0))

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: int, arg1: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(int,int)"""
        return ChunkPos._wrap(_World.toLocalChunkPos(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getPlayTime(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getPlayTime()"""
        return int._wrap(super(ServerWorld, self).getPlayTime())

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_World, self).setColumn(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def collide(self, arg0: 'BoundingBox', arg1: bool) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.BoundingBox> dev.ultreon.quantum.world.World.collide(dev.ultreon.quantum.util.BoundingBox,boolean)"""
        return 'List'._wrap(super(_World, self).collide(arg0, _boolean.valueOf(arg1)))

    @overload
    def isAlwaysLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isAlwaysLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_World, self).isAlwaysLoaded(arg0))

    @overload
    def getChunk(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunk(int,int)"""
        return 'Chunk'._wrap(super(_World, self).getChunk(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getChunksAround(self, arg0: 'Vec3d') -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.World.getChunksAround(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'List'._wrap(super(_World, self).getChunksAround(arg0))

    @overload
    def rayCast(self, arg0: 'Ray') -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray)"""
        return 'util.BlockHitResult'._wrap(super(_World, self).rayCast(arg0))

    @overload
    def sync(self, arg0: 'Vec3i'):
        """public void dev.ultreon.quantum.world.ServerWorld.sync(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        super(_ServerWorld, self).sync(arg0)

    @overload
    def rayCast(self, arg0: 'Ray', arg1: float) -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.BlockHitResult'._wrap(super(_World, self).rayCast(arg0, _float.valueOf(arg1)))

    @overload
    def unloadChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.unloadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_World, self).unloadChunk(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntities()"""
        return 'Collection'._wrap(super(World, self).getEntities())

    @overload
    def getChunkAt(self, arg0: 'BlockPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.World.getChunkAt(dev.ultreon.quantum.world.BlockPos)"""
        return 'Chunk'._wrap(super(_World, self).getChunkAt(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'BlockProperties') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.world.World.set(int,int,int,int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'CompletableFuture'._wrap(super(_World, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool._wrap(super(_ServerWorld, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4)))

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_World, self).get(arg0))

    @overload
    def getEntitiesByClass(self, arg0: 'Class') -> 'Collection':
        """public <T extends dev.ultreon.quantum.entity.Entity> java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntitiesByClass(java.lang.Class<T>)"""
        return 'Collection'._wrap(super(_World, self).getEntitiesByClass(arg0))

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'WorldStorage', arg2: 'MapType'):
        """public dev.ultreon.quantum.world.ServerWorld(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.world.WorldStorage,dev.ultreon.ubo.types.MapType)"""
        val = _ServerWorld(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def load(self):
        """public void dev.ultreon.quantum.world.ServerWorld.load() throws java.io.IOException"""
        super(ServerWorld, self).load()

    @overload
    def isLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.isLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_ServerWorld, self).isLoaded(arg0))

    @override
    @overload
    def setSpawnPoint(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.world.World.setSpawnPoint(int,int)"""
        super(_World, self).setSpawnPoint(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def intersectEntities(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.world.World.intersectEntities(dev.ultreon.quantum.util.BoundingBox)"""
        return bool._wrap(super(_World, self).intersectEntities(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.ServerWorld.dispose()"""
        super(ServerWorld, self).dispose()

    @overload
    def entitiesWithinDst(self, arg0: 'Entity', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.entitiesWithinDst(dev.ultreon.quantum.entity.Entity,int)"""
        return 'List'._wrap(super(_World, self).entitiesWithinDst(arg0, _int.valueOf(arg1)))

    @overload
    def refreshChunks(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.world.ServerWorld.refreshChunks(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_ServerWorld, self).refreshChunks(arg0)

    @overload
    def getChunk(self, arg0: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'._wrap(super(_ServerWorld, self).getChunk(arg0))

    @staticmethod
    @overload
    def toChunkPos(arg0: 'BlockPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(dev.ultreon.quantum.world.BlockPos)"""
        return ChunkPos._wrap(_World.toChunkPos(arg0))

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_World, self).setColumn(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def getSpawnPoint(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.ServerWorld.getSpawnPoint()"""
        return 'BlockPos'._wrap(super(ServerWorld, self).getSpawnPoint())

    @override
    @overload
    def updateNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).updateNeighbours(arg0)

    @overload
    def continueBreaking(self, arg0: 'BlockPos', arg1: float, arg2: 'Player') -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.ServerWorld.continueBreaking(dev.ultreon.quantum.world.BlockPos,float,dev.ultreon.quantum.entity.player.Player)"""
        return 'BreakResult'._wrap(super(_ServerWorld, self).continueBreaking(arg0, _float.valueOf(arg1), arg2))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float) -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def updateChunk(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunk(dev.ultreon.quantum.world.Chunk)"""
        super(_World, self).updateChunk(arg0)

    @overload
    def spawn(self, arg0: 'Entity') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.ServerWorld.spawn(T)"""
        return 'entity.Entity'._wrap(super(_ServerWorld, self).spawn(arg0))

    @overload
    def collideEntities(self, arg0: 'Entity', arg1: 'BoundingBox') -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.collideEntities(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.util.BoundingBox)"""
        return 'List'._wrap(super(_World, self).collideEntities(arg0, arg1))

    @overload
    def getBreakProgress(self, arg0: 'BlockPos') -> float:
        """public float dev.ultreon.quantum.world.World.getBreakProgress(dev.ultreon.quantum.world.BlockPos)"""
        return float._wrap(super(_World, self).getBreakProgress(arg0))

    @override
    @overload
    def startBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.startBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_World, self).startBreaking(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def sendAllTrackingExcept(self, arg0: int, arg1: int, arg2: int, arg3: 'Packet', arg4: 'ServerPlayer'):
        """public void dev.ultreon.quantum.world.ServerWorld.sendAllTrackingExcept(int,int,int,dev.ultreon.quantum.network.packets.Packet<? extends dev.ultreon.quantum.network.client.ClientPacketHandler>,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_ServerWorld, self).sendAllTrackingExcept(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4)

    @overload
    def regenerateChunk(self, arg0: 'ChunkPos'):
        """public void dev.ultreon.quantum.world.ServerWorld.regenerateChunk(dev.ultreon.quantum.world.ChunkPos)"""
        super(_ServerWorld, self).regenerateChunk(arg0)

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Predicate') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.util.function.Predicate<dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def getPlayersWithinRange(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.world.ServerWorld.getPlayersWithinRange(double,double,double,float)"""
        return 'List'._wrap(super(_ServerWorld, self).getPlayersWithinRange(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_World, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getTerrainGenerator(self) -> 'gen.TerrainGenerator':
        """public dev.ultreon.quantum.world.gen.TerrainGenerator dev.ultreon.quantum.world.ServerWorld.getTerrainGenerator()"""
        return 'gen.TerrainGenerator'._wrap(super(ServerWorld, self).getTerrainGenerator())

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_World, self).drop(arg0, arg1, arg2)

    @override
    @overload
    def closeMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.closeMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_World, self).closeMenu(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getTotalChunks(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getTotalChunks()"""
        return int._wrap(super(ServerWorld, self).getTotalChunks())

    @overload
    def saveRegion(self, arg0: 'Region', arg1: bool):
        """public void dev.ultreon.quantum.world.ServerWorld.saveRegion(dev.ultreon.quantum.world.ServerWorld$Region,boolean)"""
        super(_ServerWorld, self).saveRegion(arg0, _boolean.valueOf(arg1))

    @overload
    def unloadChunk(self, arg0: 'ChunkPos', arg1: bool) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.unloadChunk(dev.ultreon.quantum.world.ChunkPos,boolean)"""
        return bool._wrap(super(_ServerWorld, self).unloadChunk(arg0, _boolean.valueOf(arg1)))

    @overload
    def sendAllTracking(self, arg0: int, arg1: int, arg2: int, arg3: 'Packet'):
        """public void dev.ultreon.quantum.world.ServerWorld.sendAllTracking(int,int,int,dev.ultreon.quantum.network.packets.Packet<? extends dev.ultreon.quantum.network.client.ClientPacketHandler>)"""
        super(_ServerWorld, self).sendAllTracking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def rayCastEntity(self, arg0: 'Ray') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3i') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getRenderDistance()"""
        return int._wrap(super(ServerWorld, self).getRenderDistance())

    @overload
    def getStorage(self) -> 'WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.world.ServerWorld.getStorage()"""
        return 'WorldStorage'._wrap(super(ServerWorld, self).getStorage())

    @override
    @overload
    def isClientSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.isClientSide()"""
        return bool._wrap(super(ServerWorld, self).isClientSide())

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vector3') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(com.badlogic.gdx.math.Vector3)"""
        return ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @override
    @overload
    def getSeed(self) -> int:
        """public long dev.ultreon.quantum.world.World.getSeed()"""
        return int._wrap(super(World, self).getSeed())

    @overload
    def spawn(self, arg0: 'Entity', arg1: 'MapType') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.ServerWorld.spawn(T,dev.ultreon.ubo.types.MapType)"""
        return 'entity.Entity'._wrap(super(_ServerWorld, self).spawn(arg0, arg1))

    @overload
    def loadChunk(self, arg0: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld.loadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'._wrap(super(_ServerWorld, self).loadChunk(arg0))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: 'BlockPos') -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return BlockPos._wrap(_World.toLocalBlockPos(arg0))

    @overload
    def destroyBlock(self, arg0: 'BlockPos', arg1: 'Player') -> bool:
        """public boolean dev.ultreon.quantum.world.World.destroyBlock(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        return bool._wrap(super(_World, self).destroyBlock(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def stopBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.world.World.stopBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_World, self).stopBreaking(arg0, arg1)

    @overload
    def isOutOfWorldBounds(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(int,int,int)"""
        return bool._wrap(super(_World, self).isOutOfWorldBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def isOutOfWorldBounds(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(dev.ultreon.quantum.world.BlockPos)"""
        return bool._wrap(super(_World, self).isOutOfWorldBounds(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def recordOutOfBounds(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.ServerWorld.recordOutOfBounds(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_ServerWorld, self).recordOutOfBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def getChunksToLoad(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld.getChunksToLoad()"""
        return int._wrap(super(ServerWorld, self).getChunksToLoad())

    @staticmethod
    @overload
    def getChunkSaves() -> int:
        """public static long dev.ultreon.quantum.world.ServerWorld.getChunkSaves()"""
        return int._wrap(_ServerWorld.getChunkSaves())

    @override
    @overload
    def getLoadedChunks(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.world.ServerChunk> dev.ultreon.quantum.world.ServerWorld.getLoadedChunks()"""
        return 'Collection'._wrap(super(ServerWorld, self).getLoadedChunks())

    @overload
    def loadChunk(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld.loadChunk(int,int)"""
        return 'Chunk'._wrap(super(_ServerWorld, self).loadChunk(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getDimension(self) -> 'DimensionInfo':
        """public dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.World.getDimension()"""
        return 'DimensionInfo'._wrap(super(World, self).getDimension())

    @overload
    def setupSpawn(self):
        """public void dev.ultreon.quantum.world.ServerWorld.setupSpawn()"""
        super(ServerWorld, self).setupSpawn()

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3d') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @overload
    def loadChunk(self, arg0: int, arg1: int, arg2: bool) -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld.loadChunk(int,int,boolean)"""
        return 'ServerChunk'._wrap(super(_ServerWorld, self).loadChunk(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.World.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_World, self).getBlockEntity(arg0))

    @override
    @overload
    def setBlockEntity(self, arg0: 'BlockPos', arg1: 'BlockEntity'):
        """public void dev.ultreon.quantum.world.ServerWorld.setBlockEntity(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntity)"""
        super(_ServerWorld, self).setBlockEntity(arg0, arg1)

    @override
    @overload
    def despawn(self, arg0: int):
        """public void dev.ultreon.quantum.world.World.despawn(int)"""
        super(_World, self).despawn(_int.valueOf(arg0))

    @overload
    def isLoaded(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.isLoaded(dev.ultreon.quantum.world.BlockPos)"""
        return bool._wrap(super(_ServerWorld, self).isLoaded(arg0))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Class') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'._wrap(super(_World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def loadChunkNow(self, arg0: int, arg1: int) -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld.loadChunkNow(int,int)"""
        return 'Chunk'._wrap(super(_ServerWorld, self).loadChunkNow(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int) -> 'BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int)"""
        return BlockPos._wrap(_World.toLocalBlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def doRefresh(self, arg0: 'ChunkRefresher'):
        """public void dev.ultreon.quantum.world.ServerWorld.doRefresh(dev.ultreon.quantum.world.ChunkRefresher)"""
        super(_ServerWorld, self).doRefresh(arg0)

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.World.getHighest(int,int)"""
        return int._wrap(super(_World, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def spawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.world.ServerWorld.spawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(_ServerWorld, self).spawnParticles(arg0, arg1, arg2, _int.valueOf(arg3))

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.world.ServerWorld.getServer()"""
        return 'server.QuantumServer'._wrap(super(ServerWorld, self).getServer())

    @overload
    def saveAsync(self, arg0: bool) -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Boolean> dev.ultreon.quantum.world.ServerWorld.saveAsync(boolean)"""
        return 'CompletableFuture'._wrap(super(_ServerWorld, self).saveAsync(_boolean.valueOf(arg0)))

    @override
    @overload
    def getChunksLoaded(self) -> int:
        """public int dev.ultreon.quantum.world.World.getChunksLoaded()"""
        return int._wrap(super(World, self).getChunksLoaded())

    @overload
    def saveRegion(self, arg0: 'Region'):
        """public void dev.ultreon.quantum.world.ServerWorld.saveRegion(dev.ultreon.quantum.world.ServerWorld$Region)"""
        super(_ServerWorld, self).saveRegion(arg0)

    @override
    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.world.ServerWorld.playSound(dev.ultreon.quantum.world.SoundEvent,double,double,double)"""
        super(_ServerWorld, self).playSound(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @staticmethod
    @overload
    def toChunkVec(arg0: 'BlockPos') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(dev.ultreon.quantum.world.BlockPos)"""
        return vector.Vec2i._wrap(_World.toChunkVec(arg0))

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool._wrap(super(_World, self).set(arg0, arg1, _int.valueOf(arg2)))

    @overload
    def prepareSpawn(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.world.ServerWorld.prepareSpawn(dev.ultreon.quantum.entity.player.Player)"""
        super(_ServerWorld, self).prepareSpawn(arg0)

    @overload
    def refreshChunks(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.world.ServerWorld.refreshChunks(dev.ultreon.quantum.entity.player.Player)"""
        super(_ServerWorld, self).refreshChunks(arg0)

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: 'ChunkPos') -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return ChunkPos._wrap(_World.toLocalChunkPos(arg0))

    @overload
    def doRefreshNow(self, arg0: 'ChunkRefresher'):
        """public void dev.ultreon.quantum.world.ServerWorld.doRefreshNow(dev.ultreon.quantum.world.ChunkRefresher)"""
        super(_ServerWorld, self).doRefreshNow(arg0)

    @staticmethod
    @overload
    def toChunkPos(arg0: int, arg1: int, arg2: int) -> 'ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(int,int,int)"""
        return ChunkPos._wrap(_World.toChunkPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_World, self).openMenu(arg0)

    @staticmethod
    @overload
    def getChunkLoads() -> int:
        """public static long dev.ultreon.quantum.world.ServerWorld.getChunkLoads()"""
        return int._wrap(_ServerWorld.getChunkLoads())

    @overload
    def unloadChunk(self, arg0: 'ChunkPos', arg1: bool, arg2: bool) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.unloadChunk(dev.ultreon.quantum.world.ChunkPos,boolean,boolean)"""
        return bool._wrap(super(_ServerWorld, self).unloadChunk(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def sync(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.ServerWorld.sync(dev.ultreon.quantum.world.BlockPos)"""
        super(_ServerWorld, self).sync(arg0)

    @override
    @overload
    def fillCrashInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.world.World.fillCrashInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(_World, self).fillCrashInfo(arg0)

    @overload
    def getEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.world.World.getEntity(int)"""
        return 'entity.Entity'._wrap(super(_World, self).getEntity(_int.valueOf(arg0)))

    @overload
    def save(self, arg0: bool):
        """public synchronized void dev.ultreon.quantum.world.ServerWorld.save(boolean) throws java.io.IOException"""
        super(_ServerWorld, self).save(_boolean.valueOf(arg0))

    @overload
    def getBiome(self, arg0: 'BlockPos') -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.World.getBiome(dev.ultreon.quantum.world.BlockPos)"""
        return 'Biome'._wrap(super(_World, self).getBiome(arg0))

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.world.ServerWorld.tick()"""
        super(ServerWorld, self).tick()

    @staticmethod
    @overload
    def getChunkUnloads() -> int:
        """public static long dev.ultreon.quantum.world.ServerWorld.getChunkUnloads()"""
        return int._wrap(_ServerWorld.getChunkUnloads())

    @override
    @overload
    def getUID(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.world.World.getUID()"""
        return 'UUID'._wrap(super(World, self).getUID())

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_World, self).set(arg0, arg1))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int, arg3: 'Vec3i') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return vector.Vec3i._wrap(_World.toLocalBlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def refreshChunks(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.world.ServerWorld.refreshChunks(float,float)"""
        super(_ServerWorld, self).refreshChunks(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_World, self).drop(arg0, arg1)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_ServerWorld, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)) 
 
 
# CLASS: dev.ultreon.quantum.world.IllegalChunkStateException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import dev.ultreon.quantum.world.IllegalChunkStateException as _IllegalChunkStateException
_IllegalChunkStateException = _IllegalChunkStateException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IllegalChunkStateException():
    """dev.ultreon.quantum.world.IllegalChunkStateException"""
 
    @staticmethod
    def _wrap(java_value: _IllegalChunkStateException) -> 'IllegalChunkStateException':
        return IllegalChunkStateException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IllegalChunkStateException):
        """
        Dynamic initializer for IllegalChunkStateException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IllegalChunkStateException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IllegalChunkStateException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.world.IllegalChunkStateException(java.lang.String)"""
        val = _IllegalChunkStateException(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.UseResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UseResult():
    """dev.ultreon.quantum.world.UseResult"""
 
    @staticmethod
    def _wrap(java_value: _UseResult) -> 'UseResult':
        return UseResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UseResult):
        """
        Dynamic initializer for UseResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UseResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UseResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'UseResult':
        """public static dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.world.UseResult.valueOf(java.lang.String)"""
        return UseResult._wrap(_UseResult.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['UseResult']:
        """public static dev.ultreon.quantum.world.UseResult[] dev.ultreon.quantum.world.UseResult.values()"""
        return List[UseResult]._wrap(_UseResult.values())


UseResult.SKIP = UseResult._wrap(_SKIP.SKIP)

UseResult.DENY = UseResult._wrap(_DENY.DENY)

UseResult.ALLOW = UseResult._wrap(_ALLOW.ALLOW) 
 
 
# CLASS: dev.ultreon.quantum.world.RegionPos
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import dev.ultreon.quantum.world.RegionPos as _RegionPos
_RegionPos = _RegionPos
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegionPos():
    """dev.ultreon.quantum.world.RegionPos"""
 
    @staticmethod
    def _wrap(java_value: _RegionPos) -> 'RegionPos':
        return RegionPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegionPos):
        """
        Dynamic initializer for RegionPos.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegionPos__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegionPos__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.RegionPos.x()"""
        return int._wrap(super(RegionPos, self).x())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.RegionPos.equals(java.lang.Object)"""
        return bool._wrap(super(_RegionPos, self).equals(arg0))

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.RegionPos.z()"""
        return int._wrap(super(RegionPos, self).z())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.world.RegionPos(int,int)"""
        val = _RegionPos(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.RegionPos.toString()"""
        return str._wrap(super(RegionPos, self).toString())

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
        """public int dev.ultreon.quantum.world.RegionPos.hashCode()"""
        return int._wrap(super(RegionPos, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.Location
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.Location as _Location
_Location = _Location
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Location():
    """dev.ultreon.quantum.world.Location"""
 
    @staticmethod
    def _wrap(java_value: _Location) -> 'Location':
        return Location(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Location):
        """
        Dynamic initializer for Location.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Location__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Location__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.quantum.world.Location(dev.ultreon.quantum.world.ServerWorld,double,double,double)"""
        val = _Location(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))
        self.__wrapper = val

    @property
    def world(self, value: 'util.Identifier'):
        super(_Location).world(value)

    @overload
    def __init__(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.world.Location(dev.ultreon.quantum.util.Identifier,double,double,double,float,float)"""
        val = _Location(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.Location(double,double,double)"""
        val = _Location(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
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

    @overload
    def __init__(self, arg0: 'World', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.world.Location(dev.ultreon.quantum.world.World,double,double,double,float,float)"""
        val = _Location(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public dev.ultreon.quantum.world.Location(double,double,double,float,float)"""
        val = _Location(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))
        self.__wrapper = val

    @overload
    def cpy(self) -> 'Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.world.Location.cpy()"""
        return 'Location'._wrap(super(Location, self).cpy())

    @overload
    def getSeverWorld(self) -> 'ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.world.Location.getSeverWorld()"""
        return 'ServerWorld'._wrap(super(Location, self).getSeverWorld())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @property
    def world(self) -> Identifier:
        return Identifier._wrap(super(_Location).world())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBlockPos(self) -> 'BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.Location.getBlockPos()"""
        return 'BlockPos'._wrap(super(Location, self).getBlockPos())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.BreakResult
import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BreakResult():
    """dev.ultreon.quantum.world.BreakResult"""
 
    @staticmethod
    def _wrap(java_value: _BreakResult) -> 'BreakResult':
        return BreakResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BreakResult):
        """
        Dynamic initializer for BreakResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BreakResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BreakResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['BreakResult']:
        """public static dev.ultreon.quantum.world.BreakResult[] dev.ultreon.quantum.world.BreakResult.values()"""
        return List[BreakResult]._wrap(_BreakResult.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BreakResult':
        """public static dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.BreakResult.valueOf(java.lang.String)"""
        return BreakResult._wrap(_BreakResult.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


BreakResult.BROKEN = BreakResult._wrap(_BROKEN.BROKEN)

BreakResult.CONTINUE = BreakResult._wrap(_CONTINUE.CONTINUE)

BreakResult.FAILED = BreakResult._wrap(_FAILED.FAILED) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld$RecordedChange
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.ServerWorld as _ServerWorld_RecordedChange
_RecordedChange = _ServerWorld_RecordedChange.RecordedChange
from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class RecordedChange():
    """dev.ultreon.quantum.world.ServerWorld.RecordedChange"""
 
    @staticmethod
    def _wrap(java_value: _RecordedChange) -> 'RecordedChange':
        return RecordedChange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecordedChange):
        """
        Dynamic initializer for RecordedChange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecordedChange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecordedChange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def block(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.ServerWorld$RecordedChange.block()"""
        return 'state.BlockProperties'._wrap(super(RecordedChange, self).block())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public dev.ultreon.quantum.world.ServerWorld$RecordedChange(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        val = _RecordedChange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.x()"""
        return int._wrap(super(RecordedChange, self).x())

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.z()"""
        return int._wrap(super(RecordedChange, self).z())

    @overload
    def y(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.y()"""
        return int._wrap(super(RecordedChange, self).y())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.ServerWorld$RecordedChange.save()"""
        return 'types.MapType'._wrap(super(RecordedChange, self).save())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$RecordedChange.hashCode()"""
        return int._wrap(super(RecordedChange, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.ServerWorld$RecordedChange.toString()"""
        return str._wrap(super(RecordedChange, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$RecordedChange.equals(java.lang.Object)"""
        return bool._wrap(super(_RecordedChange, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.world.HeightMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.HeightMap as _HeightMap
_HeightMap = _HeightMap
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeightMap():
    """dev.ultreon.quantum.world.HeightMap"""
 
    @staticmethod
    def _wrap(java_value: _HeightMap) -> 'HeightMap':
        return HeightMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeightMap):
        """
        Dynamic initializer for HeightMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeightMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeightMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.HeightMap(int)"""
        val = _HeightMap(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.world.HeightMap.getWidth()"""
        return int._wrap(super(HeightMap, self).getWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int, arg1: int) -> int:
        """public short dev.ultreon.quantum.world.HeightMap.get(int,int)"""
        return int._wrap(super(_HeightMap, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def getMap(self) -> List[int]:
        """public short[] dev.ultreon.quantum.world.HeightMap.getMap()"""
        return List[int]._wrap(super(HeightMap, self).getMap())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def load(self, arg0: 'short'):
        """public void dev.ultreon.quantum.world.HeightMap.load(short[])"""
        super(_HeightMap, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def save(self) -> List[int]:
        """public short[] dev.ultreon.quantum.world.HeightMap.save()"""
        return List[int]._wrap(super(HeightMap, self).save())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.HeightMap.set(int,int,short)"""
        super(_HeightMap, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.Biome$Builder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import it.unimi.dsi.fastutil.longs.Long2ReferenceFunction as Long2ReferenceFunction
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.world.Biome as _Biome_Builder
_Builder = _Biome_Builder.Builder
try:
    from pyquantum.world.gen import layer
except ImportError:
    layer = _import_once("pyquantum.world.gen.layer")

import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.world.Biome.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def layer(self, arg0: 'TerrainLayer') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.layer(dev.ultreon.quantum.world.gen.layer.TerrainLayer)"""
        return 'Builder'._wrap(super(_Builder, self).layer(arg0))

    @overload
    def temperatureEnd(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.temperatureEnd(float)"""
        return 'Builder'._wrap(super(_Builder, self).temperatureEnd(_float.valueOf(arg0)))

    @overload
    def feature(self, arg0: 'WorldGenFeature') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.feature(dev.ultreon.quantum.world.gen.WorldGenFeature)"""
        return 'Builder'._wrap(super(_Builder, self).feature(arg0))

    @overload
    def doesNotGenerate(self) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.doesNotGenerate()"""
        return 'Builder'._wrap(super(Builder, self).doesNotGenerate())

    @overload
    def temperatureStart(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.temperatureStart(float)"""
        return 'Builder'._wrap(super(_Builder, self).temperatureStart(_float.valueOf(arg0)))

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
    def noise(self, arg0: 'NoiseConfig') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.noise(dev.ultreon.quantum.world.gen.noise.NoiseConfig)"""
        return 'Builder'._wrap(super(_Builder, self).noise(arg0))

    @overload
    def domainWarping(self, arg0: 'Long2ReferenceFunction') -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.domainWarping(it.unimi.dsi.fastutil.longs.Long2ReferenceFunction<dev.ultreon.quantum.world.gen.noise.DomainWarping>)"""
        return 'Builder'._wrap(super(_Builder, self).domainWarping(arg0))

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
    def ocean(self) -> 'Builder':
        """public dev.ultreon.quantum.world.Biome$Builder dev.ultreon.quantum.world.Biome$Builder.ocean()"""
        return 'Builder'._wrap(super(Builder, self).ocean())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def build(self) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Biome$Builder.build()"""
        return 'Biome'._wrap(super(Builder, self).build())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.WorldSaveInfo
from pyquantum_helper import import_once as _import_once
import dev.ultreon.libs.datetime.v0.DateTime as _DateTime
_DateTime = _DateTime
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.world.WorldSaveInfo as _WorldSaveInfo
_WorldSaveInfo = _WorldSaveInfo
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
try:
    from pycorelibs.datetime import v0
except ImportError:
    v0 = _import_once("pycorelibs.datetime.v0")

from builtins import bool
import dev.ultreon.quantum.util.GameMode as _GameMode
_GameMode = _GameMode
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class WorldSaveInfo():
    """dev.ultreon.quantum.world.WorldSaveInfo"""
 
    @staticmethod
    def _wrap(java_value: _WorldSaveInfo) -> 'WorldSaveInfo':
        return WorldSaveInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldSaveInfo):
        """
        Dynamic initializer for WorldSaveInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldSaveInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldSaveInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def lastSave(self) -> 'v0.DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.quantum.world.WorldSaveInfo.lastSave()"""
        return 'v0.DateTime'._wrap(super(WorldSaveInfo, self).lastSave())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldSaveInfo.equals(java.lang.Object)"""
        return bool._wrap(super(_WorldSaveInfo, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.WorldSaveInfo.name()"""
        return str._wrap(super(WorldSaveInfo, self).name())

    @overload
    def seed(self) -> int:
        """public long dev.ultreon.quantum.world.WorldSaveInfo.seed()"""
        return int._wrap(super(WorldSaveInfo, self).seed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def lastPlayedInMode(self) -> 'util.GameMode':
        """public dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.world.WorldSaveInfo.lastPlayedInMode()"""
        return 'util.GameMode'._wrap(super(WorldSaveInfo, self).lastPlayedInMode())

    @overload
    def setName(self, arg0: str):
        """public void dev.ultreon.quantum.world.WorldSaveInfo.setName(java.lang.String)"""
        super(_WorldSaveInfo, self).setName(arg0)

    @overload
    def gamemode(self) -> 'util.GameMode':
        """public dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.world.WorldSaveInfo.gamemode()"""
        return 'util.GameMode'._wrap(super(WorldSaveInfo, self).gamemode())

    @overload
    def generatorVersion(self) -> int:
        """public int dev.ultreon.quantum.world.WorldSaveInfo.generatorVersion()"""
        return int._wrap(super(WorldSaveInfo, self).generatorVersion())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.WorldSaveInfo.toString()"""
        return str._wrap(super(WorldSaveInfo, self).toString())

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
    def __init__(self, arg0: int, arg1: int, arg2: 'GameMode', arg3: 'GameMode', arg4: str, arg5: 'DateTime'):
        """public dev.ultreon.quantum.world.WorldSaveInfo(long,int,dev.ultreon.quantum.util.GameMode,dev.ultreon.quantum.util.GameMode,java.lang.String,dev.ultreon.libs.datetime.v0.DateTime)"""
        val = _WorldSaveInfo(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.WorldSaveInfo.hashCode()"""
        return int._wrap(super(WorldSaveInfo, self).hashCode())

    @overload
    def save(self, arg0: 'WorldStorage'):
        """public void dev.ultreon.quantum.world.WorldSaveInfo.save(dev.ultreon.quantum.world.WorldStorage) throws java.io.IOException"""
        super(_WorldSaveInfo, self).save(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def picture(self, arg0: 'WorldStorage') -> 'Optional':
        """public java.util.Optional<com.badlogic.gdx.graphics.Texture> dev.ultreon.quantum.world.WorldSaveInfo.picture(dev.ultreon.quantum.world.WorldStorage)"""
        return 'Optional'._wrap(super(_WorldSaveInfo, self).picture(arg0))

    @staticmethod
    @overload
    def fromMap(arg0: 'MapType') -> 'WorldSaveInfo':
        """public static dev.ultreon.quantum.world.WorldSaveInfo dev.ultreon.quantum.world.WorldSaveInfo.fromMap(dev.ultreon.ubo.types.MapType)"""
        return WorldSaveInfo._wrap(_WorldSaveInfo.fromMap(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.world.DimensionInfo
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
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
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import dev.ultreon.quantum.world.DimensionInfo as _DimensionInfo
_DimensionInfo = _DimensionInfo
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DimensionInfo():
    """dev.ultreon.quantum.world.DimensionInfo"""
 
    @staticmethod
    def _wrap(java_value: _DimensionInfo) -> 'DimensionInfo':
        return DimensionInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DimensionInfo):
        """
        Dynamic initializer for DimensionInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DimensionInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DimensionInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.DimensionInfo.getId()"""
        return 'util.Identifier'._wrap(super(DimensionInfo, self).getId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.DimensionInfo.equals(java.lang.Object)"""
        return bool._wrap(super(_DimensionInfo, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.DimensionInfo.hashCode()"""
        return int._wrap(super(DimensionInfo, self).hashCode())

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
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.world.DimensionInfo(dev.ultreon.quantum.util.Identifier)"""
        val = _DimensionInfo(arg0)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.world.DimensionInfo.getName()"""
        return 'text.TextObject'._wrap(super(DimensionInfo, self).getName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())


DimensionInfo.OVERWORLD = DimensionInfo._wrap(_OVERWORLD.OVERWORLD) 
 
 
# CLASS: dev.ultreon.quantum.world.ChunkRefresher
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.world.ChunkRefresher as _ChunkRefresher
_ChunkRefresher = _ChunkRefresher
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChunkRefresher():
    """dev.ultreon.quantum.world.ChunkRefresher"""
 
    @staticmethod
    def _wrap(java_value: _ChunkRefresher) -> 'ChunkRefresher':
        return ChunkRefresher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkRefresher):
        """
        Dynamic initializer for ChunkRefresher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkRefresher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkRefresher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addUnloading(self, arg0: 'Collection'):
        """public void dev.ultreon.quantum.world.ChunkRefresher.addUnloading(java.util.Collection<dev.ultreon.quantum.world.ChunkPos>)"""
        super(_ChunkRefresher, self).addUnloading(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.ChunkRefresher()"""
        val = _ChunkRefresher()
        self.__wrapper = val

    @overload
    def addLoading(self, arg0: 'Collection'):
        """public void dev.ultreon.quantum.world.ChunkRefresher.addLoading(java.util.Collection<dev.ultreon.quantum.world.ChunkPos>)"""
        super(_ChunkRefresher, self).addLoading(arg0)

    @overload
    def freeze(self):
        """public void dev.ultreon.quantum.world.ChunkRefresher.freeze()"""
        super(ChunkRefresher, self).freeze()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isFrozen(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ChunkRefresher.isFrozen()"""
        return bool._wrap(super(ChunkRefresher, self).isFrozen())

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
    def __init__(self):
        """public dev.ultreon.quantum.world.ChunkRefresher()"""
        val = _ChunkRefresher()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.world.Chunk
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
import java.util.Collection as Collection
try:
    from pyquantum import collection
except ImportError:
    collection = _import_once("pyquantum.collection")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
import dev.ultreon.quantum.world.gen.TreeData as _TreeData
_TreeData = _TreeData
from builtins import bool
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.util.Collection as _Collection
_Collection = _Collection
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.World as _World
_World = _World
import java.util.Map as Map
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class Chunk():
    """dev.ultreon.quantum.world.Chunk"""
 
    @staticmethod
    def _wrap(java_value: _Chunk) -> 'Chunk':
        return Chunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Chunk):
        """
        Dynamic initializer for Chunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Chunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Chunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(_Chunk, self).removeBlockEntity(arg0)

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_Chunk, self).getSunlight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool._wrap(super(Chunk, self).isReady())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Chunk, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int._wrap(super(_Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getPos(self) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'ChunkPos'._wrap(super(Chunk, self).getPos())

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_Chunk, self).getBlockLight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(_Chunk, self).setTreeData(arg0)

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(_Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties._wrap(_Chunk.loadBlock(arg0))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int)"""
        return int._wrap(super(_Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'Biome'._wrap(super(_Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Chunk, self).setFast(arg0, arg1)

    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.Chunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Chunk, self).set(arg0, arg1)

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Chunk, self).setFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(arg0))

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Chunk, self).getSunlight(arg0))

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).getFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Chunk, self).getBlockLight(arg0))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(arg0))

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(arg0))

    @overload
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'._wrap(super(_Chunk, self).getBlockEntity(arg0))

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int._wrap(super(_Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.Chunk.dispose()"""
        super(Chunk, self).dispose()

    @overload
    def getWorld(self) -> 'World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.world.Chunk.getWorld()"""
        return 'World'._wrap(super(Chunk, self).getWorld())

    @property
    def storage(self) -> Storage:
        return Storage._wrap(super(_Chunk).storage())

    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool._wrap(super(Chunk, self).isActive())

    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(_Chunk, self).startBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str._wrap(super(Chunk, self).toString())

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block._wrap(_Chunk.decodeBlock(arg0))

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).getFast(arg0))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'BreakResult'._wrap(super(_Chunk, self).continueBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'._wrap(super(Chunk, self).getBreaking())

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int._wrap(super(_Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'._wrap(super(Chunk, self).getBlockEntities())

    @property
    def treeData(self) -> TreeData:
        return TreeData._wrap(super(_Chunk).treeData())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_Chunk, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int._wrap(super(Chunk, self).hashCode())

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'._wrap(super(Chunk, self).getOffset())

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'Biome'._wrap(super(_Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool._wrap(super(Chunk, self).isDisposed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool._wrap(super(_Chunk, self).equals(arg0))

    @property
    def biomeStorage(self) -> Storage:
        return Storage._wrap(super(_Chunk).biomeStorage())

    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(_Chunk, self).stopBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float._wrap(super(_Chunk, self).getBrightness(_int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.quantum.world.ChunkAccess
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.ChunkAccess as _ChunkAccess
_ChunkAccess = _ChunkAccess
from abc import abstractmethod, ABC
 
class ChunkAccess():
    """dev.ultreon.quantum.world.ChunkAccess"""
 
    @staticmethod
    def _wrap(java_value: _ChunkAccess) -> 'ChunkAccess':
        return ChunkAccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkAccess):
        """
        Dynamic initializer for ChunkAccess.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkAccess__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkAccess__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.LightMap as _LightMap
_LightMap = _LightMap
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LightMap():
    """dev.ultreon.quantum.world.LightMap"""
 
    @staticmethod
    def _wrap(java_value: _LightMap) -> 'LightMap':
        return LightMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LightMap):
        """
        Dynamic initializer for LightMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LightMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LightMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.LightMap.getBlockLight(int,int,int)"""
        return int._wrap(super(_LightMap, self).getBlockLight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.world.LightMap.getData()"""
        return List[int]._wrap(super(LightMap, self).getData())

    @overload
    def setBlockLight(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.world.LightMap.setBlockLight(int,int,int,int)"""
        super(_LightMap, self).setBlockLight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.LightMap.getSunlight(int,int,int)"""
        return int._wrap(super(_LightMap, self).getSunlight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.LightMap(int)"""
        val = _LightMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bytes):
        """public dev.ultreon.quantum.world.LightMap(byte[])"""
        val = _LightMap(bytes)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def load(self, arg0: bytes):
        """public void dev.ultreon.quantum.world.LightMap.load(byte[])"""
        super(_LightMap, self).load(bytes)

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
    def setSunlight(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.world.LightMap.setSunlight(int,int,int,int)"""
        super(_LightMap, self).setSunlight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def save(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.world.LightMap.save()"""
        return List[int]._wrap(super(LightMap, self).save())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.ServerWorld$Region
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.ServerChunk as _ServerChunk
_ServerChunk = _ServerChunk
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
import dev.ultreon.quantum.world.RegionPos as _RegionPos
_RegionPos = _RegionPos
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld_Region
_Region = _ServerWorld_Region.Region
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Region():
    """dev.ultreon.quantum.world.ServerWorld.Region"""
 
    @staticmethod
    def _wrap(java_value: _Region) -> 'Region':
        return Region(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Region):
        """
        Dynamic initializer for Region.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Region__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Region__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def activate(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.activate(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'._wrap(super(_Region, self).activate(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def deactivate(self, arg0: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.deactivate(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'._wrap(super(_Region, self).deactivate(arg0))

    @overload
    def isDirty(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$Region.isDirty()"""
        return bool._wrap(super(Region, self).isDirty())

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
    def __init__(self, arg0: 'ServerWorld', arg1: 'RegionPos'):
        """public dev.ultreon.quantum.world.ServerWorld$Region(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.RegionPos)"""
        val = _Region(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ServerWorld', arg1: 'RegionPos', arg2: 'Map'):
        """public dev.ultreon.quantum.world.ServerWorld$Region(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.RegionPos,java.util.Map<dev.ultreon.quantum.world.ChunkPos, dev.ultreon.quantum.world.ServerChunk>)"""
        val = _Region(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def openChunkNow(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.openChunkNow(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'._wrap(super(_Region, self).openChunkNow(arg0, arg1))

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$Region.isEmpty()"""
        return bool._wrap(super(Region, self).isEmpty())

    @overload
    def openChunk(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.openChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'._wrap(super(_Region, self).openChunk(arg0, arg1))

    @overload
    def getActiveChunks(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.ServerWorld$Region.getActiveChunks()"""
        return 'Set'._wrap(super(Region, self).getActiveChunks())

    @overload
    def putChunk(self, arg0: 'ChunkPos', arg1: 'ServerChunk') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.putChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ServerChunk)"""
        return 'Chunk'._wrap(super(_Region, self).putChunk(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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
    def getChunk(self, arg0: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'._wrap(super(_Region, self).getChunk(arg0))

    @overload
    def writeUnlock(self):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.writeUnlock()"""
        super(Region, self).writeUnlock()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPos(self) -> 'RegionPos':
        """public dev.ultreon.quantum.world.RegionPos dev.ultreon.quantum.world.ServerWorld$Region.getPos()"""
        return 'RegionPos'._wrap(super(Region, self).getPos())

    @overload
    def hasActiveChunks(self) -> bool:
        """public boolean dev.ultreon.quantum.world.ServerWorld$Region.hasActiveChunks()"""
        return bool._wrap(super(Region, self).hasActiveChunks())

    @overload
    def generateChunk(self, arg0: 'ChunkPos', arg1: 'ChunkPos'):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.generateChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        super(_Region, self).generateChunk(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def pos(self) -> 'RegionPos':
        """public dev.ultreon.quantum.world.RegionPos dev.ultreon.quantum.world.ServerWorld$Region.pos()"""
        return 'RegionPos'._wrap(super(Region, self).pos())

    @overload
    def writeLock(self):
        """public void dev.ultreon.quantum.world.ServerWorld$Region.writeLock()"""
        super(Region, self).writeLock()

    @overload
    def generateChunkNow(self, arg0: 'ChunkPos', arg1: 'ChunkPos') -> 'ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.world.ServerWorld$Region.generateChunkNow(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.ChunkPos)"""
        return 'ServerChunk'._wrap(super(_Region, self).generateChunkNow(arg0, arg1))

    @overload
    def getChunkCount(self) -> int:
        """public int dev.ultreon.quantum.world.ServerWorld$Region.getChunkCount()"""
        return int._wrap(super(Region, self).getChunkCount())

    @overload
    def trySet(self, arg0: 'Supplier') -> 'util.Result':
        """public <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.world.ServerWorld$Region.trySet(com.google.common.base.Supplier<T>)"""
        return 'util.Result'._wrap(super(_Region, self).trySet(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getActiveChunk(self, arg0: 'ChunkPos') -> 'Chunk':
        """public dev.ultreon.quantum.world.Chunk dev.ultreon.quantum.world.ServerWorld$Region.getActiveChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Chunk'._wrap(super(_Region, self).getActiveChunk(arg0))

    @overload
    def getChunks(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.world.ServerChunk> dev.ultreon.quantum.world.ServerWorld$Region.getChunks()"""
        return 'Collection'._wrap(super(Region, self).getChunks())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.SeededSupplier
from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.SeededSupplier as _SeededSupplier
_SeededSupplier = _SeededSupplier
 
class SeededSupplier():
    """dev.ultreon.quantum.world.SeededSupplier"""
 
    @staticmethod
    def _wrap(java_value: _SeededSupplier) -> 'SeededSupplier':
        return SeededSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SeededSupplier):
        """
        Dynamic initializer for SeededSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SeededSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SeededSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, arg0: int):
        """public abstract T dev.ultreon.quantum.world.SeededSupplier.get(long)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.world.WorldStorage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import dev.ultreon.quantum.world.WorldSaveInfo as _WorldSaveInfo
_WorldSaveInfo = _WorldSaveInfo
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldStorage():
    """dev.ultreon.quantum.world.WorldStorage"""
 
    @staticmethod
    def _wrap(java_value: _WorldStorage) -> 'WorldStorage':
        return WorldStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldStorage):
        """
        Dynamic initializer for WorldStorage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldStorage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldStorage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createWorld(self):
        """public void dev.ultreon.quantum.world.WorldStorage.createWorld() throws java.io.IOException"""
        super(WorldStorage, self).createWorld()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def regionExists(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.regionExists(int,int) throws java.io.IOException"""
        return bool._wrap(super(_WorldStorage, self).regionExists(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.world.WorldStorage(java.lang.String)"""
        val = _WorldStorage(arg0)
        self.__wrapper = val

    @overload
    def exists(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.exists(java.lang.String)"""
        return bool._wrap(super(_WorldStorage, self).exists(arg0))

    @overload
    def regionFile(self, arg0: int, arg1: int) -> 'File':
        """public java.io.File dev.ultreon.quantum.world.WorldStorage.regionFile(int,int)"""
        return 'File'._wrap(super(_WorldStorage, self).regionFile(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def hasInfo(self) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.hasInfo()"""
        return bool._wrap(super(WorldStorage, self).hasInfo())

    @overload
    def loadInfo(self) -> 'WorldSaveInfo':
        """public dev.ultreon.quantum.world.WorldSaveInfo dev.ultreon.quantum.world.WorldStorage.loadInfo()"""
        return 'WorldSaveInfo'._wrap(super(WorldStorage, self).loadInfo())

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
    def read(self, arg0: str, *arg1: 'types.DataType') -> 'types.DataType':
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.quantum.world.WorldStorage.read(java.lang.String,T...) throws java.io.IOException"""
        return 'types.DataType'._wrap(super(_WorldStorage, self).read(arg0, arg1))

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.WorldStorage.getName()"""
        return str._wrap(super(WorldStorage, self).getName())

    @overload
    def createDir(self, arg0: str):
        """public void dev.ultreon.quantum.world.WorldStorage.createDir(java.lang.String) throws java.io.IOException"""
        super(_WorldStorage, self).createDir(arg0)

    @overload
    def write(self, arg0: 'DataType', arg1: str):
        """public void dev.ultreon.quantum.world.WorldStorage.write(dev.ultreon.ubo.types.DataType<?>,java.lang.String) throws java.io.IOException"""
        super(_WorldStorage, self).write(arg0, arg1)

    @overload
    def saveInfo(self, arg0: 'WorldSaveInfo'):
        """public void dev.ultreon.quantum.world.WorldStorage.saveInfo(dev.ultreon.quantum.world.WorldSaveInfo) throws java.io.IOException"""
        super(_WorldStorage, self).saveInfo(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def hashSHA256(arg0: bytes) -> List[int]:
        """public static byte[] dev.ultreon.quantum.world.WorldStorage.hashSHA256(byte[])"""
        return List[int]._wrap(_WorldStorage.hashSHA256(bytes))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getDirectory(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.world.WorldStorage.getDirectory()"""
        return 'Path'._wrap(super(WorldStorage, self).getDirectory())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Path'):
        """public dev.ultreon.quantum.world.WorldStorage(java.nio.file.Path)"""
        val = _WorldStorage(arg0)
        self.__wrapper = val

    @overload
    def getSHA256Name(self) -> str:
        """public <V,K> java.lang.String dev.ultreon.quantum.world.WorldStorage.getSHA256Name()"""
        return str._wrap(super(WorldStorage, self).getSHA256Name())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def regionFile(self, arg0: 'RegionPos') -> 'File':
        """public java.io.File dev.ultreon.quantum.world.WorldStorage.regionFile(dev.ultreon.quantum.world.RegionPos)"""
        return 'File'._wrap(super(_WorldStorage, self).regionFile(arg0))

    @overload
    def __init__(self, arg0: 'File'):
        """public dev.ultreon.quantum.world.WorldStorage(java.io.File)"""
        val = _WorldStorage(arg0)
        self.__wrapper = val

    @overload
    def delete(self) -> bool:
        """public boolean dev.ultreon.quantum.world.WorldStorage.delete() throws java.io.IOException"""
        return bool._wrap(super(WorldStorage, self).delete())

    @staticmethod
    @overload
    def createFolderName() -> str:
        """public static <V,K> java.lang.String dev.ultreon.quantum.world.WorldStorage.createFolderName()"""
        return str._wrap(_WorldStorage.createFolderName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.ChunkPos
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.libs.commons.v0.vector.Vec2d as _Vec2d
_Vec2d = _Vec2d
from builtins import type
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.world.RegionPos as _RegionPos
_RegionPos = _RegionPos
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.lang.Class as _Class
_Class = _Class
 
class ChunkPos():
    """dev.ultreon.quantum.world.ChunkPos"""
 
    @staticmethod
    def _wrap(java_value: _ChunkPos) -> 'ChunkPos':
        return ChunkPos(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkPos):
        """
        Dynamic initializer for ChunkPos.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkPos__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkPos__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.ChunkPos.toString()"""
        return str._wrap(super(ChunkPos, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def compareTo(self, arg0: 'ChunkPos') -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.compareTo(dev.ultreon.quantum.world.ChunkPos)"""
        return int._wrap(super(_ChunkPos, self).compareTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getChunkOrigin(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.world.ChunkPos.getChunkOrigin()"""
        return 'vector.Vec3d'._wrap(super(ChunkPos, self).getChunkOrigin())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def x(self) -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.x()"""
        return int._wrap(super(ChunkPos, self).x())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def vec(self) -> 'vector.Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.quantum.world.ChunkPos.vec()"""
        return 'vector.Vec2d'._wrap(super(ChunkPos, self).vec())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.hashCode()"""
        return int._wrap(super(ChunkPos, self).hashCode())

    @staticmethod
    @overload
    def parse(arg0: str) -> 'RegionPos':
        """public static dev.ultreon.quantum.world.RegionPos dev.ultreon.quantum.world.ChunkPos.parse(java.lang.String)"""
        return RegionPos._wrap(_ChunkPos.parse(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def offset(self, arg0: int, arg1: int) -> 'ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.ChunkPos.offset(int,int)"""
        return 'ChunkPos'._wrap(super(_ChunkPos, self).offset(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.world.ChunkPos(int,int)"""
        val = _ChunkPos(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.ChunkPos.equals(java.lang.Object)"""
        return bool._wrap(super(_ChunkPos, self).equals(arg0))

    @overload
    def z(self) -> int:
        """public int dev.ultreon.quantum.world.ChunkPos.z()"""
        return int._wrap(super(ChunkPos, self).z()) 
 
 
# CLASS: dev.ultreon.quantum.world.BlockFlags
from builtins import str
import dev.ultreon.quantum.world.BlockFlags as _BlockFlags
_BlockFlags = _BlockFlags
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockFlags():
    """dev.ultreon.quantum.world.BlockFlags"""
 
    @staticmethod
    def _wrap(java_value: _BlockFlags) -> 'BlockFlags':
        return BlockFlags(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockFlags):
        """
        Dynamic initializer for BlockFlags.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockFlags__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockFlags__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.BlockFlags()"""
        val = _BlockFlags()
        self.__wrapper = val

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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.BlockFlags()"""
        val = _BlockFlags()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())