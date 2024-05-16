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
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldGenFeature(ABC, pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.world.gen.WorldGenFeature"""
 
    @staticmethod
    def __wrap(java_value: __WorldGenFeature) -> 'WorldGenFeature':
        return WorldGenFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldGenFeature):
        """
        Dynamic initializer for WorldGenFeature.
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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__WorldGenFeature, self).create(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = __WorldGenFeature()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int):
        """public abstract boolean dev.ultreon.quantum.world.gen.WorldGenFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = __WorldGenFeature()
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(WorldGenFeature, self).dispose()

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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.WorldGenFeature
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
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldGenFeature(ABC, pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.world.gen.WorldGenFeature"""
 
    @staticmethod
    def __wrap(java_value: __WorldGenFeature) -> 'WorldGenFeature':
        return WorldGenFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldGenFeature):
        """
        Dynamic initializer for WorldGenFeature.
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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__WorldGenFeature, self).create(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = __WorldGenFeature()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int):
        """public abstract boolean dev.ultreon.quantum.world.gen.WorldGenFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = __WorldGenFeature()
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(WorldGenFeature, self).dispose()

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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.WorldGenFeature 
 
 
# CLASS: dev.ultreon.quantum.world.gen.WorldGenInfo
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.world.gen.WorldGenInfo as __WorldGenInfo
__WorldGenInfo = __WorldGenInfo
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldGenInfo():
    """dev.ultreon.quantum.world.gen.WorldGenInfo"""
 
    @staticmethod
    def __wrap(java_value: __WorldGenInfo) -> 'WorldGenInfo':
        return WorldGenInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldGenInfo):
        """
        Dynamic initializer for WorldGenInfo.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.WorldGenInfo()"""
        val = __WorldGenInfo()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.WorldGenInfo()"""
        val = __WorldGenInfo()
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.CaveNoiseGenerator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.CaveNoiseGenerator as __CaveNoiseGenerator
__CaveNoiseGenerator = __CaveNoiseGenerator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CaveNoiseGenerator(__NoiseGenerator, NoiseGenerator):
    """dev.ultreon.quantum.world.gen.CaveNoiseGenerator"""
 
    @staticmethod
    def __wrap(java_value: __CaveNoiseGenerator) -> 'CaveNoiseGenerator':
        return CaveNoiseGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CaveNoiseGenerator):
        """
        Dynamic initializer for CaveNoiseGenerator.
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
    def evaluateNoise(self, arg0: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double)"""
        return float.__wrap(super(__CaveNoiseGenerator, self).evaluateNoise(__double.valueOf(arg0)))

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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.CaveNoiseGenerator(long)"""
        val = __CaveNoiseGenerator(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double,double,double)"""
        return float.__wrap(super(__CaveNoiseGenerator, self).evaluateNoise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double,double,double,double)"""
        return float.__wrap(super(__CaveNoiseGenerator, self).evaluateNoise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

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
    def evaluateNoise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double,double)"""
        return float.__wrap(super(__CaveNoiseGenerator, self).evaluateNoise(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.RecordingChunk
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.world.gen.RecordingChunk as __RecordingChunk
__RecordingChunk = __RecordingChunk
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RecordingChunk(pyquantum.__ChunkAccess, world.ChunkAccess):
    """dev.ultreon.quantum.world.gen.RecordingChunk"""
 
    @staticmethod
    def __wrap(java_value: __RecordingChunk) -> 'RecordingChunk':
        return RecordingChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecordingChunk):
        """
        Dynamic initializer for RecordingChunk.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.gen.RecordingChunk.getHighest(int,int)"""
        return int.__wrap(super(__RecordingChunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.gen.RecordingChunk.getFast(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__RecordingChunk, self).getFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'BuilderChunk'):
        """public dev.ultreon.quantum.world.gen.RecordingChunk(dev.ultreon.quantum.world.BuilderChunk)"""
        val = __RecordingChunk(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.gen.RecordingChunk.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__RecordingChunk, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.gen.RecordingChunk.getOffset()"""
        return 'vector.Vec3i'.__wrap(super(RecordingChunk, self).getOffset())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.RecordingChunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__RecordingChunk, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.RecordingChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__RecordingChunk, self).setFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.TerrainGenerator
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pyquantum.world.gen import biome
except ImportError:
    biome = __import_once__("pyquantum.world.gen.biome")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.TerrainGenerator as __TerrainGenerator
