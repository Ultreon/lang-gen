from __future__ import annotations
from overload import overload


 
from builtins import str
import dev.ultreon.quantum.client.model.model.ModelType as _ModelType
_ModelType = _ModelType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
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
 
class ModelType():
    """dev.ultreon.quantum.client.model.model.ModelType"""
 
    @staticmethod
    def _wrap(java_value: _ModelType) -> 'ModelType':
        return ModelType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelType):
        """
        Dynamic initializer for ModelType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelType__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ModelType':
        """public static dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.valueOf(java.lang.String)"""
        return ModelType._wrap(_ModelType.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['ModelType']:
        """public static dev.ultreon.quantum.client.model.model.ModelType[] dev.ultreon.quantum.client.model.model.ModelType.values()"""
        return List[ModelType]._wrap(_ModelType.values())

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


ModelType.GLB = ModelType._wrap(_GLB.GLB)

ModelType.G3DB = ModelType._wrap(_G3DB.G3DB)

ModelType.GLTF = ModelType._wrap(_GLTF.GLTF)

ModelType.G3DJ = ModelType._wrap(_G3DJ.G3DJ)

 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.ModelType
from builtins import str
import dev.ultreon.quantum.client.model.model.ModelType as _ModelType
_ModelType = _ModelType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
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
 
class ModelType():
    """dev.ultreon.quantum.client.model.model.ModelType"""
 
    @staticmethod
    def _wrap(java_value: _ModelType) -> 'ModelType':
        return ModelType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelType):
        """
        Dynamic initializer for ModelType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelType__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ModelType':
        """public static dev.ultreon.quantum.client.model.model.ModelType dev.ultreon.quantum.client.model.model.ModelType.valueOf(java.lang.String)"""
        return ModelType._wrap(_ModelType.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['ModelType']:
        """public static dev.ultreon.quantum.client.model.model.ModelType[] dev.ultreon.quantum.client.model.model.ModelType.values()"""
        return List[ModelType]._wrap(_ModelType.values())

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


ModelType.GLB = ModelType._wrap(_GLB.GLB)

ModelType.G3DB = ModelType._wrap(_G3DB.G3DB)

ModelType.GLTF = ModelType._wrap(_GLTF.GLTF)

ModelType.G3DJ = ModelType._wrap(_G3DJ.G3DJ)

 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.ModelType 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5Model
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_Display
_Display = _Json5ModelLoader_Display.Display
import com.google.common.collect.Table as _Table
_Table = _Table
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.model.item.ItemModel as _ItemModel
_ItemModel = _ItemModel
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import dev.ultreon.quantum.registry.RegistryKey as _RegistryKey
_RegistryKey = _RegistryKey
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.client.model.model.Json5Model as _Json5Model
_Json5Model = _Json5Model
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class Json5Model():
    """dev.ultreon.quantum.client.model.model.Json5Model"""
 
    @staticmethod
    def _wrap(java_value: _Json5Model) -> 'Json5Model':
        return Json5Model(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Json5Model):
        """
        Dynamic initializer for Json5Model.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Json5Model__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Json5Model__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.model.Json5Model.dispose()"""
        super(Json5Model, self).dispose()

    @override
    @overload
    def getItemOffset(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5Model.getItemOffset()"""
        return 'math.Vector3'._wrap(super(Json5Model, self).getItemOffset())

    @override
    @overload
    def loadInto(self, arg0: 'BlockPos', arg1: 'ClientChunk'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.loadInto(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.client.world.ClientChunk)"""
        super(_block.BlockModel, self).loadInto(arg0, arg1)

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
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.model.Json5Model.getModel()"""
        return 'g3d.Model'._wrap(super(Json5Model, self).getModel())

    @overload
    def getKey(self) -> 'registry.RegistryKey':
        """public dev.ultreon.quantum.registry.RegistryKey<?> dev.ultreon.quantum.client.model.model.Json5Model.getKey()"""
        return 'registry.RegistryKey'._wrap(super(Json5Model, self).getKey())

    @property
    def display(self) -> Display:
        return Display._wrap(super(_Json5Model).display())

    @override
    @overload
    def isCustom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5Model.isCustom()"""
        return bool._wrap(super(Json5Model, self).isCustom())

    @override
    @overload
    def getItemScale(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5Model.getItemScale()"""
        return 'math.Vector3'._wrap(super(Json5Model, self).getItemScale())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getOffset()"""
        return 'math.Vector3'._wrap(super(item.ItemModel, self).getOffset())

    @override
    @overload
    def render(self, arg0: 'Vector3', arg1: 'Scene3D'):
        """public default void dev.ultreon.quantum.client.model.block.BlockModel.render(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.client.render.Scene3D)"""
        super(_block.BlockModel, self).render(arg0, arg1)

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.model.Json5Model.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(_Json5Model, self).load(arg0)

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.model.Json5Model.resourceId()"""
        return 'util.Identifier'._wrap(super(Json5Model, self).resourceId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def bake(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.model.Json5Model.bake()"""
        return 'g3d.Model'._wrap(super(Json5Model, self).bake())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'RegistryKey', arg1: 'Map', arg2: 'List', arg3: bool, arg4: 'Display', arg5: 'Table'):
        """public dev.ultreon.quantum.client.model.model.Json5Model(dev.ultreon.quantum.registry.RegistryKey<?>,java.util.Map<java.lang.String, dev.ultreon.quantum.util.Identifier>,java.util.List<dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement>,boolean,dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display,com.google.common.collect.Table<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>, dev.ultreon.quantum.client.model.model.Json5Model>)"""
        val = _Json5Model(arg0, arg1, arg2, _boolean.valueOf(arg3), arg4, arg5)
        self.__wrapper = val

    @overload
    def getOverrides(self) -> 'pygcollect.Table':
        """public com.google.common.collect.Table<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>, dev.ultreon.quantum.client.model.model.Json5Model> dev.ultreon.quantum.client.model.model.Json5Model.getOverrides()"""
        return 'pygcollect.Table'._wrap(super(Json5Model, self).getOverrides())

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

    @override
    @overload
    def getScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getScale()"""
        return 'math.Vector3'._wrap(super(item.ItemModel, self).getScale())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import dev.ultreon.quantum.util.Axis as _Axis
_Axis = _Axis
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_ElementRotation
_ElementRotation = _Json5ModelLoader_ElementRotation.ElementRotation
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ElementRotation():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.ElementRotation"""
 
    @staticmethod
    def _wrap(java_value: _ElementRotation) -> 'ElementRotation':
        return ElementRotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ElementRotation):
        """
        Dynamic initializer for ElementRotation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ElementRotation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ElementRotation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Axis', arg2: float, arg3: bool):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation(com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.util.Axis,float,boolean)"""
        val = _ElementRotation(arg0, arg1, _float.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.hashCode()"""
        return int._wrap(super(ElementRotation, self).hashCode())

    @overload
    def angle(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.angle()"""
        return float._wrap(super(ElementRotation, self).angle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def axis(self) -> 'util.Axis':
        """public dev.ultreon.quantum.util.Axis dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.axis()"""
        return 'util.Axis'._wrap(super(ElementRotation, self).axis())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.toString()"""
        return str._wrap(super(ElementRotation, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.equals(java.lang.Object)"""
        return bool._wrap(super(_ElementRotation, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def rescale(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.rescale()"""
        return bool._wrap(super(ElementRotation, self).rescale())

    @overload
    def originVec(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.originVec()"""
        return 'math.Vector3'._wrap(super(ElementRotation, self).originVec())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def deserialize(arg0: 'Json5Object') -> 'ElementRotation':
        """public static dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation.deserialize(de.marhali.json5.Json5Object)"""
        return ElementRotation._wrap(_ElementRotation.deserialize(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_FaceElement
_FaceElement = _Json5ModelLoader_FaceElement.FaceElement
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_UVs
_UVs = _Json5ModelLoader_UVs.UVs
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FaceElement():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.FaceElement"""
 
    @staticmethod
    def _wrap(java_value: _FaceElement) -> 'FaceElement':
        return FaceElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FaceElement):
        """
        Dynamic initializer for FaceElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FaceElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FaceElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def texture(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.texture()"""
        return str._wrap(super(FaceElement, self).texture())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.toString()"""
        return str._wrap(super(FaceElement, self).toString())

    @overload
    def rotation(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.rotation()"""
        return int._wrap(super(FaceElement, self).rotation())

    @overload
    def uvs(self) -> 'UVs':
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.uvs()"""
        return 'UVs'._wrap(super(FaceElement, self).uvs())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.hashCode()"""
        return int._wrap(super(FaceElement, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: 'UVs', arg2: int, arg3: int, arg4: str):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement(java.lang.String,dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs,int,int,java.lang.String)"""
        val = _FaceElement(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def cullface(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.cullface()"""
        return str._wrap(super(FaceElement, self).cullface())

    @overload
    def tintindex(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.tintindex()"""
        return int._wrap(super(FaceElement, self).tintindex())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement.equals(java.lang.Object)"""
        return bool._wrap(super(_FaceElement, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_Display
_Display = _Json5ModelLoader_Display.Display
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Display():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.Display"""
 
    @staticmethod
    def _wrap(java_value: _Display) -> 'Display':
        return Display(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Display):
        """
        Dynamic initializer for Display.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Display__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Display__wrapper":
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
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display.equals(java.lang.Object)"""
        return bool._wrap(super(_Display, self).equals(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display()"""
        val = _Display()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display.toString()"""
        return str._wrap(super(Display, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display.hashCode()"""
        return int._wrap(super(Display, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$Display()"""
        val = _Display()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_UVs
_UVs = _Json5ModelLoader_UVs.UVs
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UVs():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.UVs"""
 
    @staticmethod
    def _wrap(java_value: _UVs) -> 'UVs':
        return UVs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UVs):
        """
        Dynamic initializer for UVs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UVs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UVs__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs(float,float,float,float)"""
        val = _UVs(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @overload
    def y2(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.y2()"""
        return float._wrap(super(UVs, self).y2())

    @overload
    def y1(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.y1()"""
        return float._wrap(super(UVs, self).y1())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.hashCode()"""
        return int._wrap(super(UVs, self).hashCode())

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
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs(float,float,float,float,int,int)"""
        val = _UVs(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.toString()"""
        return str._wrap(super(UVs, self).toString())

    @overload
    def x2(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.x2()"""
        return float._wrap(super(UVs, self).x2())

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
    def x1(self) -> float:
        """public float dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.x1()"""
        return float._wrap(super(UVs, self).x1())

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
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$UVs.equals(java.lang.Object)"""
        return bool._wrap(super(_UVs, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_ModelElement
_ModelElement = _Json5ModelLoader_ModelElement.ModelElement
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader_ElementRotation
_ElementRotation = _Json5ModelLoader_ElementRotation.ElementRotation
import java.lang.Class as _Class
_Class = _Class
 
class ModelElement():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader.ModelElement"""
 
    @staticmethod
    def _wrap(java_value: _ModelElement) -> 'ModelElement':
        return ModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelElement):
        """
        Dynamic initializer for ModelElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rotation(self) -> 'ElementRotation':
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.rotation()"""
        return 'ElementRotation'._wrap(super(ModelElement, self).rotation())

    @overload
    def blockFaceFaceElementMap(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.world.CubicDirection, dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement> dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.blockFaceFaceElementMap()"""
        return 'Map'._wrap(super(ModelElement, self).blockFaceFaceElementMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.hashCode()"""
        return int._wrap(super(ModelElement, self).hashCode())

    @overload
    def __init__(self, arg0: 'Map', arg1: bool, arg2: 'ElementRotation', arg3: 'Vector3', arg4: 'Vector3'):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement(java.util.Map<dev.ultreon.quantum.world.CubicDirection, dev.ultreon.quantum.client.model.model.Json5ModelLoader$FaceElement>,boolean,dev.ultreon.quantum.client.model.model.Json5ModelLoader$ElementRotation,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _ModelElement(arg0, _boolean.valueOf(arg1), arg2, arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def from(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.from()"""
        return 'math.Vector3'._wrap(super(ModelElement, self).from())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.equals(java.lang.Object)"""
        return bool._wrap(super(_ModelElement, self).equals(arg0))

    @overload
    def to(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.to()"""
        return 'math.Vector3'._wrap(super(ModelElement, self).to())

    @overload
    def bake(self, arg0: int, arg1: 'ModelBuilder', arg2: 'Map'):
        """public void dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.bake(int,com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.String, dev.ultreon.quantum.util.Identifier>)"""
        super(_ModelElement, self).bake(_int.valueOf(arg0), arg1, arg2)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.toString()"""
        return str._wrap(super(ModelElement, self).toString())

    @overload
    def shade(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.model.Json5ModelLoader$ModelElement.shade()"""
        return bool._wrap(super(ModelElement, self).shade()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.model.Json5ModelLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
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
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.model import block
except ImportError:
    block = _import_once("pyquantum.client.model.block")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.model.model.Json5ModelLoader as _Json5ModelLoader
_Json5ModelLoader = _Json5ModelLoader
import de.marhali.json5.Json5Element as Json5Element
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.model.Json5Model as _Json5Model
_Json5Model = _Json5Model
import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Json5ModelLoader():
    """dev.ultreon.quantum.client.model.model.Json5ModelLoader"""
 
    @staticmethod
    def _wrap(java_value: _Json5ModelLoader) -> 'Json5ModelLoader':
        return Json5ModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Json5ModelLoader):
        """
        Dynamic initializer for Json5ModelLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Json5ModelLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Json5ModelLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'Item') -> 'Json5Model':
        """public dev.ultreon.quantum.client.model.model.Json5Model dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.item.Item) throws java.io.IOException"""
        return 'Json5Model'._wrap(super(_Json5ModelLoader, self).load(arg0))

    @overload
    def load(self, arg0: 'RegistryKey', arg1: 'Json5Element') -> 'Json5Model':
        """public dev.ultreon.quantum.client.model.model.Json5Model dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.registry.RegistryKey<?>,de.marhali.json5.Json5Element)"""
        return 'Json5Model'._wrap(super(_Json5ModelLoader, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'Block') -> 'Json5Model':
        """public dev.ultreon.quantum.client.model.model.Json5Model dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.block.Block) throws java.io.IOException"""
        return 'Json5Model'._wrap(super(_Json5ModelLoader, self).load(arg0))

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
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader()"""
        val = _Json5ModelLoader()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'RegistryKey', arg1: 'Identifier') -> 'block.BlockModel':
        """public dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.model.model.Json5ModelLoader.load(dev.ultreon.quantum.registry.RegistryKey<?>,dev.ultreon.quantum.util.Identifier)"""
        return 'block.BlockModel'._wrap(super(_Json5ModelLoader, self).load(arg0, arg1))

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
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader(dev.ultreon.quantum.resources.ResourceManager)"""
        val = _Json5ModelLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.model.Json5ModelLoader()"""
        val = _Json5ModelLoader()
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