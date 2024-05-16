from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
import dev.ultreon.quantum.world.gen.layer.AirTerrainLayer as __AirTerrainLayer
__AirTerrainLayer = __AirTerrainLayer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AirTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.AirTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __AirTerrainLayer) -> 'AirTerrainLayer':
        return AirTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AirTerrainLayer):
        """
        Dynamic initializer for AirTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = __AirTerrainLayer()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = __AirTerrainLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.AirTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__AirTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.AirTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
import dev.ultreon.quantum.world.gen.layer.AirTerrainLayer as __AirTerrainLayer
__AirTerrainLayer = __AirTerrainLayer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AirTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.AirTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __AirTerrainLayer) -> 'AirTerrainLayer':
        return AirTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AirTerrainLayer):
        """
        Dynamic initializer for AirTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = __AirTerrainLayer()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = __AirTerrainLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.AirTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__AirTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.AirTerrainLayer 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer as __VoidGuardTerrainLayer
__VoidGuardTerrainLayer = __VoidGuardTerrainLayer
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
from builtins import int
 
class VoidGuardTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __VoidGuardTerrainLayer) -> 'VoidGuardTerrainLayer':
        return VoidGuardTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VoidGuardTerrainLayer):
        """
        Dynamic initializer for VoidGuardTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__VoidGuardTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer()"""
        val = __VoidGuardTerrainLayer()
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
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer()"""
        val = __VoidGuardTerrainLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.TerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
from builtins import int
 
class TerrainLayer(ABC):
    """dev.ultreon.quantum.world.gen.layer.TerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __TerrainLayer) -> 'TerrainLayer':
        return TerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TerrainLayer):
        """
        Dynamic initializer for TerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

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
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.TerrainLayer()"""
        val = __TerrainLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract boolean dev.ultreon.quantum.world.gen.layer.TerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.TerrainLayer()"""
        val = __TerrainLayer()
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
import dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer as __SurfaceTerrainLayer
__SurfaceTerrainLayer = __SurfaceTerrainLayer
from builtins import int
 
class SurfaceTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __SurfaceTerrainLayer) -> 'SurfaceTerrainLayer':
        return SurfaceTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SurfaceTerrainLayer):
        """
        Dynamic initializer for SurfaceTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__SurfaceTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Block', arg1: int):
        """public dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer(dev.ultreon.quantum.block.Block,int)"""
        val = __SurfaceTerrainLayer(arg0, __int.valueOf(arg1))
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
import java.lang.Long as __long
import dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer as __GroundTerrainLayer
__GroundTerrainLayer = __GroundTerrainLayer
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
from builtins import int
 
class GroundTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __GroundTerrainLayer) -> 'GroundTerrainLayer':
        return GroundTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GroundTerrainLayer):
        """
        Dynamic initializer for GroundTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__GroundTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Block', arg1: int, arg2: int):
        """public dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer(dev.ultreon.quantum.block.Block,int,int)"""
        val = __GroundTerrainLayer(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer as __WaterTerrainLayer
__WaterTerrainLayer = __WaterTerrainLayer
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
from builtins import int
 
class WaterTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __WaterTerrainLayer) -> 'WaterTerrainLayer':
        return WaterTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WaterTerrainLayer):
        """
        Dynamic initializer for WaterTerrainLayer.
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
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__WaterTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer(int)"""
        val = __WaterTerrainLayer(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer()"""
        val = __WaterTerrainLayer()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer()"""
        val = __WaterTerrainLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
import dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer as __UndergroundTerrainLayer
__UndergroundTerrainLayer = __UndergroundTerrainLayer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UndergroundTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __UndergroundTerrainLayer) -> 'UndergroundTerrainLayer':
        return UndergroundTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UndergroundTerrainLayer):
        """
        Dynamic initializer for UndergroundTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Block', arg1: int):
        """public dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer(dev.ultreon.quantum.block.Block,int)"""
        val = __UndergroundTerrainLayer(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__UndergroundTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as __TerrainLayer
__TerrainLayer = __TerrainLayer
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
import dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer as __StoneyPeaksTerrainLayer
__StoneyPeaksTerrainLayer = __StoneyPeaksTerrainLayer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StoneyPeaksTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer"""
 
    @staticmethod
    def __wrap(java_value: __StoneyPeaksTerrainLayer) -> 'StoneyPeaksTerrainLayer':
        return StoneyPeaksTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StoneyPeaksTerrainLayer):
        """
        Dynamic initializer for StoneyPeaksTerrainLayer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TerrainLayer, self).create(arg0)

    @overload
    def __init__(self, arg0: 'Block', arg1: int):
        """public dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer(dev.ultreon.quantum.block.Block,int)"""
        val = __StoneyPeaksTerrainLayer(arg0, __int.valueOf(arg1))
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool.__wrap(super(__StoneyPeaksTerrainLayer, self).handle(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

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