__TerrainGenerator = __TerrainGenerator
import dev.ultreon.quantum.world.gen.noise.DomainWarping as __DomainWarping
__DomainWarping = __DomainWarping
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.gen.biome.BiomeData as __BiomeData
__BiomeData = __BiomeData
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.BuilderChunk as __BuilderChunk
__BuilderChunk = __BuilderChunk
import reactor.core.Disposable as __Disposable
__Disposable = __Disposable
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TerrainGenerator(__Disposable, Disposable):
    """dev.ultreon.quantum.world.gen.TerrainGenerator"""
 
    @staticmethod
    def __wrap(java_value: __TerrainGenerator) -> 'TerrainGenerator':
        return TerrainGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TerrainGenerator):
        """
        Dynamic initializer for TerrainGenerator.
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
    def __init__(self, arg0: 'DomainWarping', arg1: 'DomainWarping', arg2: 'NoiseConfig'):
        """public dev.ultreon.quantum.world.gen.TerrainGenerator(dev.ultreon.quantum.world.gen.noise.DomainWarping,dev.ultreon.quantum.world.gen.noise.DomainWarping,dev.ultreon.quantum.world.gen.noise.NoiseConfig)"""
        val = __TerrainGenerator(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def buildBiomeCenters(self, arg0: 'BuilderChunk'):
        """public void dev.ultreon.quantum.world.gen.TerrainGenerator.buildBiomeCenters(dev.ultreon.quantum.world.BuilderChunk)"""
        super(__TerrainGenerator, self).buildBiomeCenters(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLayerDomain(self) -> 'noise.DomainWarping':
        """public dev.ultreon.quantum.world.gen.noise.DomainWarping dev.ultreon.quantum.world.gen.TerrainGenerator.getLayerDomain()"""
        return 'noise.DomainWarping'.__wrap(super(TerrainGenerator, self).getLayerDomain())

    @override
    @overload
    def isDisposed(self) -> bool:
        """public default boolean reactor.core.Disposable.isDisposed()"""
        return bool.__wrap(super(Disposable, self).isDisposed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.TerrainGenerator.dispose()"""
        super(TerrainGenerator, self).dispose()

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
    def generate(self, arg0: 'BuilderChunk', arg1: 'Collection') -> 'world.BuilderChunk':
        """public dev.ultreon.quantum.world.BuilderChunk dev.ultreon.quantum.world.gen.TerrainGenerator.generate(dev.ultreon.quantum.world.BuilderChunk,java.util.Collection<dev.ultreon.quantum.world.ServerWorld$RecordedChange>)"""
        return 'world.BuilderChunk'.__wrap(super(__TerrainGenerator, self).generate(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def registerBiome(self, arg0: 'ServerWorld', arg1: int, arg2: 'Biome', arg3: float, arg4: float, arg5: bool) -> 'biome.BiomeData':
        """public dev.ultreon.quantum.world.gen.biome.BiomeData dev.ultreon.quantum.world.gen.TerrainGenerator.registerBiome(dev.ultreon.quantum.world.ServerWorld,long,dev.ultreon.quantum.world.Biome,float,float,boolean)"""
        return 'biome.BiomeData'.__wrap(super(__TerrainGenerator, self).registerBiome(arg0, __long.valueOf(arg1), arg2, __float.valueOf(arg3), __float.valueOf(arg4), __boolean.valueOf(arg5)))

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
    def create(self, arg0: 'ServerWorld', arg1: int):
        """public void dev.ultreon.quantum.world.gen.TerrainGenerator.create(dev.ultreon.quantum.world.ServerWorld,long)"""
        super(__TerrainGenerator, self).create(arg0, __long.valueOf(arg1)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.TreeGenerator
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.gen.TreeData as __TreeData
__TreeData = __TreeData
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.world.gen.TreeGenerator as __TreeGenerator
__TreeGenerator = __TreeGenerator
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class TreeGenerator():
    """dev.ultreon.quantum.world.gen.TreeGenerator"""
 
    @staticmethod
    def __wrap(java_value: __TreeGenerator) -> 'TreeGenerator':
        return TreeGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeGenerator):
        """
        Dynamic initializer for TreeGenerator.
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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'DomainWarping'):
        """public dev.ultreon.quantum.world.gen.TreeGenerator(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.world.gen.noise.DomainWarping)"""
        val = __TreeGenerator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def create(self, arg0: int):
        """public void dev.ultreon.quantum.world.gen.TreeGenerator.create(long)"""
        super(__TreeGenerator, self).create(__long.valueOf(arg0))

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

    @staticmethod
    @overload
    def findLocalMaxima(arg0: 'double', arg1: int, arg2: int) -> 'List':
        """public static java.util.List<dev.ultreon.libs.commons.v0.vector.Vec2i> dev.ultreon.quantum.world.gen.TreeGenerator.findLocalMaxima(double[][],int,int)"""
        return List.__wrap(__TreeGenerator.findLocalMaxima(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def generateTreeData(self, arg0: 'Chunk') -> 'TreeData':
        """public dev.ultreon.quantum.world.gen.TreeData dev.ultreon.quantum.world.gen.TreeGenerator.generateTreeData(dev.ultreon.quantum.world.Chunk)"""
        return 'TreeData'.__wrap(super(__TreeGenerator, self).generateTreeData(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.Neighbour8Direction
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.Neighbour8Direction as __Neighbour8Direction
__Neighbour8Direction = __Neighbour8Direction
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

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
 
class Neighbour8Direction(__Enum, Enum):
    """dev.ultreon.quantum.world.gen.Neighbour8Direction"""
 
    @staticmethod
    def __wrap(java_value: __Neighbour8Direction) -> 'Neighbour8Direction':
        return Neighbour8Direction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Neighbour8Direction):
        """
        Dynamic initializer for Neighbour8Direction.
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
 
    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.SE
    SE: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.SE)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.S
    S: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.S)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.W
    W: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.W)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.NE
    NE: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.NE)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.E
    E: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.E)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.N
    N: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.N)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.SW
    SW: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.SW)

    # public static final dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.NW
    NW: 'Neighbour8Direction' = __wrap(__Neighbour8Direction.NW)


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

    @overload
    def vec(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.gen.Neighbour8Direction.vec()"""
        return 'vector.Vec2i'.__wrap(super(Neighbour8Direction, self).vec())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Neighbour8Direction':
        """public static dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.valueOf(java.lang.String)"""
        return Neighbour8Direction.__wrap(__Neighbour8Direction.valueOf(arg0))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Neighbour8Direction']:
        """public static dev.ultreon.quantum.world.gen.Neighbour8Direction[] dev.ultreon.quantum.world.gen.Neighbour8Direction.values()"""
        return List[Neighbour8Direction].__wrap(__Neighbour8Direction.values())

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.TreeData
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.gen.TreeData as __TreeData
__TreeData = __TreeData
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TreeData():
    """dev.ultreon.quantum.world.gen.TreeData"""
 
    @staticmethod
    def __wrap(java_value: __TreeData) -> 'TreeData':
        return TreeData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeData):
        """
        Dynamic initializer for TreeData.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.TreeData()"""
        val = __TreeData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.TreeData()"""
        val = __TreeData()
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.PerlinNoiseGenerator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.world.gen.PerlinNoiseGenerator as __PerlinNoiseGenerator
__PerlinNoiseGenerator = __PerlinNoiseGenerator
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PerlinNoiseGenerator():
    """dev.ultreon.quantum.world.gen.PerlinNoiseGenerator"""
 
    @staticmethod
    def __wrap(java_value: __PerlinNoiseGenerator) -> 'PerlinNoiseGenerator':
        return PerlinNoiseGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerlinNoiseGenerator):
        """
        Dynamic initializer for PerlinNoiseGenerator.
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
 
    @staticmethod
    @overload
    def generatePerlinNoise(arg0: int, arg1: int, arg2: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generatePerlinNoise(int,int,int)"""
        return List[List[float]].__wrap(__PerlinNoiseGenerator.generatePerlinNoise(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def generateHeightMap(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> List[int]:
        """public static byte[] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generateHeightMap(int,int,int,int,int)"""
        return List[int].__wrap(__PerlinNoiseGenerator.generateHeightMap(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def generateWhiteNoise(arg0: int, arg1: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generateWhiteNoise(int,int)"""
        return List[List[float]].__wrap(__PerlinNoiseGenerator.generateWhiteNoise(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def generatePerlinNoise(arg0: 'float', arg1: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generatePerlinNoise(float[][],int)"""
        return List[List[float]].__wrap(__PerlinNoiseGenerator.generatePerlinNoise(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def interpolate(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.interpolate(float,float,float)"""
        return float.__wrap(__PerlinNoiseGenerator.interpolate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.PerlinNoiseGenerator()"""
        val = __PerlinNoiseGenerator()
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.PerlinNoiseGenerator()"""
        val = __PerlinNoiseGenerator()
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

    @staticmethod
    @overload
    def generateSmoothNoise(arg0: 'float', arg1: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generateSmoothNoise(float[][],int)"""
        return List[List[float]].__wrap(__PerlinNoiseGenerator.generateSmoothNoise(arg0, __int.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.Carver
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.gen.Carver as __Carver
__Carver = __Carver
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import de.articdive.jnoise.core.api.pipeline.NoiseSource as NoiseSource
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Carver():
    """dev.ultreon.quantum.world.gen.Carver"""
 
    @staticmethod
    def __wrap(java_value: __Carver) -> 'Carver':
        return Carver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Carver):
        """
        Dynamic initializer for Carver.
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

    @overload
    def carve(self, arg0: 'BuilderChunk', arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.gen.Carver.carve(dev.ultreon.quantum.world.BuilderChunk,int,int)"""
        return int.__wrap(super(__Carver, self).carve(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSurfaceHeightNoise(self, arg0: float, arg1: float) -> int:
        """public int dev.ultreon.quantum.world.gen.Carver.getSurfaceHeightNoise(float,float)"""
        return int.__wrap(super(__Carver, self).getSurfaceHeightNoise(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'DomainWarping', arg1: 'NoiseSource', arg2: int):
        """public dev.ultreon.quantum.world.gen.Carver(dev.ultreon.quantum.world.gen.noise.DomainWarping,de.articdive.jnoise.core.api.pipeline.NoiseSource,long)"""
        val = __Carver(arg0, arg1, __long.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val