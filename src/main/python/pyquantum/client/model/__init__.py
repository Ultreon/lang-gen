from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.client.model.ModelImporter as __ModelImporter
__ModelImporter = __ModelImporter
from abc import abstractmethod, ABC
 
class ModelImporter(ABC):
    """dev.ultreon.quantum.client.model.ModelImporter"""
 
    @staticmethod
    def __wrap(java_value: __ModelImporter) -> 'ModelImporter':
        return ModelImporter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelImporter):
        """
        Dynamic initializer for ModelImporter.
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
 
    @abstractmethod
    def getModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.ModelImporter.getModel()"""
        pass

    @abstractmethod
    def createModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.ModelImporter.createModel()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.model.ModelImporter
import dev.ultreon.quantum.client.model.ModelImporter as __ModelImporter
__ModelImporter = __ModelImporter
from abc import abstractmethod, ABC
 
class ModelImporter(ABC):
    """dev.ultreon.quantum.client.model.ModelImporter"""
 
    @staticmethod
    def __wrap(java_value: __ModelImporter) -> 'ModelImporter':
        return ModelImporter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelImporter):
        """
        Dynamic initializer for ModelImporter.
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
import dev.ultreon.quantum.client.model.WorldRenderContext as __WorldRenderContext
__WorldRenderContext = __WorldRenderContext
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.render.RenderContext as __RenderContext
__RenderContext = __RenderContext
 
class WorldRenderContext(ABC):
    """dev.ultreon.quantum.client.model.WorldRenderContext"""
 
    @staticmethod
    def __wrap(java_value: __WorldRenderContext) -> 'WorldRenderContext':
        return WorldRenderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldRenderContext):
        """
        Dynamic initializer for WorldRenderContext.
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
 
    @abstractmethod
    def getHolder(self, ):
        """public abstract T dev.ultreon.quantum.client.render.RenderContext.getHolder()"""
        pass

    @abstractmethod
    def getWorld(self, ):
        """public abstract dev.ultreon.quantum.world.World dev.ultreon.quantum.client.model.WorldRenderContext.getWorld()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.model.WorldRenderContextImpl
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

from builtins import object
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.client.model.WorldRenderContextImpl as __WorldRenderContextImpl
__WorldRenderContextImpl = __WorldRenderContextImpl
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldRenderContextImpl():
    """dev.ultreon.quantum.client.model.WorldRenderContextImpl"""
 
    @staticmethod
    def __wrap(java_value: __WorldRenderContextImpl) -> 'WorldRenderContextImpl':
        return WorldRenderContextImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldRenderContextImpl):
        """
        Dynamic initializer for WorldRenderContextImpl.
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
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.client.model.WorldRenderContextImpl.getWorld()"""
        return 'world.World'.__wrap(super(WorldRenderContextImpl, self).getWorld())

    @overload
    def relative(self, arg0: 'Vec3d', arg1: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.model.WorldRenderContextImpl.relative(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__WorldRenderContextImpl, self).relative(arg0, arg1))

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
    def __init__(self, arg0: 'Scene3D', arg1: object, arg2: 'World', arg3: float, arg4: 'Vec3d'):
        """public dev.ultreon.quantum.client.model.WorldRenderContextImpl(dev.ultreon.quantum.client.render.Scene3D,T,dev.ultreon.quantum.world.World,float,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __WorldRenderContextImpl(arg0, arg1, arg2, __float.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getHolder(self) -> object:
        """public T dev.ultreon.quantum.client.model.WorldRenderContextImpl.getHolder()"""
        return object.__wrap(super(WorldRenderContextImpl, self).getHolder())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.BakedModel
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.model.BakedModel as __BakedModel
__BakedModel = __BakedModel
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BakedModel(ABC):
    """dev.ultreon.quantum.client.model.BakedModel"""
 
    @staticmethod
    def __wrap(java_value: __BakedModel) -> 'BakedModel':
        return BakedModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BakedModel):
        """
        Dynamic initializer for BakedModel.
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
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.BakedModel.getModel()"""
        return 'g3d.Model'.__wrap(super(BakedModel, self).getModel())

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
    def __init__(self, arg0: 'Identifier', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.BakedModel(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.Model)"""
        val = __BakedModel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def resourceId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.BakedModel.resourceId()"""
        return 'util.Identifier'.__wrap(super(BakedModel, self).resourceId())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.EntityModelInstance
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.model.EntityModelInstance as __EntityModelInstance
__EntityModelInstance = __EntityModelInstance
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class EntityModelInstance():
    """dev.ultreon.quantum.client.model.EntityModelInstance"""
 
    @staticmethod
    def __wrap(java_value: __EntityModelInstance) -> 'EntityModelInstance':
        return EntityModelInstance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityModelInstance):
        """
        Dynamic initializer for EntityModelInstance.
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
    def scale(self, arg0: 'Vec3f'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        super(__EntityModelInstance, self).scale(arg0)

    @overload
    def scale(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__EntityModelInstance, self).scale(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'QVModel', arg1: 'Entity'):
        """public dev.ultreon.quantum.client.model.EntityModelInstance(dev.ultreon.quantum.client.model.QVModel,T)"""
        val = __EntityModelInstance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTextures(self, arg0: 'Identifier'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.setTextures(dev.ultreon.quantum.util.Identifier)"""
        super(__EntityModelInstance, self).setTextures(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def translate(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(int,int,int)"""
        super(__EntityModelInstance, self).translate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def setTranslation(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.setTranslation(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__EntityModelInstance, self).setTranslation(arg0)

    @overload
    def setTranslation(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.setTranslation(double,double,double)"""
        super(__EntityModelInstance, self).setTranslation(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @overload
    def getModel(self) -> 'QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.EntityModelInstance.getModel()"""
        return 'QVModel'.__wrap(super(EntityModelInstance, self).getModel())

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(com.badlogic.gdx.math.Vector3)"""
        super(__EntityModelInstance, self).translate(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def translate(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__EntityModelInstance, self).translate(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def rotateZ(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.rotateZ(double)"""
        super(__EntityModelInstance, self).rotateZ(__double.valueOf(arg0))

    @overload
    def scale(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(int,int,int)"""
        super(__EntityModelInstance, self).scale(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def rotateX(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.rotateX(double)"""
        super(__EntityModelInstance, self).rotateX(__double.valueOf(arg0))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(float,float,float)"""
        super(__EntityModelInstance, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: 'Vec3f'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        super(__EntityModelInstance, self).translate(arg0)

    @overload
    def getTranslation(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.EntityModelInstance.getTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__EntityModelInstance, self).getTranslation(arg0))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(float,float,float)"""
        super(__EntityModelInstance, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def getNode(self, arg0: str) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.EntityModelInstance.getNode(java.lang.String)"""
        return 'model.Node'.__wrap(super(__EntityModelInstance, self).getNode(arg0))

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public T dev.ultreon.quantum.client.model.EntityModelInstance.getEntity()"""
        return 'entity.Entity'.__wrap(super(EntityModelInstance, self).getEntity())

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.translate(double,double,double)"""
        super(__EntityModelInstance, self).translate(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(com.badlogic.gdx.math.Vector3)"""
        super(__EntityModelInstance, self).scale(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def scale(self, arg0: int):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(int)"""
        super(__EntityModelInstance, self).scale(__int.valueOf(arg0))

    @overload
    def render(self, arg0: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.render(dev.ultreon.quantum.client.model.WorldRenderContext<? super T>)"""
        super(__EntityModelInstance, self).render(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rotateY(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.rotateY(double)"""
        super(__EntityModelInstance, self).rotateY(__double.valueOf(arg0))

    @overload
    def getTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.EntityModelInstance.getTransform()"""
        return 'math.Matrix4'.__wrap(super(EntityModelInstance, self).getTransform())

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.model.EntityModelInstance.scale(double,double,double)"""
        super(__EntityModelInstance, self).scale(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.EntityDrawBuffer
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.model.EntityDrawBuffer as __EntityDrawBuffer
__EntityDrawBuffer = __EntityDrawBuffer
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

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
from builtins import int
 
class EntityDrawBuffer():
    """dev.ultreon.quantum.client.model.EntityDrawBuffer"""
 
    @staticmethod
    def __wrap(java_value: __EntityDrawBuffer) -> 'EntityDrawBuffer':
        return EntityDrawBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityDrawBuffer):
        """
        Dynamic initializer for EntityDrawBuffer.
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
    def __init__(self, arg0: 'Entity'):
        """public dev.ultreon.quantum.client.model.EntityDrawBuffer(dev.ultreon.quantum.entity.Entity)"""
        val = __EntityDrawBuffer(arg0)
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
    def getHolder(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.client.model.EntityDrawBuffer.getHolder()"""
        return 'entity.Entity'.__wrap(super(EntityDrawBuffer, self).getHolder())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.QVModel
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = __import_once__("pyquantum.client.render.shader")

import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as __OpenShaderProvider
__OpenShaderProvider = __OpenShaderProvider
import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController
__AnimationController = __AnimationController
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController_AnimationDesc
__AnimationDesc = __AnimationController_AnimationDesc.AnimationDesc
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class QVModel():
    """dev.ultreon.quantum.client.model.QVModel"""
 
    @staticmethod
    def __wrap(java_value: __QVModel) -> 'QVModel':
        return QVModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QVModel):
        """
        Dynamic initializer for QVModel.
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
    def isAnimationStopped(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationStopped()"""
        return bool.__wrap(super(QVModel, self).isAnimationStopped())

    @overload
    def setPreviousAnimation(self, arg0: 'AnimationDesc'):
        """public void dev.ultreon.quantum.client.model.QVModel.setPreviousAnimation(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        super(__QVModel, self).setPreviousAnimation(arg0)

    @overload
    def getInstance(self) -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.model.QVModel.getInstance()"""
        return 'g3d.ModelInstance'.__wrap(super(QVModel, self).getInstance())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getNextAnimation(self) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.getNextAnimation()"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(QVModel, self).getNextAnimation())

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.QVModel.dispose()"""
        super(QVModel, self).dispose()

    @overload
    def animate(self, arg0: str, arg1: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).animate(arg0, __float.valueOf(arg1)))

    @overload
    def isAnimationPlaying(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationPlaying()"""
        return bool.__wrap(super(QVModel, self).isAnimationPlaying())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def animate(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).animate(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @overload
    def getShaderProvider(self) -> 'shader.OpenShaderProvider':
        """public dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.model.QVModel.getShaderProvider()"""
        return 'shader.OpenShaderProvider'.__wrap(super(QVModel, self).getShaderProvider())

    @overload
    def setAllowSameAnimation(self, arg0: bool):
        """public void dev.ultreon.quantum.client.model.QVModel.setAllowSameAnimation(boolean)"""
        super(__QVModel, self).setAllowSameAnimation(__boolean.valueOf(arg0))

    @overload
    def setAnimation(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).setAnimation(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.update(float)"""
        super(__QVModel, self).update(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def queue(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.queue(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).queue(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @overload
    def setAnimation(self, arg0: str) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).setAnimation(arg0))

    @overload
    def getAnimationController(self) -> 'utils.AnimationController':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController dev.ultreon.quantum.client.model.QVModel.getAnimationController()"""
        return 'utils.AnimationController'.__wrap(super(QVModel, self).getAnimationController())

    @overload
    def setAnimation(self, arg0: str, arg1: int) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,int)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).setAnimation(arg0, __int.valueOf(arg1)))

    @overload
    def action(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.action(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).action(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __float.valueOf(arg6)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).setAnimation(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setNextAnimation(self, arg0: 'AnimationDesc'):
        """public void dev.ultreon.quantum.client.model.QVModel.setNextAnimation(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        super(__QVModel, self).setNextAnimation(arg0)

    @overload
    def action(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.action(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).action(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @overload
    def stopAnimation(self):
        """public void dev.ultreon.quantum.client.model.QVModel.stopAnimation()"""
        super(QVModel, self).stopAnimation()

    @overload
    def getTransitionCurrentTime(self) -> float:
        """public float dev.ultreon.quantum.client.model.QVModel.getTransitionCurrentTime()"""
        return float.__wrap(super(QVModel, self).getTransitionCurrentTime())

    @overload
    def animate(self, arg0: str, arg1: 'AnimationListener', arg2: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).animate(arg0, arg1, __float.valueOf(arg2)))

    @overload
    def setTransitionTargetTime(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.setTransitionTargetTime(float)"""
        super(__QVModel, self).setTransitionTargetTime(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ModelInstance'):
        """public dev.ultreon.quantum.client.model.QVModel(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = __QVModel(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setCurrentAnimation(self, arg0: 'AnimationDesc'):
        """public void dev.ultreon.quantum.client.model.QVModel.setCurrentAnimation(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        super(__QVModel, self).setCurrentAnimation(arg0)

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).setAnimation(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getTransitionTargetTime(self) -> float:
        """public float dev.ultreon.quantum.client.model.QVModel.getTransitionTargetTime()"""
        return float.__wrap(super(QVModel, self).getTransitionTargetTime())

    @overload
    def isAnimationFinished(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationFinished()"""
        return bool.__wrap(super(QVModel, self).isAnimationFinished())

    @overload
    def queue(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.queue(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).queue(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __float.valueOf(arg6)))

    @overload
    def isSameAnimationAllowed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isSameAnimationAllowed()"""
        return bool.__wrap(super(QVModel, self).isSameAnimationAllowed())

    @overload
    def pauseAnimation(self):
        """public void dev.ultreon.quantum.client.model.QVModel.pauseAnimation()"""
        super(QVModel, self).pauseAnimation()

    @overload
    def getQueuedTransitionTime(self) -> float:
        """public float dev.ultreon.quantum.client.model.QVModel.getQueuedTransitionTime()"""
        return float.__wrap(super(QVModel, self).getQueuedTransitionTime())

    @overload
    def animate(self, arg0: str, arg1: int, arg2: 'AnimationListener', arg3: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).animate(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3)))

    @overload
    def isAnimationPaused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.QVModel.isAnimationPaused()"""
        return bool.__wrap(super(QVModel, self).isAnimationPaused())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def animate(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.animate(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).animate(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __float.valueOf(arg6)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def resumeAnimation(self):
        """public void dev.ultreon.quantum.client.model.QVModel.resumeAnimation()"""
        super(QVModel, self).resumeAnimation()

    @overload
    def setQueuedTransitionTime(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.setQueuedTransitionTime(float)"""
        super(__QVModel, self).setQueuedTransitionTime(__float.valueOf(arg0))

    @overload
    def setAnimation(self, arg0: str, arg1: 'AnimationListener') -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.setAnimation(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(__QVModel, self).setAnimation(arg0, arg1))

    @overload
    def getCurrentAnimation(self) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.getCurrentAnimation()"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(QVModel, self).getCurrentAnimation())

    @overload
    def setTransitionCurrentTime(self, arg0: float):
        """public void dev.ultreon.quantum.client.model.QVModel.setTransitionCurrentTime(float)"""
        super(__QVModel, self).setTransitionCurrentTime(__float.valueOf(arg0))

    @overload
    def getPreviousAnimation(self) -> 'utils.AnimationController$AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc dev.ultreon.quantum.client.model.QVModel.getPreviousAnimation()"""
        return 'utils.AnimationController$AnimationDesc'.__wrap(super(QVModel, self).getPreviousAnimation())