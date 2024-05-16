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
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties_Builder
__Builder = __ModelProperties_Builder.Builder
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties
__ModelProperties = __ModelProperties
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.client.model.block.ModelProperties.Builder"""
 
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def top(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.top(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).top(arg0))

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
    def rotateHorizontal(self, arg0: 'CubicDirection') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.rotateHorizontal(dev.ultreon.quantum.world.CubicDirection)"""
        return 'Builder'.__wrap(super(__Builder, self).rotateHorizontal(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def front(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.front(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).front(arg0))

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
    def build(self) -> 'ModelProperties':
        """public dev.ultreon.quantum.client.model.block.ModelProperties dev.ultreon.quantum.client.model.block.ModelProperties$Builder.build()"""
        return 'ModelProperties'.__wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def back(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.back(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).back(arg0))

    @overload
    def left(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.left(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).left(arg0))

    @overload
    def right(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.right(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).right(arg0))

    @overload
    def bottom(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.bottom(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).bottom(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.ModelProperties$Builder
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties_Builder
__Builder = __ModelProperties_Builder.Builder
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties
__ModelProperties = __ModelProperties
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.client.model.block.ModelProperties.Builder"""
 
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def top(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.top(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).top(arg0))

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
    def rotateHorizontal(self, arg0: 'CubicDirection') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.rotateHorizontal(dev.ultreon.quantum.world.CubicDirection)"""
        return 'Builder'.__wrap(super(__Builder, self).rotateHorizontal(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def front(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.front(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).front(arg0))

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
    def build(self) -> 'ModelProperties':
        """public dev.ultreon.quantum.client.model.block.ModelProperties dev.ultreon.quantum.client.model.block.ModelProperties$Builder.build()"""
        return 'ModelProperties'.__wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def back(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.back(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).back(arg0))

    @overload
    def left(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.left(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).left(arg0))

    @overload
    def right(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.right(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).right(arg0))

    @overload
    def bottom(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.bottom(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'.__wrap(super(__Builder, self).bottom(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.ModelProperties$Builder 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.G3DModel
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.block.G3DModel as __G3DModel
__G3DModel = __G3DModel
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class G3DModel(__BlockModel, BlockModel):
    """dev.ultreon.quantum.client.model.block.G3DModel"""
 
    @staticmethod
    def __wrap(java_value: __G3DModel) -> 'G3DModel':
        return G3DModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __G3DModel):
        """
        Dynamic initializer for G3DModel.
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
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.G3DModel.resourceId()"""
        return 'util.Identifier'.__wrap(super(G3DModel, self).resourceId())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ModelConfig'):
        """public dev.ultreon.quantum.client.model.block.G3DModel(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig)"""
        val = __G3DModel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.block.G3DModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(__G3DModel, self).load(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemScale()"""
        return 'math.Vector3'.__wrap(super(BlockModel, self).getItemScale())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(__BlockModel, self).render(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemOffset()"""
        return 'math.Vector3'.__wrap(super(BlockModel, self).getItemOffset())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def dispose(self):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.dispose()"""
        super(BlockModel, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public void dev.ultreon.quantum.client.model.block.G3DModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__G3DModel, self).loadInto(arg0, arg1)

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.block.G3DModel.getModel()"""
        return 'g3d.Model'.__wrap(super(G3DModel, self).getModel())

    @override
    @overload
    def isCustom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.G3DModel.isCustom()"""
        return bool.__wrap(super(G3DModel, self).isCustom())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.model.block.G3DModel(dev.ultreon.quantum.util.Identifier)"""
        val = __G3DModel(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BakedModelRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = __import_once__("pyquantum.client.atlas")

import dev.ultreon.quantum.client.model.block.BakedModelRegistry as __BakedModelRegistry
__BakedModelRegistry = __BakedModelRegistry
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import dev.ultreon.quantum.client.atlas.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
 
class BakedModelRegistry(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.model.block.BakedModelRegistry"""
 
    @staticmethod
    def __wrap(java_value: __BakedModelRegistry) -> 'BakedModelRegistry':
        return BakedModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BakedModelRegistry):
        """
        Dynamic initializer for BakedModelRegistry.
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
        """public int dev.ultreon.quantum.client.model.block.BakedModelRegistry.hashCode()"""
        return int.__wrap(super(BakedModelRegistry, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.block.BakedModelRegistry.toString()"""
        return str.__wrap(super(BakedModelRegistry, self).toString())

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
    def bakedModels(self) -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<dev.ultreon.quantum.block.Block, java.util.List<dev.ultreon.libs.commons.v0.tuple.Pair<java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>, dev.ultreon.quantum.client.model.block.BakedCubeModel>>> dev.ultreon.quantum.client.model.block.BakedModelRegistry.bakedModels()"""
        return 'pygcollect.ImmutableMap'.__wrap(super(BakedModelRegistry, self).bakedModels())

    @overload
    def __init__(self, arg0: 'TextureAtlas', arg1: 'ImmutableMap'):
        """public dev.ultreon.quantum.client.model.block.BakedModelRegistry(dev.ultreon.quantum.client.atlas.TextureAtlas,com.google.common.collect.ImmutableMap<dev.ultreon.quantum.block.Block, java.util.List<dev.ultreon.libs.commons.v0.tuple.Pair<java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>, dev.ultreon.quantum.client.model.block.BakedCubeModel>>>)"""
        val = __BakedModelRegistry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.BakedModelRegistry.equals(java.lang.Object)"""
        return bool.__wrap(super(__BakedModelRegistry, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.block.BakedModelRegistry.dispose()"""
        super(BakedModelRegistry, self).dispose()

    @overload
    def atlas(self) -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.model.block.BakedModelRegistry.atlas()"""
        return 'atlas.TextureAtlas'.__wrap(super(BakedModelRegistry, self).atlas()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import dev.ultreon.quantum.client.model.block.G3DModel as __G3DModel_ModelConfig
__ModelConfig = __G3DModel_ModelConfig.ModelConfig
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModelConfig():
    """dev.ultreon.quantum.client.model.block.G3DModel.ModelConfig"""
 
    @staticmethod
    def __wrap(java_value: __ModelConfig) -> 'ModelConfig':
        return ModelConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelConfig):
        """
        Dynamic initializer for ModelConfig.
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
 
    # public static final dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.BLOCKBENCH
    BLOCKBENCH: 'ModelConfig' = __wrap(__ModelConfig.BLOCKBENCH)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def scale(self, arg0: 'Vector3') -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.scale(com.badlogic.gdx.math.Vector3)"""
        return 'ModelConfig'.__wrap(super(__ModelConfig, self).scale(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig()"""
        val = __ModelConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def translation(self, arg0: 'Vector3') -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.translation(com.badlogic.gdx.math.Vector3)"""
        return 'ModelConfig'.__wrap(super(__ModelConfig, self).translation(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig()"""
        val = __ModelConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scale(self, arg0: float) -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.scale(float)"""
        return 'ModelConfig'.__wrap(super(__ModelConfig, self).scale(__float.valueOf(arg0)))

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
    def scale(self, arg0: float, arg1: float, arg2: float) -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.scale(float,float,float)"""
        return 'ModelConfig'.__wrap(super(__ModelConfig, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def translation(self, arg0: float, arg1: float, arg2: float) -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.translation(float,float,float)"""
        return 'ModelConfig'.__wrap(super(__ModelConfig, self).translation(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BlockModelRegistry
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
from builtins import str
try:
    from pyquantum.client import texture
except ImportError:
    texture = __import_once__("pyquantum.client.texture")

from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = __import_once__("pyquantum.client.atlas")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
import dev.ultreon.quantum.client.model.block.BlockModelRegistry as __BlockModelRegistry
__BlockModelRegistry = __BlockModelRegistry
import dev.ultreon.quantum.client.model.block.BakedModelRegistry as __BakedModelRegistry
__BakedModelRegistry = __BakedModelRegistry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.client.model import model
except ImportError:
    model = __import_once__("pyquantum.client.model.model")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.atlas.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
from builtins import int
 
class BlockModelRegistry():
    """dev.ultreon.quantum.client.model.block.BlockModelRegistry"""
 
    @staticmethod
    def __wrap(java_value: __BlockModelRegistry) -> 'BlockModelRegistry':
        return BlockModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockModelRegistry):
        """
        Dynamic initializer for BlockModelRegistry.
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

    @staticmethod
    @overload
    def get(arg0: 'BlockProperties') -> 'BlockModel':
        """public static dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.model.block.BlockModelRegistry.get(dev.ultreon.quantum.block.state.BlockProperties)"""
        return BlockModel.__wrap(__BlockModelRegistry.get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stitch(arg0: 'TextureManager') -> 'atlas.TextureAtlas':
        """public static dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.model.block.BlockModelRegistry.stitch(dev.ultreon.quantum.client.texture.TextureManager)"""
        return atlas.TextureAtlas.__wrap(__BlockModelRegistry.stitch(arg0))

    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'Predicate', arg2: 'CubeModel'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.register(dev.ultreon.quantum.block.Block,java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.client.model.block.CubeModel)"""
        __BlockModelRegistry.register(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def load(arg0: 'Json5ModelLoader'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.load(dev.ultreon.quantum.client.model.model.Json5ModelLoader)"""
        __BlockModelRegistry.load(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.block.BlockModelRegistry()"""
        val = __BlockModelRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def bakeJsonModels(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.bakeJsonModels(dev.ultreon.quantum.client.QuantumClient)"""
        __BlockModelRegistry.bakeJsonModels(arg0)

    @staticmethod
    @overload
    def bake(arg0: 'TextureAtlas') -> 'BakedModelRegistry':
        """public static dev.ultreon.quantum.client.model.block.BakedModelRegistry dev.ultreon.quantum.client.model.block.BlockModelRegistry.bake(dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return BakedModelRegistry.__wrap(__BlockModelRegistry.bake(arg0))

    @staticmethod
    @overload
    def registerDefault(arg0: 'Block'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.registerDefault(dev.ultreon.quantum.block.Block)"""
        __BlockModelRegistry.registerDefault(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def registerCustom(arg0: 'Block', arg1: 'Predicate', arg2: 'Supplier'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.registerCustom(dev.ultreon.quantum.block.Block,java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        __BlockModelRegistry.registerCustom(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def registerDefault(arg0: 'Supplier'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.registerDefault(java.util.function.Supplier<dev.ultreon.quantum.block.Block>)"""
        __BlockModelRegistry.registerDefault(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def register(arg0: 'Supplier', arg1: 'Predicate', arg2: 'Supplier'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.register(java.util.function.Supplier<dev.ultreon.quantum.block.Block>,java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.CubeModel>)"""
        __BlockModelRegistry.register(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.BlockModelRegistry()"""
        val = __BlockModelRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BakedCubeModel
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import dev.ultreon.quantum.client.model.BakedModel as __BakedModel
__BakedModel = __BakedModel
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
import dev.ultreon.quantum.client.model.block.BakedCubeModel as __BakedCubeModel
__BakedCubeModel = __BakedCubeModel
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties
__ModelProperties = __ModelProperties
from builtins import int
 
class BakedCubeModel(client.__BakedModel, model.BakedModel, __BlockModel, BlockModel):
    """dev.ultreon.quantum.client.model.block.BakedCubeModel"""
 
    @staticmethod
    def __wrap(java_value: __BakedCubeModel) -> 'BakedCubeModel':
        return BakedCubeModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BakedCubeModel):
        """
        Dynamic initializer for BakedCubeModel.
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
        """public int dev.ultreon.quantum.client.model.block.BakedCubeModel.hashCode()"""
        return int.__wrap(super(BakedCubeModel, self).hashCode())

    @overload
    def north(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.north()"""
        return 'g2d.TextureRegion'.__wrap(super(BakedCubeModel, self).north())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'ModelProperties') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return BakedCubeModel.__wrap(__BakedCubeModel.of(arg0, arg1, arg2))

    @property
    def properties(self) -> ModelProperties:
        return ModelProperties.__wrap(super(__BakedCubeModel).properties())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'TextureRegion', arg3: 'TextureRegion', arg4: 'TextureRegion', arg5: 'TextureRegion', arg6: 'TextureRegion', arg7: 'ModelProperties') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return BakedCubeModel.__wrap(__BakedCubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.BakedCubeModel.equals(java.lang.Object)"""
        return bool.__wrap(super(__BakedCubeModel, self).equals(arg0))

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.BakedModel.resourceId()"""
        return 'util.Identifier'.__wrap(super(model.BakedModel, self).resourceId())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return BakedCubeModel.__wrap(__BakedCubeModel.of(arg0, arg1))

    @overload
    def west(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.west()"""
        return 'g2d.TextureRegion'.__wrap(super(BakedCubeModel, self).west())

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.BakedModel.getModel()"""
        return 'g3d.Model'.__wrap(super(model.BakedModel, self).getModel())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemOffset()"""
        return 'math.Vector3'.__wrap(super(BlockModel, self).getItemOffset())

    @overload
    def top(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.top()"""
        return 'g2d.TextureRegion'.__wrap(super(BakedCubeModel, self).top())

    @override
    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__BlockModel, self).loadInto(arg0, arg1)

    @staticmethod
    @overload
    def defaultModel() -> 'BakedCubeModel':
        """public static synchronized dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.defaultModel()"""
        return BakedCubeModel.__wrap(__BakedCubeModel.defaultModel())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.block.BakedCubeModel.toString()"""
        return str.__wrap(super(BakedCubeModel, self).toString())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'TextureRegion', arg3: 'TextureRegion', arg4: 'TextureRegion', arg5: 'TextureRegion', arg6: 'TextureRegion') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return BakedCubeModel.__wrap(__BakedCubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @overload
    def bottom(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.bottom()"""
        return 'g2d.TextureRegion'.__wrap(super(BakedCubeModel, self).bottom())

    @overload
    def east(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.east()"""
        return 'g2d.TextureRegion'.__wrap(super(BakedCubeModel, self).east())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemScale()"""
        return 'math.Vector3'.__wrap(super(BlockModel, self).getItemScale())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(__BlockModel, self).render(arg0, arg1)

    @override
    @overload
    def isCustom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.BakedCubeModel.isCustom()"""
        return bool.__wrap(super(BakedCubeModel, self).isCustom())

    @overload
    def south(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.south()"""
        return 'g2d.TextureRegion'.__wrap(super(BakedCubeModel, self).south())

    @override
    @overload
    def dispose(self):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.dispose()"""
        super(BlockModel, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.block.BakedCubeModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(__BakedCubeModel, self).load(arg0)

    @staticmethod
    @overload
    def createModel(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'TextureRegion', arg3: 'TextureRegion', arg4: 'TextureRegion', arg5: 'TextureRegion', arg6: 'TextureRegion') -> 'g3d.Model':
        """public static com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.block.BakedCubeModel.createModel(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return g3d.Model.__wrap(__BakedCubeModel.createModel(arg0, arg1, arg2, arg3, arg4, arg5, arg6)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BlockModel
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.resources.LoadableResource as __LoadableResource
__LoadableResource = __LoadableResource
 
class BlockModel(ABC, client.__LoadableResource, resources.LoadableResource):
    """dev.ultreon.quantum.client.model.block.BlockModel"""
 
    @staticmethod
    def __wrap(java_value: __BlockModel) -> 'BlockModel':
        return BlockModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockModel):
        """
        Dynamic initializer for BlockModel.
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
    def dispose(self):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.dispose()"""
        super(BlockModel, self).dispose()

    @abstractmethod
    def resourceId(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.BlockModel.resourceId()"""
        pass

    @abstractmethod
    def isCustom(self, ):
        """public abstract boolean dev.ultreon.quantum.client.model.block.BlockModel.isCustom()"""
        pass

    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemScale()"""
        return 'math.Vector3'.__wrap(super(BlockModel, self).getItemScale())

    @abstractmethod
    def load(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.resources.LoadableResource.load(dev.ultreon.quantum.client.QuantumClient)"""
        pass

    @abstractmethod
    def getModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.block.BlockModel.getModel()"""
        pass

    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(__BlockModel, self).render(arg0, arg1)

    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemOffset()"""
        return 'math.Vector3'.__wrap(super(BlockModel, self).getItemOffset())

    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__BlockModel, self).loadInto(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.CubeModel
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = __import_once__("pyquantum.client.atlas")

import dev.ultreon.quantum.client.model.block.CubeModel as __CubeModel
__CubeModel = __CubeModel
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import dev.ultreon.quantum.client.model.block.BakedCubeModel as __BakedCubeModel
__BakedCubeModel = __BakedCubeModel
 
class CubeModel():
    """dev.ultreon.quantum.client.model.block.CubeModel"""
 
    @staticmethod
    def __wrap(java_value: __CubeModel) -> 'CubeModel':
        return CubeModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CubeModel):
        """
        Dynamic initializer for CubeModel.
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

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier', arg6: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5))

    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.resourceId()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).resourceId())

    @overload
    def bottom(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.bottom()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).bottom())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def top(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.top()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).top())

    @overload
    def front(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.front()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).front())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.block.CubeModel.toString()"""
        return str.__wrap(super(CubeModel, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.block.CubeModel.hashCode()"""
        return int.__wrap(super(CubeModel, self).hashCode())

    @overload
    def back(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.back()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).back())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.CubeModel.equals(java.lang.Object)"""
        return bool.__wrap(super(__CubeModel, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier', arg6: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1))

    @overload
    def all(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.client.model.block.CubeModel.all()"""
        return 'Set'.__wrap(super(CubeModel, self).all())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3))

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

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2))

    @overload
    def right(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.right()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).right())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier', arg6: 'Identifier', arg7: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel.__wrap(__CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def left(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.left()"""
        return 'util.Identifier'.__wrap(super(CubeModel, self).left())

    @overload
    def bake(self, arg0: 'Identifier', arg1: 'TextureAtlas') -> 'BakedCubeModel':
        """public dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.CubeModel.bake(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return 'BakedCubeModel'.__wrap(super(__CubeModel, self).bake(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.ModelProperties
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.world.CubicDirection as __CubicDirection
__CubicDirection = __CubicDirection
from builtins import str
import dev.ultreon.quantum.client.world.FaceProperties as __FaceProperties
__FaceProperties = __FaceProperties
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties_Builder
__Builder = __ModelProperties_Builder.Builder
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.model.block.ModelProperties as __ModelProperties
__ModelProperties = __ModelProperties
from builtins import int
 
class ModelProperties():
    """dev.ultreon.quantum.client.model.block.ModelProperties"""
 
    @staticmethod
    def __wrap(java_value: __ModelProperties) -> 'ModelProperties':
        return ModelProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelProperties):
        """
        Dynamic initializer for ModelProperties.
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
 
    @property
    def back(self) -> FaceProperties:
        return FaceProperties.__wrap(super(__ModelProperties).back())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @property
    def bottom(self) -> FaceProperties:
        return FaceProperties.__wrap(super(__ModelProperties).bottom())

    @property
    def right(self) -> FaceProperties:
        return FaceProperties.__wrap(super(__ModelProperties).right())

    @overload
    def __init__(self, arg0: 'FaceProperties', arg1: 'CubicDirection'):
        """public dev.ultreon.quantum.client.model.block.ModelProperties(dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.world.CubicDirection)"""
        val = __ModelProperties(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @property
    def rotation(self) -> CubicDirection:
        return CubicDirection.__wrap(super(__ModelProperties).rotation())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.ModelProperties.equals(java.lang.Object)"""
        return bool.__wrap(super(__ModelProperties, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.block.ModelProperties.hashCode()"""
        return int.__wrap(super(ModelProperties, self).hashCode())

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
    def front(self) -> FaceProperties:
        return FaceProperties.__wrap(super(__ModelProperties).front())

    @overload
    def __init__(self, arg0: 'FaceProperties', arg1: 'FaceProperties', arg2: 'FaceProperties', arg3: 'FaceProperties', arg4: 'FaceProperties', arg5: 'FaceProperties', arg6: 'CubicDirection'):
        """public dev.ultreon.quantum.client.model.block.ModelProperties(dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.world.CubicDirection)"""
        val = __ModelProperties(arg0, arg1, arg2, arg3, arg4, arg5, arg6)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @property
    def top(self) -> FaceProperties:
        return FaceProperties.__wrap(super(__ModelProperties).top())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @property
    def left(self) -> FaceProperties:
        return FaceProperties.__wrap(super(__ModelProperties).left())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties.builder()"""
        return Builder.__wrap(__ModelProperties.builder())