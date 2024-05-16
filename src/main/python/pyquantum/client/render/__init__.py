from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.render.ShaderContext as _ShaderContext
_ShaderContext = _ShaderContext
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = _import_once("pyquantum.client.render.shader")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as _OpenShaderProvider
_OpenShaderProvider = _OpenShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderContext():
    """dev.ultreon.quantum.client.render.ShaderContext"""
 
    @staticmethod
    def _wrap(java_value: _ShaderContext) -> 'ShaderContext':
        return ShaderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderContext):
        """
        Dynamic initializer for ShaderContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = _ShaderContext()
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

    @staticmethod
    @overload
    def set(arg0: 'OpenShaderProvider'):
        """public static void dev.ultreon.quantum.client.render.ShaderContext.set(dev.ultreon.quantum.client.render.shader.OpenShaderProvider)"""
        _ShaderContext.set(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = _ShaderContext()
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'shader.OpenShaderProvider':
        """public static dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.render.ShaderContext.get()"""
        return shader.OpenShaderProvider._wrap(_ShaderContext.get())

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
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.render.ShaderContext as _ShaderContext
_ShaderContext = _ShaderContext
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = _import_once("pyquantum.client.render.shader")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as _OpenShaderProvider
_OpenShaderProvider = _OpenShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderContext():
    """dev.ultreon.quantum.client.render.ShaderContext"""
 
    @staticmethod
    def _wrap(java_value: _ShaderContext) -> 'ShaderContext':
        return ShaderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderContext):
        """
        Dynamic initializer for ShaderContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = _ShaderContext()
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

    @staticmethod
    @overload
    def set(arg0: 'OpenShaderProvider'):
        """public static void dev.ultreon.quantum.client.render.ShaderContext.set(dev.ultreon.quantum.client.render.shader.OpenShaderProvider)"""
        _ShaderContext.set(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = _ShaderContext()
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'shader.OpenShaderProvider':
        """public static dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.render.ShaderContext.get()"""
        return shader.OpenShaderProvider._wrap(_ShaderContext.get())

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
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderContext 
 
 
# CLASS: dev.ultreon.quantum.client.render.Models3D
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
import java.util.function.Consumer as Consumer
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.Models3D as _Models3D
_Models3D = _Models3D
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Models3D():
    """dev.ultreon.quantum.client.render.Models3D"""
 
    @staticmethod
    def _wrap(java_value: _Models3D) -> 'Models3D':
        return Models3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Models3D):
        """
        Dynamic initializer for Models3D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Models3D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Models3D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def loadModel(self, arg0: 'Identifier') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.loadModel(dev.ultreon.quantum.util.Identifier)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).loadModel(arg0))

    @overload
    def generateModel(self, arg0: 'Identifier', arg1: 'Consumer') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.generateModel(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).generateModel(arg0, arg1))

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.render.Models3D.reload()"""
        super(Models3D, self).reload()

    @overload
    def generateModel(self, arg0: 'Identifier', arg1: 'Function') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.generateModel(dev.ultreon.quantum.util.Identifier,java.util.function.Function<com.badlogic.gdx.graphics.g3d.utils.ModelBuilder, com.badlogic.gdx.graphics.g3d.Model>)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).generateModel(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float, arg3: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createBox(float,float,float,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).createBox(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.Models3D.dispose()"""
        super(Models3D, self).dispose()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createSphere(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).createSphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createCone(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).createCone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createCylinder(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).createCylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def createCube(self, arg0: float, arg1: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createCube(float,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).createCube(_float.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Identifier', arg1: 'Model'):
        """public void dev.ultreon.quantum.client.render.Models3D.add(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.Model)"""
        super(_Models3D, self).add(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getModel(self, arg0: 'Identifier') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.getModel(dev.ultreon.quantum.util.Identifier)"""
        return 'g3d.Model'._wrap(super(_Models3D, self).getModel(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def unloadModel(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Models3D.unloadModel(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_Models3D, self).unloadModel(arg0))

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


Models3D.INSTANCE = Models3D._wrap(_INSTANCE.INSTANCE) 
 
 
# CLASS: dev.ultreon.quantum.client.render.EntityTextures
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
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
import it.unimi.dsi.fastutil.longs.Long2ObjectMap as _Long2ObjectMap
_Long2ObjectMap = _Long2ObjectMap
import it.unimi.dsi.fastutil.longs.Long2ObjectMap as Long2ObjectMap
import dev.ultreon.quantum.client.render.EntityTextures as _EntityTextures
_EntityTextures = _EntityTextures
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityTextures():
    """dev.ultreon.quantum.client.render.EntityTextures"""
 
    @staticmethod
    def _wrap(java_value: _EntityTextures) -> 'EntityTextures':
        return EntityTextures(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityTextures):
        """
        Dynamic initializer for EntityTextures.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityTextures__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityTextures__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, arg0: int) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.render.EntityTextures.get(long)"""
        return 'graphics.Texture'._wrap(super(_EntityTextures, self).get(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: 'Identifier') -> 'EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.render.EntityTextures.set(long,dev.ultreon.quantum.util.Identifier)"""
        return 'EntityTextures'._wrap(super(_EntityTextures, self).set(_long.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTextureMap(self) -> 'Long2ObjectMap':
        """public it.unimi.dsi.fastutil.longs.Long2ObjectMap<com.badlogic.gdx.graphics.Texture> dev.ultreon.quantum.client.render.EntityTextures.getTextureMap()"""
        return 'Long2ObjectMap'._wrap(super(EntityTextures, self).getTextureMap())

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
    def createMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.render.EntityTextures.createMaterial()"""
        return 'g3d.Material'._wrap(super(EntityTextures, self).createMaterial())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.EntityTextures()"""
        val = _EntityTextures()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.EntityTextures()"""
        val = _EntityTextures()
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
 
 
# CLASS: dev.ultreon.quantum.client.render.SourceBlending
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import dev.ultreon.quantum.client.render.SourceBlending as _SourceBlending
_SourceBlending = _SourceBlending
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
 
class SourceBlending():
    """dev.ultreon.quantum.client.render.SourceBlending"""
 
    @staticmethod
    def _wrap(java_value: _SourceBlending) -> 'SourceBlending':
        return SourceBlending(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SourceBlending):
        """
        Dynamic initializer for SourceBlending.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SourceBlending__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SourceBlending__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['SourceBlending']:
        """public static dev.ultreon.quantum.client.render.SourceBlending[] dev.ultreon.quantum.client.render.SourceBlending.values()"""
        return List[SourceBlending]._wrap(_SourceBlending.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SourceBlending':
        """public static dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.valueOf(java.lang.String)"""
        return SourceBlending._wrap(_SourceBlending.valueOf(arg0))


SourceBlending.ONE = SourceBlending._wrap(_ONE.ONE)

SourceBlending.CONSTANT_ALPHA = SourceBlending._wrap(_CONSTANT_ALPHA.CONSTANT_ALPHA)

SourceBlending.SRC_COLOR = SourceBlending._wrap(_SRC_COLOR.SRC_COLOR)

SourceBlending.ZERO = SourceBlending._wrap(_ZERO.ZERO)

SourceBlending.ONE_MINUS_CONSTANT_COLOR = SourceBlending._wrap(_ONE_MINUS_CONSTANT_COLOR.ONE_MINUS_CONSTANT_COLOR)

SourceBlending.DST_ALPHA = SourceBlending._wrap(_DST_ALPHA.DST_ALPHA)

SourceBlending.CONSTANT_COLOR = SourceBlending._wrap(_CONSTANT_COLOR.CONSTANT_COLOR)

SourceBlending.ONE_MINUS_SRC_ALPHA = SourceBlending._wrap(_ONE_MINUS_SRC_ALPHA.ONE_MINUS_SRC_ALPHA)

SourceBlending.DST_COLOR = SourceBlending._wrap(_DST_COLOR.DST_COLOR)

SourceBlending.ONE_MINUS_DST_COLOR = SourceBlending._wrap(_ONE_MINUS_DST_COLOR.ONE_MINUS_DST_COLOR)

SourceBlending.ONE_MINUS_DST_ALPHA = SourceBlending._wrap(_ONE_MINUS_DST_ALPHA.ONE_MINUS_DST_ALPHA)

SourceBlending.SRC_ALPHA_SATURATE = SourceBlending._wrap(_SRC_ALPHA_SATURATE.SRC_ALPHA_SATURATE)

SourceBlending.ONE_MINUS_CONSTANT_ALPHA = SourceBlending._wrap(_ONE_MINUS_CONSTANT_ALPHA.ONE_MINUS_CONSTANT_ALPHA)

SourceBlending.SRC_ALPHA = SourceBlending._wrap(_SRC_ALPHA.SRC_ALPHA)

SourceBlending.ONE_MINUS_SRC_COLOR = SourceBlending._wrap(_ONE_MINUS_SRC_COLOR.ONE_MINUS_SRC_COLOR) 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderPrograms
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.ShaderPrograms as _ShaderPrograms
_ShaderPrograms = _ShaderPrograms
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderPrograms():
    """dev.ultreon.quantum.client.render.ShaderPrograms"""
 
    @staticmethod
    def _wrap(java_value: _ShaderPrograms) -> 'ShaderPrograms':
        return ShaderPrograms(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderPrograms):
        """
        Dynamic initializer for ShaderPrograms.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderPrograms__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderPrograms__wrapper":
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createShader(arg0: 'Identifier') -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram dev.ultreon.quantum.client.render.ShaderPrograms.createShader(dev.ultreon.quantum.util.Identifier)"""
        return glutils.ShaderProgram._wrap(_ShaderPrograms.createShader(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.render.ShaderPrograms.init()"""
            _ShaderPrograms.init()

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
        """public dev.ultreon.quantum.client.render.ShaderPrograms()"""
        val = _ShaderPrograms()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.ShaderPrograms()"""
        val = _ShaderPrograms()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.render.RenderLayer
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.Shader as _Shader
_Shader = _Shader
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
import dev.ultreon.quantum.client.render.RenderLayer as _RenderLayer
_RenderLayer = _RenderLayer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderLayer():
    """dev.ultreon.quantum.client.render.RenderLayer"""
 
    @staticmethod
    def _wrap(java_value: _RenderLayer) -> 'RenderLayer':
        return RenderLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderLayer):
        """
        Dynamic initializer for RenderLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.RenderLayer()"""
        val = _RenderLayer()
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

    @overload
    def nopInit(self):
        """public void dev.ultreon.quantum.client.render.RenderLayer.nopInit()"""
        super(RenderLayer, self).nopInit()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.render.RenderLayer.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_RenderLayer, self).getShader(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.RenderLayer()"""
        val = _RenderLayer()
        self.__wrapper = val

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
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


RenderLayer.WATER = RenderLayer._wrap(_WATER.WATER)

RenderLayer.DEFAULT = RenderLayer._wrap(_DEFAULT.DEFAULT) 
 
 
# CLASS: dev.ultreon.quantum.client.render.FlatFoliageRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyquantum.client.render import meshing
except ImportError:
    meshing = _import_once("pyquantum.client.render.meshing")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.quantum.client.render.NormalBlockRenderer as _NormalBlockRenderer
_NormalBlockRenderer = _NormalBlockRenderer
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.FlatFoliageRenderer as _FlatFoliageRenderer
_FlatFoliageRenderer = _FlatFoliageRenderer
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FlatFoliageRenderer():
    """dev.ultreon.quantum.client.render.FlatFoliageRenderer"""
 
    @staticmethod
    def _wrap(java_value: _FlatFoliageRenderer) -> 'FlatFoliageRenderer':
        return FlatFoliageRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlatFoliageRenderer):
        """
        Dynamic initializer for FlatFoliageRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlatFoliageRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlatFoliageRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def renderEast(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderEast(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_FlatFoliageRenderer, self).renderEast(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def renderWest(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderWest(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_FlatFoliageRenderer, self).renderWest(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @staticmethod
    @overload
    def getV2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getV2(arg0))

    @staticmethod
    @overload
    def getU2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getU2(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def renderTop(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderTop(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_FlatFoliageRenderer, self).renderTop(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.FlatFoliageRenderer()"""
        val = _FlatFoliageRenderer()
        self.__wrapper = val

    @override
    @overload
    def renderNorth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderNorth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_FlatFoliageRenderer, self).renderNorth(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def renderSouth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderSouth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_FlatFoliageRenderer, self).renderSouth(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

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

    @staticmethod
    @overload
    def getV(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getV(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getU(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getU(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.FlatFoliageRenderer()"""
        val = _FlatFoliageRenderer()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def renderBottom(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderBottom(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_FlatFoliageRenderer, self).renderBottom(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.RenderContext
import dev.ultreon.quantum.client.render.RenderContext as _RenderContext
_RenderContext = _RenderContext
from abc import abstractmethod, ABC
 
class RenderContext():
    """dev.ultreon.quantum.client.render.RenderContext"""
 
    @staticmethod
    def _wrap(java_value: _RenderContext) -> 'RenderContext':
        return RenderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderContext):
        """
        Dynamic initializer for RenderContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getHolder(self, ):
        """public abstract T dev.ultreon.quantum.client.render.RenderContext.getHolder()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.BlockRenderer
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.render.BlockRenderer as _BlockRenderer
_BlockRenderer = _BlockRenderer
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

try:
    from pyquantum.client.render import meshing
except ImportError:
    meshing = _import_once("pyquantum.client.render.meshing")

from abc import abstractmethod, ABC
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

 
class BlockRenderer():
    """dev.ultreon.quantum.client.render.BlockRenderer"""
 
    @staticmethod
    def _wrap(java_value: _BlockRenderer) -> 'BlockRenderer':
        return BlockRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockRenderer):
        """
        Dynamic initializer for BlockRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def renderBottom(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public abstract void dev.ultreon.quantum.client.render.BlockRenderer.renderBottom(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        pass

    @abstractmethod
    def renderWest(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public abstract void dev.ultreon.quantum.client.render.BlockRenderer.renderWest(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        pass

    @abstractmethod
    def renderSouth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public abstract void dev.ultreon.quantum.client.render.BlockRenderer.renderSouth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        pass

    @abstractmethod
    def renderEast(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public abstract void dev.ultreon.quantum.client.render.BlockRenderer.renderEast(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        pass

    @abstractmethod
    def renderNorth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public abstract void dev.ultreon.quantum.client.render.BlockRenderer.renderNorth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        pass

    @abstractmethod
    def renderTop(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public abstract void dev.ultreon.quantum.client.render.BlockRenderer.renderTop(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.DestinationBlending
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.render.DestinationBlending as _DestinationBlending
_DestinationBlending = _DestinationBlending
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
 
class DestinationBlending():
    """dev.ultreon.quantum.client.render.DestinationBlending"""
 
    @staticmethod
    def _wrap(java_value: _DestinationBlending) -> 'DestinationBlending':
        return DestinationBlending(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DestinationBlending):
        """
        Dynamic initializer for DestinationBlending.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DestinationBlending__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DestinationBlending__wrapper":
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
    def valueOf(arg0: str) -> 'DestinationBlending':
        """public static dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.valueOf(java.lang.String)"""
        return DestinationBlending._wrap(_DestinationBlending.valueOf(arg0))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['DestinationBlending']:
        """public static dev.ultreon.quantum.client.render.DestinationBlending[] dev.ultreon.quantum.client.render.DestinationBlending.values()"""
        return List[DestinationBlending]._wrap(_DestinationBlending.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


DestinationBlending.DST_COLOR = DestinationBlending._wrap(_DST_COLOR.DST_COLOR)

DestinationBlending.ONE_MINUS_DST_ALPHA = DestinationBlending._wrap(_ONE_MINUS_DST_ALPHA.ONE_MINUS_DST_ALPHA)

DestinationBlending.ZERO = DestinationBlending._wrap(_ZERO.ZERO)

DestinationBlending.SRC_COLOR = DestinationBlending._wrap(_SRC_COLOR.SRC_COLOR)

DestinationBlending.SRC_ALPHA_SATURATE = DestinationBlending._wrap(_SRC_ALPHA_SATURATE.SRC_ALPHA_SATURATE)

DestinationBlending.DST_ALPHA = DestinationBlending._wrap(_DST_ALPHA.DST_ALPHA)

DestinationBlending.CONSTANT_COLOR = DestinationBlending._wrap(_CONSTANT_COLOR.CONSTANT_COLOR)

DestinationBlending.ONE_MINUS_CONSTANT_ALPHA = DestinationBlending._wrap(_ONE_MINUS_CONSTANT_ALPHA.ONE_MINUS_CONSTANT_ALPHA)

DestinationBlending.ONE_MINUS_CONSTANT_COLOR = DestinationBlending._wrap(_ONE_MINUS_CONSTANT_COLOR.ONE_MINUS_CONSTANT_COLOR)

DestinationBlending.CONSTANT_ALPHA = DestinationBlending._wrap(_CONSTANT_ALPHA.CONSTANT_ALPHA)

DestinationBlending.ONE_MINUS_DST_COLOR = DestinationBlending._wrap(_ONE_MINUS_DST_COLOR.ONE_MINUS_DST_COLOR)

DestinationBlending.ONE = DestinationBlending._wrap(_ONE.ONE)

DestinationBlending.SRC_ALPHA = DestinationBlending._wrap(_SRC_ALPHA.SRC_ALPHA)

DestinationBlending.ONE_MINUS_SRC_ALPHA = DestinationBlending._wrap(_ONE_MINUS_SRC_ALPHA.ONE_MINUS_SRC_ALPHA)

DestinationBlending.ONE_MINUS_SRC_COLOR = DestinationBlending._wrap(_ONE_MINUS_SRC_COLOR.ONE_MINUS_SRC_COLOR) 
 
 
# CLASS: dev.ultreon.quantum.client.render.ModelObject
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
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = _import_once("pyquantum.client.render.shader")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as _OpenShaderProvider
_OpenShaderProvider = _OpenShaderProvider
import dev.ultreon.quantum.client.render.ModelObject as _ModelObject
_ModelObject = _ModelObject
import dev.ultreon.quantum.client.util.RenderableArray as _RenderableArray
_RenderableArray = _RenderableArray
try:
    from pyquantum.client import util
except ImportError:
    util = _import_once("pyquantum.client.util")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelObject():
    """dev.ultreon.quantum.client.render.ModelObject"""
 
    @staticmethod
    def _wrap(java_value: _ModelObject) -> 'ModelObject':
        return ModelObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelObject):
        """
        Dynamic initializer for ModelObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def model(self) -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.ModelObject.model()"""
        return 'g3d.ModelInstance'._wrap(super(ModelObject, self).model())

    @overload
    def __init__(self, arg0: 'OpenShaderProvider', arg1: 'ModelInstance', arg2: 'RenderableArray'):
        """public dev.ultreon.quantum.client.render.ModelObject(dev.ultreon.quantum.client.render.shader.OpenShaderProvider,com.badlogic.gdx.graphics.g3d.ModelInstance,dev.ultreon.quantum.client.util.RenderableArray)"""
        val = _ModelObject(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.ModelObject.dispose()"""
        super(ModelObject, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def shaderProvider(self) -> 'shader.OpenShaderProvider':
        """public dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.render.ModelObject.shaderProvider()"""
        return 'shader.OpenShaderProvider'._wrap(super(ModelObject, self).shaderProvider())

    @overload
    def renderables(self) -> 'util.RenderableArray':
        """public dev.ultreon.quantum.client.util.RenderableArray dev.ultreon.quantum.client.render.ModelObject.renderables()"""
        return 'util.RenderableArray'._wrap(super(ModelObject, self).renderables())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.render.ModelObject.hashCode()"""
        return int._wrap(super(ModelObject, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.ModelObject.toString()"""
        return str._wrap(super(ModelObject, self).toString())

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
        """public boolean dev.ultreon.quantum.client.render.ModelObject.equals(java.lang.Object)"""
        return bool._wrap(super(_ModelObject, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.render.Scene3D
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

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
try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

import com.badlogic.gdx.graphics.g3d.utils.MeshBuilder as _MeshBuilder
_MeshBuilder = _MeshBuilder
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.Scene3D as _Scene3D
_Scene3D = _Scene3D
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Scene3D():
    """dev.ultreon.quantum.client.render.Scene3D"""
 
    @staticmethod
    def _wrap(java_value: _Scene3D) -> 'Scene3D':
        return Scene3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Scene3D):
        """
        Dynamic initializer for Scene3D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Scene3D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Scene3D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def destroy(self, arg0: 'QVModel') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Scene3D.destroy(dev.ultreon.quantum.client.model.QVModel)"""
        return bool._wrap(super(_Scene3D, self).destroy(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def activate(self, arg0: 'ModelInstance'):
        """public void dev.ultreon.quantum.client.render.Scene3D.activate(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        super(_Scene3D, self).activate(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def deactivate(self, arg0: 'ModelInstance'):
        """public void dev.ultreon.quantum.client.render.Scene3D.deactivate(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        super(_Scene3D, self).deactivate(arg0)

    @overload
    def destroy(self, arg0: 'ModelInstance') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Scene3D.destroy(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        return bool._wrap(super(_Scene3D, self).destroy(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.render.Scene3D.update(float)"""
        super(_Scene3D, self).update(_float.valueOf(arg0))

    @overload
    def add(self, arg0: 'ModelInstance'):
        """public void dev.ultreon.quantum.client.render.Scene3D.add(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        super(_Scene3D, self).add(arg0)

    @overload
    def create(self, arg0: 'Model', arg1: 'Matrix4') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4)"""
        return 'g3d.ModelInstance'._wrap(super(_Scene3D, self).create(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def add(self, arg0: 'AnimationController'):
        """public void dev.ultreon.quantum.client.render.Scene3D.add(com.badlogic.gdx.graphics.g3d.utils.AnimationController)"""
        super(_Scene3D, self).add(arg0)

    @overload
    def create(self, arg0: 'Model', arg1: float, arg2: float, arg3: float) -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model,float,float,float)"""
        return 'g3d.ModelInstance'._wrap(super(_Scene3D, self).create(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def create(self, arg0: 'Model', arg1: 'Vector3') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Vector3)"""
        return 'g3d.ModelInstance'._wrap(super(_Scene3D, self).create(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'QVModel'):
        """public void dev.ultreon.quantum.client.render.Scene3D.add(dev.ultreon.quantum.client.model.QVModel)"""
        super(_Scene3D, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def meshBuilder(self) -> 'utils.MeshBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshBuilder dev.ultreon.quantum.client.render.Scene3D.meshBuilder()"""
        return 'utils.MeshBuilder'._wrap(super(Scene3D, self).meshBuilder())

    @overload
    def destroy(self, arg0: 'AnimationController') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Scene3D.destroy(com.badlogic.gdx.graphics.g3d.utils.AnimationController)"""
        return bool._wrap(super(_Scene3D, self).destroy(arg0))

    @overload
    def finish(self, arg0: 'Array', arg1: 'Pool'):
        """public void dev.ultreon.quantum.client.render.Scene3D.finish(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_Scene3D, self).finish(arg0, arg1)

    @overload
    def create(self, arg0: 'Model') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model)"""
        return 'g3d.ModelInstance'._wrap(super(_Scene3D, self).create(arg0))

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
    def clear(self):
        """public void dev.ultreon.quantum.client.render.Scene3D.clear()"""
        super(Scene3D, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


Scene3D.WORLD = Scene3D._wrap(_WORLD.WORLD)

Scene3D.BACKGROUND = Scene3D._wrap(_BACKGROUND.BACKGROUND) 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderContext$ShaderMode
from builtins import str
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
import dev.ultreon.quantum.client.render.ShaderContext as _ShaderContext_ShaderMode
_ShaderMode = _ShaderContext_ShaderMode.ShaderMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderMode():
    """dev.ultreon.quantum.client.render.ShaderContext.ShaderMode"""
 
    @staticmethod
    def _wrap(java_value: _ShaderMode) -> 'ShaderMode':
        return ShaderMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderMode):
        """
        Dynamic initializer for ShaderMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderMode__wrapper":
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
    def valueOf(arg0: str) -> 'ShaderMode':
        """public static dev.ultreon.quantum.client.render.ShaderContext$ShaderMode dev.ultreon.quantum.client.render.ShaderContext$ShaderMode.valueOf(java.lang.String)"""
        return ShaderMode._wrap(_ShaderMode.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['ShaderMode']:
        """public static dev.ultreon.quantum.client.render.ShaderContext$ShaderMode[] dev.ultreon.quantum.client.render.ShaderContext$ShaderMode.values()"""
        return List[ShaderMode]._wrap(_ShaderMode.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


ShaderMode.DEPTH = ShaderMode._wrap(_DEPTH.DEPTH)

ShaderMode.DIFFUSE = ShaderMode._wrap(_DIFFUSE.DIFFUSE) 
 
 
# CLASS: dev.ultreon.quantum.client.render.NormalBlockRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyquantum.client.render import meshing
except ImportError:
    meshing = _import_once("pyquantum.client.render.meshing")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.quantum.client.render.NormalBlockRenderer as _NormalBlockRenderer
_NormalBlockRenderer = _NormalBlockRenderer
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NormalBlockRenderer():
    """dev.ultreon.quantum.client.render.NormalBlockRenderer"""
 
    @staticmethod
    def _wrap(java_value: _NormalBlockRenderer) -> 'NormalBlockRenderer':
        return NormalBlockRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NormalBlockRenderer):
        """
        Dynamic initializer for NormalBlockRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NormalBlockRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NormalBlockRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def renderTop(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderTop(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_NormalBlockRenderer, self).renderTop(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @staticmethod
    @overload
    def getV2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getV2(arg0))

    @staticmethod
    @overload
    def getU2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getU2(arg0))

    @override
    @overload
    def renderBottom(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderBottom(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_NormalBlockRenderer, self).renderBottom(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

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
    def renderEast(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderEast(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_NormalBlockRenderer, self).renderEast(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getV(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getV(arg0))

    @override
    @overload
    def renderSouth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderSouth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_NormalBlockRenderer, self).renderSouth(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def renderWest(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderWest(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_NormalBlockRenderer, self).renderWest(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.NormalBlockRenderer()"""
        val = _NormalBlockRenderer()
        self.__wrapper = val

    @staticmethod
    @overload
    def getU(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float._wrap(_NormalBlockRenderer.getU(arg0))

    @override
    @overload
    def renderNorth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderNorth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_NormalBlockRenderer, self).renderNorth(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.NormalBlockRenderer()"""
        val = _NormalBlockRenderer()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.render.Meshes3D
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.Meshes3D as _Meshes3D
_Meshes3D = _Meshes3D
import java.util.function.Consumer as Consumer
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
import java.util.function.Function as Function
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Meshes3D():
    """dev.ultreon.quantum.client.render.Meshes3D"""
 
    @staticmethod
    def _wrap(java_value: _Meshes3D) -> 'Meshes3D':
        return Meshes3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Meshes3D):
        """
        Dynamic initializer for Meshes3D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Meshes3D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Meshes3D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unloadMesh(self, arg0: 'Mesh') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Meshes3D.unloadMesh(com.badlogic.gdx.graphics.Mesh)"""
        return bool._wrap(super(_Meshes3D, self).unloadMesh(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createCone(float,float,float,int)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).createCone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def generateMesh(self, arg0: 'VertexAttributes', arg1: 'Consumer') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.generateMesh(com.badlogic.gdx.graphics.VertexAttributes,java.util.function.Consumer<com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder>)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).generateMesh(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Mesh'):
        """public void dev.ultreon.quantum.client.render.Meshes3D.add(com.badlogic.gdx.graphics.Mesh)"""
        super(_Meshes3D, self).add(arg0)

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.Meshes3D.dispose()"""
        super(Meshes3D, self).dispose()

    @overload
    def createCube(self, arg0: float) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createCube(float)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).createCube(_float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def generateMesh(self, arg0: int, arg1: 'Consumer') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.generateMesh(long,java.util.function.Consumer<com.badlogic.gdx.graphics.g3d.utils.MeshBuilder>)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).generateMesh(_long.valueOf(arg0), arg1))

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
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createCylinder(float,float,float,int)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).createCylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.render.Meshes3D.reload()"""
        super(Meshes3D, self).reload()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def generateMesh(self, arg0: 'Function') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.generateMesh(java.util.function.Function<com.badlogic.gdx.graphics.g3d.utils.MeshBuilder, com.badlogic.gdx.graphics.Mesh>)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).generateMesh(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createBox(float,float,float)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).createBox(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createSphere(float,float,float,int,int)"""
        return 'graphics.Mesh'._wrap(super(_Meshes3D, self).createSphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


Meshes3D.INSTANCE = Meshes3D._wrap(_INSTANCE.INSTANCE)