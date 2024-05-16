from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.model.ModelImporter as _ModelImporter
_ModelImporter = _ModelImporter
 
class ModelImporter():
    """dev.ultreon.quantum.client.model.ModelImporter"""
 
    @staticmethod
    def _wrap(java_value: _ModelImporter) -> 'ModelImporter':
        return ModelImporter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelImporter):
        """
        Dynamic initializer for ModelImporter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelImporter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelImporter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.ModelImporter.getModel()"""
        pass

    @abstractmethod
    def createModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.ModelImporter.createModel()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.model.ModelImporter
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.model.ModelImporter as _ModelImporter
_ModelImporter = _ModelImporter
 
class ModelImporter():
    """dev.ultreon.quantum.client.model.ModelImporter"""
 
    @staticmethod
    def _wrap(java_value: _ModelImporter) -> 'ModelImporter':
        return ModelImporter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelImporter):
        """
        Dynamic initializer for ModelImporter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelImporter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelImporter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.ModelImporter.getModel()"""
        pass

    @abstractmethod
    def createModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.ModelImporter.createModel()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.model.ModelImporter 
 
 
# CLASS: dev.ultreon.quantum.client.model.WorldRenderContext
import dev.ultreon.quantum.client.render.RenderContext as _RenderContext
_RenderContext = _RenderContext
import dev.ultreon.quantum.client.model.WorldRenderContext as _WorldRenderContext
_WorldRenderContext = _WorldRenderContext
from abc import abstractmethod, ABC
 
