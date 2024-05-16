from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.world.ClientChunk as _ClientChunk
_ClientChunk = _ClientChunk
import dev.ultreon.quantum.client.world.ChunkMesh as _ChunkMesh
_ChunkMesh = _ChunkMesh
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChunkMesh():
    """dev.ultreon.quantum.client.world.ChunkMesh"""
 
    @staticmethod
    def _wrap(java_value: _ChunkMesh) -> 'ChunkMesh':
        return ChunkMesh(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkMesh):
        """
        Dynamic initializer for ChunkMesh.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkMesh__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkMesh__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = _ChunkMesh()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Mesh'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh)"""
        val = _ChunkMesh(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def getMeshesDisposed() -> int:
        """public static long dev.ultreon.quantum.client.world.ChunkMesh.getMeshesDisposed()"""
        return int._wrap(_ChunkMesh.getMeshesDisposed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Mesh', arg1: 'Material'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Material)"""
        val = _ChunkMesh(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def chunk(self) -> ClientChunk:
        return ClientChunk._wrap(super(_ChunkMesh).chunk())

    @property
    def chunk(self, value: 'ClientChunk'):
        super(_ChunkMesh).chunk(value)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _ChunkMesh(arg0)
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
    def reset(self):
        """public void dev.ultreon.quantum.client.world.ChunkMesh.reset()"""
        super(ChunkMesh, self).reset()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = _ChunkMesh()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.world.ChunkMesh
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.world.ClientChunk as _ClientChunk
_ClientChunk = _ClientChunk
import dev.ultreon.quantum.client.world.ChunkMesh as _ChunkMesh
_ChunkMesh = _ChunkMesh
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChunkMesh():
    """dev.ultreon.quantum.client.world.ChunkMesh"""
 
    @staticmethod
    def _wrap(java_value: _ChunkMesh) -> 'ChunkMesh':
        return ChunkMesh(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkMesh):
        """
        Dynamic initializer for ChunkMesh.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkMesh__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkMesh__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = _ChunkMesh()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Mesh'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh)"""
        val = _ChunkMesh(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def getMeshesDisposed() -> int:
        """public static long dev.ultreon.quantum.client.world.ChunkMesh.getMeshesDisposed()"""
        return int._wrap(_ChunkMesh.getMeshesDisposed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Mesh', arg1: 'Material'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Material)"""
        val = _ChunkMesh(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def chunk(self) -> ClientChunk:
        return ClientChunk._wrap(super(_ChunkMesh).chunk())

    @property
    def chunk(self, value: 'ClientChunk'):
        super(_ChunkMesh).chunk(value)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.world.ChunkMesh(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _ChunkMesh(arg0)
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
    def reset(self):
        """public void dev.ultreon.quantum.client.world.ChunkMesh.reset()"""
        super(ChunkMesh, self).reset()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.ChunkMesh()"""
        val = _ChunkMesh()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.world.ChunkMesh 
 
 
# CLASS: dev.ultreon.quantum.client.world.FaceProperties
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.world.FaceProperties as _FaceProperties
_FaceProperties = _FaceProperties
import dev.ultreon.quantum.client.world.FaceProperties as _FaceProperties_Builder
_Builder = _FaceProperties_Builder.Builder
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FaceProperties():
    """dev.ultreon.quantum.client.world.FaceProperties"""
 
    @staticmethod
    def _wrap(java_value: _FaceProperties) -> 'FaceProperties':
        return FaceProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FaceProperties):
        """
        Dynamic initializer for FaceProperties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FaceProperties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FaceProperties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.FaceProperties()"""
        val = _FaceProperties()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.world.FaceProperties.hashCode()"""
        return int._wrap(super(FaceProperties, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.world.FaceProperties.equals(java.lang.Object)"""
        return bool._wrap(super(_FaceProperties, self).equals(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.world.FaceProperties()"""
        val = _FaceProperties()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.client.world.FaceProperties$Builder dev.ultreon.quantum.client.world.FaceProperties.builder()"""
        return Builder._wrap(_FaceProperties.builder()) 
 
 
# CLASS: dev.ultreon.quantum.client.world.Skybox
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.world.Skybox as _Skybox
_Skybox = _Skybox
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Skybox():
    """dev.ultreon.quantum.client.world.Skybox"""
 
    @staticmethod
    def _wrap(java_value: _Skybox) -> 'Skybox':
        return Skybox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Skybox):
        """
        Dynamic initializer for Skybox.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Skybox__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Skybox__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.Skybox()"""
        val = _Skybox()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.world.Skybox()"""
        val = _Skybox()
        self.__wrapper = val

    @overload
    def update(self, arg0: int):
        """public void dev.ultreon.quantum.client.world.Skybox.update(int)"""
        super(_Skybox, self).update(_int.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.world.ClientChunk
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.Chunk as _Chunk
_Chunk = _Chunk
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import com.badlogic.gdx.graphics.g3d.ModelInstance as _ModelInstance
_ModelInstance = _ModelInstance
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.world.ClientWorld as _ClientWorld
_ClientWorld = _ClientWorld
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

try:
    from pyquantum.world import gen
except ImportError:
    gen = _import_once("pyquantum.world.gen")

from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

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
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.world.BreakResult as _BreakResult
_BreakResult = _BreakResult
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
import java.lang.Runnable as Runnable
from builtins import float
from builtins import object
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

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

import dev.ultreon.quantum.client.world.ClientChunk as _ClientChunk
_ClientChunk = _ClientChunk
import java.util.Map as Map
import dev.ultreon.quantum.world.Biome as _Biome
_Biome = _Biome
import dev.ultreon.quantum.client.QuantumClient as _QuantumClient
_QuantumClient = _QuantumClient
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class ClientChunk():
    """dev.ultreon.quantum.client.world.ClientChunk"""
 
    @staticmethod
    def _wrap(java_value: _ClientChunk) -> 'ClientChunk':
        return ClientChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientChunk):
        """
        Dynamic initializer for ClientChunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientChunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientChunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.world.RenderablePool dev.ultreon.quantum.client.world.ClientChunk.RENDERABLE_POOL
    RENDERABLE_POOL: 'RenderablePool' = _wrap(_RenderablePool.RENDERABLE_POOL)


    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_world.Chunk, self).get(arg0))

    @overload
    def getSunlight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_world.Chunk, self).getSunlight(arg0))

    @overload
    def get(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_world.Chunk, self).get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCustomRendered(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.state.BlockProperties> dev.ultreon.quantum.client.world.ClientChunk.getCustomRendered()"""
        return 'Map'._wrap(super(ClientChunk, self).getCustomRendered())

    @overload
    def getSunlight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getSunlight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_world.Chunk, self).getSunlight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getBounds(self) -> object:
        """public java.lang.Object dev.ultreon.quantum.client.world.ClientChunk.getBounds()"""
        return object._wrap(super(ClientChunk, self).getBounds())

    @overload
    def getBrightness(self, arg0: int) -> float:
        """public float dev.ultreon.quantum.world.Chunk.getBrightness(int)"""
        return float._wrap(super(_world.Chunk, self).getBrightness(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.Chunk.toString()"""
        return str._wrap(super(world.Chunk, self).toString())

    @overload
    def getBiome(self, arg0: int, arg1: int, arg2: int) -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int,int)"""
        return 'world.Biome'._wrap(super(_world.Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def getBlockEntity(self, arg0: 'Vec3i') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'entity.BlockEntity'._wrap(super(_world.Chunk, self).getBlockEntity(arg0))

    @override
    @overload
    def removeBlockEntity(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.world.Chunk.removeBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        super(_world.Chunk, self).removeBlockEntity(arg0)

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int)"""
        return int._wrap(super(_world.Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getBlockEntity(self, arg0: int, arg1: int, arg2: int) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(int,int,int)"""
        return 'entity.BlockEntity'._wrap(super(_world.Chunk, self).getBlockEntity(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def stopBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.stopBreaking(int,int,int)"""
        super(_world.Chunk, self).stopBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientChunk.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_ClientChunk, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getBlockLight(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return int._wrap(super(_world.Chunk, self).getBlockLight(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @property
    def treeData(self, value: 'gen.TreeData'):
        super(_Chunk).treeData(value)

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.Chunk.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_world.Chunk, self).getBlockEntity(arg0))

    @overload
    def getBlockLight(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getBlockLight(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_world.Chunk, self).getBlockLight(arg0))

    @overload
    def getFast(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.client.world.ClientChunk.getFast(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_ClientChunk, self).getFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getFast(self, arg0: 'Vec3i') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.getFast(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'state.BlockProperties'._wrap(super(_world.Chunk, self).getFast(arg0))

    @staticmethod
    @overload
    def loadBlock(arg0: 'MapType') -> 'state.BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.loadBlock(dev.ultreon.ubo.types.MapType)"""
        return state.BlockProperties._wrap(_Chunk.loadBlock(arg0))

    @overload
    def __init__(self, arg0: 'ClientWorld', arg1: int, arg2: int, arg3: 'ChunkPos', arg4: 'Storage', arg5: 'Storage', arg6: 'Map'):
        """public dev.ultreon.quantum.client.world.ClientChunk(dev.ultreon.quantum.client.world.ClientWorld,int,int,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        val = _ClientChunk(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, arg6)
        self.__wrapper = val

    @overload
    def updated(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.updated()"""
        super(ClientChunk, self).updated()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.Chunk.hashCode()"""
        return int._wrap(super(world.Chunk, self).hashCode())

    @override
    @overload
    def startBreaking(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.world.Chunk.startBreaking(int,int,int)"""
        super(_world.Chunk, self).startBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getOffset(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.Chunk.getOffset()"""
        return 'vector.Vec3i'._wrap(super(world.Chunk, self).getOffset())

    @overload
    def setFast(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientChunk.setFast(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_ClientChunk, self).setFast(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getBiome(self, arg0: int, arg1: int) -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.Chunk.getBiome(int,int)"""
        return 'world.Biome'._wrap(super(_world.Chunk, self).getBiome(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def whileLocked(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.whileLocked(java.lang.Runnable)"""
        super(_ClientChunk, self).whileLocked(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isActive()"""
        return bool._wrap(super(world.Chunk, self).isActive())

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int)"""
        return int._wrap(super(_world.Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def onUpdated(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.onUpdated()"""
        super(ClientChunk, self).onUpdated()

    @override
    @overload
    def isReady(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isReady()"""
        return bool._wrap(super(world.Chunk, self).isReady())

    @overload
    def continueBreaking(self, arg0: int, arg1: int, arg2: int, arg3: float) -> 'world.BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.world.Chunk.continueBreaking(int,int,int,float)"""
        return 'world.BreakResult'._wrap(super(_world.Chunk, self).continueBreaking(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def setTreeData(self, arg0: 'TreeData'):
        """public void dev.ultreon.quantum.world.Chunk.setTreeData(dev.ultreon.quantum.world.gen.TreeData)"""
        super(_world.Chunk, self).setTreeData(arg0)

    @overload
    def __init__(self, arg0: 'ClientWorld', arg1: 'ChunkPos', arg2: 'Storage', arg3: 'Storage', arg4: 'Map'):
        """public dev.ultreon.quantum.client.world.ClientChunk(dev.ultreon.quantum.client.world.ClientWorld,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        val = _ClientChunk(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def getLightLevel(self, arg0: int, arg1: int, arg2: int) -> float:
        """public float dev.ultreon.quantum.client.world.ClientChunk.getLightLevel(int,int,int) throws dev.ultreon.quantum.util.PosOutOfBoundsException"""
        return float._wrap(super(_ClientChunk, self).getLightLevel(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.equals(java.lang.Object)"""
        return bool._wrap(super(_world.Chunk, self).equals(arg0))

    @override
    @overload
    def getBlockEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity> dev.ultreon.quantum.world.Chunk.getBlockEntities()"""
        return 'Collection'._wrap(super(world.Chunk, self).getBlockEntities())

    @property
    def storage(self) -> Storage:
        return Storage._wrap(super(_Chunk).storage())

    @overload
    def loadCustomRendered(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.loadCustomRendered()"""
        super(ClientChunk, self).loadCustomRendered()

    @staticmethod
    @overload
    def decodeBlock(arg0: 'PacketIO') -> 'block.Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.world.Chunk.decodeBlock(dev.ultreon.quantum.network.PacketIO)"""
        return block.Block._wrap(_Chunk.decodeBlock(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.dispose()"""
        super(ClientChunk, self).dispose()

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.Chunk.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_world.Chunk, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def ascend(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.quantum.world.Chunk.ascend(int,int,int,int)"""
        return int._wrap(super(_world.Chunk, self).ascend(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.Chunk.getPos()"""
        return 'world.ChunkPos'._wrap(super(world.Chunk, self).getPos())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getClient(self) -> 'client.QuantumClient':
        """public dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.world.ClientChunk.getClient()"""
        return 'client.QuantumClient'._wrap(super(ClientChunk, self).getClient())

    @override
    @overload
    def getWorld(self) -> 'ClientWorld':
        """public dev.ultreon.quantum.client.world.ClientWorld dev.ultreon.quantum.client.world.ClientChunk.getWorld()"""
        return 'ClientWorld'._wrap(super(ClientChunk, self).getWorld())

    @overload
    def renderModels(self, arg0: 'Scene3D'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.renderModels(dev.ultreon.quantum.client.render.Scene3D)"""
        super(_ClientChunk, self).renderModels(arg0)

    @property
    def treeData(self) -> TreeData:
        return TreeData._wrap(super(_Chunk).treeData())

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.Chunk.isDisposed()"""
        return bool._wrap(super(world.Chunk, self).isDisposed())

    @override
    @overload
    def getBreaking(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.BlockPos, java.lang.Float> dev.ultreon.quantum.world.Chunk.getBreaking()"""
        return 'Map'._wrap(super(world.Chunk, self).getBreaking())

    @override
    @overload
    def set(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.set(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_ClientChunk, self).set(arg0, arg1)

    @overload
    def getHighest(self, arg0: int, arg1: int, arg2: 'BlockMetaPredicate') -> int:
        """public int dev.ultreon.quantum.world.Chunk.getHighest(int,int,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return int._wrap(super(_world.Chunk, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def addModel(self, arg0: 'BlockPos', arg1: 'ModelInstance') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.world.ClientChunk.addModel(dev.ultreon.quantum.world.BlockPos,com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        return 'g3d.ModelInstance'._wrap(super(_ClientChunk, self).addModel(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setFast(self, arg0: 'Vec3i', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.client.world.ClientChunk.setFast(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_ClientChunk, self).setFast(arg0, arg1)

    @property
    def biomeStorage(self) -> Storage:
        return Storage._wrap(super(_Chunk).biomeStorage())

    @overload
    def destroyModels(self):
        """public void dev.ultreon.quantum.client.world.ClientChunk.destroyModels()"""
        super(ClientChunk, self).destroyModels() 
 
 
# CLASS: dev.ultreon.quantum.client.world.ClientWorld
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.util.function.Predicate as Predicate
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

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
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

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

import dev.ultreon.quantum.client.world.ClientChunk as _ClientChunk
_ClientChunk = _ClientChunk
import dev.ultreon.quantum.client.util.Rot as _Rot
_Rot = _Rot
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
import java.lang.Double as _double
import dev.ultreon.quantum.client.world.ClientWorld as _ClientWorld
_ClientWorld = _ClientWorld
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
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
try:
    from pyquantum.client import util
except ImportError:
    util = _import_once("pyquantum.client.util")

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
 
class ClientWorld():
    """dev.ultreon.quantum.client.world.ClientWorld"""
 
    @staticmethod
    def _wrap(java_value: _ClientWorld) -> 'ClientWorld':
        return ClientWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientWorld):
        """
        Dynamic initializer for ClientWorld.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientWorld__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientWorld__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.world.World.OVERWORLD
    OVERWORLD: 'util.Identifier' = _wrap(_util.Identifier.OVERWORLD)


    @overload
    def getChunksAround(self, arg0: 'Vec3d') -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.ChunkPos> dev.ultreon.quantum.world.World.getChunksAround(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'List'._wrap(super(_world.World, self).getChunksAround(arg0))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float) -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.EntityHitResult'._wrap(super(_world.World, self).rayCastEntity(arg0, _float.valueOf(arg1)))

    @overload
    def getBiome(self, arg0: 'BlockPos') -> 'world.Biome':
        """public dev.ultreon.quantum.world.Biome dev.ultreon.quantum.world.World.getBiome(dev.ultreon.quantum.world.BlockPos)"""
        return 'world.Biome'._wrap(super(_world.World, self).getBiome(arg0))

    @staticmethod
    @property
    def DAY_BOTTOM_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the DAY_BOTTOM_COLOR property.
     
        :param value: Value to set for the DAY_BOTTOM_COLOR property.
        """
     
        super('util.RgbColor').DAY_BOTTOM_COLOR(value)

    @overload
    def get(self, arg0: 'BlockPos') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(dev.ultreon.quantum.world.BlockPos)"""
        return 'state.BlockProperties'._wrap(super(_world.World, self).get(arg0))

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

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3d') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return world.ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @overload
    def getAllEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.client.world.ClientWorld.getAllEntities()"""
        return 'Collection'._wrap(super(ClientWorld, self).getAllEntities())

    @overload
    def getEntitiesByClass(self, arg0: 'Class') -> 'Collection':
        """public <T extends dev.ultreon.quantum.entity.Entity> java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntitiesByClass(java.lang.Class<T>)"""
        return 'Collection'._wrap(super(_world.World, self).getEntitiesByClass(arg0))

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

    @override
    @overload
    def getSeed(self) -> int:
        """public long dev.ultreon.quantum.world.World.getSeed()"""
        return int._wrap(super(world.World, self).getSeed())

    @override
    @overload
    def stopBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.stopBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_ClientWorld, self).stopBreaking(arg0, arg1)

    @overload
    def entitiesWithinDst(self, arg0: 'Entity', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.entitiesWithinDst(dev.ultreon.quantum.entity.Entity,int)"""
        return 'List'._wrap(super(_world.World, self).entitiesWithinDst(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def despawn(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.world.World.despawn(dev.ultreon.quantum.entity.Entity)"""
        super(_world.World, self).despawn(arg0)

    @override
    @overload
    def despawn(self, arg0: int):
        """public void dev.ultreon.quantum.world.World.despawn(int)"""
        super(_world.World, self).despawn(_int.valueOf(arg0))

    @override
    @overload
    def updateNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(_world.World, self).updateNeighbours(arg0)

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: int, arg1: int) -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(int,int)"""
        return world.ChunkPos._wrap(_World.toLocalChunkPos(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool._wrap(super(_world.World, self).set(arg0, arg1, _int.valueOf(arg2)))

    @overload
    def spawn(self, arg0: 'Entity') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T)"""
        return 'entity.Entity'._wrap(super(_world.World, self).spawn(arg0))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: 'BlockPos') -> 'world.BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return world.BlockPos._wrap(_World.toLocalBlockPos(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getSkyColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.world.ClientWorld.getSkyColor()"""
        return 'util.RgbColor'._wrap(super(ClientWorld, self).getSkyColor())

    @overload
    def isOutOfWorldBounds(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(int,int,int)"""
        return bool._wrap(super(_world.World, self).isOutOfWorldBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isClientSide(self) -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientWorld.isClientSide()"""
        return bool._wrap(super(ClientWorld, self).isClientSide())

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
    def playSound(self, arg0: 'SoundEvent', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.world.ClientWorld.playSound(dev.ultreon.quantum.world.SoundEvent,double,double,double)"""
        super(_ClientWorld, self).playSound(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @overload
    def getDaytime(self) -> int:
        """public int dev.ultreon.quantum.client.world.ClientWorld.getDaytime()"""
        return int._wrap(super(ClientWorld, self).getDaytime())

    @override
    @overload
    def startBreaking(self, arg0: 'BlockPos', arg1: 'Player'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.startBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_ClientWorld, self).startBreaking(arg0, arg1)

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_world.World, self).setColumn(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def setDaytime(self, arg0: int):
        """public void dev.ultreon.quantum.client.world.ClientWorld.setDaytime(int)"""
        super(_ClientWorld, self).setDaytime(_int.valueOf(arg0))

    @overload
    def addEntity(self, arg0: int, arg1: 'EntityType', arg2: 'Vec3d', arg3: 'MapType'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.addEntity(int,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.ubo.types.MapType)"""
        super(_ClientWorld, self).addEntity(_int.valueOf(arg0), arg1, arg2, arg3)

    @staticmethod
    @overload
    def toChunkPos(arg0: 'BlockPos') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(dev.ultreon.quantum.world.BlockPos)"""
        return world.ChunkPos._wrap(_World.toChunkPos(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def setColumn(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.world.World.setColumn(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_world.World, self).setColumn(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def updateChunk(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.updateChunk(dev.ultreon.quantum.world.Chunk)"""
        super(_ClientWorld, self).updateChunk(arg0)

    @overload
    def getChunk(self, arg0: int, arg1: int) -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunk(int,int)"""
        return 'ClientChunk'._wrap(super(_ClientWorld, self).getChunk(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.world.ClientWorld(dev.ultreon.quantum.client.QuantumClient)"""
        val = _ClientWorld(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def toChunkPos(arg0: int, arg1: int, arg2: int) -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toChunkPos(int,int,int)"""
        return world.ChunkPos._wrap(_World.toChunkPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isServerSide(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isServerSide()"""
        return bool._wrap(super(world.World, self).isServerSide())

    @overload
    def intersectEntities(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.world.World.intersectEntities(dev.ultreon.quantum.util.BoundingBox)"""
        return bool._wrap(super(_world.World, self).intersectEntities(arg0))

    @overload
    def loadChunk(self, arg0: 'ChunkPos', arg1: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.loadChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(_ClientWorld, self).loadChunk(arg0, arg1)

    @staticmethod
    @property
    def NIGHT_TOP_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the NIGHT_TOP_COLOR property.
     
        :param value: Value to set for the NIGHT_TOP_COLOR property.
        """
     
        super('util.RgbColor').NIGHT_TOP_COLOR(value)

    @staticmethod
    @property
    def DAY_BOTTOM_COLOR_() -> RgbColor:
        """
        Getter for the DAY_BOTTOM_COLOR property.
     
        :return: Value of DAY_BOTTOM_COLOR
        """
     
        return super(RgbColor).DAY_BOTTOM_COLOR()

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vector3') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(com.badlogic.gdx.math.Vector3)"""
        return world.ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @overload
    def getHighest(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.World.getHighest(int,int)"""
        return int._wrap(super(_world.World, self).getHighest(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def isAlwaysLoaded(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isAlwaysLoaded(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_world.World, self).isAlwaysLoaded(arg0))

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_world.World, self).drop(arg0, arg1)

    @override
    @overload
    def updateChunkAndNeighbours(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.world.World.updateChunkAndNeighbours(dev.ultreon.quantum.world.Chunk)"""
        super(_world.World, self).updateChunkAndNeighbours(arg0)

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.client.world.ClientWorld.tick()"""
        super(ClientWorld, self).tick()

    @overload
    def collide(self, arg0: 'BoundingBox', arg1: bool) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.BoundingBox> dev.ultreon.quantum.world.World.collide(dev.ultreon.quantum.util.BoundingBox,boolean)"""
        return 'List'._wrap(super(_world.World, self).collide(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def destroyBlock(self, arg0: 'BlockPos', arg1: 'Player') -> bool:
        """public boolean dev.ultreon.quantum.world.World.destroyBlock(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        return bool._wrap(super(_world.World, self).destroyBlock(arg0, arg1))

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int) -> 'world.BlockPos':
        """public static dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int)"""
        return world.BlockPos._wrap(_World.toLocalBlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def unloadChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.unloadChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_world.World, self).unloadChunk(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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

    @overload
    def rayCast(self, arg0: 'Ray') -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray)"""
        return 'util.BlockHitResult'._wrap(super(_world.World, self).rayCast(arg0))

    @staticmethod
    @property
    def NIGHT_BOTTOM_COLOR_(value: 'util.RgbColor'):
        """
        Setter for the NIGHT_BOTTOM_COLOR property.
     
        :param value: Value to set for the NIGHT_BOTTOM_COLOR property.
        """
     
        super('util.RgbColor').NIGHT_BOTTOM_COLOR(value)

    @overload
    def rayCast(self, arg0: 'Ray', arg1: float) -> 'util.BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.world.World.rayCast(dev.ultreon.quantum.util.Ray,float)"""
        return 'util.BlockHitResult'._wrap(super(_world.World, self).rayCast(arg0, _float.valueOf(arg1)))

    @overload
    def removeEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.client.world.ClientWorld.removeEntity(int)"""
        return 'entity.Entity'._wrap(super(_ClientWorld, self).removeEntity(_int.valueOf(arg0)))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Class') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'._wrap(super(_world.World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def get(self, arg0: int, arg1: int, arg2: int) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.world.World.get(int,int,int)"""
        return 'state.BlockProperties'._wrap(super(_world.World, self).get(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_world.World, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.world.World.isDisposed()"""
        return bool._wrap(super(world.World, self).isDisposed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toLocalChunkPos(arg0: 'ChunkPos') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.toLocalChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return world.ChunkPos._wrap(_World.toLocalChunkPos(arg0))

    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.client.world.ClientWorld.getRenderDistance()"""
        return int._wrap(super(ClientWorld, self).getRenderDistance())

    @override
    @overload
    def getUID(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.world.World.getUID()"""
        return 'UUID'._wrap(super(world.World, self).getUID())

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'Predicate') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,java.util.function.Predicate<dev.ultreon.quantum.entity.Entity>)"""
        return 'util.EntityHitResult'._wrap(super(_world.World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @override
    @overload
    def getSpawnPoint(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.world.World.getSpawnPoint()"""
        return 'world.BlockPos'._wrap(super(world.World, self).getSpawnPoint())

    @override
    @overload
    def onChunkUpdated(self, arg0: 'Chunk'):
        """public void dev.ultreon.quantum.client.world.ClientWorld.onChunkUpdated(dev.ultreon.quantum.world.Chunk)"""
        super(_ClientWorld, self).onChunkUpdated(arg0)

    @overload
    def getBlockEntity(self, arg0: 'BlockPos') -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.world.World.getBlockEntity(dev.ultreon.quantum.world.BlockPos)"""
        return 'entity.BlockEntity'._wrap(super(_world.World, self).getBlockEntity(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientWorld.set(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,int)"""
        return bool._wrap(super(_ClientWorld, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4)))

    @overload
    def rayCastEntity(self, arg0: 'Ray') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray)"""
        return 'util.EntityHitResult'._wrap(super(_world.World, self).rayCastEntity(arg0))

    @override
    @overload
    def setSpawnPoint(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.world.World.setSpawnPoint(int,int)"""
        super(_world.World, self).setSpawnPoint(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def rayCastEntity(self, arg0: 'Ray', arg1: float, arg2: 'EntityType') -> 'util.EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.world.World.rayCastEntity(dev.ultreon.quantum.util.Ray,float,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'util.EntityHitResult'._wrap(super(_world.World, self).rayCastEntity(arg0, _float.valueOf(arg1), arg2))

    @overload
    def getChunkAt(self, arg0: 'BlockPos') -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunkAt(dev.ultreon.quantum.world.BlockPos)"""
        return 'ClientChunk'._wrap(super(_ClientWorld, self).getChunkAt(arg0))

    @staticmethod
    @overload
    def blockToChunkPos(arg0: 'Vec3i') -> 'world.ChunkPos':
        """public static dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.world.World.blockToChunkPos(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return world.ChunkPos._wrap(_World.blockToChunkPos(arg0))

    @override
    @overload
    def getChunksLoaded(self) -> int:
        """public int dev.ultreon.quantum.world.World.getChunksLoaded()"""
        return int._wrap(super(world.World, self).getChunksLoaded())

    @overload
    def collideEntities(self, arg0: 'Entity', arg1: 'BoundingBox') -> 'List':
        """public java.util.List<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.collideEntities(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.util.BoundingBox)"""
        return 'List'._wrap(super(_world.World, self).collideEntities(arg0, arg1))

    @overload
    def getChunk(self, arg0: 'ChunkPos') -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'ClientChunk'._wrap(super(_ClientWorld, self).getChunk(arg0))

    @staticmethod
    @property
    def SKYBOX_ROTATION_(value: 'util.Rot'):
        """
        Setter for the SKYBOX_ROTATION property.
     
        :param value: Value to set for the SKYBOX_ROTATION property.
        """
     
        super('util.Rot').SKYBOX_ROTATION(value)

    @staticmethod
    @overload
    def toChunkVec(arg0: 'BlockPos') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.World.toChunkVec(dev.ultreon.quantum.world.BlockPos)"""
        return vector.Vec2i._wrap(_World.toChunkVec(arg0))

    @override
    @overload
    def closeMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.closeMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_world.World, self).closeMenu(arg0)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'BlockProperties') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.world.World.set(int,int,int,int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'CompletableFuture'._wrap(super(_world.World, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6))

    @overload
    def getEntity(self, arg0: int) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.world.World.getEntity(int)"""
        return 'entity.Entity'._wrap(super(_world.World, self).getEntity(_int.valueOf(arg0)))

    @override
    @overload
    def getDimension(self) -> 'world.DimensionInfo':
        """public dev.ultreon.quantum.world.DimensionInfo dev.ultreon.quantum.world.World.getDimension()"""
        return 'world.DimensionInfo'._wrap(super(world.World, self).getDimension())

    @overload
    def isOutOfWorldBounds(self, arg0: 'BlockPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isOutOfWorldBounds(dev.ultreon.quantum.world.BlockPos)"""
        return bool._wrap(super(_world.World, self).isOutOfWorldBounds(arg0))

    @overload
    def isSpawnChunk(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.world.World.isSpawnChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return bool._wrap(super(_world.World, self).isSpawnChunk(arg0))

    @overload
    def set(self, arg0: 'BlockPos', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.world.World.set(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_world.World, self).set(arg0, arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.world.ClientWorld.dispose()"""
        super(ClientWorld, self).dispose()

    @overload
    def continueBreaking(self, arg0: 'BlockPos', arg1: float, arg2: 'Player') -> 'world.BreakResult':
        """public dev.ultreon.quantum.world.BreakResult dev.ultreon.quantum.client.world.ClientWorld.continueBreaking(dev.ultreon.quantum.world.BlockPos,float,dev.ultreon.quantum.entity.player.Player)"""
        return 'world.BreakResult'._wrap(super(_ClientWorld, self).continueBreaking(arg0, _float.valueOf(arg1), arg2))

    @override
    @overload
    def setBlockEntity(self, arg0: 'BlockPos', arg1: 'BlockEntity'):
        """public void dev.ultreon.quantum.world.World.setBlockEntity(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntity)"""
        super(_world.World, self).setBlockEntity(arg0, arg1)

    @overload
    def isChunkInvalidated(self, arg0: 'Chunk') -> bool:
        """public boolean dev.ultreon.quantum.client.world.ClientWorld.isChunkInvalidated(dev.ultreon.quantum.world.Chunk)"""
        return bool._wrap(super(_ClientWorld, self).isChunkInvalidated(arg0))

    @overload
    def onPlayerAttack(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.world.ClientWorld.onPlayerAttack(int,int)"""
        super(_ClientWorld, self).onPlayerAttack(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTotalChunks(self) -> int:
        """public int dev.ultreon.quantum.client.world.ClientWorld.getTotalChunks()"""
        return int._wrap(super(ClientWorld, self).getTotalChunks())

    @staticmethod
    @property
    def DAY_TOP_COLOR_() -> RgbColor:
        """
        Getter for the DAY_TOP_COLOR property.
     
        :return: Value of DAY_TOP_COLOR
        """
     
        return super(RgbColor).DAY_TOP_COLOR()

    @overload
    def getGlobalSunlight(self) -> float:
        """public float dev.ultreon.quantum.client.world.ClientWorld.getGlobalSunlight()"""
        return float._wrap(super(ClientWorld, self).getGlobalSunlight())

    @overload
    def getBreakProgress(self, arg0: 'BlockPos') -> float:
        """public float dev.ultreon.quantum.world.World.getBreakProgress(dev.ultreon.quantum.world.BlockPos)"""
        return float._wrap(super(_world.World, self).getBreakProgress(arg0))

    @override
    @overload
    def drop(self, arg0: 'ItemStack', arg1: 'Vec3d', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.world.World.drop(dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_world.World, self).drop(arg0, arg1, arg2)

    @overload
    def getChunkAt(self, arg0: int, arg1: int, arg2: int) -> 'ClientChunk':
        """public dev.ultreon.quantum.client.world.ClientChunk dev.ultreon.quantum.client.world.ClientWorld.getChunkAt(int,int,int)"""
        return 'ClientChunk'._wrap(super(_ClientWorld, self).getChunkAt(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getEntities(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.world.World.getEntities()"""
        return 'Collection'._wrap(super(world.World, self).getEntities())

    @override
    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.World.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_world.World, self).openMenu(arg0)

    @staticmethod
    @overload
    def toLocalBlockPos(arg0: int, arg1: int, arg2: int, arg3: 'Vec3i') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.world.World.toLocalBlockPos(int,int,int,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return vector.Vec3i._wrap(_World.toLocalBlockPos(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getLoadedChunks(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.client.world.ClientChunk> dev.ultreon.quantum.client.world.ClientWorld.getLoadedChunks()"""
        return 'Collection'._wrap(super(ClientWorld, self).getLoadedChunks())

    @overload
    def spawn(self, arg0: 'Entity', arg1: 'MapType') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.world.World.spawn(T,dev.ultreon.ubo.types.MapType)"""
        return 'entity.Entity'._wrap(super(_world.World, self).spawn(arg0, arg1))

    @override
    @overload
    def spawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.client.world.ClientWorld.spawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(_ClientWorld, self).spawnParticles(arg0, arg1, arg2, _int.valueOf(arg3))

    @override
    @overload
    def fillCrashInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.world.World.fillCrashInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(_world.World, self).fillCrashInfo(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.world.FaceProperties$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.world.FaceProperties as _FaceProperties
_FaceProperties = _FaceProperties
import dev.ultreon.quantum.client.world.FaceProperties as _FaceProperties_Builder
_Builder = _FaceProperties_Builder.Builder
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.client.world.FaceProperties.Builder"""
 
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
    def randomRotation(self) -> 'Builder':
        """public dev.ultreon.quantum.client.world.FaceProperties$Builder dev.ultreon.quantum.client.world.FaceProperties$Builder.randomRotation()"""
        return 'Builder'._wrap(super(Builder, self).randomRotation())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.FaceProperties$Builder()"""
        val = _Builder()
        self.__wrapper = val

    @overload
    def build(self) -> 'FaceProperties':
        """public dev.ultreon.quantum.client.world.FaceProperties dev.ultreon.quantum.client.world.FaceProperties$Builder.build()"""
        return 'FaceProperties'._wrap(super(Builder, self).build())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.world.FaceProperties$Builder()"""
        val = _Builder()
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
 
 
# CLASS: dev.ultreon.quantum.client.world.WorldRenderer
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleSystem as _ParticleSystem
_ParticleSystem = _ParticleSystem
import dev.ultreon.quantum.client.world.WorldRenderer as _WorldRenderer
_WorldRenderer = _WorldRenderer
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.client import management
except ImportError:
    management = _import_once("pyquantum.client.management")

import dev.ultreon.quantum.client.world.Skybox as _Skybox
_Skybox = _Skybox
import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
import com.badlogic.gdx.graphics.g3d.Environment as _Environment
_Environment = _Environment
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldRenderer():
    """dev.ultreon.quantum.client.world.WorldRenderer"""
 
    @staticmethod
    def _wrap(java_value: _WorldRenderer) -> 'WorldRenderer':
        return WorldRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldRenderer):
        """
        Dynamic initializer for WorldRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def free(self, arg0: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.free(dev.ultreon.quantum.client.world.ClientChunk)"""
        super(_WorldRenderer, self).free(arg0)

    @staticmethod
    @overload
    def getChunkMeshFrees() -> int:
        """public static long dev.ultreon.quantum.client.world.WorldRenderer.getChunkMeshFrees()"""
        return int._wrap(_WorldRenderer.getChunkMeshFrees())

    @overload
    def addParticles(self, arg0: 'ParticleEffect', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.addParticles(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(_WorldRenderer, self).addParticles(arg0, arg1, arg2, _int.valueOf(arg3))

    @overload
    def getMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.world.WorldRenderer.getMaterial()"""
        return 'g3d.Material'._wrap(super(WorldRenderer, self).getMaterial())

    @staticmethod
    @overload
    def getVertexCount() -> int:
        """public static long dev.ultreon.quantum.client.world.WorldRenderer.getVertexCount()"""
        return int._wrap(_WorldRenderer.getVertexCount())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def buildOutlineBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'MeshPartBuilder'):
        """public static void dev.ultreon.quantum.client.world.WorldRenderer.buildOutlineBox(float,float,float,float,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        _WorldRenderer.buildOutlineBox(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def getEnvironment(self) -> 'g3d.Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment dev.ultreon.quantum.client.world.WorldRenderer.getEnvironment()"""
        return 'g3d.Environment'._wrap(super(WorldRenderer, self).getEnvironment())

    @overload
    def getSkybox(self) -> 'Skybox':
        """public dev.ultreon.quantum.client.world.Skybox dev.ultreon.quantum.client.world.WorldRenderer.getSkybox()"""
        return 'Skybox'._wrap(super(WorldRenderer, self).getSkybox())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.dispose()"""
        super(WorldRenderer, self).dispose()

    @overload
    def collectEntity(self, arg0: 'Entity', arg1: 'Scene3D'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.collectEntity(dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.client.render.Scene3D)"""
        super(_WorldRenderer, self).collectEntity(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def reload(self, arg0: 'ReloadContext', arg1: 'MaterialManager'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.reload(dev.ultreon.quantum.resources.ReloadContext,dev.ultreon.quantum.client.management.MaterialManager)"""
        super(_WorldRenderer, self).reload(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ClientWorld'):
        """public dev.ultreon.quantum.client.world.WorldRenderer(dev.ultreon.quantum.client.world.ClientWorld)"""
        val = _WorldRenderer(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def getPoolPeak() -> int:
        """public static int dev.ultreon.quantum.client.world.WorldRenderer.getPoolPeak()"""
        return int._wrap(_WorldRenderer.getPoolPeak())

    @staticmethod
    @overload
    def buildOutlineBox(arg0: float, arg1: float, arg2: float, arg3: float) -> 'graphics.Mesh':
        """public static com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.world.WorldRenderer.buildOutlineBox(float,float,float,float)"""
        return graphics.Mesh._wrap(_WorldRenderer.buildOutlineBox(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def buildLine(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'MeshPartBuilder'):
        """public static void dev.ultreon.quantum.client.world.WorldRenderer.buildLine(float,float,float,float,float,float,float,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        _WorldRenderer.buildLine(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7)

    @staticmethod
    @overload
    def getPoolFree() -> int:
        """public static long dev.ultreon.quantum.client.world.WorldRenderer.getPoolFree()"""
        return int._wrap(_WorldRenderer.getPoolFree())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def getPoolMax() -> int:
        """public static int dev.ultreon.quantum.client.world.WorldRenderer.getPoolMax()"""
        return int._wrap(_WorldRenderer.getPoolMax())

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.world.WorldRenderer.isDisposed()"""
        return bool._wrap(super(WorldRenderer, self).isDisposed())

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.client.world.WorldRenderer.getWorld()"""
        return 'world.World'._wrap(super(WorldRenderer, self).getWorld())

    @overload
    def updateBackground(self):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.updateBackground()"""
        super(WorldRenderer, self).updateBackground()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def removeEntity(self, arg0: int):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.removeEntity(int)"""
        super(_WorldRenderer, self).removeEntity(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTransparentMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.world.WorldRenderer.getTransparentMaterial()"""
        return 'g3d.Material'._wrap(super(WorldRenderer, self).getTransparentMaterial())

    @overload
    def deferDispose(self, arg0: 'Disposable') -> 'utils.Disposable':
        """public <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.world.WorldRenderer.deferDispose(T)"""
        return 'utils.Disposable'._wrap(super(_WorldRenderer, self).deferDispose(arg0))

    @overload
    def render(self, arg0: 'Scene3D'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.render(dev.ultreon.quantum.client.render.Scene3D)"""
        super(_WorldRenderer, self).render(arg0)

    @overload
    def getBreakingTex(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.world.WorldRenderer.getBreakingTex()"""
        return 'graphics.Texture'._wrap(super(WorldRenderer, self).getBreakingTex())

    @overload
    def getLoadedChunks(self) -> int:
        """public int dev.ultreon.quantum.client.world.WorldRenderer.getLoadedChunks()"""
        return int._wrap(super(WorldRenderer, self).getLoadedChunks())

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
    def remove(self, arg0: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.world.WorldRenderer.remove(dev.ultreon.quantum.client.world.ClientChunk)"""
        super(_WorldRenderer, self).remove(arg0)

    @overload
    def getVisibleChunks(self) -> int:
        """public int dev.ultreon.quantum.client.world.WorldRenderer.getVisibleChunks()"""
        return int._wrap(super(WorldRenderer, self).getVisibleChunks())

    @overload
    def getParticleSystem(self) -> 'particles.ParticleSystem':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSystem dev.ultreon.quantum.client.world.WorldRenderer.getParticleSystem()"""
        return 'particles.ParticleSystem'._wrap(super(WorldRenderer, self).getParticleSystem())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.world.RenderablePool
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.world.RenderablePool as _RenderablePool
_RenderablePool = _RenderablePool
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderablePool():
    """dev.ultreon.quantum.client.world.RenderablePool"""
 
    @staticmethod
    def _wrap(java_value: _RenderablePool) -> 'RenderablePool':
        return RenderablePool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderablePool):
        """
        Dynamic initializer for RenderablePool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderablePool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderablePool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def free(self, arg0: 'Renderable'):
        """public void dev.ultreon.quantum.client.world.RenderablePool.free(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_RenderablePool, self).free(arg0)

    @overload
    def getObtainedCount(self) -> int:
        """public int dev.ultreon.quantum.client.world.RenderablePool.getObtainedCount()"""
        return int._wrap(super(RenderablePool, self).getObtainedCount())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int._wrap(super(utils.Pool, self).getFree())

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void dev.ultreon.quantum.client.world.RenderablePool.freeAll(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_RenderablePool, self).freeAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(_utils.Pool, self).fill(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.world.RenderablePool.flush()"""
        super(RenderablePool, self).flush()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.world.RenderablePool()"""
        val = _RenderablePool()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.world.RenderablePool()"""
        val = _RenderablePool()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def obtain(self) -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable dev.ultreon.quantum.client.world.RenderablePool.obtain()"""
        return 'g3d.Renderable'._wrap(super(RenderablePool, self).obtain())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())