from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.AirTerrainLayer as _AirTerrainLayer
_AirTerrainLayer = _AirTerrainLayer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AirTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.AirTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _AirTerrainLayer) -> 'AirTerrainLayer':
        return AirTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AirTerrainLayer):
        """
        Dynamic initializer for AirTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AirTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AirTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = _AirTerrainLayer()
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

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.AirTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_AirTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = _AirTerrainLayer()
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.AirTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.AirTerrainLayer as _AirTerrainLayer
_AirTerrainLayer = _AirTerrainLayer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AirTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.AirTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _AirTerrainLayer) -> 'AirTerrainLayer':
        return AirTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AirTerrainLayer):
        """
        Dynamic initializer for AirTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AirTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AirTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = _AirTerrainLayer()
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

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.AirTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_AirTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.AirTerrainLayer()"""
        val = _AirTerrainLayer()
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.AirTerrainLayer 
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer as _VoidGuardTerrainLayer
_VoidGuardTerrainLayer = _VoidGuardTerrainLayer
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VoidGuardTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _VoidGuardTerrainLayer) -> 'VoidGuardTerrainLayer':
        return VoidGuardTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VoidGuardTerrainLayer):
        """
        Dynamic initializer for VoidGuardTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VoidGuardTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VoidGuardTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer()"""
        val = _VoidGuardTerrainLayer()
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
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_VoidGuardTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.VoidGuardTerrainLayer()"""
        val = _VoidGuardTerrainLayer()
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

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.TerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.TerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _TerrainLayer) -> 'TerrainLayer':
        return TerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TerrainLayer):
        """
        Dynamic initializer for TerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

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
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.TerrainLayer()"""
        val = _TerrainLayer()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.TerrainLayer()"""
        val = _TerrainLayer()
        self.__wrapper = val

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

    @abstractmethod
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract boolean dev.ultreon.quantum.world.gen.layer.TerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        pass

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer as _SurfaceTerrainLayer
_SurfaceTerrainLayer = _SurfaceTerrainLayer
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SurfaceTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _SurfaceTerrainLayer) -> 'SurfaceTerrainLayer':
        return SurfaceTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SurfaceTerrainLayer):
        """
        Dynamic initializer for SurfaceTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SurfaceTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SurfaceTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Block', arg1: int):
        """public dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer(dev.ultreon.quantum.block.Block,int)"""
        val = _SurfaceTerrainLayer(arg0, _int.valueOf(arg1))
        self.__wrapper = val

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

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.SurfaceTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_SurfaceTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer as _GroundTerrainLayer
_GroundTerrainLayer = _GroundTerrainLayer
import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GroundTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _GroundTerrainLayer) -> 'GroundTerrainLayer':
        return GroundTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GroundTerrainLayer):
        """
        Dynamic initializer for GroundTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GroundTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GroundTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Block', arg1: int, arg2: int):
        """public dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer(dev.ultreon.quantum.block.Block,int,int)"""
        val = _GroundTerrainLayer(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.GroundTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_GroundTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer as _WaterTerrainLayer
_WaterTerrainLayer = _WaterTerrainLayer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WaterTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _WaterTerrainLayer) -> 'WaterTerrainLayer':
        return WaterTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WaterTerrainLayer):
        """
        Dynamic initializer for WaterTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WaterTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WaterTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer(int)"""
        val = _WaterTerrainLayer(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_WaterTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

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

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer()"""
        val = _WaterTerrainLayer()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.layer.WaterTerrainLayer()"""
        val = _WaterTerrainLayer()
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer as _UndergroundTerrainLayer
_UndergroundTerrainLayer = _UndergroundTerrainLayer
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UndergroundTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _UndergroundTerrainLayer) -> 'UndergroundTerrainLayer':
        return UndergroundTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UndergroundTerrainLayer):
        """
        Dynamic initializer for UndergroundTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UndergroundTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UndergroundTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @overload
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_UndergroundTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

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
    def __init__(self, arg0: 'Block', arg1: int):
        """public dev.ultreon.quantum.world.gen.layer.UndergroundTerrainLayer(dev.ultreon.quantum.block.Block,int)"""
        val = _UndergroundTerrainLayer(arg0, _int.valueOf(arg1))
        self.__wrapper = val

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

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.gen.layer.TerrainLayer as _TerrainLayer
_TerrainLayer = _TerrainLayer
import dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer as _StoneyPeaksTerrainLayer
_StoneyPeaksTerrainLayer = _StoneyPeaksTerrainLayer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StoneyPeaksTerrainLayer():
    """dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer"""
 
    @staticmethod
    def _wrap(java_value: _StoneyPeaksTerrainLayer) -> 'StoneyPeaksTerrainLayer':
        return StoneyPeaksTerrainLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StoneyPeaksTerrainLayer):
        """
        Dynamic initializer for StoneyPeaksTerrainLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StoneyPeaksTerrainLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StoneyPeaksTerrainLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.dispose()"""
        super(TerrainLayer, self).dispose()

    @overload
    def __init__(self, arg0: 'Block', arg1: int):
        """public dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer(dev.ultreon.quantum.block.Block,int)"""
        val = _StoneyPeaksTerrainLayer(arg0, _int.valueOf(arg1))
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
    def handle(self, arg0: 'World', arg1: 'Chunk', arg2: 'RNG', arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.layer.StoneyPeaksTerrainLayer.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Chunk,dev.ultreon.quantum.world.rng.RNG,int,int,int,int)"""
        return bool._wrap(super(_StoneyPeaksTerrainLayer, self).handle(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.layer.TerrainLayer.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TerrainLayer, self).create(arg0)

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