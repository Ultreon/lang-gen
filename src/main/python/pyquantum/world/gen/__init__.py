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
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldGenFeature():
    """dev.ultreon.quantum.world.gen.WorldGenFeature"""
 
    @staticmethod
    def _wrap(java_value: _WorldGenFeature) -> 'WorldGenFeature':
        return WorldGenFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldGenFeature):
        """
        Dynamic initializer for WorldGenFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldGenFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldGenFeature__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = _WorldGenFeature()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_WorldGenFeature, self).create(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = _WorldGenFeature()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(WorldGenFeature, self).dispose()

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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.WorldGenFeature
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
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldGenFeature():
    """dev.ultreon.quantum.world.gen.WorldGenFeature"""
 
    @staticmethod
    def _wrap(java_value: _WorldGenFeature) -> 'WorldGenFeature':
        return WorldGenFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldGenFeature):
        """
        Dynamic initializer for WorldGenFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldGenFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldGenFeature__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = _WorldGenFeature()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_WorldGenFeature, self).create(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.WorldGenFeature()"""
        val = _WorldGenFeature()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(WorldGenFeature, self).dispose()

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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.WorldGenFeature 
 
 
# CLASS: dev.ultreon.quantum.world.gen.WorldGenInfo
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.WorldGenInfo as _WorldGenInfo
_WorldGenInfo = _WorldGenInfo
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldGenInfo():
    """dev.ultreon.quantum.world.gen.WorldGenInfo"""
 
    @staticmethod
    def _wrap(java_value: _WorldGenInfo) -> 'WorldGenInfo':
        return WorldGenInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldGenInfo):
        """
        Dynamic initializer for WorldGenInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldGenInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldGenInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.WorldGenInfo()"""
        val = _WorldGenInfo()
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.WorldGenInfo()"""
        val = _WorldGenInfo()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.CaveNoiseGenerator
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
import dev.ultreon.quantum.world.gen.CaveNoiseGenerator as _CaveNoiseGenerator
_CaveNoiseGenerator = _CaveNoiseGenerator
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CaveNoiseGenerator():
    """dev.ultreon.quantum.world.gen.CaveNoiseGenerator"""
 
    @staticmethod
    def _wrap(java_value: _CaveNoiseGenerator) -> 'CaveNoiseGenerator':
        return CaveNoiseGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CaveNoiseGenerator):
        """
        Dynamic initializer for CaveNoiseGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CaveNoiseGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CaveNoiseGenerator__wrapper":
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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.CaveNoiseGenerator(long)"""
        val = _CaveNoiseGenerator(_long.valueOf(arg0))
        self.__wrapper = val

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
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double,double,double)"""
        return float._wrap(super(_CaveNoiseGenerator, self).evaluateNoise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

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
    def evaluateNoise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double,double)"""
        return float._wrap(super(_CaveNoiseGenerator, self).evaluateNoise(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def evaluateNoise(self, arg0: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double)"""
        return float._wrap(super(_CaveNoiseGenerator, self).evaluateNoise(_double.valueOf(arg0)))

    @overload
    def evaluateNoise(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.quantum.world.gen.CaveNoiseGenerator.evaluateNoise(double,double,double,double)"""
        return float._wrap(super(_CaveNoiseGenerator, self).evaluateNoise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.RecordingChunk
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
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.gen.RecordingChunk as _RecordingChunk
_RecordingChunk = _RecordingChunk
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RecordingChunk():
    """dev.ultreon.quantum.world.gen.RecordingChunk"""
 
    @staticmethod
    def _wrap(java_value: _RecordingChunk) -> 'RecordingChunk':
        return RecordingChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecordingChunk):
        """
        Dynamic initializer for RecordingChunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecordingChunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecordingChunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'BuilderChunk'):
        """public dev.ultreon.quantum.world.gen.RecordingChunk(dev.ultreon.quantum.world.BuilderChunk)"""
        val = _RecordingChunk(arg0)
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

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.gen.RecordingChunk.getHighest(int,int)"""
        return int._wrap(super(_RecordingChunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.RecordingChunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_RecordingChunk, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.RecordingChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_RecordingChunk, self).setFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.gen.RecordingChunk.getOffset()"""
        return 'vector.Vec3i'._wrap(super(RecordingChunk, self).getOffset())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.gen.RecordingChunk.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_RecordingChunk, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.gen.RecordingChunk.getFast(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_RecordingChunk, self).getFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.TerrainGenerator
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.world.gen.biome.BiomeData as _BiomeData
_BiomeData = _BiomeData
from pyquantum_helper import override
try:
    from pyquantum.world.gen import biome
except ImportError:
    biome = _import_once("pyquantum.world.gen.biome")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.gen.TerrainGenerator as _TerrainGenerator
_TerrainGenerator = _TerrainGenerator
import dev.ultreon.quantum.world.BuilderChunk as _BuilderChunk
_BuilderChunk = _BuilderChunk
import java.lang.Float as _float
import dev.ultreon.quantum.world.gen.noise.DomainWarping as _DomainWarping
_DomainWarping = _DomainWarping
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import reactor.core.Disposable as _Disposable
_Disposable = _Disposable
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TerrainGenerator():
    """dev.ultreon.quantum.world.gen.TerrainGenerator"""
 
    @staticmethod
    def _wrap(java_value: _TerrainGenerator) -> 'TerrainGenerator':
        return TerrainGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TerrainGenerator):
        """
        Dynamic initializer for TerrainGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TerrainGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TerrainGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'DomainWarping', arg1: 'DomainWarping', arg2: 'NoiseConfig'):
        """public dev.ultreon.quantum.world.gen.TerrainGenerator(dev.ultreon.quantum.world.gen.noise.DomainWarping,dev.ultreon.quantum.world.gen.noise.DomainWarping,dev.ultreon.quantum.world.gen.noise.NoiseConfig)"""
        val = _TerrainGenerator(arg0, arg1, arg2)
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
    def generate(self, arg0: 'BuilderChunk', arg1: 'Collection') -> 'world.BuilderChunk':
        """public dev.ultreon.quantum.world.BuilderChunk dev.ultreon.quantum.world.gen.TerrainGenerator.generate(dev.ultreon.quantum.world.BuilderChunk,java.util.Collection<dev.ultreon.quantum.world.ServerWorld$RecordedChange>)"""
        return 'world.BuilderChunk'._wrap(super(_TerrainGenerator, self).generate(arg0, arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.TerrainGenerator.dispose()"""
        super(TerrainGenerator, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getLayerDomain(self) -> 'noise.DomainWarping':
        """public dev.ultreon.quantum.world.gen.noise.DomainWarping dev.ultreon.quantum.world.gen.TerrainGenerator.getLayerDomain()"""
        return 'noise.DomainWarping'._wrap(super(TerrainGenerator, self).getLayerDomain())

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
    def buildBiomeCenters(self, arg0: 'BuilderChunk'):
        """public void dev.ultreon.quantum.world.gen.TerrainGenerator.buildBiomeCenters(dev.ultreon.quantum.world.BuilderChunk)"""
        super(_TerrainGenerator, self).buildBiomeCenters(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def registerBiome(self, arg0: 'ServerWorld', arg1: int, arg2: 'Biome', arg3: float, arg4: float, arg5: bool) -> 'biome.BiomeData':
        """public dev.ultreon.quantum.world.gen.biome.BiomeData dev.ultreon.quantum.world.gen.TerrainGenerator.registerBiome(dev.ultreon.quantum.world.ServerWorld,long,dev.ultreon.quantum.world.Biome,float,float,boolean)"""
        return 'biome.BiomeData'._wrap(super(_TerrainGenerator, self).registerBiome(arg0, _long.valueOf(arg1), arg2, _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5)))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public default boolean reactor.core.Disposable.isDisposed()"""
        return bool._wrap(super(Disposable, self).isDisposed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def create(self, arg0: 'ServerWorld', arg1: int):
        """public void dev.ultreon.quantum.world.gen.TerrainGenerator.create(dev.ultreon.quantum.world.ServerWorld,long)"""
        super(_TerrainGenerator, self).create(arg0, _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.TreeGenerator
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
from builtins import float
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.world.gen.TreeGenerator as _TreeGenerator
_TreeGenerator = _TreeGenerator
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.TreeData as _TreeData
_TreeData = _TreeData
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TreeGenerator():
    """dev.ultreon.quantum.world.gen.TreeGenerator"""
 
    @staticmethod
    def _wrap(java_value: _TreeGenerator) -> 'TreeGenerator':
        return TreeGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeGenerator):
        """
        Dynamic initializer for TreeGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def findLocalMaxima(arg0: 'double', arg1: int, arg2: int) -> 'List':
        """public static java.util.List<dev.ultreon.libs.commons.v0.vector.Vec2i> dev.ultreon.quantum.world.gen.TreeGenerator.findLocalMaxima(double[][],int,int)"""
        return List._wrap(_TreeGenerator.findLocalMaxima(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def create(self, arg0: int):
        """public void dev.ultreon.quantum.world.gen.TreeGenerator.create(long)"""
        super(_TreeGenerator, self).create(_long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'NoiseConfig', arg1: 'DomainWarping'):
        """public dev.ultreon.quantum.world.gen.TreeGenerator(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.world.gen.noise.DomainWarping)"""
        val = _TreeGenerator(arg0, arg1)
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
    def generateTreeData(self, arg0: 'Chunk') -> 'TreeData':
        """public dev.ultreon.quantum.world.gen.TreeData dev.ultreon.quantum.world.gen.TreeGenerator.generateTreeData(dev.ultreon.quantum.world.Chunk)"""
        return 'TreeData'._wrap(super(_TreeGenerator, self).generateTreeData(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.Neighbour8Direction
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.Neighbour8Direction as _Neighbour8Direction
_Neighbour8Direction = _Neighbour8Direction
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
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
 
class Neighbour8Direction():
    """dev.ultreon.quantum.world.gen.Neighbour8Direction"""
 
    @staticmethod
    def _wrap(java_value: _Neighbour8Direction) -> 'Neighbour8Direction':
        return Neighbour8Direction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Neighbour8Direction):
        """
        Dynamic initializer for Neighbour8Direction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Neighbour8Direction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Neighbour8Direction__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['Neighbour8Direction']:
        """public static dev.ultreon.quantum.world.gen.Neighbour8Direction[] dev.ultreon.quantum.world.gen.Neighbour8Direction.values()"""
        return List[Neighbour8Direction]._wrap(_Neighbour8Direction.values())

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

    @overload
    def vec(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.gen.Neighbour8Direction.vec()"""
        return 'vector.Vec2i'._wrap(super(Neighbour8Direction, self).vec())

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
    def valueOf(arg0: str) -> 'Neighbour8Direction':
        """public static dev.ultreon.quantum.world.gen.Neighbour8Direction dev.ultreon.quantum.world.gen.Neighbour8Direction.valueOf(java.lang.String)"""
        return Neighbour8Direction._wrap(_Neighbour8Direction.valueOf(arg0))


Neighbour8Direction.NW = Neighbour8Direction._wrap(_NW.NW)

Neighbour8Direction.E = Neighbour8Direction._wrap(_E.E)

Neighbour8Direction.S = Neighbour8Direction._wrap(_S.S)

Neighbour8Direction.N = Neighbour8Direction._wrap(_N.N)

Neighbour8Direction.SE = Neighbour8Direction._wrap(_SE.SE)

Neighbour8Direction.W = Neighbour8Direction._wrap(_W.W)

Neighbour8Direction.NE = Neighbour8Direction._wrap(_NE.NE)

Neighbour8Direction.SW = Neighbour8Direction._wrap(_SW.SW) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.TreeData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.TreeData as _TreeData
_TreeData = _TreeData
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TreeData():
    """dev.ultreon.quantum.world.gen.TreeData"""
 
    @staticmethod
    def _wrap(java_value: _TreeData) -> 'TreeData':
        return TreeData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeData):
        """
        Dynamic initializer for TreeData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.TreeData()"""
        val = _TreeData()
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
        """public dev.ultreon.quantum.world.gen.TreeData()"""
        val = _TreeData()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.PerlinNoiseGenerator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.world.gen.PerlinNoiseGenerator as _PerlinNoiseGenerator
_PerlinNoiseGenerator = _PerlinNoiseGenerator
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PerlinNoiseGenerator():
    """dev.ultreon.quantum.world.gen.PerlinNoiseGenerator"""
 
    @staticmethod
    def _wrap(java_value: _PerlinNoiseGenerator) -> 'PerlinNoiseGenerator':
        return PerlinNoiseGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PerlinNoiseGenerator):
        """
        Dynamic initializer for PerlinNoiseGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PerlinNoiseGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PerlinNoiseGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def generateSmoothNoise(arg0: 'float', arg1: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generateSmoothNoise(float[][],int)"""
        return List[List[float]]._wrap(_PerlinNoiseGenerator.generateSmoothNoise(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def generateHeightMap(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> List[int]:
        """public static byte[] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generateHeightMap(int,int,int,int,int)"""
        return List[int]._wrap(_PerlinNoiseGenerator.generateHeightMap(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.PerlinNoiseGenerator()"""
        val = _PerlinNoiseGenerator()
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

    @staticmethod
    @overload
    def interpolate(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.interpolate(float,float,float)"""
        return float._wrap(_PerlinNoiseGenerator.interpolate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def generatePerlinNoise(arg0: 'float', arg1: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generatePerlinNoise(float[][],int)"""
        return List[List[float]]._wrap(_PerlinNoiseGenerator.generatePerlinNoise(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.PerlinNoiseGenerator()"""
        val = _PerlinNoiseGenerator()
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

    @staticmethod
    @overload
    def generatePerlinNoise(arg0: int, arg1: int, arg2: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generatePerlinNoise(int,int,int)"""
        return List[List[float]]._wrap(_PerlinNoiseGenerator.generatePerlinNoise(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def generateWhiteNoise(arg0: int, arg1: int) -> List[List[float]]:
        """public static float[][] dev.ultreon.quantum.world.gen.PerlinNoiseGenerator.generateWhiteNoise(int,int)"""
        return List[List[float]]._wrap(_PerlinNoiseGenerator.generateWhiteNoise(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.Carver
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.world.gen.Carver as _Carver
_Carver = _Carver
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import de.articdive.jnoise.core.api.pipeline.NoiseSource as NoiseSource
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Carver():
    """dev.ultreon.quantum.world.gen.Carver"""
 
    @staticmethod
    def _wrap(java_value: _Carver) -> 'Carver':
        return Carver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Carver):
        """
        Dynamic initializer for Carver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Carver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Carver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSurfaceHeightNoise(self, arg0: float, arg1: float) -> int:
        """public int dev.ultreon.quantum.world.gen.Carver.getSurfaceHeightNoise(float,float)"""
        return int._wrap(super(_Carver, self).getSurfaceHeightNoise(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'DomainWarping', arg1: 'NoiseSource', arg2: int):
        """public dev.ultreon.quantum.world.gen.Carver(dev.ultreon.quantum.world.gen.noise.DomainWarping,de.articdive.jnoise.core.api.pipeline.NoiseSource,long)"""
        val = _Carver(arg0, arg1, _long.valueOf(arg2))
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
    def carve(self, arg0: 'BuilderChunk', arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.gen.Carver.carve(dev.ultreon.quantum.world.BuilderChunk,int,int)"""
        return int._wrap(super(_Carver, self).carve(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())