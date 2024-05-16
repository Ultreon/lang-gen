from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import dev.ultreon.quantum.entity.ai.PathPoint as __PathPoint
__PathPoint = __PathPoint
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.entity.ai.Path as __Path
__Path = __Path
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Path():
    """dev.ultreon.quantum.entity.ai.Path"""
 
    @staticmethod
    def __wrap(java_value: __Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Path):
        """
        Dynamic initializer for Path.
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
        """public int dev.ultreon.quantum.entity.ai.Path.hashCode()"""
        return int.__wrap(super(Path, self).hashCode())

    @overload
    def points(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d> dev.ultreon.quantum.entity.ai.Path.points()"""
        return 'List'.__wrap(super(Path, self).points())

    @overload
    def start(self) -> 'PathPoint':
        """public dev.ultreon.quantum.entity.ai.PathPoint dev.ultreon.quantum.entity.ai.Path.start()"""
        return 'PathPoint'.__wrap(super(Path, self).start())

    @overload
    def __init__(self, arg0: 'List', arg1: 'PathPoint', arg2: 'Vec3d'):
        """public dev.ultreon.quantum.entity.ai.Path(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d>,dev.ultreon.quantum.entity.ai.PathPoint,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __Path(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.equals(java.lang.Object)"""
        return bool.__wrap(super(__Path, self).equals(arg0))

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
    def isDone(self, arg0: 'PathPoint') -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.isDone(dev.ultreon.quantum.entity.ai.PathPoint)"""
        return bool.__wrap(super(__Path, self).isDone(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.ai.Path.toString()"""
        return str.__wrap(super(Path, self).toString())

    @overload
    def end(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.Path.end()"""
        return 'vector.Vec3d'.__wrap(super(Path, self).end())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.Path
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import dev.ultreon.quantum.entity.ai.PathPoint as __PathPoint
__PathPoint = __PathPoint
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.entity.ai.Path as __Path
__Path = __Path
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Path():
    """dev.ultreon.quantum.entity.ai.Path"""
 
    @staticmethod
    def __wrap(java_value: __Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Path):
        """
        Dynamic initializer for Path.
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
        """public int dev.ultreon.quantum.entity.ai.Path.hashCode()"""
        return int.__wrap(super(Path, self).hashCode())

    @overload
    def points(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d> dev.ultreon.quantum.entity.ai.Path.points()"""
        return 'List'.__wrap(super(Path, self).points())

    @overload
    def start(self) -> 'PathPoint':
        """public dev.ultreon.quantum.entity.ai.PathPoint dev.ultreon.quantum.entity.ai.Path.start()"""
        return 'PathPoint'.__wrap(super(Path, self).start())

    @overload
    def __init__(self, arg0: 'List', arg1: 'PathPoint', arg2: 'Vec3d'):
        """public dev.ultreon.quantum.entity.ai.Path(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d>,dev.ultreon.quantum.entity.ai.PathPoint,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __Path(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.equals(java.lang.Object)"""
        return bool.__wrap(super(__Path, self).equals(arg0))

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
    def isDone(self, arg0: 'PathPoint') -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Path.isDone(dev.ultreon.quantum.entity.ai.PathPoint)"""
        return bool.__wrap(super(__Path, self).isDone(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.ai.Path.toString()"""
        return str.__wrap(super(Path, self).toString())

    @overload
    def end(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.Path.end()"""
        return 'vector.Vec3d'.__wrap(super(Path, self).end())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.Path 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.Navigator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.entity.ai.Navigator as __Navigator
__Navigator = __Navigator
from builtins import int
 
class Navigator():
    """dev.ultreon.quantum.entity.ai.Navigator"""
 
    @staticmethod
    def __wrap(java_value: __Navigator) -> 'Navigator':
        return Navigator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Navigator):
        """
        Dynamic initializer for Navigator.
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
    def stop(self):
        """public void dev.ultreon.quantum.entity.ai.Navigator.stop()"""
        super(Navigator, self).stop()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.ai.Navigator.tick()"""
        super(Navigator, self).tick()

    @overload
    def setPath(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.entity.ai.Navigator.setPath(dev.ultreon.quantum.entity.ai.Path)"""
        super(__Navigator, self).setPath(arg0)

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
    def __init__(self, arg0: 'LivingEntity'):
        """public dev.ultreon.quantum.entity.ai.Navigator(dev.ultreon.quantum.entity.LivingEntity)"""
        val = __Navigator(arg0)
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
    def randomPath(self, arg0: 'RNG'):
        """public void dev.ultreon.quantum.entity.ai.Navigator.randomPath(dev.ultreon.quantum.world.rng.RNG)"""
        super(__Navigator, self).randomPath(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def hasPath(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.Navigator.hasPath()"""
        return bool.__wrap(super(Navigator, self).hasPath()) 
 
 
# CLASS: dev.ultreon.quantum.entity.ai.PathPoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import dev.ultreon.quantum.entity.ai.PathPoint as __PathPoint
__PathPoint = __PathPoint
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

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
 
class PathPoint():
    """dev.ultreon.quantum.entity.ai.PathPoint"""
 
    @staticmethod
    def __wrap(java_value: __PathPoint) -> 'PathPoint':
        return PathPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathPoint):
        """
        Dynamic initializer for PathPoint.
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
        """public java.lang.String dev.ultreon.quantum.entity.ai.PathPoint.toString()"""
        return str.__wrap(super(PathPoint, self).toString())

    @overload
    def look(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.PathPoint.look()"""
        return 'vector.Vec3d'.__wrap(super(PathPoint, self).look())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Vec3d', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public dev.ultreon.quantum.entity.ai.PathPoint(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __PathPoint(arg0, arg1, arg2)
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.ai.PathPoint.equals(java.lang.Object)"""
        return bool.__wrap(super(__PathPoint, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def position(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.PathPoint.position()"""
        return 'vector.Vec3d'.__wrap(super(PathPoint, self).position())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.ai.PathPoint.hashCode()"""
        return int.__wrap(super(PathPoint, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def motion(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.ai.PathPoint.motion()"""
        return 'vector.Vec3d'.__wrap(super(PathPoint, self).motion())