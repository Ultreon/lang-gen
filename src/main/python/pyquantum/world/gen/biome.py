from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator
__BiomeGenerator = __BiomeGenerator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator_Index
__Index = __BiomeGenerator_Index.Index
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Index():
    """dev.ultreon.quantum.world.gen.biome.BiomeGenerator.Index"""
 
    @staticmethod
    def __wrap(java_value: __Index) -> 'Index':
        return Index(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Index):
        """
        Dynamic initializer for Index.
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
    def biomeGenerator(self) -> BiomeGenerator:
        return BiomeGenerator.__wrap(super(__Index).biomeGenerator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'BiomeGenerator'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        val = __Index(arg0)
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

    @property
    def biomeGenerator(self, value: 'BiomeGenerator'):
        super(__Index).biomeGenerator(value)

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
    def __init__(self, arg0: 'BiomeGenerator', arg1: 'Integer'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator,java.lang.Integer)"""
        val = __Index(arg0, arg1)
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator
__BiomeGenerator = __BiomeGenerator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator_Index
__Index = __BiomeGenerator_Index.Index
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Index():
    """dev.ultreon.quantum.world.gen.biome.BiomeGenerator.Index"""
 
    @staticmethod
    def __wrap(java_value: __Index) -> 'Index':
        return Index(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Index):
        """
        Dynamic initializer for Index.
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
    def biomeGenerator(self) -> BiomeGenerator:
        return BiomeGenerator.__wrap(super(__Index).biomeGenerator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'BiomeGenerator'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        val = __Index(arg0)
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

    @property
    def biomeGenerator(self, value: 'BiomeGenerator'):
        super(__Index).biomeGenerator(value)

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
    def __init__(self, arg0: 'BiomeGenerator', arg1: 'Integer'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index(dev.ultreon.quantum.world.gen.biome.BiomeGenerator,java.lang.Integer)"""
        val = __Index(arg0, arg1)
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeGenerator$Index 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.Biomes
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.Biomes as __Biomes
__Biomes = __Biomes
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
 
class Biomes():
    """dev.ultreon.quantum.world.gen.biome.Biomes"""
 
    @staticmethod
    def __wrap(java_value: __Biomes) -> 'Biomes':
        return Biomes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Biomes):
        """
        Dynamic initializer for Biomes.
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
 
    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.OCEAN
    OCEAN: 'world.Biome' = __wrap(__world.Biome.OCEAN)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.PLAINS
    PLAINS: 'world.Biome' = __wrap(__world.Biome.PLAINS)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.FOREST
    FOREST: 'world.Biome' = __wrap(__world.Biome.FOREST)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.VOID
    VOID: 'world.Biome' = __wrap(__world.Biome.VOID)

    # public static final dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.Biomes.DESERT
    DESERT: 'world.Biome' = __wrap(__world.Biome.DESERT)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.biome.Biomes()"""
        val = __Biomes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.biome.Biomes()"""
        val = __Biomes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.world.gen.biome.Biomes.init()"""
            __Biomes.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeGenerator
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum.world import gen
except ImportError:
    gen = __import_once__("pyquantum.world.gen")

from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator
__BiomeGenerator = __BiomeGenerator
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.world.gen.TreeData as __TreeData
__TreeData = __TreeData
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.BuilderChunk as __BuilderChunk
__BuilderChunk = __BuilderChunk
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.world.gen.TreeGenerator as __TreeGenerator
__TreeGenerator = __TreeGenerator
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
from builtins import int
import java.util.List as List
 
