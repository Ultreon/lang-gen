from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.model.model.ModelType as __ModelType
__ModelType = __ModelType
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
 
class ModelType():
    """dev.ultreon.quantum.client.model.model.ModelType"""
 
    @staticmethod
    def __wrap(java_value: __ModelType) -> 'ModelType':
        return ModelType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelType):
        """
        Dynamic initializer for ModelType.
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
 
    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.G3DJ
    G3DJ: 'ModelType' = __wrap(__ModelType.G3DJ)

    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.GLTF
    GLTF: 'ModelType' = __wrap(__ModelType.GLTF)

    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.GLB
    GLB: 'ModelType' = __wrap(__ModelType.GLB)

    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.G3DB
    G3DB: 'ModelType' = __wrap(__ModelType.G3DB)


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
    def values() -> List['ModelType']:
        """public static dev.ultreon.quantum.client.model.model.ModelType[] dev.ultreon.quantum.client.model.model.ModelType.values()"""
        return List[ModelType].__wrap(__ModelType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ModelType':
        """public static dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.valueOf(java.lang.String)"""
        return ModelType.__wrap(__ModelType.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.ModelType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.model.model.ModelType as __ModelType
__ModelType = __ModelType
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
 
class ModelType():
    """dev.ultreon.quantum.client.model.model.ModelType"""
 
    @staticmethod
    def __wrap(java_value: __ModelType) -> 'ModelType':
        return ModelType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelType):
        """
        Dynamic initializer for ModelType.
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
 
    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.G3DJ
    G3DJ: 'ModelType' = __wrap(__ModelType.G3DJ)

    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.GLTF
    GLTF: 'ModelType' = __wrap(__ModelType.GLTF)

    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.GLB
    GLB: 'ModelType' = __wrap(__ModelType.GLB)

    # public static final dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.G3DB
    G3DB: 'ModelType' = __wrap(__ModelType.G3DB)


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
    def values() -> List['ModelType']:
        """public static dev.ultreon.quantum.client.model.model.ModelType[] dev.ultreon.quantum.client.model.model.ModelType.values()"""
        return List[ModelType].__wrap(__ModelType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ModelType':
        """public static dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.valueOf(java.lang.String)"""
        return ModelType.__wrap(__ModelType.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.ModelType 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5Model
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.registry.RegistryKey as __RegistryKey
__RegistryKey = __RegistryKey
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_Display
__Display = __Json5ModelLoader_Display.Display
import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.client.model.model.Json5Model as __Json5Model
__Json5Model = __Json5Model
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import com.google.common.collect.Table as __Table
__Table = __Table
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

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.item.ItemModel as __ItemModel
__ItemModel = __ItemModel
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class Json5Model():
    """dev.ultreon.quantum.client.model.model.Json5Model"""
 
    @staticmethod
    def __wrap(java_value: __Json5Model) -> 'Json5Model':
        return Json5Model(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Json5Model):
        """
        Dynamic initializer for Json5Model.
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
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.model.Json5Model.resourceId()"""
        return 'util.Identifier'.__wrap(super(Json5Model, self).resourceId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5Model.getItemOffset()"""
        return 'math.Vector3'.__wrap(super(Json5Model, self).getItemOffset())

    @override
    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(__block.BlockModel, self).loadInto(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getOverrides(self) -> 'pygcollect.Table':
        """public com.google.common.collect.Table<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>, dev.ultreon.quantum.client.model.model.Json5Model> dev.ultreon.quantum.client.model.model.Json5Model.getOverrides()"""
        return 'pygcollect.Table'.__wrap(super(Json5Model, self).getOverrides())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.model.Json5Model.dispose()"""
        super(Json5Model, self).dispose()

    @overload
    def __init__(self, arg0: 'RegistryKey', arg1: 'Map', arg2: 'List', arg3: bool, arg4: 'Display', arg5: 'Table'):
        """public dev.ultreon.quantum.client.model.model.Json5Model(dev.ultreon.quantum.registry.RegistryKey<?>,java.util.Map<java.lang.String, dev.ultreon.quantum.util.Identifier>,java.util.List<dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement>,boolean,dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display,com.google.common.collect.Table<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>, dev.ultreon.quantum.client.model.model.Json5Model>)"""
        val = __Json5Model(arg0, arg1, arg2, __boolean.valueOf(arg3), arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def bake(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.model.Json5Model.bake()"""
        return 'g3d.Model'.__wrap(super(Json5Model, self).bake())

    @override
    @overload
    def getScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getScale()"""
        return 'math.Vector3'.__wrap(super(item.ItemModel, self).getScale())

    @property
    def display(self) -> Display:
        return Display.__wrap(super(__Json5Model).display())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(__block.BlockModel, self).render(arg0, arg1)

    @override
    @overload
    def getOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getOffset()"""
        return 'math.Vector3'.__wrap(super(item.ItemModel, self).getOffset())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.model.Json5Model.getModel()"""
        return 'g3d.Model'.__wrap(super(Json5Model, self).getModel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5Model.getItemScale()"""
        return 'math.Vector3'.__wrap(super(Json5Model, self).getItemScale())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.model.Json5Model.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(__Json5Model, self).load(arg0)

    @overload
    def getKey(self) -> 'registry.RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<?> dev.ultreon.quantum.client.model.model.Json5Model.getKey()"""
        return 'registry.RegistryKey'.__wrap(super(Json5Model, self).getKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isCustom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5Model.isCustom()"""
        return bool.__wrap(super(Json5Model, self).isCustom())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.util.Axis as __Axis
__Axis = __Axis
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_ElementRotation
__ElementRotation = __Json5ModelLoader_ElementRotation.ElementRotation
import de.marhali.json5.Json5Object as Json5Object
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ElementRotation():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.ElementRotation"""
 
    @staticmethod
    def __wrap(java_value: __ElementRotation) -> 'ElementRotation':
        return ElementRotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ElementRotation):
        """
        Dynamic initializer for ElementRotation.
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
    def angle(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.angle()"""
        return float.__wrap(super(ElementRotation, self).angle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def axis(self) -> 'util.Axis':
        """public dev.ultreon.quantum.util.Axis dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.axis()"""
        return 'util.Axis'.__wrap(super(ElementRotation, self).axis())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.toString()"""
        return str.__wrap(super(ElementRotation, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.hashCode()"""
        return int.__wrap(super(ElementRotation, self).hashCode())

    @overload
    def originVec(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.originVec()"""
        return 'math.Vector3'.__wrap(super(ElementRotation, self).originVec())

    @overload
    def rescale(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.rescale()"""
        return bool.__wrap(super(ElementRotation, self).rescale())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.equals(java.lang.Object)"""
        return bool.__wrap(super(__ElementRotation, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def deserialize(arg0: 'Json5Object') -> 'ElementRotation':
        """public static dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.deserialize(de.marhali.json5.Json5Object)"""
        return ElementRotation.__wrap(__ElementRotation.deserialize(arg0))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Axis', arg2: float, arg3: bool):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.util.Axis,float,boolean)"""
        val = __ElementRotation(arg0, arg1, __float.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_UVs
__UVs = __Json5ModelLoader_UVs.UVs
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_FaceElement
__FaceElement = __Json5ModelLoader_FaceElement.FaceElement
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FaceElement():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.FaceElement"""
 
    @staticmethod
    def __wrap(java_value: __FaceElement) -> 'FaceElement':
        return FaceElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FaceElement):
        """
        Dynamic initializer for FaceElement.
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
    def rotation(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.rotation()"""
        return int.__wrap(super(FaceElement, self).rotation())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.equals(java.lang.Object)"""
        return bool.__wrap(super(__FaceElement, self).equals(arg0))

    @overload
    def uvs(self) -> 'UVs':
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.uvs()"""
        return 'UVs'.__wrap(super(FaceElement, self).uvs())

    @overload
    def texture(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.texture()"""
        return str.__wrap(super(FaceElement, self).texture())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.hashCode()"""
        return int.__wrap(super(FaceElement, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def cullface(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.cullface()"""
        return str.__wrap(super(FaceElement, self).cullface())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'UVs', arg2: int, arg3: int, arg4: str):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement(java.lang.String,dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs,int,int,java.lang.String)"""
        val = __FaceElement(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), arg4)
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
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.toString()"""
        return str.__wrap(super(FaceElement, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tintindex(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.tintindex()"""
        return int.__wrap(super(FaceElement, self).tintindex()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display
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
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_Display
__Display = __Json5ModelLoader_Display.Display
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Display():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.Display"""
 
    @staticmethod
    def __wrap(java_value: __Display) -> 'Display':
        return Display(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Display):
        """
        Dynamic initializer for Display.
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display.toString()"""
        return str.__wrap(super(Display, self).toString())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display()"""
        val = __Display()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display()"""
        val = __Display()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display.equals(java.lang.Object)"""
        return bool.__wrap(super(__Display, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display.hashCode()"""
        return int.__wrap(super(Display, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_UVs
__UVs = __Json5ModelLoader_UVs.UVs
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UVs():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.UVs"""
 
    @staticmethod
    def __wrap(java_value: __UVs) -> 'UVs':
        return UVs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UVs):
        """
        Dynamic initializer for UVs.
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
    def y1(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.y1()"""
        return float.__wrap(super(UVs, self).y1())

    @overload
    def x2(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.x2()"""
        return float.__wrap(super(UVs, self).x2())

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
    def x1(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.x1()"""
        return float.__wrap(super(UVs, self).x1())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs(float,float,float,float)"""
        val = __UVs(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.toString()"""
        return str.__wrap(super(UVs, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.equals(java.lang.Object)"""
        return bool.__wrap(super(__UVs, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs(float,float,float,float,int,int)"""
        val = __UVs(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def y2(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.y2()"""
        return float.__wrap(super(UVs, self).y2())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.hashCode()"""
        return int.__wrap(super(UVs, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_ModelElement
__ModelElement = __Json5ModelLoader_ModelElement.ModelElement
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader_ElementRotation
__ElementRotation = __Json5ModelLoader_ElementRotation.ElementRotation
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ModelElement():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.ModelElement"""
 
    @staticmethod
    def __wrap(java_value: __ModelElement) -> 'ModelElement':
        return ModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelElement):
        """
        Dynamic initializer for ModelElement.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def shade(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.shade()"""
        return bool.__wrap(super(ModelElement, self).shade())

    @overload
    def from(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.from()"""
        return 'math.Vector3'.__wrap(super(ModelElement, self).from())

    @overload
    def rotation(self) -> 'ElementRotation':
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.rotation()"""
        return 'ElementRotation'.__wrap(super(ModelElement, self).rotation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.equals(java.lang.Object)"""
        return bool.__wrap(super(__ModelElement, self).equals(arg0))

    @overload
    def blockFaceFaceElementMap(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.CubicDirection, dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement> dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.blockFaceFaceElementMap()"""
        return 'Map'.__wrap(super(ModelElement, self).blockFaceFaceElementMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.toString()"""
        return str.__wrap(super(ModelElement, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Map', arg1: bool, arg2: 'ElementRotation', arg3: 'Vector3', arg4: 'Vector3'):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement(java.util.Map<dev.ultreon.quantum.world.CubicDirection, dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement>,boolean,dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __ModelElement(arg0, __boolean.valueOf(arg1), arg2, arg3, arg4)
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
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.hashCode()"""
        return int.__wrap(super(ModelElement, self).hashCode())

    @overload
    def to(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.to()"""
        return 'math.Vector3'.__wrap(super(ModelElement, self).to())

    @overload
    def bake(self, arg0: int, arg1: 'ModelBuilder', arg2: 'Map'):
        """public void dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.bake(int,com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.String, dev.ultreon.quantum.util.Identifier>)"""
        super(__ModelElement, self).bake(__int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.model.model.Json5Model as __Json5Model
__Json5Model = __Json5Model
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
try:
    from pyquantum.client.model import block
except ImportError:
    block = __import_once__("pyquantum.client.model.block")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import de.marhali.json5.Json5Element as Json5Element
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

from builtins import bool
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as __Json5ModelLoader
__Json5ModelLoader = __Json5ModelLoader
from builtins import int
 
class Json5ModelLoader():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader"""
 
    @staticmethod
    def __wrap(java_value: __Json5ModelLoader) -> 'Json5ModelLoader':
        return Json5ModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Json5ModelLoader):
        """
        Dynamic initializer for Json5ModelLoader.
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
    def load(self, arg0: 'RegistryKey', arg1: 'Json5Element') -> 'Json5Model':
        """public dev.ultreon.quantum.client.model.model.Json5Model dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.registry.RegistryKey<?>,de.marhali.json5.Json5Element)"""
        return 'Json5Model'.__wrap(super(__Json5ModelLoader, self).load(arg0, arg1))

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
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader()"""
        val = __Json5ModelLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self, arg0: 'RegistryKey', arg1: 'Identifier') -> 'block.BlockModel':
        """public dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.registry.RegistryKey<?>,dev.ultreon.quantum.util.Identifier)"""
        return 'block.BlockModel'.__wrap(super(__Json5ModelLoader, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'Item') -> 'Json5Model':
        """public dev.ultreon.quantum.client.model.model.Json5Model dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.item.Item) throws java.io.IOException"""
        return 'Json5Model'.__wrap(super(__Json5ModelLoader, self).load(arg0))

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
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader(dev.ultreon.quantum.resources.ResourceManager)"""
        val = __Json5ModelLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self, arg0: 'Block') -> 'Json5Model':
        """public dev.ultreon.quantum.client.model.model.Json5Model dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.block.Block) throws java.io.IOException"""
        return 'Json5Model'.__wrap(super(__Json5ModelLoader, self).load(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader()"""
        val = __Json5ModelLoader()
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