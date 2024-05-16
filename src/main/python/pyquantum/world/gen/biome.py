from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator_Index
_Index = _BiomeGenerator_Index.Index
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.Integer as Integer
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator
_BiomeGenerator = _BiomeGenerator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Index():
    """dev.ultreon.quantum.world.gen.biome.BiomeGenerator.Index"""
 
    @staticmethod
    def _wrap(java_value: _Index) -> 'Index':
        return Index(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Index):
        """
        Dynamic initializer for Index.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Index__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Index__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: 'BiomeGenerator'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        val = _Index(arg0)
        self.__wrapper = val

    @property
    def biomeGenerator(self) -> BiomeGenerator:
        return BiomeGenerator._wrap(super(_Index).biomeGenerator())

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

    @property
    def biomeGenerator(self, value: 'BiomeGenerator'):
        super(_Index).biomeGenerator(value)

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
    def __init__(self, arg0: 'BiomeGenerator', arg1: 'Integer'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator,java.lang.Integer)"""
        val = _Index(arg0, arg1)
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator_Index
_Index = _BiomeGenerator_Index.Index
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.Integer as Integer
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator
_BiomeGenerator = _BiomeGenerator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Index():
    """dev.ultreon.quantum.world.gen.biome.BiomeGenerator.Index"""
 
    @staticmethod
    def _wrap(java_value: _Index) -> 'Index':
        return Index(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Index):
        """
        Dynamic initializer for Index.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Index__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Index__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: 'BiomeGenerator'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        val = _Index(arg0)
        self.__wrapper = val

    @property
    def biomeGenerator(self) -> BiomeGenerator:
        return BiomeGenerator._wrap(super(_Index).biomeGenerator())

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

    @property
    def biomeGenerator(self, value: 'BiomeGenerator'):
        super(_Index).biomeGenerator(value)

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
    def __init__(self, arg0: 'BiomeGenerator', arg1: 'Integer'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator,java.lang.Integer)"""
        val = _Index(arg0, arg1)
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.Biomes
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
import dev.ultreon.quantum.world.gen.biome.Biomes as _Biomes
_Biomes = _Biomes
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Biomes():
    """dev.ultreon.quantum.world.gen.biome.Biomes"""
 
    @staticmethod
    def _wrap(java_value: _Biomes) -> 'Biomes':
        return Biomes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Biomes):
        """
        Dynamic initializer for Biomes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Biomes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Biomes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.PLAINS
    PLAINS: 'world.Biome' = _wrap(_world.Biome.PLAINS)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.OCEAN
    OCEAN: 'world.Biome' = _wrap(_world.Biome.OCEAN)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.VOID
    VOID: 'world.Biome' = _wrap(_world.Biome.VOID)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.FOREST
    FOREST: 'world.Biome' = _wrap(_world.Biome.FOREST)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.DESERT
    DESERT: 'world.Biome' = _wrap(_world.Biome.DESERT)


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
        """public dev.ultreon.quantum.world.gen.biome.Biomes()"""
        val = _Biomes()
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.world.gen.biome.Biomes.init()"""
            _Biomes.init()

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
        """public dev.ultreon.quantum.world.gen.biome.Biomes()"""
        val = _Biomes()
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeGenerator
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
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.BuilderChunk as _BuilderChunk
_BuilderChunk = _BuilderChunk
import dev.ultreon.quantum.world.gen.TreeGenerator as _TreeGenerator
_TreeGenerator = _TreeGenerator
import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.gen.TreeData as _TreeData
_TreeData = _TreeData
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator
_BiomeGenerator = _BiomeGenerator
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class BiomeGenerator():
    """dev.ultreon.quantum.world.gen.biome.BiomeGenerator"""
 
    @staticmethod
    def _wrap(java_value: _BiomeGenerator) -> 'BiomeGenerator':
        return BiomeGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiomeGenerator):
        """
        Dynamic initializer for BiomeGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiomeGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiomeGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBiome(self) -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.BiomeGenerator.getBiome()"""
        return 'world.Biome'._wrap(super(BiomeGenerator, self).getBiome())

    @overload
    def generateTerrainFeatures(self, arg0: 'RecordingChunk', arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.world.gen.biome.BiomeGenerator.generateTerrainFeatures(dev.ultreon.quantum.world.gen.RecordingChunk,int,int,int)"""
        super(_BiomeGenerator, self).generateTerrainFeatures(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

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
    def createTreeData(self, arg0: 'Chunk') -> 'gen.TreeData':
        """public dev.ultreon.quantum.world.gen.TreeData dev.ultreon.quantum.world.gen.biome.BiomeGenerator.createTreeData(dev.ultreon.quantum.world.Chunk)"""
        return 'gen.TreeData'._wrap(super(_BiomeGenerator, self).createTreeData(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.biome.BiomeGenerator.dispose()"""
        super(BiomeGenerator, self).dispose()

    @property
    def treeGenerator(self) -> TreeGenerator:
        return TreeGenerator._wrap(super(_BiomeGenerator).treeGenerator())

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
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.world.gen.biome.BiomeGenerator.getWorld()"""
        return 'world.World'._wrap(super(BiomeGenerator, self).getWorld())

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
    def processColumn(self, arg0: 'BuilderChunk', arg1: int, arg2: int, arg3: int, arg4: 'Collection') -> 'world.BuilderChunk':
        """public dev.ultreon.quantum.world.BuilderChunk dev.ultreon.quantum.world.gen.biome.BiomeGenerator.processColumn(dev.ultreon.quantum.world.BuilderChunk,int,int,int,java.util.Collection<dev.ultreon.quantum.world.ServerWorld$RecordedChange>)"""
        return 'world.BuilderChunk'._wrap(super(_BiomeGenerator, self).processColumn(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'World', arg1: 'Biome', arg2: 'DomainWarping', arg3: 'List', arg4: 'List'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Biome,dev.ultreon.quantum.world.gen.noise.DomainWarping,java.util.List<dev.ultreon.quantum.world.gen.layer.TerrainLayer>,java.util.List<dev.ultreon.quantum.world.gen.WorldGenFeature>)"""
        val = _BiomeGenerator(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @property
    def treeGenerator(self, value: 'gen.TreeGenerator'):
        super(_BiomeGenerator).treeGenerator(value)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeData
from builtins import str
import dev.ultreon.quantum.world.gen.biome.BiomeData as _BiomeData
_BiomeData = _BiomeData
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as _BiomeGenerator
_BiomeGenerator = _BiomeGenerator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BiomeData():
    """dev.ultreon.quantum.world.gen.biome.BiomeData"""
 
    @staticmethod
    def _wrap(java_value: _BiomeData) -> 'BiomeData':
        return BiomeData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiomeData):
        """
        Dynamic initializer for BiomeData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiomeData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiomeData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.biome.BiomeData.equals(java.lang.Object)"""
        return bool._wrap(super(_BiomeData, self).equals(arg0))

    @overload
    def isOcean(self) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.biome.BiomeData.isOcean()"""
        return bool._wrap(super(BiomeData, self).isOcean())

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
    def biomeGen(self) -> 'BiomeGenerator':
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator dev.ultreon.quantum.world.gen.biome.BiomeData.biomeGen()"""
        return 'BiomeGenerator'._wrap(super(BiomeData, self).biomeGen())

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
        """public java.lang.String dev.ultreon.quantum.world.gen.biome.BiomeData.toString()"""
        return str._wrap(super(BiomeData, self).toString())

    @overload
    def temperatureStartThreshold(self) -> float:
        """public float dev.ultreon.quantum.world.gen.biome.BiomeData.temperatureStartThreshold()"""
        return float._wrap(super(BiomeData, self).temperatureStartThreshold())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: bool, arg3: 'BiomeGenerator'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeData(float,float,boolean,dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        val = _BiomeData(_float.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2), arg3)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.gen.biome.BiomeData.hashCode()"""
        return int._wrap(super(BiomeData, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def temperatureEndThreshold(self) -> float:
        """public float dev.ultreon.quantum.world.gen.biome.BiomeData.temperatureEndThreshold()"""
        return float._wrap(super(BiomeData, self).temperatureEndThreshold()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder
from builtins import str
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
import dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder as _BiomeCenterFinder
_BiomeCenterFinder = _BiomeCenterFinder
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BiomeCenterFinder():
    """dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder"""
 
    @staticmethod
    def _wrap(java_value: _BiomeCenterFinder) -> 'BiomeCenterFinder':
        return BiomeCenterFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiomeCenterFinder):
        """
        Dynamic initializer for BiomeCenterFinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiomeCenterFinder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiomeCenterFinder__wrapper":
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder()"""
        val = _BiomeCenterFinder()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder()"""
        val = _BiomeCenterFinder()
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeIndex
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
from builtins import bool
import dev.ultreon.quantum.world.gen.biome.BiomeIndex as _BiomeIndex
_BiomeIndex = _BiomeIndex
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BiomeIndex():
    """dev.ultreon.quantum.world.gen.biome.BiomeIndex"""
 
    @staticmethod
    def _wrap(java_value: _BiomeIndex) -> 'BiomeIndex':
        return BiomeIndex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiomeIndex):
        """
        Dynamic initializer for BiomeIndex.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiomeIndex__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiomeIndex__wrapper":
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.biome.BiomeIndex.equals(java.lang.Object)"""
        return bool._wrap(super(_BiomeIndex, self).equals(arg0))

    @overload
    def distance(self) -> float:
        """public double dev.ultreon.quantum.world.gen.biome.BiomeIndex.distance()"""
        return float._wrap(super(BiomeIndex, self).distance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.world.gen.biome.BiomeIndex.index()"""
        return int._wrap(super(BiomeIndex, self).index())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public dev.ultreon.quantum.world.gen.biome.BiomeIndex(int,double)"""
        val = _BiomeIndex(_int.valueOf(arg0), _double.valueOf(arg1))
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
        """public java.lang.String dev.ultreon.quantum.world.gen.biome.BiomeIndex.toString()"""
        return str._wrap(super(BiomeIndex, self).toString())

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
        """public int dev.ultreon.quantum.world.gen.biome.BiomeIndex.hashCode()"""
        return int._wrap(super(BiomeIndex, self).hashCode())