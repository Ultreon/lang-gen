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
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties_Builder
_Builder = _ModelProperties_Builder.Builder
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties
_ModelProperties = _ModelProperties
import java.lang.Integer as _int
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.client.model.block.ModelProperties.Builder"""
 
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
    def right(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.right(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).right(arg0))

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
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = _Builder()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = _Builder()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bottom(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.bottom(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).bottom(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def rotateHorizontal(self, arg0: 'CubicDirection') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.rotateHorizontal(dev.ultreon.quantum.world.CubicDirection)"""
        return 'Builder'._wrap(super(_Builder, self).rotateHorizontal(arg0))

    @overload
    def front(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.front(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).front(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def left(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.left(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).left(arg0))

    @overload
    def back(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.back(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).back(arg0))

    @overload
    def build(self) -> 'ModelProperties':
        """public dev.ultreon.quantum.client.model.block.ModelProperties dev.ultreon.quantum.client.model.block.ModelProperties$Builder.build()"""
        return 'ModelProperties'._wrap(super(Builder, self).build())

    @overload
    def top(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.top(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).top(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.ModelProperties$Builder
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
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties_Builder
_Builder = _ModelProperties_Builder.Builder
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties
_ModelProperties = _ModelProperties
import java.lang.Integer as _int
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.client.model.block.ModelProperties.Builder"""
 
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
    def right(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.right(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).right(arg0))

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
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = _Builder()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder()"""
        val = _Builder()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bottom(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.bottom(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).bottom(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def rotateHorizontal(self, arg0: 'CubicDirection') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.rotateHorizontal(dev.ultreon.quantum.world.CubicDirection)"""
        return 'Builder'._wrap(super(_Builder, self).rotateHorizontal(arg0))

    @overload
    def front(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.front(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).front(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def left(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.left(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).left(arg0))

    @overload
    def back(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.back(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).back(arg0))

    @overload
    def build(self) -> 'ModelProperties':
        """public dev.ultreon.quantum.client.model.block.ModelProperties dev.ultreon.quantum.client.model.block.ModelProperties$Builder.build()"""
        return 'ModelProperties'._wrap(super(Builder, self).build())

    @overload
    def top(self, arg0: 'FaceProperties') -> 'Builder':
        """public dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties$Builder.top(dev.ultreon.quantum.client.world.FaceProperties)"""
        return 'Builder'._wrap(super(_Builder, self).top(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.ModelProperties$Builder 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.G3DModel
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.model.block.G3DModel as _G3DModel
_G3DModel = _G3DModel
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class G3DModel():
    """dev.ultreon.quantum.client.model.block.G3DModel"""
 
    @staticmethod
    def _wrap(java_value: _G3DModel) -> 'G3DModel':
        return G3DModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _G3DModel):
        """
        Dynamic initializer for G3DModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_G3DModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_G3DModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ModelConfig'):
        """public dev.ultreon.quantum.client.model.block.G3DModel(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig)"""
        val = _G3DModel(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemScale()"""
        return 'math.Vector3'._wrap(super(BlockModel, self).getItemScale())

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.block.G3DModel.getModel()"""
        return 'g3d.Model'._wrap(super(G3DModel, self).getModel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isCustom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.G3DModel.isCustom()"""
        return bool._wrap(super(G3DModel, self).isCustom())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(_BlockModel, self).render(arg0, arg1)

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.block.G3DModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(_G3DModel, self).load(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.model.block.G3DModel(dev.ultreon.quantum.util.Identifier)"""
        val = _G3DModel(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemOffset()"""
        return 'math.Vector3'._wrap(super(BlockModel, self).getItemOffset())

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
        super(_G3DModel, self).loadInto(arg0, arg1)

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.G3DModel.resourceId()"""
        return 'util.Identifier'._wrap(super(G3DModel, self).resourceId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BakedModelRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = _import_once("pyquantum.client.atlas")

import dev.ultreon.quantum.client.model.block.BakedModelRegistry as _BakedModelRegistry
_BakedModelRegistry = _BakedModelRegistry
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Integer as _int
import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BakedModelRegistry():
    """dev.ultreon.quantum.client.model.block.BakedModelRegistry"""
 
    @staticmethod
    def _wrap(java_value: _BakedModelRegistry) -> 'BakedModelRegistry':
        return BakedModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BakedModelRegistry):
        """
        Dynamic initializer for BakedModelRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BakedModelRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BakedModelRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.block.BakedModelRegistry.toString()"""
        return str._wrap(super(BakedModelRegistry, self).toString())

    @overload
    def atlas(self) -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.model.block.BakedModelRegistry.atlas()"""
        return 'atlas.TextureAtlas'._wrap(super(BakedModelRegistry, self).atlas())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def bakedModels(self) -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<dev.ultreon.quantum.block.Block, java.util.List<dev.ultreon.libs.commons.v0.tuple.Pair<java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>, dev.ultreon.quantum.client.model.block.BakedCubeModel>>> dev.ultreon.quantum.client.model.block.BakedModelRegistry.bakedModels()"""
        return 'pygcollect.ImmutableMap'._wrap(super(BakedModelRegistry, self).bakedModels())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.BakedModelRegistry.equals(java.lang.Object)"""
        return bool._wrap(super(_BakedModelRegistry, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.block.BakedModelRegistry.hashCode()"""
        return int._wrap(super(BakedModelRegistry, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TextureAtlas', arg1: 'ImmutableMap'):
        """public dev.ultreon.quantum.client.model.block.BakedModelRegistry(dev.ultreon.quantum.client.atlas.TextureAtlas,com.google.common.collect.ImmutableMap<dev.ultreon.quantum.block.Block, java.util.List<dev.ultreon.libs.commons.v0.tuple.Pair<java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>, dev.ultreon.quantum.client.model.block.BakedCubeModel>>>)"""
        val = _BakedModelRegistry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.block.BakedModelRegistry.dispose()"""
        super(BakedModelRegistry, self).dispose() 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.model.block.G3DModel as _G3DModel_ModelConfig
_ModelConfig = _G3DModel_ModelConfig.ModelConfig
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelConfig():
    """dev.ultreon.quantum.client.model.block.G3DModel.ModelConfig"""
 
    @staticmethod
    def _wrap(java_value: _ModelConfig) -> 'ModelConfig':
        return ModelConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelConfig):
        """
        Dynamic initializer for ModelConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def scale(self, arg0: float) -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.scale(float)"""
        return 'ModelConfig'._wrap(super(_ModelConfig, self).scale(_float.valueOf(arg0)))

    @overload
    def translation(self, arg0: float, arg1: float, arg2: float) -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.translation(float,float,float)"""
        return 'ModelConfig'._wrap(super(_ModelConfig, self).translation(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

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
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig()"""
        val = _ModelConfig()
        self.__wrapper = val

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float) -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.scale(float,float,float)"""
        return 'ModelConfig'._wrap(super(_ModelConfig, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

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
    def scale(self, arg0: 'Vector3') -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.scale(com.badlogic.gdx.math.Vector3)"""
        return 'ModelConfig'._wrap(super(_ModelConfig, self).scale(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def translation(self, arg0: 'Vector3') -> 'ModelConfig':
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig.translation(com.badlogic.gdx.math.Vector3)"""
        return 'ModelConfig'._wrap(super(_ModelConfig, self).translation(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.G3DModel$ModelConfig()"""
        val = _ModelConfig()
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


ModelConfig.BLOCKBENCH = ModelConfig._wrap(_BLOCKBENCH.BLOCKBENCH) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BlockModelRegistry
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
from builtins import str
try:
    from pyquantum.client import texture
except ImportError:
    texture = _import_once("pyquantum.client.texture")

from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = _import_once("pyquantum.client.atlas")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BakedModelRegistry as _BakedModelRegistry
_BakedModelRegistry = _BakedModelRegistry
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.block.BlockModelRegistry as _BlockModelRegistry
_BlockModelRegistry = _BlockModelRegistry
import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

try:
    from pyquantum.client.model import model
except ImportError:
    model = _import_once("pyquantum.client.model.model")

import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockModelRegistry():
    """dev.ultreon.quantum.client.model.block.BlockModelRegistry"""
 
    @staticmethod
    def _wrap(java_value: _BlockModelRegistry) -> 'BlockModelRegistry':
        return BlockModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockModelRegistry):
        """
        Dynamic initializer for BlockModelRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockModelRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockModelRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'Predicate', arg2: 'CubeModel'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.register(dev.ultreon.quantum.block.Block,java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.client.model.block.CubeModel)"""
        _BlockModelRegistry.register(arg0, arg1, arg2)

    @staticmethod
    @overload
    def registerCustom(arg0: 'Block', arg1: 'Predicate', arg2: 'Supplier'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.registerCustom(dev.ultreon.quantum.block.Block,java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        _BlockModelRegistry.registerCustom(arg0, arg1, arg2)

    @staticmethod
    @overload
    def bakeJsonModels(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.bakeJsonModels(dev.ultreon.quantum.client.QuantumClient)"""
        _BlockModelRegistry.bakeJsonModels(arg0)

    @staticmethod
    @overload
    def registerDefault(arg0: 'Supplier'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.registerDefault(java.util.function.Supplier<dev.ultreon.quantum.block.Block>)"""
        _BlockModelRegistry.registerDefault(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: 'BlockProperties') -> 'BlockModel':
        """public static dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.model.block.BlockModelRegistry.get(dev.ultreon.quantum.block.state.BlockProperties)"""
        return BlockModel._wrap(_BlockModelRegistry.get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.block.BlockModelRegistry()"""
        val = _BlockModelRegistry()
        self.__wrapper = val

    @staticmethod
    @overload
    def bake(arg0: 'TextureAtlas') -> 'BakedModelRegistry':
        """public static dev.ultreon.quantum.client.model.block.BakedModelRegistry dev.ultreon.quantum.client.model.block.BlockModelRegistry.bake(dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return BakedModelRegistry._wrap(_BlockModelRegistry.bake(arg0))

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

    @staticmethod
    @overload
    def load(arg0: 'Json5ModelLoader'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.load(dev.ultreon.quantum.client.model.model.Json5ModelLoader)"""
        _BlockModelRegistry.load(arg0)

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
    def registerDefault(arg0: 'Block'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.registerDefault(dev.ultreon.quantum.block.Block)"""
        _BlockModelRegistry.registerDefault(arg0)

    @staticmethod
    @overload
    def register(arg0: 'Supplier', arg1: 'Predicate', arg2: 'Supplier'):
        """public static void dev.ultreon.quantum.client.model.block.BlockModelRegistry.register(java.util.function.Supplier<dev.ultreon.quantum.block.Block>,java.util.function.Predicate<dev.ultreon.quantum.block.state.BlockProperties>,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.CubeModel>)"""
        _BlockModelRegistry.register(arg0, arg1, arg2)

    @staticmethod
    @overload
    def stitch(arg0: 'TextureManager') -> 'atlas.TextureAtlas':
        """public static dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.model.block.BlockModelRegistry.stitch(dev.ultreon.quantum.client.texture.TextureManager)"""
        return atlas.TextureAtlas._wrap(_BlockModelRegistry.stitch(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.block.BlockModelRegistry()"""
        val = _BlockModelRegistry()
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
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BakedCubeModel
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BakedCubeModel as _BakedCubeModel
_BakedCubeModel = _BakedCubeModel
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties
_ModelProperties = _ModelProperties
import dev.ultreon.quantum.client.model.BakedModel as _BakedModel
_BakedModel = _BakedModel
import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BakedCubeModel():
    """dev.ultreon.quantum.client.model.block.BakedCubeModel"""
 
    @staticmethod
    def _wrap(java_value: _BakedCubeModel) -> 'BakedCubeModel':
        return BakedCubeModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BakedCubeModel):
        """
        Dynamic initializer for BakedCubeModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BakedCubeModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BakedCubeModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.block.BakedCubeModel.hashCode()"""
        return int._wrap(super(BakedCubeModel, self).hashCode())

    @staticmethod
    @overload
    def defaultModel() -> 'BakedCubeModel':
        """public static synchronized dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.defaultModel()"""
        return BakedCubeModel._wrap(_BakedCubeModel.defaultModel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.BakedCubeModel.equals(java.lang.Object)"""
        return bool._wrap(super(_BakedCubeModel, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def bottom(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.bottom()"""
        return 'g2d.TextureRegion'._wrap(super(BakedCubeModel, self).bottom())

    @override
    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(_BlockModel, self).render(arg0, arg1)

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'TextureRegion', arg3: 'TextureRegion', arg4: 'TextureRegion', arg5: 'TextureRegion', arg6: 'TextureRegion', arg7: 'ModelProperties') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return BakedCubeModel._wrap(_BakedCubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return BakedCubeModel._wrap(_BakedCubeModel.of(arg0, arg1))

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.BakedModel.getModel()"""
        return 'g3d.Model'._wrap(super(model.BakedModel, self).getModel())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemOffset()"""
        return 'math.Vector3'._wrap(super(BlockModel, self).getItemOffset())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.block.BakedCubeModel.toString()"""
        return str._wrap(super(BakedCubeModel, self).toString())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'TextureRegion', arg3: 'TextureRegion', arg4: 'TextureRegion', arg5: 'TextureRegion', arg6: 'TextureRegion') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return BakedCubeModel._wrap(_BakedCubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @overload
    def south(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.south()"""
        return 'g2d.TextureRegion'._wrap(super(BakedCubeModel, self).south())

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.block.BakedCubeModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(_BakedCubeModel, self).load(arg0)

    @overload
    def top(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.top()"""
        return 'g2d.TextureRegion'._wrap(super(BakedCubeModel, self).top())

    @overload
    def east(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.east()"""
        return 'g2d.TextureRegion'._wrap(super(BakedCubeModel, self).east())

    @overload
    def north(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.north()"""
        return 'g2d.TextureRegion'._wrap(super(BakedCubeModel, self).north())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'ModelProperties') -> 'BakedCubeModel':
        """public static dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.BakedCubeModel.of(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return BakedCubeModel._wrap(_BakedCubeModel.of(arg0, arg1, arg2))

    @override
    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemScale()"""
        return 'math.Vector3'._wrap(super(BlockModel, self).getItemScale())

    @staticmethod
    @overload
    def createModel(arg0: 'Identifier', arg1: 'TextureRegion', arg2: 'TextureRegion', arg3: 'TextureRegion', arg4: 'TextureRegion', arg5: 'TextureRegion', arg6: 'TextureRegion') -> 'g3d.Model':
        """public static com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.block.BakedCubeModel.createModel(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return g3d.Model._wrap(_BakedCubeModel.createModel(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isCustom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.BakedCubeModel.isCustom()"""
        return bool._wrap(super(BakedCubeModel, self).isCustom())

    @override
    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(_BlockModel, self).loadInto(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dispose(self):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.dispose()"""
        super(BlockModel, self).dispose()

    @overload
    def west(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.model.block.BakedCubeModel.west()"""
        return 'g2d.TextureRegion'._wrap(super(BakedCubeModel, self).west())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.BakedModel.resourceId()"""
        return 'util.Identifier'._wrap(super(model.BakedModel, self).resourceId())

    @property
    def properties(self) -> ModelProperties:
        return ModelProperties._wrap(super(_BakedCubeModel).properties()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.BlockModel
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
import dev.ultreon.quantum.client.resources.LoadableResource as _LoadableResource
_LoadableResource = _LoadableResource
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

 
class BlockModel():
    """dev.ultreon.quantum.client.model.block.BlockModel"""
 
    @staticmethod
    def _wrap(java_value: _BlockModel) -> 'BlockModel':
        return BlockModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockModel):
        """
        Dynamic initializer for BlockModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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

    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemScale()"""
        return 'math.Vector3'._wrap(super(BlockModel, self).getItemScale())

    @abstractmethod
    def isCustom(self, ):
        """public abstract boolean dev.ultreon.quantum.client.model.block.BlockModel.isCustom()"""
        pass

    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(_BlockModel, self).loadInto(arg0, arg1)

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
        super(_BlockModel, self).render(arg0, arg1)

    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.block.BlockModel.getItemOffset()"""
        return 'math.Vector3'._wrap(super(BlockModel, self).getItemOffset()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.CubeModel
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = _import_once("pyquantum.client.atlas")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.block.BakedCubeModel as _BakedCubeModel
_BakedCubeModel = _BakedCubeModel
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Set as Set
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import dev.ultreon.quantum.client.model.block.CubeModel as _CubeModel
_CubeModel = _CubeModel
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubeModel():
    """dev.ultreon.quantum.client.model.block.CubeModel"""
 
    @staticmethod
    def _wrap(java_value: _CubeModel) -> 'CubeModel':
        return CubeModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubeModel):
        """
        Dynamic initializer for CubeModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubeModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubeModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def back(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.back()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).back())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier', arg6: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @overload
    def front(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.front()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).front())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5))

    @overload
    def right(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.right()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).right())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def top(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.top()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).top())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4))

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
    def all(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.client.model.block.CubeModel.all()"""
        return 'Set'._wrap(super(CubeModel, self).all())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier', arg6: 'Identifier', arg7: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.block.CubeModel.hashCode()"""
        return int._wrap(super(CubeModel, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.CubeModel.equals(java.lang.Object)"""
        return bool._wrap(super(_CubeModel, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.block.CubeModel.toString()"""
        return str._wrap(super(CubeModel, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1))

    @overload
    def left(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.left()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).left())

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'Identifier', arg3: 'Identifier', arg4: 'Identifier', arg5: 'Identifier', arg6: 'Identifier') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @staticmethod
    @overload
    def of(arg0: 'Identifier', arg1: 'Identifier', arg2: 'ModelProperties') -> 'CubeModel':
        """public static dev.ultreon.quantum.client.model.block.CubeModel dev.ultreon.quantum.client.model.block.CubeModel.of(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.model.block.ModelProperties)"""
        return CubeModel._wrap(_CubeModel.of(arg0, arg1, arg2))

    @overload
    def bake(self, arg0: 'Identifier', arg1: 'TextureAtlas') -> 'BakedCubeModel':
        """public dev.ultreon.quantum.client.model.block.BakedCubeModel dev.ultreon.quantum.client.model.block.CubeModel.bake(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return 'BakedCubeModel'._wrap(super(_CubeModel, self).bake(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.resourceId()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).resourceId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def bottom(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.block.CubeModel.bottom()"""
        return 'util.Identifier'._wrap(super(CubeModel, self).bottom()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.block.ModelProperties
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
import dev.ultreon.quantum.client.world.FaceProperties as _FaceProperties
_FaceProperties = _FaceProperties
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties_Builder
_Builder = _ModelProperties_Builder.Builder
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.CubicDirection as _CubicDirection
_CubicDirection = _CubicDirection
import dev.ultreon.quantum.client.model.block.ModelProperties as _ModelProperties
_ModelProperties = _ModelProperties
import java.lang.Integer as _int
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelProperties():
    """dev.ultreon.quantum.client.model.block.ModelProperties"""
 
    @staticmethod
    def _wrap(java_value: _ModelProperties) -> 'ModelProperties':
        return ModelProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelProperties):
        """
        Dynamic initializer for ModelProperties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelProperties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelProperties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'FaceProperties', arg1: 'CubicDirection'):
        """public dev.ultreon.quantum.client.model.block.ModelProperties(dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.world.CubicDirection)"""
        val = _ModelProperties(arg0, arg1)
        self.__wrapper = val

    @property
    def top(self) -> FaceProperties:
        return FaceProperties._wrap(super(_ModelProperties).top())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.block.ModelProperties.equals(java.lang.Object)"""
        return bool._wrap(super(_ModelProperties, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.block.ModelProperties.hashCode()"""
        return int._wrap(super(ModelProperties, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def rotation(self) -> CubicDirection:
        return CubicDirection._wrap(super(_ModelProperties).rotation())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FaceProperties', arg1: 'FaceProperties', arg2: 'FaceProperties', arg3: 'FaceProperties', arg4: 'FaceProperties', arg5: 'FaceProperties', arg6: 'CubicDirection'):
        """public dev.ultreon.quantum.client.model.block.ModelProperties(dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.client.world.FaceProperties,dev.ultreon.quantum.world.CubicDirection)"""
        val = _ModelProperties(arg0, arg1, arg2, arg3, arg4, arg5, arg6)
        self.__wrapper = val

    @property
    def right(self) -> FaceProperties:
        return FaceProperties._wrap(super(_ModelProperties).right())

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

    @property
    def bottom(self) -> FaceProperties:
        return FaceProperties._wrap(super(_ModelProperties).bottom())

    @property
    def back(self) -> FaceProperties:
        return FaceProperties._wrap(super(_ModelProperties).back())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.client.model.block.ModelProperties$Builder dev.ultreon.quantum.client.model.block.ModelProperties.builder()"""
        return Builder._wrap(_ModelProperties.builder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @property
    def front(self) -> FaceProperties:
        return FaceProperties._wrap(super(_ModelProperties).front())

    @property
    def left(self) -> FaceProperties:
        return FaceProperties._wrap(super(_ModelProperties).left())