class BiomeGenerator(pyquantum.__ServerDisposable, server.ServerDisposable):
    """dev.ultreon.quantum.world.gen.biome.BiomeGenerator"""
 
    @staticmethod
    def __wrap(java_value: __BiomeGenerator) -> 'BiomeGenerator':
        return BiomeGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiomeGenerator):
        """
        Dynamic initializer for BiomeGenerator.
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
    def getBiome(self) -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.gen.biome.BiomeGenerator.getBiome()"""
        return 'world.Biome'.__wrap(super(BiomeGenerator, self).getBiome())

    @property
    def treeGenerator(self) -> TreeGenerator:
        return TreeGenerator.__wrap(super(__BiomeGenerator).treeGenerator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.world.gen.biome.BiomeGenerator.getWorld()"""
        return 'world.World'.__wrap(super(BiomeGenerator, self).getWorld())

    @overload
    def __init__(self, arg0: 'World', arg1: 'Biome', arg2: 'DomainWarping', arg3: 'List', arg4: 'List'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.Biome,dev.ultreon.quantum.world.gen.noise.DomainWarping,java.util.List<dev.ultreon.quantum.world.gen.layer.TerrainLayer>,java.util.List<dev.ultreon.quantum.world.gen.WorldGenFeature>)"""
        val = __BiomeGenerator(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.biome.BiomeGenerator.dispose()"""
        super(BiomeGenerator, self).dispose()

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

    @property
    def treeGenerator(self, value: 'gen.TreeGenerator'):
        super(__BiomeGenerator).treeGenerator(value)

    @overload
    def createTreeData(self, arg0: 'Chunk') -> 'gen.TreeData':
        """public dev.ultreon.quantum.world.gen.TreeData dev.ultreon.quantum.world.gen.biome.BiomeGenerator.createTreeData(dev.ultreon.quantum.world.Chunk)"""
        return 'gen.TreeData'.__wrap(super(__BiomeGenerator, self).createTreeData(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def processColumn(self, arg0: 'BuilderChunk', arg1: int, arg2: int, arg3: int, arg4: 'Collection') -> 'world.BuilderChunk':
        """public dev.ultreon.quantum.world.BuilderChunk dev.ultreon.quantum.world.gen.biome.BiomeGenerator.processColumn(dev.ultreon.quantum.world.BuilderChunk,int,int,int,java.util.Collection<dev.ultreon.quantum.world.ServerWorld$RecordedChange>)"""
        return 'world.BuilderChunk'.__wrap(super(__BiomeGenerator, self).processColumn(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def generateTerrainFeatures(self, arg0: 'RecordingChunk', arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.world.gen.biome.BiomeGenerator.generateTerrainFeatures(dev.ultreon.quantum.world.gen.RecordingChunk,int,int,int)"""
        super(__BiomeGenerator, self).generateTerrainFeatures(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeData
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.biome.BiomeGenerator as __BiomeGenerator
__BiomeGenerator = __BiomeGenerator
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.quantum.world.gen.biome.BiomeData as __BiomeData
__BiomeData = __BiomeData
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BiomeData():
    """dev.ultreon.quantum.world.gen.biome.BiomeData"""
 
    @staticmethod
    def __wrap(java_value: __BiomeData) -> 'BiomeData':
        return BiomeData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiomeData):
        """
        Dynamic initializer for BiomeData.
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
    def biomeGen(self) -> 'BiomeGenerator':
        """public dev.ultreon.quantum.world.gen.biome.BiomeGenerator dev.ultreon.quantum.world.gen.biome.BiomeData.biomeGen()"""
        return 'BiomeGenerator'.__wrap(super(BiomeData, self).biomeGen())

    @overload
    def temperatureStartThreshold(self) -> float:
        """public float dev.ultreon.quantum.world.gen.biome.BiomeData.temperatureStartThreshold()"""
        return float.__wrap(super(BiomeData, self).temperatureStartThreshold())

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
    def __init__(self, arg0: float, arg1: float, arg2: bool, arg3: 'BiomeGenerator'):
        """public dev.ultreon.quantum.world.gen.biome.BiomeData(float,float,boolean,dev.ultreon.quantum.world.gen.biome.BiomeGenerator)"""
        val = __BiomeData(__float.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2), arg3)
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
        """public int dev.ultreon.quantum.world.gen.biome.BiomeData.hashCode()"""
        return int.__wrap(super(BiomeData, self).hashCode())

    @overload
    def isOcean(self) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.biome.BiomeData.isOcean()"""
        return bool.__wrap(super(BiomeData, self).isOcean())

    @overload
    def temperatureEndThreshold(self) -> float:
        """public float dev.ultreon.quantum.world.gen.biome.BiomeData.temperatureEndThreshold()"""
        return float.__wrap(super(BiomeData, self).temperatureEndThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.biome.BiomeData.equals(java.lang.Object)"""
        return bool.__wrap(super(__BiomeData, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.gen.biome.BiomeData.toString()"""
        return str.__wrap(super(BiomeData, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder as __BiomeCenterFinder
__BiomeCenterFinder = __BiomeCenterFinder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BiomeCenterFinder():
    """dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder"""
 
    @staticmethod
    def __wrap(java_value: __BiomeCenterFinder) -> 'BiomeCenterFinder':
        return BiomeCenterFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiomeCenterFinder):
        """
        Dynamic initializer for BiomeCenterFinder.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder()"""
        val = __BiomeCenterFinder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.biome.BiomeCenterFinder()"""
        val = __BiomeCenterFinder()
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.biome.BiomeIndex
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
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
import dev.ultreon.quantum.world.gen.biome.BiomeIndex as __BiomeIndex
__BiomeIndex = __BiomeIndex
from builtins import bool
from builtins import int
 
class BiomeIndex():
    """dev.ultreon.quantum.world.gen.biome.BiomeIndex"""
 
    @staticmethod
    def __wrap(java_value: __BiomeIndex) -> 'BiomeIndex':
        return BiomeIndex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiomeIndex):
        """
        Dynamic initializer for BiomeIndex.
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

    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.world.gen.biome.BiomeIndex.index()"""
        return int.__wrap(super(BiomeIndex, self).index())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.gen.biome.BiomeIndex.toString()"""
        return str.__wrap(super(BiomeIndex, self).toString())

    @overload
    def distance(self) -> float:
        """public double dev.ultreon.quantum.world.gen.biome.BiomeIndex.distance()"""
        return float.__wrap(super(BiomeIndex, self).distance())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.biome.BiomeIndex.equals(java.lang.Object)"""
        return bool.__wrap(super(__BiomeIndex, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.gen.biome.BiomeIndex.hashCode()"""
        return int.__wrap(super(BiomeIndex, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public dev.ultreon.quantum.world.gen.biome.BiomeIndex(int,double)"""
        val = __BiomeIndex(__int.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val