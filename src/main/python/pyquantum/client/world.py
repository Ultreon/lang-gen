from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.world.ChunkMesh as __ChunkMesh
__ChunkMesh = __ChunkMesh
import dev.ultreon.quantum.client.world.ClientChunk as __ClientChunk
__ClientChunk = __ClientChunk
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ChunkMesh():
    """dev.ultreon.quantum.client.world.ChunkMesh"""
 
    @staticmethod
    def __wrap(java_value: __ChunkMesh) -> 'ChunkMesh':
        return ChunkMesh(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkMesh):
        """
        Dynamic initializer for ChunkMesh.
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
    def __init__(self):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = __ChunkMesh()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = __ChunkMesh()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @property
    def chunk(self) -> ClientChunk:
        return ClientChunk.__wrap(super(__ChunkMesh).chunk())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def chunk(self, value: 'ClientChunk'):
        super(__ChunkMesh).chunk(value)

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
    def __init__(self, arg0: 'Mesh', arg1: 'Material'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Material)"""
        val = __ChunkMesh(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getMeshesDisposed() -> int:
        """public static long dev.ultreon.quantum.client.world.ChunkMesh.getMeshesDisposed()"""
        return int.__wrap(__ChunkMesh.getMeshesDisposed())

    @override
    @overload
    def reset(self):
        """public void dev.ultreon.quantum.client.world.ChunkMesh.reset()"""
        super(ChunkMesh, self).reset()

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
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = __ChunkMesh(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Mesh'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh)"""
        val = __ChunkMesh(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.world.ChunkMesh
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.world.ChunkMesh as __ChunkMesh
__ChunkMesh = __ChunkMesh
import dev.ultreon.quantum.client.world.ClientChunk as __ClientChunk
__ClientChunk = __ClientChunk
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ChunkMesh():
    """dev.ultreon.quantum.client.world.ChunkMesh"""
 
    @staticmethod
    def __wrap(java_value: __ChunkMesh) -> 'ChunkMesh':
        return ChunkMesh(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkMesh):
        """
        Dynamic initializer for ChunkMesh.
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
    def __init__(self):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = __ChunkMesh()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = __ChunkMesh()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @property
    def chunk(self) -> ClientChunk:
        return ClientChunk.__wrap(super(__ChunkMesh).chunk())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def chunk(self, value: 'ClientChunk'):
        super(__ChunkMesh).chunk(value)

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
    def __init__(self, arg0: 'Mesh', arg1: 'Material'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Material)"""
        val = __ChunkMesh(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getMeshesDisposed() -> int:
        """public static long dev.ultreon.quantum.client.world.ChunkMesh.getMeshesDisposed()"""
        return int.__wrap(__ChunkMesh.getMeshesDisposed())

    @override
    @overload
    def reset(self):
        """public void dev.ultreon.quantum.client.world.ChunkMesh.reset()"""
        super(ChunkMesh, self).reset()

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
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = __ChunkMesh(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Mesh'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh)"""
        val = __ChunkMesh(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.world.ChunkMesh 
 
 
# CLASS: dev.ultreon.quantum.client.world.FaceProperties
from builtins import str
import dev.ultreon.quantum.client.world.FaceProperties as __FaceProperties
__FaceProperties = __FaceProperties
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.world.FaceProperties as __FaceProperties_Builder
__Builder = __FaceProperties_Builder.Builder
from builtins import int
 
class FaceProperties():
    """dev.ultreon.quantum.client.world.FaceProperties"""
 
    @staticmethod
    def __wrap(java_value: __FaceProperties) -> 'FaceProperties':
        return FaceProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FaceProperties):
        """
        Dynamic initializer for FaceProperties.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.world.FaceProperties.equals(java.lang.Object)"""
        return bool.__wrap(super(__FaceProperties, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.FaceProperties()"""
        val = __FaceProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.world.FaceProperties.hashCode()"""
        return int.__wrap(super(FaceProperties, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.world.FaceProperties()"""
        val = __FaceProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.client.world.FaceProperties$Builder dev.ultreon.quantum.client.world.FaceProperties.builder()"""
        return Builder.__wrap(__FaceProperties.builder())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.world.Skybox
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.client.world.Skybox as __Skybox
__Skybox = __Skybox
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Skybox():
    """dev.ultreon.quantum.client.world.Skybox"""
 
    @staticmethod
    def __wrap(java_value: __Skybox) -> 'Skybox':
        return Skybox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Skybox):
        """
        Dynamic initializer for Skybox.
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
    def update(self, arg0: int):
        """public void dev.ultreon.quantum.client.world.Skybox.update(int)"""
        super(__Skybox, self).update(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.Skybox()"""
        val = __Skybox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.world.Skybox()"""
        val = __Skybox()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.world.ClientChunk
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
import dev.ultreon.quantum.client.world.ClientWorld as __ClientWorld
__ClientWorld = __ClientWorld
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.client.world.ClientChunk as __ClientChunk
__ClientChunk = __ClientChunk
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
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.world.Biome as __Biome
__Biome = __Biome
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.world.BreakResult as __BreakResult
__BreakResult = __BreakResult
import java.lang.Runnable as Runnable
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
from builtins import object
import dev.ultreon.quantum.client.QuantumClient as __QuantumClient
__QuantumClient = __QuantumClient
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

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

 
class ClientChunk():
    """dev.ultreon.quantum.client.world.ClientChunk"""
 
    @staticmethod
    def __wrap(java_value: __ClientChunk) -> 'ClientChunk':
        return ClientChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientChunk):
        """
        Dynamic initializer for ClientChunk.
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
 
    # public static final dev.ultreon.quantum.client.world.RenderablePool dev.ultreon.quantum.client.world.ClientChunk.RENDERABLE_POOL
    RENDERABLE_POOL: 'RenderablePool' = __wrap(__RenderablePool.RENDERABLE_POOL)


    @override
    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool.__wrap(super(world.Chunk, self).isReady())

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int.__wrap(super(__world.Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'world.Biome'.__wrap(super(__world.Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getLightLevel(self, arg0: int, arg1: int, arg2: int) -> float:
        """public float dev.ultreon.quantum.client.world.ClientChunk.getLightLevel(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return float.__wrap(super(__ClientChunk, self).getLightLevel(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'world.ChunkPos'.__wrap(super(world.Chunk, self).getPos())

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int)"""
        return int.__wrap(super(__world.Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ClientWorld', arg1: int, arg2: int, arg3: 'ChunkPos', arg4: 'Storage', arg5: 'Storage', arg6: 'Map'):
        """public dev.ultreon.quantum.client.world.ClientChunk(dev.ultreon.quantum.client.world.ClientWorld,int,int,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        val = __ClientChunk(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, arg6)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCustomRendered(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.state.BlockProperties> dev.ultreon.quantum.client.world.ClientChunk.getCustomRendered()"""
        return 'Map'.__wrap(super(ClientChunk, self).getCustomRendered())

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__world.Chunk, self).getSunlight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool.__wrap(super(world.Chunk, self).isActive())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block.__wrap(__Chunk.decodeBlock(arg0))

    @override
    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'.__wrap(super(world.Chunk, self).getBlockEntities())

    @overload
    def getBounds(self) -> object:
        """public java.lang.Object dev.ultreon.quantum.client.world.ClientChunk.getBounds()"""
        return object.__wrap(super(ClientChunk, self).getBounds())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__world.Chunk, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int.__wrap(super(__world.Chunk, self).getBlockLight(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__ClientChunk, self).setFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @property
    def biomeStorage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).biomeStorage())

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__world.Chunk, self).get(arg0))

    @override
    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(__world.Chunk, self).stopBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(__Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'.__wrap(super(__world.Chunk, self).getBlockEntity(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__world.Chunk, self).get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int.__wrap(super(world.Chunk, self).hashCode())

    @overload
    def updated(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.updated()"""
        super(ClientChunk, self).updated()

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.client.world.ClientChunk.getFast(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__ClientChunk, self).getFast(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str.__wrap(super(world.Chunk, self).toString())

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'.__wrap(super(__world.Chunk, self).getFast(arg0))

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__world.Chunk, self).getSunlight(arg0))

    @overload
    def __init__(self, arg0: 'ClientWorld', arg1: 'ChunkPos', arg2: 'Storage', arg3: 'Storage', arg4: 'Map'):
        """public dev.ultreon.quantum.client.world.ClientChunk(dev.ultreon.quantum.client.world.ClientWorld,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        val = __ClientChunk(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__world.Chunk, self).getBlockLight(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float.__wrap(super(__world.Chunk, self).getBrightness(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.onUpdated()"""
        super(ClientChunk, self).onUpdated()

    @overload
    def whileLocked(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.whileLocked(java.lang.Runnable)"""
        super(__ClientChunk, self).whileLocked(arg0)

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'world.Biome'.__wrap(super(__world.Chunk, self).getBiome(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool.__wrap(super(__world.Chunk, self).equals(arg0))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties.__wrap(__Chunk.loadBlock(arg0))

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__world.Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'.__wrap(super(world.Chunk, self).getOffset())

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool.__wrap(super(world.Chunk, self).isDisposed())

    @overload
    def addModel(self, arg0: 'BlockPos', arg1: 'ModelInstance') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.world.ClientChunk.addModel(dev.ultreon.quantum.world.BlockPos,com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        return 'g3d.ModelInstance'.__wrap(super(__ClientChunk, self).addModel(arg0, arg1))

    @override
    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(__world.Chunk, self).setTreeData(arg0)

    @property
    def treeData(self) -> TreeData:
        return TreeData.__wrap(super(__Chunk).treeData())

    @override
    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(__world.Chunk, self).startBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientChunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__ClientChunk, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def getWorld(self) -> 'ClientWorld':
        """public dev.ultreon.quantum.client.world.ClientWorld dev.ultreon.quantum.client.world.ClientChunk.getWorld()"""
        return 'ClientWorld'.__wrap(super(ClientChunk, self).getWorld())

    @property
    def storage(self) -> Storage:
        return Storage.__wrap(super(__Chunk).storage())

    @overload
    def loadCustomRendered(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.loadCustomRendered()"""
        super(ClientChunk, self).loadCustomRendered()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.dispose()"""
        super(ClientChunk, self).dispose()

    @overload
    def renderModels(self, arg0: 'Scene3D'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.renderModels(dev.ultreon.quantum.client.render.Scene3D)"""
        super(__ClientChunk, self).renderModels(arg0)

    @overload
    def getClient(self) -> 'client.QuantumClient':
        """public dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.world.ClientChunk.getClient()"""
        return 'client.QuantumClient'.__wrap(super(ClientChunk, self).getClient())

    @override
    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__ClientChunk, self).set(arg0, arg1)

    @override
    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__ClientChunk, self).setFast(arg0, arg1)

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int.__wrap(super(__world.Chunk, self).ascend(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'.__wrap(super(__world.Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'.__wrap(super(world.Chunk, self).getBreaking())

    @override
    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(__world.Chunk, self).removeBlockEntity(arg0)

    @overload
    def destroyModels(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.destroyModels()"""
        super(ClientChunk, self).destroyModels()

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int.__wrap(super(__world.Chunk, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'world.BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'world.BreakResult'.__wrap(super(__world.Chunk, self).continueBreaking(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))) 
 
 
# CLASS: dev.ultreon.quantum.client.world.ClientWorld
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.util.EntityHitResult as __EntityHitResult
__EntityHitResult = __EntityHitResult
import java.util.function.Predicate as Predicate
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
import dev.ultreon.quantum.client.world.ClientWorld as __ClientWorld
__ClientWorld = __ClientWorld
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.world.ClientChunk as __ClientChunk
__ClientChunk = __ClientChunk
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
import dev.ultreon.quantum.client.util.Rot as __Rot
__Rot = __Rot
import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

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
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
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
try:
    from pyquantum.client import util
except ImportError:
    util = __import_once__("pyquantum.client.util")

import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

import java.util.List as List
 
class ClientWorld():
    """dev.ultreon.quantum.client.world.ClientWorld"""
 
    @staticmethod
    def __wrap(java_value: __ClientWorld) -> 'ClientWorld':
        return ClientWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientWorld):
        """
        Dynamic initializer for ClientWorld.
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
    def unloadChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.unloadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__world.World, self).unloadChunk(arg0))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.World.getHighest(int,int)"""
        return int.__wrap(super(__world.World, self).getHighest(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def updateChunkAndNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunkAndNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(__world.World, self).updateChunkAndNeighbours(arg0)

    @overload
    def isAlwaysLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isAlwaysLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__world.World, self).isAlwaysLoaded(arg0))

    @staticmethod
    @property
    def DAY_BOTTOM_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the DAY_BOTTOM_COLOR property.
     
        :param value: Value to set for the DAY_BOTTOM_COLOR property.
        """
     
        super('util.RgbColor').DAY_BOTTOM_COLOR(value)

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__world.World, self).drop(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.world.ClientWorld.playSound(dev.ultreon.quantum.world.SoundEvent,double,double,double)"""
        super(__ClientWorld, self).playSound(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @override
    @overload
    def updateNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(__world.World, self).updateNeighbours(arg0)

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'EntityType') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'util.EntityHitResult'.__wrap(super(__world.World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @override
    @overload
    def despawn(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.world.World.despawn(dev.ultreon.quantum.entity.Entity)"""
        super(__world.World, self).despawn(arg0)

    @staticmethod
    @property
    def NIGHT_TOP_COLOR_() -> RgbColor:
        """
        Getter for the NIGHT_TOP_COLOR property.
     
        :return: Value of NIGHT_TOP_COLOR
        """
     
        return super(RgbColor).NIGHT_TOP_COLOR()

    @staticmethod
    @property
    def SUN_RISE_COLOR_() -> RgbColor:
        """
        Getter for the SUN_RISE_COLOR property.
     
        :return: Value of SUN_RISE_COLOR
        """
     
        return super(RgbColor).SUN_RISE_COLOR()

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool.__wrap(super(__world.World, self).set(arg0, arg1, __int.valueOf(arg2)))

    @override
    @overload
    def setSpawnPoint(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.world.World.setSpawnPoint(int,int)"""
        super(__world.World, self).setSpawnPoint(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.client.world.ClientWorld.getRenderDistance()"""
        return int.__wrap(super(ClientWorld, self).getRenderDistance())

    @override
    @overload
    def stopBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.stopBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__ClientWorld, self).stopBreaking(arg0, arg1)

    @override
    @overload
    def getSeed(self) -> int:
        """public long dev.ultreon.quantum.world.World.getSeed()"""
        return int.__wrap(super(world.World, self).getSeed())

    @overload
    def getBreakProgress(self, arg0: 'BlockPos') -> float:
        """public float dev.ultreon.quantum.world.World.getBreakProgress(dev.ultreon.quantum.world.BlockPos)"""
        return float.__wrap(super(__world.World, self).getBreakProgress(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'BlockProperties') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.world.World.set(int,int,int,int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'CompletableFuture'.__wrap(super(__world.World, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6))

    @overload
    def isChunkInvalidated(self, arg0: 'Chunk') -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientWorld.isChunkInvalidated(dev.ultreon.quantum.world.Chunk)"""
        return bool.__wrap(super(__ClientWorld, self).isChunkInvalidated(arg0))

    @staticmethod
    @property
    def SUN_RISE_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the SUN_RISE_COLOR property.
     
        :param value: Value to set for the SUN_RISE_COLOR property.
        """
     
        super('util.RgbColor').SUN_RISE_COLOR(value)

    @override
    @overload
    def onChunkUpdated(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.onChunkUpdated(dev.ultreon.quantum.world.Chunk)"""
        super(__ClientWorld, self).onChunkUpdated(arg0)

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'.__wrap(super(__world.World, self).get(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vector3') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(com.badlogic.gdx.math.Vector3)"""
        return world.ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @property
    def DAY_TOP_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the DAY_TOP_COLOR property.
     
        :param value: Value to set for the DAY_TOP_COLOR property.
        """
     
        super('util.RgbColor').DAY_TOP_COLOR(value)

    @override
    @overload
    def isClientSide(self) -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientWorld.isClientSide()"""
        return bool.__wrap(super(ClientWorld, self).isClientSide())

    @overload
    def entitiesWithinDst(self, arg0: 'Entity', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.entitiesWithinDst(dev.ultreon.quantum.entity.Entity,int)"""
        return 'List'.__wrap(super(__world.World, self).entitiesWithinDst(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.world.ClientWorld(dev.ultreon.quantum.client.QuantumClient)"""
        val = __ClientWorld(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @property
    def NIGHT_TOP_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the NIGHT_TOP_COLOR property.
     
        :param value: Value to set for the NIGHT_TOP_COLOR property.
        """
     
        super('util.RgbColor').NIGHT_TOP_COLOR(value)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__world.World, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__world.World, self).setColumn(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @property
    def DAY_BOTTOM_COLOR_() -> RgbColor:
        """
        Getter for the DAY_BOTTOM_COLOR property.
     
        :return: Value of DAY_BOTTOM_COLOR
        """
     
        return super(RgbColor).DAY_BOTTOM_COLOR()

    @override
    @overload
    def fillCrashInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.world.World.fillCrashInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(__world.World, self).fillCrashInfo(arg0)

    @overload
    def isSpawnChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isSpawnChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__world.World, self).isSpawnChunk(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3d') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return world.ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: 'ChunkPos') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return world.ChunkPos.__wrap(__World.toLocalChunkPos(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getChunkAt(self, arg0: int, arg1: int, arg2: int) -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunkAt(int,int,int)"""
        return 'ClientChunk'.__wrap(super(__ClientWorld, self).getChunkAt(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def spawn(self, arg0: 'Entity') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T)"""
        return 'entity.Entity'.__wrap(super(__world.World, self).spawn(arg0))

    @overload
    def rayCast(self, arg0: 'Ray', arg1: float) -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.BlockHitResult'.__wrap(super(__world.World, self).rayCast(arg0, __float.valueOf(arg1)))

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.client.world.ClientWorld.tick()"""
        super(ClientWorld, self).tick()

    @overload
    def getGlobalSunlight(self) -> float:
        """public float dev.ultreon.quantum.client.world.ClientWorld.getGlobalSunlight()"""
        return float.__wrap(super(ClientWorld, self).getGlobalSunlight())

    @overload
    def getChunk(self, arg0: 'ChunkPos') -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'ClientChunk'.__wrap(super(__ClientWorld, self).getChunk(arg0))

    @overload
    def removeEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.client.world.ClientWorld.removeEntity(int)"""
        return 'entity.Entity'.__wrap(super(__ClientWorld, self).removeEntity(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isOutOfWorldBounds(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(int,int,int)"""
        return bool.__wrap(super(__world.World, self).isOutOfWorldBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Class') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'.__wrap(super(__world.World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @overload
    def getBiome(self, arg0: 'BlockPos') -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.World.getBiome(dev.ultreon.quantum.world.BlockPos)"""
        return 'world.Biome'.__wrap(super(__world.World, self).getBiome(arg0))

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: int, arg1: int) -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(int,int)"""
        return world.ChunkPos.__wrap(__World.toLocalChunkPos(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getAllEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.client.world.ClientWorld.getAllEntities()"""
        return 'Collection'.__wrap(super(ClientWorld, self).getAllEntities())

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.World.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'.__wrap(super(__world.World, self).getBlockEntity(arg0))

    @overload
    def intersectEntities(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.world.World.intersectEntities(dev.ultreon.quantum.util.BoundingBox)"""
        return bool.__wrap(super(__world.World, self).intersectEntities(arg0))

    @staticmethod
    @property
    def NIGHT_BOTTOM_COLOR_() -> RgbColor:
        """
        Getter for the NIGHT_BOTTOM_COLOR property.
     
        :return: Value of NIGHT_BOTTOM_COLOR
        """
     
        return super(RgbColor).NIGHT_BOTTOM_COLOR()

    @staticmethod
    @property
    def SKYBOX_ROTATION_() -> Rot:
        """
        Getter for the SKYBOX_ROTATION property.
     
        :return: Value of SKYBOX_ROTATION
        """
     
        return super(Rot).SKYBOX_ROTATION()

    @override
    @overload
    def startBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.startBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__ClientWorld, self).startBreaking(arg0, arg1)

    @override
    @overload
    def getEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntities()"""
        return 'Collection'.__wrap(super(world.World, self).getEntities())

    @staticmethod
    @property
    def NIGHT_BOTTOM_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the NIGHT_BOTTOM_COLOR property.
     
        :param value: Value to set for the NIGHT_BOTTOM_COLOR property.
        """
     
        super('util.RgbColor').NIGHT_BOTTOM_COLOR(value)

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__world.World, self).setColumn(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: 'BlockPos') -> 'world.BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return world.BlockPos.__wrap(__World.toLocalBlockPos(arg0))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float) -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.EntityHitResult'.__wrap(super(__world.World, self).rayCastEntity(arg0, __float.valueOf(arg1)))

    @overload
    def getChunksAround(self, arg0: 'Vec3d') -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.World.getChunksAround(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'List'.__wrap(super(__world.World, self).getChunksAround(arg0))

    @overload
    def getSkyColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.world.ClientWorld.getSkyColor()"""
        return 'util.RgbColor'.__wrap(super(ClientWorld, self).getSkyColor())

    @overload
    def getEntitiesByClass(self, arg0: 'Class') -> 'Collection':
        """public <T extends dev.ultreon.quantum.entity.Entity> java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntitiesByClass(java.lang.Class<T>)"""
        return 'Collection'.__wrap(super(__world.World, self).getEntitiesByClass(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientWorld.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool.__wrap(super(__ClientWorld, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4)))

    @override
    @overload
    def getChunksLoaded(self) -> int:
        """public int dev.ultreon.quantum.world.World.getChunksLoaded()"""
        return int.__wrap(super(world.World, self).getChunksLoaded())

    @overload
    def getChunk(self, arg0: int, arg1: int) -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunk(int,int)"""
        return 'ClientChunk'.__wrap(super(__ClientWorld, self).getChunk(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int) -> 'world.BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int)"""
        return world.BlockPos.__wrap(__World.toLocalBlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def isOutOfWorldBounds(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(dev.ultreon.quantum.world.BlockPos)"""
        return bool.__wrap(super(__world.World, self).isOutOfWorldBounds(arg0))

    @override
    @overload
    def getDimension(self) -> 'world.DimensionInfo':
        """public dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.World.getDimension()"""
        return 'world.DimensionInfo'.__wrap(super(world.World, self).getDimension())

    @override
    @overload
    def getUID(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.world.World.getUID()"""
        return 'UUID'.__wrap(super(world.World, self).getUID())

    @overload
    def setDaytime(self, arg0: int):
        """public void dev.ultreon.quantum.client.world.ClientWorld.setDaytime(int)"""
        super(__ClientWorld, self).setDaytime(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def continueBreaking(self, arg0: 'BlockPos', arg1: float, arg2: 'Player') -> 'world.BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.client.world.ClientWorld.continueBreaking(dev.ultreon.quantum.world.BlockPos,float,dev.ultreon.quantum.entity.player.Player)"""
        return 'world.BreakResult'.__wrap(super(__ClientWorld, self).continueBreaking(arg0, __float.valueOf(arg1), arg2))

    @overload
    def rayCastEntity(self, arg0: 'Ray') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray)"""
        return 'util.EntityHitResult'.__wrap(super(__world.World, self).rayCastEntity(arg0))

    @overload
    def rayCast(self, arg0: 'Ray') -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray)"""
        return 'util.BlockHitResult'.__wrap(super(__world.World, self).rayCast(arg0))

    @override
    @overload
    def closeMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.closeMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__world.World, self).closeMenu(arg0)

    @override
    @overload
    def getTotalChunks(self) -> int:
        """public int dev.ultreon.quantum.client.world.ClientWorld.getTotalChunks()"""
        return int.__wrap(super(ClientWorld, self).getTotalChunks())

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__world.World, self).set(arg0, arg1))

    @override
    @overload
    def despawn(self, arg0: int):
        """public void dev.ultreon.quantum.world.World.despawn(int)"""
        super(__world.World, self).despawn(__int.valueOf(arg0))

    @override
    @overload
    def spawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.client.world.ClientWorld.spawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(__ClientWorld, self).spawnParticles(arg0, arg1, arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def toChunkVec(arg0: int, arg1: int, arg2: int) -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(int,int,int)"""
        return vector.Vec2i.__wrap(__World.toChunkVec(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @property
    def SKYBOX_ROTATION_(value: 'util.Rot'):
        """
        Setter for the SKYBOX_ROTATION property.
     
        :param value: Value to set for the SKYBOX_ROTATION property.
        """
     
        super('util.Rot').SKYBOX_ROTATION(value)

    @overload
    def getEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.world.World.getEntity(int)"""
        return 'entity.Entity'.__wrap(super(__world.World, self).getEntity(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def toChunkPos(arg0: int, arg1: int, arg2: int) -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(int,int,int)"""
        return world.ChunkPos.__wrap(__World.toChunkPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def collide(self, arg0: 'BoundingBox', arg1: bool) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.BoundingBox> dev.ultreon.quantum.world.World.collide(dev.ultreon.quantum.util.BoundingBox,boolean)"""
        return 'List'.__wrap(super(__world.World, self).collide(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def getLoadedChunks(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.client.world.ClientChunk> dev.ultreon.quantum.client.world.ClientWorld.getLoadedChunks()"""
        return 'Collection'.__wrap(super(ClientWorld, self).getLoadedChunks())

    @overload
    def onPlayerAttack(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.world.ClientWorld.onPlayerAttack(int,int)"""
        super(__ClientWorld, self).onPlayerAttack(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.world.ClientWorld.dispose()"""
        super(ClientWorld, self).dispose()

    @override
    @overload
    def setBlockEntity(self, arg0: 'BlockPos', arg1: 'BlockEntity'):
        """public void dev.ultreon.quantum.world.World.setBlockEntity(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntity)"""
        super(__world.World, self).setBlockEntity(arg0, arg1)

    @override
    @overload
    def isServerSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isServerSide()"""
        return bool.__wrap(super(world.World, self).isServerSide())

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(int,int,int)"""
        return 'state.BlockProperties'.__wrap(super(__world.World, self).get(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getSpawnPoint(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.getSpawnPoint()"""
        return 'world.BlockPos'.__wrap(super(world.World, self).getSpawnPoint())

    @override
    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__world.World, self).openMenu(arg0)

    @overload
    def getChunkAt(self, arg0: 'BlockPos') -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunkAt(dev.ultreon.quantum.world.BlockPos)"""
        return 'ClientChunk'.__wrap(super(__ClientWorld, self).getChunkAt(arg0))

    @staticmethod
    @property
    def DAY_TOP_COLOR_() -> RgbColor:
        """
        Getter for the DAY_TOP_COLOR property.
     
        :return: Value of DAY_TOP_COLOR
        """
     
        return super(RgbColor).DAY_TOP_COLOR()

    @overload
    def loadChunk(self, arg0: 'ChunkPos', arg1: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.loadChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__ClientWorld, self).loadChunk(arg0, arg1)

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3i') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return world.ChunkPos.__wrap(__World.blockToChunkPos(arg0))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int, arg3: 'Vec3i') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return vector.Vec3i.__wrap(__World.toLocalBlockPos(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def updateChunk(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.updateChunk(dev.ultreon.quantum.world.Chunk)"""
        super(__ClientWorld, self).updateChunk(arg0)

    @overload
    def addEntity(self, arg0: int, arg1: 'EntityType', arg2: 'Vec3d', arg3: 'MapType'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.addEntity(int,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.ubo.types.MapType)"""
        super(__ClientWorld, self).addEntity(__int.valueOf(arg0), arg1, arg2, arg3)

    @overload
    def spawn(self, arg0: 'Entity', arg1: 'MapType') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T,dev.ultreon.ubo.types.MapType)"""
        return 'entity.Entity'.__wrap(super(__world.World, self).spawn(arg0, arg1))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isDisposed()"""
        return bool.__wrap(super(world.World, self).isDisposed())

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Predicate') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.util.function.Predicate<dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'.__wrap(super(__world.World, self).rayCastEntity(arg0, __float.valueOf(arg1), arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def destroyBlock(self, arg0: 'BlockPos', arg1: 'Player') -> bool:
        """public boolean dev.ultreon.quantum.world.World.destroyBlock(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        return bool.__wrap(super(__world.World, self).destroyBlock(arg0, arg1))

    @staticmethod
    @overload
    def toChunkVec(arg0: 'BlockPos') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(dev.ultreon.quantum.world.BlockPos)"""
        return vector.Vec2i.__wrap(__World.toChunkVec(arg0))

    @overload
    def getDaytime(self) -> int:
        """public int dev.ultreon.quantum.client.world.ClientWorld.getDaytime()"""
        return int.__wrap(super(ClientWorld, self).getDaytime())

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__world.World, self).drop(arg0, arg1, arg2)

    @staticmethod
    @overload
    def toChunkPos(arg0: 'BlockPos') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(dev.ultreon.quantum.world.BlockPos)"""
        return world.ChunkPos.__wrap(__World.toChunkPos(arg0))

    @overload
    def collideEntities(self, arg0: 'Entity', arg1: 'BoundingBox') -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.collideEntities(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.util.BoundingBox)"""
        return 'List'.__wrap(super(__world.World, self).collideEntities(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.quantum.client.world.FaceProperties$Builder
from builtins import str
import dev.ultreon.quantum.client.world.FaceProperties as __FaceProperties
__FaceProperties = __FaceProperties
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.world.FaceProperties as __FaceProperties_Builder
__Builder = __FaceProperties_Builder.Builder
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.client.world.FaceProperties.Builder"""
 
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
    def __init__(self):
        """public dev.ultreon.quantum.client.world.FaceProperties$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def build(self) -> 'FaceProperties':
        """public dev.ultreon.quantum.client.world.FaceProperties dev.ultreon.quantum.client.world.FaceProperties$Builder.build()"""
        return 'FaceProperties'.__wrap(super(Builder, self).build())

    @overload
    def randomRotation(self) -> 'Builder':
        """public dev.ultreon.quantum.client.world.FaceProperties$Builder dev.ultreon.quantum.client.world.FaceProperties$Builder.randomRotation()"""
        return 'Builder'.__wrap(super(Builder, self).randomRotation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.FaceProperties$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.world.WorldRenderer
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleSystem as __ParticleSystem
__ParticleSystem = __ParticleSystem
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.client.world.WorldRenderer as __WorldRenderer
__WorldRenderer = __WorldRenderer
try:
    from pyquantum.client import management
except ImportError:
    management = __import_once__("pyquantum.client.management")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.Environment as __Environment
__Environment = __Environment
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.world.Skybox as __Skybox
__Skybox = __Skybox
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class WorldRenderer():
    """dev.ultreon.quantum.client.world.WorldRenderer"""
 
    @staticmethod
    def __wrap(java_value: __WorldRenderer) -> 'WorldRenderer':
        return WorldRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldRenderer):
        """
        Dynamic initializer for WorldRenderer.
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
    def addParticles(self, arg0: 'ParticleEffect', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.addParticles(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(__WorldRenderer, self).addParticles(arg0, arg1, arg2, __int.valueOf(arg3))

    @overload
    def getTransparentMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.world.WorldRenderer.getTransparentMaterial()"""
        return 'g3d.Material'.__wrap(super(WorldRenderer, self).getTransparentMaterial())

    @overload
    def getEnvironment(self) -> 'g3d.Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment dev.ultreon.quantum.client.world.WorldRenderer.getEnvironment()"""
        return 'g3d.Environment'.__wrap(super(WorldRenderer, self).getEnvironment())

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.world.WorldRenderer.isDisposed()"""
        return bool.__wrap(super(WorldRenderer, self).isDisposed())

    @overload
    def getVisibleChunks(self) -> int:
        """public int dev.ultreon.quantum.client.world.WorldRenderer.getVisibleChunks()"""
        return int.__wrap(super(WorldRenderer, self).getVisibleChunks())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.world.WorldRenderer.getMaterial()"""
        return 'g3d.Material'.__wrap(super(WorldRenderer, self).getMaterial())

    @overload
    def render(self, arg0: 'Scene3D'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.render(dev.ultreon.quantum.client.render.Scene3D)"""
        super(__WorldRenderer, self).render(arg0)

    @overload
    def collectEntity(self, arg0: 'Entity', arg1: 'Scene3D'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.collectEntity(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.client.render.Scene3D)"""
        super(__WorldRenderer, self).collectEntity(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.dispose()"""
        super(WorldRenderer, self).dispose()

    @overload
    def getParticleSystem(self) -> 'particles.ParticleSystem':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSystem dev.ultreon.quantum.client.world.WorldRenderer.getParticleSystem()"""
        return 'particles.ParticleSystem'.__wrap(super(WorldRenderer, self).getParticleSystem())

    @overload
    def getBreakingTex(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.world.WorldRenderer.getBreakingTex()"""
        return 'graphics.Texture'.__wrap(super(WorldRenderer, self).getBreakingTex())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def buildOutlineBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'MeshPartBuilder'):
        """public static void dev.ultreon.quantum.client.world.WorldRenderer.buildOutlineBox(float,float,float,float,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        __WorldRenderer.buildOutlineBox(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def getLoadedChunks(self) -> int:
        """public int dev.ultreon.quantum.client.world.WorldRenderer.getLoadedChunks()"""
        return int.__wrap(super(WorldRenderer, self).getLoadedChunks())

    @staticmethod
    @overload
    def getVertexCount() -> int:
        """public static long dev.ultreon.quantum.client.world.WorldRenderer.getVertexCount()"""
        return int.__wrap(__WorldRenderer.getVertexCount())

    @staticmethod
    @overload
    def getPoolMax() -> int:
        """public static int dev.ultreon.quantum.client.world.WorldRenderer.getPoolMax()"""
        return int.__wrap(__WorldRenderer.getPoolMax())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def remove(self, arg0: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.remove(dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__WorldRenderer, self).remove(arg0)

    @overload
    def reload(self, arg0: 'ReloadContext', arg1: 'MaterialManager'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.reload(dev.ultreon.quantum.resources.ReloadContext,dev.ultreon.quantum.client.management.MaterialManager)"""
        super(__WorldRenderer, self).reload(arg0, arg1)

    @overload
    def updateBackground(self):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.updateBackground()"""
        super(WorldRenderer, self).updateBackground()

    @overload
    def getSkybox(self) -> 'Skybox':
        """public dev.ultreon.quantum.client.world.Skybox dev.ultreon.quantum.client.world.WorldRenderer.getSkybox()"""
        return 'Skybox'.__wrap(super(WorldRenderer, self).getSkybox())

    @overload
    def removeEntity(self, arg0: int):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.removeEntity(int)"""
        super(__WorldRenderer, self).removeEntity(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ClientWorld'):
        """public dev.ultreon.quantum.client.world.WorldRenderer(dev.ultreon.quantum.client.world.ClientWorld)"""
        val = __WorldRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getPoolFree() -> int:
        """public static long dev.ultreon.quantum.client.world.WorldRenderer.getPoolFree()"""
        return int.__wrap(__WorldRenderer.getPoolFree())

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
    def deferDispose(self, arg0: 'Disposable') -> 'utils.Disposable':
        """public <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.world.WorldRenderer.deferDispose(T)"""
        return 'utils.Disposable'.__wrap(super(__WorldRenderer, self).deferDispose(arg0))

    @staticmethod
    @overload
    def getChunkMeshFrees() -> int:
        """public static long dev.ultreon.quantum.client.world.WorldRenderer.getChunkMeshFrees()"""
        return int.__wrap(__WorldRenderer.getChunkMeshFrees())

    @staticmethod
    @overload
    def buildLine(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'MeshPartBuilder'):
        """public static void dev.ultreon.quantum.client.world.WorldRenderer.buildLine(float,float,float,float,float,float,float,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        __WorldRenderer.buildLine(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), arg7)

    @staticmethod
    @overload
    def getPoolPeak() -> int:
        """public static int dev.ultreon.quantum.client.world.WorldRenderer.getPoolPeak()"""
        return int.__wrap(__WorldRenderer.getPoolPeak())

    @staticmethod
    @overload
    def buildOutlineBox(arg0: float, arg1: float, arg2: float, arg3: float) -> 'graphics.Mesh':
        """public static com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.world.WorldRenderer.buildOutlineBox(float,float,float,float)"""
        return graphics.Mesh.__wrap(__WorldRenderer.buildOutlineBox(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def free(self, arg0: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.free(dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__WorldRenderer, self).free(arg0)

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.client.world.WorldRenderer.getWorld()"""
        return 'world.World'.__wrap(super(WorldRenderer, self).getWorld()) 
 
 
# CLASS: dev.ultreon.quantum.client.world.RenderablePool
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.world.RenderablePool as __RenderablePool
__RenderablePool = __RenderablePool
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RenderablePool():
    """dev.ultreon.quantum.client.world.RenderablePool"""
 
    @staticmethod
    def __wrap(java_value: __RenderablePool) -> 'RenderablePool':
        return RenderablePool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderablePool):
        """
        Dynamic initializer for RenderablePool.
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
    def getObtainedCount(self) -> int:
        """public int dev.ultreon.quantum.client.world.RenderablePool.getObtainedCount()"""
        return int.__wrap(super(RenderablePool, self).getObtainedCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void dev.ultreon.quantum.client.world.RenderablePool.freeAll(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__RenderablePool, self).freeAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def obtain(self) -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable dev.ultreon.quantum.client.world.RenderablePool.obtain()"""
        return 'g3d.Renderable'.__wrap(super(RenderablePool, self).obtain())

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__utils.Pool, self).fill(__int.valueOf(arg0))

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(utils.Pool, self).getFree())

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.world.RenderablePool.flush()"""
        super(RenderablePool, self).flush()

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

    @overload
    def free(self, arg0: 'Renderable'):
        """public void dev.ultreon.quantum.client.world.RenderablePool.free(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__RenderablePool, self).free(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.RenderablePool()"""
        val = __RenderablePool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.world.RenderablePool()"""
        val = __RenderablePool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))