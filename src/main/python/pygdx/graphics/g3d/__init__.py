from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.Shader as _Shader
_Shader = _Shader
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class Shader():
    """com.badlogic.gdx.graphics.g3d.Shader"""
 
    @staticmethod
    def _wrap(java_value: _Shader) -> 'Shader':
        return Shader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shader):
        """
        Dynamic initializer for Shader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def compareTo(self, arg0: 'Shader'):
        """public abstract int com.badlogic.gdx.graphics.g3d.Shader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.end()"""
        pass

    @abstractmethod
    def init(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.init()"""
        pass

    @abstractmethod
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        pass

    @abstractmethod
    def render(self, arg0: 'Renderable'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def canRender(self, arg0: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.Shader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Shader
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.Shader as _Shader
_Shader = _Shader
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class Shader():
    """com.badlogic.gdx.graphics.g3d.Shader"""
 
    @staticmethod
    def _wrap(java_value: _Shader) -> 'Shader':
        return Shader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shader):
        """
        Dynamic initializer for Shader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def compareTo(self, arg0: 'Shader'):
        """public abstract int com.badlogic.gdx.graphics.g3d.Shader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.end()"""
        pass

    @abstractmethod
    def init(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.init()"""
        pass

    @abstractmethod
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        pass

    @abstractmethod
    def render(self, arg0: 'Renderable'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def canRender(self, arg0: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.Shader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Shader 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Attribute
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Attribute():
    """com.badlogic.gdx.graphics.g3d.Attribute"""
 
    @staticmethod
    def _wrap(java_value: _Attribute) -> 'Attribute':
        return Attribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Attribute):
        """
        Dynamic initializer for Attribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Attribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Attribute__wrapper":
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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attribute.hashCode()"""
        return int._wrap(super(Attribute, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attribute.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_Attribute, self).equals(arg0))

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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(Attribute, self).toString())

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def compareTo(self, arg0: object):
        """public abstract int java.lang.Comparable.compareTo(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelBatch$RenderablePool
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.FlushablePool as _FlushablePool
_FlushablePool = _FlushablePool
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import com.badlogic.gdx.graphics.g3d.ModelBatch as _ModelBatch_RenderablePool
_RenderablePool = _ModelBatch_RenderablePool.RenderablePool
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderablePool():
    """com.badlogic.gdx.graphics.g3d.ModelBatch.RenderablePool"""
 
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
 
    @override
    @overload
    def obtain(self) -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelBatch$RenderablePool.obtain()"""
        return 'Renderable'._wrap(super(RenderablePool, self).obtain())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.FlushablePool.free(T)"""
        super(_utils.FlushablePool, self).free(arg0)

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
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.FlushablePool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_utils.FlushablePool, self).freeAll(arg0)

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.utils.FlushablePool.flush()"""
        super(utils.FlushablePool, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.g3d.ModelCache as _ModelCache_SimpleMeshPool
_SimpleMeshPool = _ModelCache_SimpleMeshPool.SimpleMeshPool
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleMeshPool():
    """com.badlogic.gdx.graphics.g3d.ModelCache.SimpleMeshPool"""
 
    @staticmethod
    def _wrap(java_value: _SimpleMeshPool) -> 'SimpleMeshPool':
        return SimpleMeshPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleMeshPool):
        """
        Dynamic initializer for SimpleMeshPool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleMeshPool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleMeshPool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool.dispose()"""
        super(SimpleMeshPool, self).dispose()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool()"""
        val = _SimpleMeshPool()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool()"""
        val = _SimpleMeshPool()
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool.flush()"""
        super(SimpleMeshPool, self).flush()

    @overload
    def obtain(self, arg0: 'VertexAttributes', arg1: int, arg2: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool.obtain(com.badlogic.gdx.graphics.VertexAttributes,int,int)"""
        return 'graphics.Mesh'._wrap(super(_SimpleMeshPool, self).obtain(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelInstance
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.ModelInstance as _ModelInstance
_ModelInstance = _ModelInstance
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.graphics.g3d.model.Animation as _Animation
_Animation = _Animation
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelInstance():
    """com.badlogic.gdx.graphics.g3d.ModelInstance"""
 
    @staticmethod
    def _wrap(java_value: _ModelInstance) -> 'ModelInstance':
        return ModelInstance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelInstance):
        """
        Dynamic initializer for ModelInstance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelInstance__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelInstance__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Model', arg1: str, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String,boolean,boolean)"""
        val = _ModelInstance(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def copyAnimations(self, arg0: 'Iterable', arg1: bool):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimations(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.model.Animation>,boolean)"""
        super(_ModelInstance, self).copyAnimations(arg0, _boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool, arg4: bool, arg5: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean,boolean,boolean)"""
        val = _ModelInstance(arg0, arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5))
        self.__wrapper = val

    @overload
    def getNode(self, arg0: str) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.ModelInstance.getNode(java.lang.String)"""
        return 'model.Node'._wrap(super(_ModelInstance, self).getNode(arg0))

    @overload
    def calculateTransforms(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.calculateTransforms()"""
        super(ModelInstance, self).calculateTransforms()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Vector3'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Vector3)"""
        val = _ModelInstance(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean,boolean)"""
        val = _ModelInstance(arg0, arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @overload
    def getAnimation(self, arg0: str) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.ModelInstance.getAnimation(java.lang.String)"""
        return 'model.Animation'._wrap(super(_ModelInstance, self).getAnimation(arg0))

    @overload
    def getNode(self, arg0: str, arg1: bool, arg2: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.ModelInstance.getNode(java.lang.String,boolean,boolean)"""
        return 'model.Node'._wrap(super(_ModelInstance, self).getNode(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Model'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model)"""
        val = _ModelInstance(arg0)
        self.__wrapper = val

    @overload
    def getRenderable(self, arg0: 'Renderable', arg1: 'Node', arg2: 'NodePart') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderable(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.model.Node,com.badlogic.gdx.graphics.g3d.model.NodePart)"""
        return 'Renderable'._wrap(super(_ModelInstance, self).getRenderable(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean)"""
        val = _ModelInstance(arg0, arg1, arg2, _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def copyAnimation(self, arg0: 'Animation', arg1: bool):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimation(com.badlogic.gdx.graphics.g3d.model.Animation,boolean)"""
        super(_ModelInstance, self).copyAnimation(arg0, _boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Model', *arg1: str):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String...)"""
        val = _ModelInstance(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: str, arg2: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String,boolean)"""
        val = _ModelInstance(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: 'Array', arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.utils.Array<java.lang.String>,boolean)"""
        val = _ModelInstance(arg0, arg1, arg2, _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ModelInstance', arg1: 'Matrix4'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.ModelInstance,com.badlogic.gdx.math.Matrix4)"""
        val = _ModelInstance(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ModelInstance'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = _ModelInstance(arg0)
        self.__wrapper = val

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.ModelInstance.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'._wrap(super(_ModelInstance, self).calculateBoundingBox(arg0))

    @overload
    def __init__(self, arg0: 'ModelInstance', arg1: 'Matrix4', arg2: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.ModelInstance,com.badlogic.gdx.math.Matrix4,boolean)"""
        val = _ModelInstance(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def copyAnimation(self, arg0: 'Animation'):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimation(com.badlogic.gdx.graphics.g3d.model.Animation)"""
        super(_ModelInstance, self).copyAnimation(arg0)

    @overload
    def getRenderable(self, arg0: 'Renderable', arg1: 'Node') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderable(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.model.Node)"""
        return 'Renderable'._wrap(super(_ModelInstance, self).getRenderable(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool, arg4: bool, arg5: bool, arg6: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean,boolean,boolean,boolean)"""
        val = _ModelInstance(arg0, arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5), _boolean.valueOf(arg6))
        self.__wrapper = val

    @overload
    def getMaterial(self, arg0: str) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.ModelInstance.getMaterial(java.lang.String)"""
        return 'Material'._wrap(super(_ModelInstance, self).getMaterial(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.utils.Array<java.lang.String>)"""
        val = _ModelInstance(arg0, arg1)
        self.__wrapper = val

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.ModelInstance.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'._wrap(super(_ModelInstance, self).extendBoundingBox(arg0))

    @overload
    def getNode(self, arg0: str, arg1: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.ModelInstance.getNode(java.lang.String,boolean)"""
        return 'model.Node'._wrap(super(_ModelInstance, self).getNode(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_ModelInstance, self).getRenderables(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4)"""
        val = _ModelInstance(arg0, arg1)
        self.__wrapper = val

    @overload
    def getRenderable(self, arg0: 'Renderable') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderable(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'Renderable'._wrap(super(_ModelInstance, self).getRenderable(arg0))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.utils.Array<java.lang.String>)"""
        val = _ModelInstance(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def getAnimation(self, arg0: str, arg1: bool) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.ModelInstance.getAnimation(java.lang.String,boolean)"""
        return 'model.Animation'._wrap(super(_ModelInstance, self).getAnimation(arg0, _boolean.valueOf(arg1)))

    @overload
    def getMaterial(self, arg0: str, arg1: bool) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.ModelInstance.getMaterial(java.lang.String,boolean)"""
        return 'Material'._wrap(super(_ModelInstance, self).getMaterial(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Model', arg1: str, arg2: bool, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String,boolean,boolean,boolean)"""
        val = _ModelInstance(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def copy(self) -> 'ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance com.badlogic.gdx.graphics.g3d.ModelInstance.copy()"""
        return 'ModelInstance'._wrap(super(ModelInstance, self).copy())

    @overload
    def copyAnimations(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimations(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.model.Animation>)"""
        super(_ModelInstance, self).copyAnimations(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', *arg2: str):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String...)"""
        val = _ModelInstance(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,float,float,float)"""
        val = _ModelInstance(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Renderable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Renderable():
    """com.badlogic.gdx.graphics.g3d.Renderable"""
 
    @staticmethod
    def _wrap(java_value: _Renderable) -> 'Renderable':
        return Renderable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Renderable):
        """
        Dynamic initializer for Renderable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Renderable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Renderable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Renderable') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.Renderable.set(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'Renderable'._wrap(super(_Renderable, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Renderable()"""
        val = _Renderable()
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Renderable()"""
        val = _Renderable()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.ModelCache as _ModelCache_TightMeshPool
_TightMeshPool = _ModelCache_TightMeshPool.TightMeshPool
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TightMeshPool():
    """com.badlogic.gdx.graphics.g3d.ModelCache.TightMeshPool"""
 
    @staticmethod
    def _wrap(java_value: _TightMeshPool) -> 'TightMeshPool':
        return TightMeshPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TightMeshPool):
        """
        Dynamic initializer for TightMeshPool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TightMeshPool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TightMeshPool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool()"""
        val = _TightMeshPool()
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool.flush()"""
        super(TightMeshPool, self).flush()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool.dispose()"""
        super(TightMeshPool, self).dispose()

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
    def obtain(self, arg0: 'VertexAttributes', arg1: int, arg2: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool.obtain(com.badlogic.gdx.graphics.VertexAttributes,int,int)"""
        return 'graphics.Mesh'._wrap(super(_TightMeshPool, self).obtain(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool()"""
        val = _TightMeshPool()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Model
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.graphics.g3d.model.Animation as _Animation
_Animation = _Animation
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import java.lang.Long as _long
try:
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = _import_once("pygdx.graphics.g3d.model.data")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Model():
    """com.badlogic.gdx.graphics.g3d.Model"""
 
    @staticmethod
    def _wrap(java_value: _Model) -> 'Model':
        return Model(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Model):
        """
        Dynamic initializer for Model.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Model__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Model__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ModelData', arg1: 'TextureProvider'):
        """public com.badlogic.gdx.graphics.g3d.Model(com.badlogic.gdx.graphics.g3d.model.data.ModelData,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        val = _Model(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Model()"""
        val = _Model()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateTransforms(self):
        """public void com.badlogic.gdx.graphics.g3d.Model.calculateTransforms()"""
        super(Model, self).calculateTransforms()

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.Model.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'._wrap(super(_Model, self).calculateBoundingBox(arg0))

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
    def getMaterial(self, arg0: str) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.Model.getMaterial(java.lang.String)"""
        return 'Material'._wrap(super(_Model, self).getMaterial(arg0))

    @overload
    def getMaterial(self, arg0: str, arg1: bool) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.Model.getMaterial(java.lang.String,boolean)"""
        return 'Material'._wrap(super(_Model, self).getMaterial(arg0, _boolean.valueOf(arg1)))

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.Model.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'._wrap(super(_Model, self).extendBoundingBox(arg0))

    @overload
    def getManagedDisposables(self) -> 'Iterable':
        """public java.lang.Iterable<com.badlogic.gdx.utils.Disposable> com.badlogic.gdx.graphics.g3d.Model.getManagedDisposables()"""
        return 'Iterable'._wrap(super(Model, self).getManagedDisposables())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getNode(self, arg0: str) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.Model.getNode(java.lang.String)"""
        return 'model.Node'._wrap(super(_Model, self).getNode(arg0))

    @overload
    def manageDisposable(self, arg0: 'Disposable'):
        """public void com.badlogic.gdx.graphics.g3d.Model.manageDisposable(com.badlogic.gdx.utils.Disposable)"""
        super(_Model, self).manageDisposable(arg0)

    @overload
    def __init__(self, arg0: 'ModelData'):
        """public com.badlogic.gdx.graphics.g3d.Model(com.badlogic.gdx.graphics.g3d.model.data.ModelData)"""
        val = _Model(arg0)
        self.__wrapper = val

    @overload
    def getAnimation(self, arg0: str) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.Model.getAnimation(java.lang.String)"""
        return 'model.Animation'._wrap(super(_Model, self).getAnimation(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getNode(self, arg0: str, arg1: bool, arg2: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.Model.getNode(java.lang.String,boolean,boolean)"""
        return 'model.Node'._wrap(super(_Model, self).getNode(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getNode(self, arg0: str, arg1: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.Model.getNode(java.lang.String,boolean)"""
        return 'model.Node'._wrap(super(_Model, self).getNode(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.Model.dispose()"""
        super(Model, self).dispose()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Model()"""
        val = _Model()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAnimation(self, arg0: str, arg1: bool) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.Model.getAnimation(java.lang.String,boolean)"""
        return 'model.Animation'._wrap(super(_Model, self).getAnimation(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.ModelCache as _ModelCache
_ModelCache = _ModelCache
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelCache():
    """com.badlogic.gdx.graphics.g3d.ModelCache"""
 
    @staticmethod
    def _wrap(java_value: _ModelCache) -> 'ModelCache':
        return ModelCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelCache):
        """
        Dynamic initializer for ModelCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.begin()"""
        super(ModelCache, self).begin()

    @overload
    def add(self, arg0: 'RenderableProvider'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.add(com.badlogic.gdx.graphics.g3d.RenderableProvider)"""
        super(_ModelCache, self).add(arg0)

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.end()"""
        super(ModelCache, self).end()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache()"""
        val = _ModelCache()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache()"""
        val = _ModelCache()
        self.__wrapper = val

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_ModelCache, self).getRenderables(arg0, arg1)

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
    def __init__(self, arg0: 'RenderableSorter', arg1: 'MeshPool'):
        """public com.badlogic.gdx.graphics.g3d.ModelCache(com.badlogic.gdx.graphics.g3d.utils.RenderableSorter,com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool)"""
        val = _ModelCache(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.dispose()"""
        super(ModelCache, self).dispose()

    @overload
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.begin(com.badlogic.gdx.graphics.Camera)"""
        super(_ModelCache, self).begin(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: 'Iterable'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelCache.add(java.lang.Iterable<T>)"""
        super(_ModelCache, self).add(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.add(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_ModelCache, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelBatch
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.ModelBatch as _ModelBatch
_ModelBatch = _ModelBatch
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.utils.ShaderProvider as _ShaderProvider
_ShaderProvider = _ShaderProvider
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.RenderContext as _RenderContext
_RenderContext = _RenderContext
import com.badlogic.gdx.graphics.g3d.utils.RenderableSorter as _RenderableSorter
_RenderableSorter = _RenderableSorter
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelBatch():
    """com.badlogic.gdx.graphics.g3d.ModelBatch"""
 
    @staticmethod
    def _wrap(java_value: _ModelBatch) -> 'ModelBatch':
        return ModelBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelBatch):
        """
        Dynamic initializer for ModelBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def render(self, arg0: 'RenderableProvider', arg1: 'Environment', arg2: 'Shader'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider,com.badlogic.gdx.graphics.g3d.Environment,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(_ModelBatch, self).render(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'RenderContext'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        val = _ModelBatch(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = _ModelBatch(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'Iterable', arg1: 'Shader'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(_ModelBatch, self).render(arg0, arg1)

    @overload
    def getRenderContext(self) -> 'utils.RenderContext':
        """public com.badlogic.gdx.graphics.g3d.utils.RenderContext com.badlogic.gdx.graphics.g3d.ModelBatch.getRenderContext()"""
        return 'utils.RenderContext'._wrap(super(ModelBatch, self).getRenderContext())

    @overload
    def __init__(self, arg0: 'RenderContext', arg1: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext,com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = _ModelBatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.begin(com.badlogic.gdx.graphics.Camera)"""
        super(_ModelBatch, self).begin(arg0)

    @overload
    def render(self, arg0: 'RenderableProvider'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider)"""
        super(_ModelBatch, self).render(arg0)

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
    def ownsRenderContext(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.ModelBatch.ownsRenderContext()"""
        return bool._wrap(super(ModelBatch, self).ownsRenderContext())

    @overload
    def render(self, arg0: 'RenderableProvider', arg1: 'Environment'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider,com.badlogic.gdx.graphics.g3d.Environment)"""
        super(_ModelBatch, self).render(arg0, arg1)

    @overload
    def getShaderProvider(self) -> 'utils.ShaderProvider':
        """public com.badlogic.gdx.graphics.g3d.utils.ShaderProvider com.badlogic.gdx.graphics.g3d.ModelBatch.getShaderProvider()"""
        return 'utils.ShaderProvider'._wrap(super(ModelBatch, self).getShaderProvider())

    @overload
    def __init__(self, arg0: 'RenderContext', arg1: 'ShaderProvider'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext,com.badlogic.gdx.graphics.g3d.utils.ShaderProvider)"""
        val = _ModelBatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ShaderProvider'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.ShaderProvider)"""
        val = _ModelBatch(arg0)
        self.__wrapper = val

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.ModelBatch.getCamera()"""
        return 'graphics.Camera'._wrap(super(ModelBatch, self).getCamera())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'RenderContext', arg1: 'ShaderProvider', arg2: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext,com.badlogic.gdx.graphics.g3d.utils.ShaderProvider,com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = _ModelBatch(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_ModelBatch, self).setCamera(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.dispose()"""
        super(ModelBatch, self).dispose()

    @overload
    def __init__(self, arg0: 'ShaderProvider', arg1: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.ShaderProvider,com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = _ModelBatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _ModelBatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def getRenderableSorter(self) -> 'utils.RenderableSorter':
        """public com.badlogic.gdx.graphics.g3d.utils.RenderableSorter com.badlogic.gdx.graphics.g3d.ModelBatch.getRenderableSorter()"""
        return 'utils.RenderableSorter'._wrap(super(ModelBatch, self).getRenderableSorter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(java.lang.String,java.lang.String)"""
        val = _ModelBatch(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch()"""
        val = _ModelBatch()
        self.__wrapper = val

    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.flush()"""
        super(ModelBatch, self).flush()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch()"""
        val = _ModelBatch()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def render(self, arg0: 'RenderableProvider', arg1: 'Shader'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(_ModelBatch, self).render(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.end()"""
        super(ModelBatch, self).end()

    @overload
    def render(self, arg0: 'Iterable', arg1: 'Environment', arg2: 'Shader'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>,com.badlogic.gdx.graphics.g3d.Environment,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(_ModelBatch, self).render(arg0, arg1, arg2)

    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_ModelBatch, self).render(arg0)

    @overload
    def render(self, arg0: 'Iterable'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>)"""
        super(_ModelBatch, self).render(arg0)

    @overload
    def render(self, arg0: 'Iterable', arg1: 'Environment'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>,com.badlogic.gdx.graphics.g3d.Environment)"""
        super(_ModelBatch, self).render(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.ModelCache as _ModelCache_MeshPool
_MeshPool = _ModelCache_MeshPool.MeshPool
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class MeshPool():
    """com.badlogic.gdx.graphics.g3d.ModelCache.MeshPool"""
 
    @staticmethod
    def _wrap(java_value: _MeshPool) -> 'MeshPool':
        return MeshPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MeshPool):
        """
        Dynamic initializer for MeshPool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MeshPool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MeshPool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def obtain(self, arg0: 'VertexAttributes', arg1: int, arg2: int):
        """public abstract com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool.obtain(com.badlogic.gdx.graphics.VertexAttributes,int,int)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool.flush()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Environment
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.g3d.Attributes as _Attributes
_Attributes = _Attributes
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import com.badlogic.gdx.graphics.g3d.Environment as _Environment
_Environment = _Environment
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx.graphics.g3d import environment
except ImportError:
    environment = _import_once("pygdx.graphics.g3d.environment")

import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
import java.util.function.Function as Function
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Environment():
    """com.badlogic.gdx.graphics.g3d.Environment"""
 
    @staticmethod
    def _wrap(java_value: _Environment) -> 'Environment':
        return Environment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Environment):
        """
        Dynamic initializer for Environment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Environment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Environment__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def same(self, arg0: 'Attributes') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return bool._wrap(super(_Attributes, self).same(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1, arg2)

    @overload
    def get(self, arg0: int) -> 'Attribute':
        """public final com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attributes.get(long)"""
        return 'Attribute'._wrap(super(_Attributes, self).get(_long.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Attributes') -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.compareTo(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return int._wrap(super(_Attributes, self).compareTo(arg0))

    @overload
    def add(self, arg0: 'BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.BaseLight)"""
        return 'Environment'._wrap(super(_Environment, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Array') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.environment.BaseLight>)"""
        return 'Environment'._wrap(super(_Environment, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.has(long)"""
        return bool._wrap(super(_Attributes, self).has(_long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.Attributes.clear()"""
        super(Attributes, self).clear()

    @overload
    def add(self, *arg0: 'environment.BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.BaseLight...)"""
        return 'Environment'._wrap(super(_Environment, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attributes.equals(java.lang.Object)"""
        return bool._wrap(super(_Attributes, self).equals(arg0))

    @override
    @overload
    def attributesHash(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.attributesHash()"""
        return int._wrap(super(Attributes, self).attributesHash())

    @overload
    def remove(self, *arg0: 'environment.BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.BaseLight...)"""
        return 'Environment'._wrap(super(_Environment, self).remove(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public final java.util.Iterator<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.iterator()"""
        return 'Iterator'._wrap(super(Attributes, self).iterator())

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def remove(self, arg0: 'Array') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.environment.BaseLight>)"""
        return 'Environment'._wrap(super(_Environment, self).remove(arg0))

    @overload
    def get(self, arg0: 'Class', arg1: int) -> 'Attribute':
        """public final <T extends com.badlogic.gdx.graphics.g3d.Attribute> T com.badlogic.gdx.graphics.g3d.Attributes.get(java.lang.Class<T>,long)"""
        return 'Attribute'._wrap(super(_Attributes, self).get(arg0, _long.valueOf(arg1)))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def same(self, arg0: 'Attributes', arg1: bool) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes,boolean)"""
        return bool._wrap(super(_Attributes, self).same(arg0, _boolean.valueOf(arg1)))

    @overload
    def add(self, arg0: 'DirectionalLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'Environment'._wrap(super(_Environment, self).add(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.size()"""
        return int._wrap(super(Attributes, self).size())

    @override
    @overload
    def sort(self):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.sort()"""
        super(Attributes, self).sort()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Environment()"""
        val = _Environment()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: 'PointLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return 'Environment'._wrap(super(_Environment, self).remove(arg0))

    @overload
    def add(self, arg0: 'SpotLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return 'Environment'._wrap(super(_Environment, self).add(arg0))

    @overload
    def get(self, arg0: 'Array', arg1: int) -> 'utils.Array':
        """public final com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.get(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>,long)"""
        return 'utils.Array'._wrap(super(_Attributes, self).get(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def compare(self, arg0: 'Attribute', arg1: 'Attribute') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.Attributes.compare(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_Attributes, self).compare(arg0, arg1))

    @override
    @overload
    def set(self, *arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        super(_Attributes, self).set(arg0)

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Environment()"""
        val = _Environment()
        self.__wrapper = val

    @override
    @overload
    def remove(self, arg0: int):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.remove(long)"""
        super(_Attributes, self).remove(_long.valueOf(arg0))

    @overload
    def remove(self, arg0: 'SpotLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return 'Environment'._wrap(super(_Environment, self).remove(arg0))

    @override
    @overload
    def getMask(self) -> int:
        """public final long com.badlogic.gdx.graphics.g3d.Attributes.getMask()"""
        return int._wrap(super(Attributes, self).getMask())

    @overload
    def add(self, arg0: 'PointLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return 'Environment'._wrap(super(_Environment, self).add(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1)

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def remove(self, arg0: 'BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.BaseLight)"""
        return 'Environment'._wrap(super(_Environment, self).remove(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute', arg3: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1, arg2, arg3)

    @override
    @overload
    def set(self, arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0)

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.hashCode()"""
        return int._wrap(super(Attributes, self).hashCode())

    @overload
    def remove(self, arg0: 'DirectionalLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'Environment'._wrap(super(_Environment, self).remove(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: 'Iterable'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        super(_Attributes, self).set(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Material
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.g3d.Attributes as _Attributes
_Attributes = _Attributes
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.util.function.ToDoubleFunction as ToDoubleFunction
import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
import java.util.function.Function as Function
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Material():
    """com.badlogic.gdx.graphics.g3d.Material"""
 
    @staticmethod
    def _wrap(java_value: _Material) -> 'Material':
        return Material(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Material):
        """
        Dynamic initializer for Material.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Material__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Material__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def same(self, arg0: 'Attributes') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return bool._wrap(super(_Attributes, self).same(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1, arg2)

    @overload
    def get(self, arg0: int) -> 'Attribute':
        """public final com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attributes.get(long)"""
        return 'Attribute'._wrap(super(_Attributes, self).get(_long.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Attributes') -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.compareTo(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return int._wrap(super(_Attributes, self).compareTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.has(long)"""
        return bool._wrap(super(_Attributes, self).has(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String)"""
        val = _Material(arg0)
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.Attributes.clear()"""
        super(Attributes, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Material.hashCode()"""
        return int._wrap(super(Material, self).hashCode())

    @override
    @overload
    def attributesHash(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.attributesHash()"""
        return int._wrap(super(Attributes, self).attributesHash())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public final java.util.Iterator<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.iterator()"""
        return 'Iterator'._wrap(super(Attributes, self).iterator())

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Material()"""
        val = _Material()
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Class', arg1: int) -> 'Attribute':
        """public final <T extends com.badlogic.gdx.graphics.g3d.Attribute> T com.badlogic.gdx.graphics.g3d.Attributes.get(java.lang.Class<T>,long)"""
        return 'Attribute'._wrap(super(_Attributes, self).get(arg0, _long.valueOf(arg1)))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def same(self, arg0: 'Attributes', arg1: bool) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes,boolean)"""
        return bool._wrap(super(_Attributes, self).same(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.size()"""
        return int._wrap(super(Attributes, self).size())

    @override
    @overload
    def sort(self):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.sort()"""
        super(Attributes, self).sort()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'Array', arg1: int) -> 'utils.Array':
        """public final com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.get(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>,long)"""
        return 'utils.Array'._wrap(super(_Attributes, self).get(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Material()"""
        val = _Material()
        self.__wrapper = val

    @overload
    def compare(self, arg0: 'Attribute', arg1: 'Attribute') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.Attributes.compare(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_Attributes, self).compare(arg0, arg1))

    @overload
    def copy(self) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.Material.copy()"""
        return 'Material'._wrap(super(Material, self).copy())

    @override
    @overload
    def set(self, *arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        super(_Attributes, self).set(arg0)

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.Material(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        val = _Material(arg0)
        self.__wrapper = val

    @override
    @overload
    def remove(self, arg0: int):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.remove(long)"""
        super(_Attributes, self).remove(_long.valueOf(arg0))

    @overload
    def __init__(self, *arg0: 'Attribute'):
        """public com.badlogic.gdx.graphics.g3d.Material(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        val = _Material(arg0)
        self.__wrapper = val

    @override
    @overload
    def getMask(self) -> int:
        """public final long com.badlogic.gdx.graphics.g3d.Attributes.getMask()"""
        return int._wrap(super(Attributes, self).getMask())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Material.equals(java.lang.Object)"""
        return bool._wrap(super(_Material, self).equals(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1)

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute', arg3: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1, arg2, arg3)

    @override
    @overload
    def set(self, arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0)

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, *arg1: 'Attribute'):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String,com.badlogic.gdx.graphics.g3d.Attribute...)"""
        val = _Material(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String,com.badlogic.gdx.graphics.g3d.Material)"""
        val = _Material(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        val = _Material(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: 'Iterable'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        super(_Attributes, self).set(arg0)

    @overload
    def __init__(self, arg0: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.Material(com.badlogic.gdx.graphics.g3d.Material)"""
        val = _Material(arg0)
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Attributes
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.g3d.Attributes as _Attributes
_Attributes = _Attributes
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
import java.util.function.Function as Function
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Attributes():
    """com.badlogic.gdx.graphics.g3d.Attributes"""
 
    @staticmethod
    def _wrap(java_value: _Attributes) -> 'Attributes':
        return Attributes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Attributes):
        """
        Dynamic initializer for Attributes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Attributes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Attributes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Attributes()"""
        val = _Attributes()
        self.__wrapper = val

    @overload
    def compare(self, arg0: 'Attribute', arg1: 'Attribute') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.Attributes.compare(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_Attributes, self).compare(arg0, arg1))

    @overload
    def same(self, arg0: 'Attributes') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return bool._wrap(super(_Attributes, self).same(arg0))

    @overload
    def set(self, *arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        super(_Attributes, self).set(arg0)

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def get(self, arg0: int) -> 'Attribute':
        """public final com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attributes.get(long)"""
        return 'Attribute'._wrap(super(_Attributes, self).get(_long.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Attributes') -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.compareTo(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return int._wrap(super(_Attributes, self).compareTo(arg0))

    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def sort(self):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.sort()"""
        super(Attributes, self).sort()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.has(long)"""
        return bool._wrap(super(_Attributes, self).has(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attributes.equals(java.lang.Object)"""
        return bool._wrap(super(_Attributes, self).equals(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.Attributes.clear()"""
        super(Attributes, self).clear()

    @overload
    def remove(self, arg0: int):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.remove(long)"""
        super(_Attributes, self).remove(_long.valueOf(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public final java.util.Iterator<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.iterator()"""
        return 'Iterator'._wrap(super(Attributes, self).iterator())

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def get(self, arg0: 'Class', arg1: int) -> 'Attribute':
        """public final <T extends com.badlogic.gdx.graphics.g3d.Attribute> T com.badlogic.gdx.graphics.g3d.Attributes.get(java.lang.Class<T>,long)"""
        return 'Attribute'._wrap(super(_Attributes, self).get(arg0, _long.valueOf(arg1)))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.hashCode()"""
        return int._wrap(super(Attributes, self).hashCode())

    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1, arg2)

    @overload
    def set(self, arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0)

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Attributes()"""
        val = _Attributes()
        self.__wrapper = val

    @overload
    def getMask(self) -> int:
        """public final long com.badlogic.gdx.graphics.g3d.Attributes.getMask()"""
        return int._wrap(super(Attributes, self).getMask())

    @overload
    def attributesHash(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.attributesHash()"""
        return int._wrap(super(Attributes, self).attributesHash())

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.size()"""
        return int._wrap(super(Attributes, self).size())

    @overload
    def set(self, arg0: 'Iterable'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        super(_Attributes, self).set(arg0)

    @overload
    def same(self, arg0: 'Attributes', arg1: bool) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes,boolean)"""
        return bool._wrap(super(_Attributes, self).same(arg0, _boolean.valueOf(arg1)))

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
    def get(self, arg0: 'Array', arg1: int) -> 'utils.Array':
        """public final com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.get(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>,long)"""
        return 'utils.Array'._wrap(super(_Attributes, self).get(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute', arg3: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(_Attributes, self).set(arg0, arg1, arg2, arg3)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$Sorter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
import com.badlogic.gdx.graphics.g3d.ModelCache as _ModelCache_Sorter
_Sorter = _ModelCache_Sorter.Sorter
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Sorter():
    """com.badlogic.gdx.graphics.g3d.ModelCache.Sorter"""
 
    @staticmethod
    def _wrap(java_value: _Sorter) -> 'Sorter':
        return Sorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Sorter):
        """
        Dynamic initializer for Sorter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Sorter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Sorter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$Sorter()"""
        val = _Sorter()
        self.__wrapper = val

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def sort(self, arg0: 'Camera', arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$Sorter.sort(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_Sorter, self).sort(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: 'Renderable', arg1: 'Renderable') -> int:
        """public int com.badlogic.gdx.graphics.g3d.ModelCache$Sorter.compare(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return int._wrap(super(_Sorter, self).compare(arg0, arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$Sorter()"""
        val = _Sorter()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.RenderableProvider
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.RenderableProvider as _RenderableProvider
_RenderableProvider = _RenderableProvider
 
class RenderableProvider():
    """com.badlogic.gdx.graphics.g3d.RenderableProvider"""
 
    @staticmethod
    def _wrap(java_value: _RenderableProvider) -> 'RenderableProvider':
        return RenderableProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderableProvider):
        """
        Dynamic initializer for RenderableProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderableProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderableProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public abstract void com.badlogic.gdx.graphics.g3d.RenderableProvider.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass