from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.entity.ai.Path as _Path
_Path = _Path
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

import java.util.List as _List
_List = _List
import dev.ultreon.quantum.entity.ai.PathPoint as _PathPoint
_PathPoint = _PathPoint
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Path():
    """dev.ultreon.quantum.entity.ai.Path"""
 
    @staticmethod
    def _wrap(java_value: _Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Path):
        """
        Dynamic initializer for Path.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Path__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Path__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'List', arg1: 'PathPoint', arg2: 'Vec3d'):
        """public dev.ultreon.quantum.entity.ai.Path(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d>,dev.ultreon.quantum.entity.ai.PathPoint,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _Path(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def points(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d> dev.ultreon.quantum.entity.ai.Path.points()"""
        return 'List'._wrap(super(Path, self).points())

    @overload
    def end(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.Path.end()"""
        return 'vector.Vec3d'._wrap(super(Path, self).end())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.equals(java.lang.Object)"""
        return bool._wrap(super(_Path, self).equals(arg0))

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.ai.Path.toString()"""
        return str._wrap(super(Path, self).toString())

    @overload
    def start(self) -> 'PathPoint':
        """public dev.ultreon.quantum.entity.ai.PathPoint dev.ultreon.quantum.entity.ai.Path.start()"""
        return 'PathPoint'._wrap(super(Path, self).start())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.ai.Path.hashCode()"""
        return int._wrap(super(Path, self).hashCode())

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
    def isDone(self, arg0: 'PathPoint') -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.isDone(dev.ultreon.quantum.entity.ai.PathPoint)"""
        return bool._wrap(super(_Path, self).isDone(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.Path
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.entity.ai.Path as _Path
_Path = _Path
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

import java.util.List as _List
_List = _List
import dev.ultreon.quantum.entity.ai.PathPoint as _PathPoint
_PathPoint = _PathPoint
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Path():
    """dev.ultreon.quantum.entity.ai.Path"""
 
    @staticmethod
    def _wrap(java_value: _Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Path):
        """
        Dynamic initializer for Path.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Path__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Path__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'List', arg1: 'PathPoint', arg2: 'Vec3d'):
        """public dev.ultreon.quantum.entity.ai.Path(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d>,dev.ultreon.quantum.entity.ai.PathPoint,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _Path(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def points(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d> dev.ultreon.quantum.entity.ai.Path.points()"""
        return 'List'._wrap(super(Path, self).points())

    @overload
    def end(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.Path.end()"""
        return 'vector.Vec3d'._wrap(super(Path, self).end())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.equals(java.lang.Object)"""
        return bool._wrap(super(_Path, self).equals(arg0))

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.ai.Path.toString()"""
        return str._wrap(super(Path, self).toString())

    @overload
    def start(self) -> 'PathPoint':
        """public dev.ultreon.quantum.entity.ai.PathPoint dev.ultreon.quantum.entity.ai.Path.start()"""
        return 'PathPoint'._wrap(super(Path, self).start())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.ai.Path.hashCode()"""
        return int._wrap(super(Path, self).hashCode())

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
    def isDone(self, arg0: 'PathPoint') -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.isDone(dev.ultreon.quantum.entity.ai.PathPoint)"""
        return bool._wrap(super(_Path, self).isDone(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.Path 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.Navigator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.entity.ai.Navigator as _Navigator
_Navigator = _Navigator
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Navigator():
    """dev.ultreon.quantum.entity.ai.Navigator"""
 
    @staticmethod
    def _wrap(java_value: _Navigator) -> 'Navigator':
        return Navigator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Navigator):
        """
        Dynamic initializer for Navigator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Navigator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Navigator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stop(self):
        """public void dev.ultreon.quantum.entity.ai.Navigator.stop()"""
        super(Navigator, self).stop()

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
    def tick(self):
        """public void dev.ultreon.quantum.entity.ai.Navigator.tick()"""
        super(Navigator, self).tick()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setPath(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.entity.ai.Navigator.setPath(dev.ultreon.quantum.entity.ai.Path)"""
        super(_Navigator, self).setPath(arg0)

    @overload
    def randomPath(self, arg0: 'RNG'):
        """public void dev.ultreon.quantum.entity.ai.Navigator.randomPath(dev.ultreon.quantum.world.rng.RNG)"""
        super(_Navigator, self).randomPath(arg0)

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
    def hasPath(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Navigator.hasPath()"""
        return bool._wrap(super(Navigator, self).hasPath())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'LivingEntity'):
        """public dev.ultreon.quantum.entity.ai.Navigator(dev.ultreon.quantum.entity.LivingEntity)"""
        val = _Navigator(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.entity.ai.PathPoint
from pyquantum_helper import import_once as _import_once
from builtins import str
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

import dev.ultreon.quantum.entity.ai.PathPoint as _PathPoint
_PathPoint = _PathPoint
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.lang.Class as _Class
_Class = _Class
 
class PathPoint():
    """dev.ultreon.quantum.entity.ai.PathPoint"""
 
    @staticmethod
    def _wrap(java_value: _PathPoint) -> 'PathPoint':
        return PathPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathPoint):
        """
        Dynamic initializer for PathPoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathPoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathPoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Vec3d', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public dev.ultreon.quantum.entity.ai.PathPoint(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _PathPoint(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def motion(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.PathPoint.motion()"""
        return 'vector.Vec3d'._wrap(super(PathPoint, self).motion())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.ai.PathPoint.hashCode()"""
        return int._wrap(super(PathPoint, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def position(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.PathPoint.position()"""
        return 'vector.Vec3d'._wrap(super(PathPoint, self).position())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def look(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.PathPoint.look()"""
        return 'vector.Vec3d'._wrap(super(PathPoint, self).look())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.PathPoint.equals(java.lang.Object)"""
        return bool._wrap(super(_PathPoint, self).equals(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.ai.PathPoint.toString()"""
        return str._wrap(super(PathPoint, self).toString())