class WorldRenderContext():
    """dev.ultreon.quantum.client.model.WorldRenderContext"""
 
    @staticmethod
    def _wrap(java_value: _WorldRenderContext) -> 'WorldRenderContext':
        return WorldRenderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldRenderContext):
        """
        Dynamic initializer for WorldRenderContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldRenderContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldRenderContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getHolder(self, ):
        """public abstract T dev.ultreon.quantum.client.render.RenderContext.getHolder()"""
        pass

    @abstractmethod
    def getWorld(self, ):
        """public abstract dev.ultreon.quantum.world.World dev.ultreon.quantum.client.model.WorldRenderContext.getWorld()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.model.WorldRenderContextImpl
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.WorldRenderContextImpl as _WorldRenderContextImpl
_WorldRenderContextImpl = _WorldRenderContextImpl
import java.lang.Object as _object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldRenderContextImpl():
    """dev.ultreon.quantum.client.model.WorldRenderContextImpl"""
 
    @staticmethod
    def _wrap(java_value: _WorldRenderContextImpl) -> 'WorldRenderContextImpl':
        return WorldRenderContextImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldRenderContextImpl):
        """
        Dynamic initializer for WorldRenderContextImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldRenderContextImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldRenderContextImpl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.client.model.WorldRenderContextImpl.getWorld()"""
        return 'world.World'._wrap(super(WorldRenderContextImpl, self).getWorld())

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
    def getHolder(self) -> object:
        """public T dev.ultreon.quantum.client.model.WorldRenderContextImpl.getHolder()"""
        return object._wrap(super(WorldRenderContextImpl, self).getHolder())

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
    def relative(self, arg0: 'Vec3d', arg1: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.model.WorldRenderContextImpl.relative(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_WorldRenderContextImpl, self).relative(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Scene3D', arg1: object, arg2: 'World', arg3: float, arg4: 'Vec3d'):
        """public dev.ultreon.quantum.client.model.WorldRenderContextImpl(dev.ultreon.quantum.client.render.Scene3D,T,dev.ultreon.quantum.world.World,float,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _WorldRenderContextImpl(arg0, arg1, arg2, _float.valueOf(arg3), arg4)
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
 
 
# CLASS: dev.ultreon.quantum.client.model.BakedModel
from pyquantum_helper import import_once as _import_once
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
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.BakedModel as _BakedModel
_BakedModel = _BakedModel
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BakedModel():
    """dev.ultreon.quantum.client.model.BakedModel"""
 
    @staticmethod
    def _wrap(java_value: _BakedModel) -> 'BakedModel':
        return BakedModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BakedModel):
        """
        Dynamic initializer for BakedModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BakedModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BakedModel__wrapper":
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
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.BakedModel.getModel()"""
        return 'g3d.Model'._wrap(super(BakedModel, self).getModel())

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
    def resourceId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.BakedModel.resourceId()"""
        return 'util.Identifier'._wrap(super(BakedModel, self).resourceId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.BakedModel(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.Model)"""
        val = _BakedModel(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.quantum.client.model.EntityModelInstance
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
import dev.ultreon.quantum.client.model.EntityModelInstance as _EntityModelInstance
_EntityModelInstance = _EntityModelInstance
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityModelInstance():
    """dev.ultreon.quantum.client.model.EntityModelInstance"""
 
    @staticmethod
    def _wrap(java_value: _EntityModelInstance) -> 'EntityModelInstance':
        return EntityModelInstance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityModelInstance):
        """
        Dynamic initializer for EntityModelInstance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityModelInstance__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityModelInstance__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def scale(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(com.badlogic.gdx.math.Vector3)"""
        super(_EntityModelInstance, self).scale(arg0)

    @overload
    def getModel(self) -> 'QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.EntityModelInstance.getModel()"""
        return 'QVModel'._wrap(super(EntityModelInstance, self).getModel())

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(double,double,double)"""
        super(_EntityModelInstance, self).scale(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def setTextures(self, arg0: 'Identifier'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.setTextures(dev.ultreon.quantum.util.Identifier)"""
        super(_EntityModelInstance, self).setTextures(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTranslation(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.setTranslation(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_EntityModelInstance, self).setTranslation(arg0)

    @overload
    def scale(self, arg0: int):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(int)"""
        super(_EntityModelInstance, self).scale(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'QVModel', arg1: 'Entity'):
        """public dev.ultreon.quantum.client.model.EntityModelInstance(dev.ultreon.quantum.client.model.QVModel,T)"""
        val = _EntityModelInstance(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def rotateZ(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.rotateZ(double)"""
        super(_EntityModelInstance, self).rotateZ(_double.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def scale(self, arg0: 'Vec3f'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        super(_EntityModelInstance, self).scale(arg0)

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(float,float,float)"""
        super(_EntityModelInstance, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def scale(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_EntityModelInstance, self).scale(arg0)

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(com.badlogic.gdx.math.Vector3)"""
        super(_EntityModelInstance, self).translate(arg0)

    @overload
    def translate(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(int,int,int)"""
        super(_EntityModelInstance, self).translate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setTranslation(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.setTranslation(double,double,double)"""
        super(_EntityModelInstance, self).setTranslation(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def rotateX(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.rotateX(double)"""
        super(_EntityModelInstance, self).rotateX(_double.valueOf(arg0))

    @overload
    def scale(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(int,int,int)"""
        super(_EntityModelInstance, self).scale(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def rotateY(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.rotateY(double)"""
        super(_EntityModelInstance, self).rotateY(_double.valueOf(arg0))

    @overload
    def getTranslation(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.EntityModelInstance.getTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_EntityModelInstance, self).getTranslation(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public T dev.ultreon.quantum.client.model.EntityModelInstance.getEntity()"""
        return 'entity.Entity'._wrap(super(EntityModelInstance, self).getEntity())

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(double,double,double)"""
        super(_EntityModelInstance, self).translate(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(float,float,float)"""
        super(_EntityModelInstance, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def translate(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_EntityModelInstance, self).translate(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def translate(self, arg0: 'Vec3f'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        super(_EntityModelInstance, self).translate(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getNode(self, arg0: str) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.EntityModelInstance.getNode(java.lang.String)"""
        return 'model.Node'._wrap(super(_EntityModelInstance, self).getNode(arg0))

    @overload
    def render(self, arg0: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.render(dev.ultreon.quantum.client.model.WorldRenderContext<? super T>)"""
        super(_EntityModelInstance, self).render(arg0)

    @overload
    def getTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.EntityModelInstance.getTransform()"""
        return 'math.Matrix4'._wrap(super(EntityModelInstance, self).getTransform())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.EntityDrawBuffer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
import dev.ultreon.quantum.client.model.EntityDrawBuffer as _EntityDrawBuffer
_EntityDrawBuffer = _EntityDrawBuffer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityDrawBuffer():
    """dev.ultreon.quantum.client.model.EntityDrawBuffer"""
 
    @staticmethod
    def _wrap(java_value: _EntityDrawBuffer) -> 'EntityDrawBuffer':
        return EntityDrawBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityDrawBuffer):
        """
        Dynamic initializer for EntityDrawBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityDrawBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityDrawBuffer__wrapper":
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
    def getHolder(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.client.model.EntityDrawBuffer.getHolder()"""
        return 'entity.Entity'._wrap(super(EntityDrawBuffer, self).getHolder())

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

    @overload
    def __init__(self, arg0: 'Entity'):
        """public dev.ultreon.quantum.client.model.EntityDrawBuffer(dev.ultreon.quantum.entity.Entity)"""
        val = _EntityDrawBuffer(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.QVModel
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.ModelInstance as _ModelInstance
_ModelInstance = _ModelInstance
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController_AnimationDesc
_AnimationDesc = _AnimationController_AnimationDesc.AnimationDesc
from builtins import float
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = _import_once("pyquantum.client.render.shader")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as _OpenShaderProvider
_OpenShaderProvider = _OpenShaderProvider
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController
_AnimationController = _AnimationController
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class QVModel():
    """dev.ultreon.quantum.client.model.QVModel"""
 
    @staticmethod
    def _wrap(java_value: _QVModel) -> 'QVModel':
        return QVModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _QVModel):
        """
        Dynamic initializer for QVModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_QVModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_QVModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setAnimation(self, arg0: str, arg1: int) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,int)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).setAnimation(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def queue(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.queue(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).queue(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @overload
    def isAnimationPaused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationPaused()"""
        return bool._wrap(super(QVModel, self).isAnimationPaused())

    @overload
    def setCurrentAnimation(self, arg0: 'AnimationDesc'):
        """public void dev.ultreon.quantum.client.model.QVModel.setCurrentAnimation(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        super(_QVModel, self).setCurrentAnimation(arg0)

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.QVModel.dispose()"""
        super(QVModel, self).dispose()

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
    def isAnimationStopped(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationStopped()"""
        return bool._wrap(super(QVModel, self).isAnimationStopped())

    @overload
    def getNextAnimation(self) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.getNextAnimation()"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(QVModel, self).getNextAnimation())

    @overload
    def getAnimationController(self) -> 'utils.AnimationController':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController dev.ultreon.quantum.client.model.QVModel.getAnimationController()"""
        return 'utils.AnimationController'._wrap(super(QVModel, self).getAnimationController())

    @overload
    def isAnimationPlaying(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationPlaying()"""
        return bool._wrap(super(QVModel, self).isAnimationPlaying())

    @overload
    def getShaderProvider(self) -> 'shader.OpenShaderProvider':
        """public dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.model.QVModel.getShaderProvider()"""
        return 'shader.OpenShaderProvider'._wrap(super(QVModel, self).getShaderProvider())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isAnimationFinished(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationFinished()"""
        return bool._wrap(super(QVModel, self).isAnimationFinished())

    @overload
    def setPreviousAnimation(self, arg0: 'AnimationDesc'):
        """public void dev.ultreon.quantum.client.model.QVModel.setPreviousAnimation(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        super(_QVModel, self).setPreviousAnimation(arg0)

    @overload
    def getCurrentAnimation(self) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.getCurrentAnimation()"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(QVModel, self).getCurrentAnimation())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).setAnimation(arg0, _int.valueOf(arg1), arg2))

    @overload
    def isSameAnimationAllowed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isSameAnimationAllowed()"""
        return bool._wrap(super(QVModel, self).isSameAnimationAllowed())

    @overload
    def setNextAnimation(self, arg0: 'AnimationDesc'):
        """public void dev.ultreon.quantum.client.model.QVModel.setNextAnimation(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        super(_QVModel, self).setNextAnimation(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getInstance(self) -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.model.QVModel.getInstance()"""
        return 'g3d.ModelInstance'._wrap(super(QVModel, self).getInstance())

    @overload
    def animate(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).animate(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _float.valueOf(arg6)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def stopAnimation(self):
        """public void dev.ultreon.quantum.client.model.QVModel.stopAnimation()"""
        super(QVModel, self).stopAnimation()

    @overload
    def __init__(self, arg0: 'ModelInstance'):
        """public dev.ultreon.quantum.client.model.QVModel(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = _QVModel(arg0)
        self.__wrapper = val

    @overload
    def setTransitionTargetTime(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.setTransitionTargetTime(float)"""
        super(_QVModel, self).setTransitionTargetTime(_float.valueOf(arg0))

    @overload
    def getPreviousAnimation(self) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.getPreviousAnimation()"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(QVModel, self).getPreviousAnimation())

    @overload
    def getTransitionCurrentTime(self) -> float:
        """public float dev.ultreon.quantum.client.model.QVModel.getTransitionCurrentTime()"""
        return float._wrap(super(QVModel, self).getTransitionCurrentTime())

    @overload
    def animate(self, arg0: str, arg1: 'AnimationListener', arg2: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).animate(arg0, arg1, _float.valueOf(arg2)))

    @overload
    def animate(self, arg0: str, arg1: int, arg2: 'AnimationListener', arg3: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).animate(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3)))

    @overload
    def setAllowSameAnimation(self, arg0: bool):
        """public void dev.ultreon.quantum.client.model.QVModel.setAllowSameAnimation(boolean)"""
        super(_QVModel, self).setAllowSameAnimation(_boolean.valueOf(arg0))

    @overload
    def queue(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.queue(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).queue(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _float.valueOf(arg6)))

    @overload
    def action(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.action(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).action(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @overload
    def setAnimation(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).setAnimation(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5))

    @overload
    def pauseAnimation(self):
        """public void dev.ultreon.quantum.client.model.QVModel.pauseAnimation()"""
        super(QVModel, self).pauseAnimation()

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).setAnimation(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def getQueuedTransitionTime(self) -> float:
        """public float dev.ultreon.quantum.client.model.QVModel.getQueuedTransitionTime()"""
        return float._wrap(super(QVModel, self).getQueuedTransitionTime())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.update(float)"""
        super(_QVModel, self).update(_float.valueOf(arg0))

    @overload
    def animate(self, arg0: str, arg1: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).animate(arg0, _float.valueOf(arg1)))

    @overload
    def action(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.action(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).action(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _float.valueOf(arg6)))

    @overload
    def setQueuedTransitionTime(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.setQueuedTransitionTime(float)"""
        super(_QVModel, self).setQueuedTransitionTime(_float.valueOf(arg0))

    @overload
    def animate(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).animate(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @overload
    def resumeAnimation(self):
        """public void dev.ultreon.quantum.client.model.QVModel.resumeAnimation()"""
        super(QVModel, self).resumeAnimation()

    @overload
    def setAnimation(self, arg0: str) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).setAnimation(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTransitionTargetTime(self) -> float:
        """public float dev.ultreon.quantum.client.model.QVModel.getTransitionTargetTime()"""
        return float._wrap(super(QVModel, self).getTransitionTargetTime())

    @overload
    def setAnimation(self, arg0: str, arg1: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'._wrap(super(_QVModel, self).setAnimation(arg0, arg1))

    @overload
    def setTransitionCurrentTime(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.setTransitionCurrentTime(float)"""
        super(_QVModel, self).setTransitionCurrentTime(_float.valueOf(arg0))