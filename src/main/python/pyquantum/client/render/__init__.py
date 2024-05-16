from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.render.ShaderContext as __ShaderContext
__ShaderContext = __ShaderContext
from builtins import type
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = __import_once__("pyquantum.client.render.shader")

import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as __OpenShaderProvider
__OpenShaderProvider = __OpenShaderProvider
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
 
class ShaderContext():
    """dev.ultreon.quantum.client.render.ShaderContext"""
 
    @staticmethod
    def __wrap(java_value: __ShaderContext) -> 'ShaderContext':
        return ShaderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderContext):
        """
        Dynamic initializer for ShaderContext.
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
    def set(arg0: 'OpenShaderProvider'):
        """public static void dev.ultreon.quantum.client.render.ShaderContext.set(dev.ultreon.quantum.client.render.shader.OpenShaderProvider)"""
        __ShaderContext.set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def get() -> 'shader.OpenShaderProvider':
        """public static dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.render.ShaderContext.get()"""
        return shader.OpenShaderProvider.__wrap(__ShaderContext.get())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = __ShaderContext()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = __ShaderContext()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.render.ShaderContext as __ShaderContext
__ShaderContext = __ShaderContext
from builtins import type
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = __import_once__("pyquantum.client.render.shader")

import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as __OpenShaderProvider
__OpenShaderProvider = __OpenShaderProvider
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
 
class ShaderContext():
    """dev.ultreon.quantum.client.render.ShaderContext"""
 
    @staticmethod
    def __wrap(java_value: __ShaderContext) -> 'ShaderContext':
        return ShaderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderContext):
        """
        Dynamic initializer for ShaderContext.
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
    def set(arg0: 'OpenShaderProvider'):
        """public static void dev.ultreon.quantum.client.render.ShaderContext.set(dev.ultreon.quantum.client.render.shader.OpenShaderProvider)"""
        __ShaderContext.set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def get() -> 'shader.OpenShaderProvider':
        """public static dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.render.ShaderContext.get()"""
        return shader.OpenShaderProvider.__wrap(__ShaderContext.get())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = __ShaderContext()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.ShaderContext()"""
        val = __ShaderContext()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderContext 
 
 
# CLASS: dev.ultreon.quantum.client.render.Models3D
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
import java.util.function.Consumer as Consumer
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.client.render.Models3D as __Models3D
__Models3D = __Models3D
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Models3D():
    """dev.ultreon.quantum.client.render.Models3D"""
 
    @staticmethod
    def __wrap(java_value: __Models3D) -> 'Models3D':
        return Models3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Models3D):
        """
        Dynamic initializer for Models3D.
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
 
    # public static final dev.ultreon.quantum.client.render.Models3D dev.ultreon.quantum.client.render.Models3D.INSTANCE
    INSTANCE: 'Models3D' = __wrap(__Models3D.INSTANCE)


    @overload
    def generateModel(self, arg0: 'Identifier', arg1: 'Consumer') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.generateModel(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).generateModel(arg0, arg1))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createCylinder(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).createCylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4))

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

    @overload
    def add(self, arg0: 'Identifier', arg1: 'Model'):
        """public void dev.ultreon.quantum.client.render.Models3D.add(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.Model)"""
        super(__Models3D, self).add(arg0, arg1)

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.render.Models3D.reload()"""
        super(Models3D, self).reload()

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
    def generateModel(self, arg0: 'Identifier', arg1: 'Function') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.generateModel(dev.ultreon.quantum.util.Identifier,java.util.function.Function<com.badlogic.gdx.graphics.g3d.utils.ModelBuilder, com.badlogic.gdx.graphics.g3d.Model>)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).generateModel(arg0, arg1))

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
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createCone(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).createCone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def getModel(self, arg0: 'Identifier') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.getModel(dev.ultreon.quantum.util.Identifier)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).getModel(arg0))

    @overload
    def unloadModel(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Models3D.unloadModel(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__Models3D, self).unloadModel(arg0))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createSphere(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).createSphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def loadModel(self, arg0: 'Identifier') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.loadModel(dev.ultreon.quantum.util.Identifier)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).loadModel(arg0))

    @overload
    def createCube(self, arg0: float, arg1: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createCube(float,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).createCube(__float.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float, arg3: 'Material') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.render.Models3D.createBox(float,float,float,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Model'.__wrap(super(__Models3D, self).createBox(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.EntityTextures
from pyquantum_helper import import_once as __import_once__
import it.unimi.dsi.fastutil.longs.Long2ObjectMap as __Long2ObjectMap
__Long2ObjectMap = __Long2ObjectMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.client.render.EntityTextures as __EntityTextures
__EntityTextures = __EntityTextures
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import it.unimi.dsi.fastutil.longs.Long2ObjectMap as Long2ObjectMap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
from builtins import bool
from builtins import int
 
class EntityTextures():
    """dev.ultreon.quantum.client.render.EntityTextures"""
 
    @staticmethod
    def __wrap(java_value: __EntityTextures) -> 'EntityTextures':
        return EntityTextures(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityTextures):
        """
        Dynamic initializer for EntityTextures.
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
    def createMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.render.EntityTextures.createMaterial()"""
        return 'g3d.Material'.__wrap(super(EntityTextures, self).createMaterial())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.EntityTextures()"""
        val = __EntityTextures()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def get(self, arg0: int) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.render.EntityTextures.get(long)"""
        return 'graphics.Texture'.__wrap(super(__EntityTextures, self).get(__long.valueOf(arg0)))

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
    def getTextureMap(self) -> 'Long2ObjectMap':
        """public it.unimi.dsi.fastutil.longs.Long2ObjectMap<com.badlogic.gdx.graphics.Texture> dev.ultreon.quantum.client.render.EntityTextures.getTextureMap()"""
        return 'Long2ObjectMap'.__wrap(super(EntityTextures, self).getTextureMap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.EntityTextures()"""
        val = __EntityTextures()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: 'Identifier') -> 'EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.render.EntityTextures.set(long,dev.ultreon.quantum.util.Identifier)"""
        return 'EntityTextures'.__wrap(super(__EntityTextures, self).set(__long.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.SourceBlending
import dev.ultreon.quantum.client.render.SourceBlending as __SourceBlending
__SourceBlending = __SourceBlending
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class SourceBlending():
    """dev.ultreon.quantum.client.render.SourceBlending"""
 
    @staticmethod
    def __wrap(java_value: __SourceBlending) -> 'SourceBlending':
        return SourceBlending(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SourceBlending):
        """
        Dynamic initializer for SourceBlending.
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
 
    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.DST_ALPHA
    DST_ALPHA: 'SourceBlending' = __wrap(__SourceBlending.DST_ALPHA)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.CONSTANT_COLOR
    CONSTANT_COLOR: 'SourceBlending' = __wrap(__SourceBlending.CONSTANT_COLOR)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ZERO
    ZERO: 'SourceBlending' = __wrap(__SourceBlending.ZERO)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE
    ONE: 'SourceBlending' = __wrap(__SourceBlending.ONE)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE_MINUS_SRC_COLOR
    ONE_MINUS_SRC_COLOR: 'SourceBlending' = __wrap(__SourceBlending.ONE_MINUS_SRC_COLOR)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE_MINUS_DST_COLOR
    ONE_MINUS_DST_COLOR: 'SourceBlending' = __wrap(__SourceBlending.ONE_MINUS_DST_COLOR)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE_MINUS_CONSTANT_ALPHA
    ONE_MINUS_CONSTANT_ALPHA: 'SourceBlending' = __wrap(__SourceBlending.ONE_MINUS_CONSTANT_ALPHA)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE_MINUS_CONSTANT_COLOR
    ONE_MINUS_CONSTANT_COLOR: 'SourceBlending' = __wrap(__SourceBlending.ONE_MINUS_CONSTANT_COLOR)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.SRC_COLOR
    SRC_COLOR: 'SourceBlending' = __wrap(__SourceBlending.SRC_COLOR)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.DST_COLOR
    DST_COLOR: 'SourceBlending' = __wrap(__SourceBlending.DST_COLOR)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.SRC_ALPHA
    SRC_ALPHA: 'SourceBlending' = __wrap(__SourceBlending.SRC_ALPHA)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE_MINUS_DST_ALPHA
    ONE_MINUS_DST_ALPHA: 'SourceBlending' = __wrap(__SourceBlending.ONE_MINUS_DST_ALPHA)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.ONE_MINUS_SRC_ALPHA
    ONE_MINUS_SRC_ALPHA: 'SourceBlending' = __wrap(__SourceBlending.ONE_MINUS_SRC_ALPHA)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.CONSTANT_ALPHA
    CONSTANT_ALPHA: 'SourceBlending' = __wrap(__SourceBlending.CONSTANT_ALPHA)

    # public static final dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.SRC_ALPHA_SATURATE
    SRC_ALPHA_SATURATE: 'SourceBlending' = __wrap(__SourceBlending.SRC_ALPHA_SATURATE)


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

    @staticmethod
    @overload
    def values() -> List['SourceBlending']:
        """public static dev.ultreon.quantum.client.render.SourceBlending[] dev.ultreon.quantum.client.render.SourceBlending.values()"""
        return List[SourceBlending].__wrap(__SourceBlending.values())

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
    def valueOf(arg0: str) -> 'SourceBlending':
        """public static dev.ultreon.quantum.client.render.SourceBlending dev.ultreon.quantum.client.render.SourceBlending.valueOf(java.lang.String)"""
        return SourceBlending.__wrap(__SourceBlending.valueOf(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderPrograms
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.render.ShaderPrograms as __ShaderPrograms
__ShaderPrograms = __ShaderPrograms
from builtins import str
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ShaderPrograms():
    """dev.ultreon.quantum.client.render.ShaderPrograms"""
 
    @staticmethod
    def __wrap(java_value: __ShaderPrograms) -> 'ShaderPrograms':
        return ShaderPrograms(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderPrograms):
        """
        Dynamic initializer for ShaderPrograms.
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

    @staticmethod
    @overload
    def createShader(arg0: 'Identifier') -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram dev.ultreon.quantum.client.render.ShaderPrograms.createShader(dev.ultreon.quantum.util.Identifier)"""
        return glutils.ShaderProgram.__wrap(__ShaderPrograms.createShader(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.ShaderPrograms()"""
        val = __ShaderPrograms()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.render.ShaderPrograms.init()"""
            __ShaderPrograms.init()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.ShaderPrograms()"""
        val = __ShaderPrograms()
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
 
 
# CLASS: dev.ultreon.quantum.client.render.RenderLayer
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.render.RenderLayer as __RenderLayer
__RenderLayer = __RenderLayer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RenderLayer():
    """dev.ultreon.quantum.client.render.RenderLayer"""
 
    @staticmethod
    def __wrap(java_value: __RenderLayer) -> 'RenderLayer':
        return RenderLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderLayer):
        """
        Dynamic initializer for RenderLayer.
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
 
    # public static final dev.ultreon.quantum.client.render.RenderLayer dev.ultreon.quantum.client.render.RenderLayer.DEFAULT
    DEFAULT: 'RenderLayer' = __wrap(__RenderLayer.DEFAULT)

    # public static final dev.ultreon.quantum.client.render.RenderLayer dev.ultreon.quantum.client.render.RenderLayer.WATER
    WATER: 'RenderLayer' = __wrap(__RenderLayer.WATER)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.render.RenderLayer.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__RenderLayer, self).getShader(arg0))

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
        """public dev.ultreon.quantum.client.render.RenderLayer()"""
        val = __RenderLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.RenderLayer()"""
        val = __RenderLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def nopInit(self):
        """public void dev.ultreon.quantum.client.render.RenderLayer.nopInit()"""
        super(RenderLayer, self).nopInit()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.FlatFoliageRenderer
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.render.FlatFoliageRenderer as __FlatFoliageRenderer
__FlatFoliageRenderer = __FlatFoliageRenderer
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyquantum.client.render import meshing
except ImportError:
    meshing = __import_once__("pyquantum.client.render.meshing")

import dev.ultreon.quantum.client.render.NormalBlockRenderer as __NormalBlockRenderer
__NormalBlockRenderer = __NormalBlockRenderer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class FlatFoliageRenderer():
    """dev.ultreon.quantum.client.render.FlatFoliageRenderer"""
 
    @staticmethod
    def __wrap(java_value: __FlatFoliageRenderer) -> 'FlatFoliageRenderer':
        return FlatFoliageRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlatFoliageRenderer):
        """
        Dynamic initializer for FlatFoliageRenderer.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.FlatFoliageRenderer()"""
        val = __FlatFoliageRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getV2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getV2(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getU(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getU(arg0))

    @override
    @overload
    def renderNorth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderNorth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__FlatFoliageRenderer, self).renderNorth(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @staticmethod
    @overload
    def getV(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getV(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def renderWest(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderWest(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__FlatFoliageRenderer, self).renderWest(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getU2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getU2(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.FlatFoliageRenderer()"""
        val = __FlatFoliageRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def renderSouth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderSouth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__FlatFoliageRenderer, self).renderSouth(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def renderTop(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderTop(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__FlatFoliageRenderer, self).renderTop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def renderBottom(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderBottom(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__FlatFoliageRenderer, self).renderBottom(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def renderEast(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.FlatFoliageRenderer.renderEast(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__FlatFoliageRenderer, self).renderEast(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8) 
 
 
# CLASS: dev.ultreon.quantum.client.render.RenderContext
import dev.ultreon.quantum.client.render.RenderContext as __RenderContext
__RenderContext = __RenderContext
from abc import abstractmethod, ABC
 
class RenderContext(ABC):
    """dev.ultreon.quantum.client.render.RenderContext"""
 
    @staticmethod
    def __wrap(java_value: __RenderContext) -> 'RenderContext':
        return RenderContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderContext):
        """
        Dynamic initializer for RenderContext.
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
 
 
# CLASS: dev.ultreon.quantum.client.render.BlockRenderer
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

try:
    from pyquantum.client.render import meshing
except ImportError:
    meshing = __import_once__("pyquantum.client.render.meshing")

import dev.ultreon.quantum.client.render.BlockRenderer as __BlockRenderer
__BlockRenderer = __BlockRenderer
from abc import abstractmethod, ABC
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

 
class BlockRenderer(ABC):
    """dev.ultreon.quantum.client.render.BlockRenderer"""
 
    @staticmethod
    def __wrap(java_value: __BlockRenderer) -> 'BlockRenderer':
        return BlockRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockRenderer):
        """
        Dynamic initializer for BlockRenderer.
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
import java.lang.Object as __object
import dev.ultreon.quantum.client.render.DestinationBlending as __DestinationBlending
__DestinationBlending = __DestinationBlending
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class DestinationBlending():
    """dev.ultreon.quantum.client.render.DestinationBlending"""
 
    @staticmethod
    def __wrap(java_value: __DestinationBlending) -> 'DestinationBlending':
        return DestinationBlending(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DestinationBlending):
        """
        Dynamic initializer for DestinationBlending.
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
 
    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ZERO
    ZERO: 'DestinationBlending' = __wrap(__DestinationBlending.ZERO)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE_MINUS_CONSTANT_COLOR
    ONE_MINUS_CONSTANT_COLOR: 'DestinationBlending' = __wrap(__DestinationBlending.ONE_MINUS_CONSTANT_COLOR)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.CONSTANT_COLOR
    CONSTANT_COLOR: 'DestinationBlending' = __wrap(__DestinationBlending.CONSTANT_COLOR)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.SRC_ALPHA_SATURATE
    SRC_ALPHA_SATURATE: 'DestinationBlending' = __wrap(__DestinationBlending.SRC_ALPHA_SATURATE)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.CONSTANT_ALPHA
    CONSTANT_ALPHA: 'DestinationBlending' = __wrap(__DestinationBlending.CONSTANT_ALPHA)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE_MINUS_CONSTANT_ALPHA
    ONE_MINUS_CONSTANT_ALPHA: 'DestinationBlending' = __wrap(__DestinationBlending.ONE_MINUS_CONSTANT_ALPHA)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE_MINUS_SRC_COLOR
    ONE_MINUS_SRC_COLOR: 'DestinationBlending' = __wrap(__DestinationBlending.ONE_MINUS_SRC_COLOR)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.SRC_COLOR
    SRC_COLOR: 'DestinationBlending' = __wrap(__DestinationBlending.SRC_COLOR)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE_MINUS_SRC_ALPHA
    ONE_MINUS_SRC_ALPHA: 'DestinationBlending' = __wrap(__DestinationBlending.ONE_MINUS_SRC_ALPHA)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.SRC_ALPHA
    SRC_ALPHA: 'DestinationBlending' = __wrap(__DestinationBlending.SRC_ALPHA)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE_MINUS_DST_ALPHA
    ONE_MINUS_DST_ALPHA: 'DestinationBlending' = __wrap(__DestinationBlending.ONE_MINUS_DST_ALPHA)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE_MINUS_DST_COLOR
    ONE_MINUS_DST_COLOR: 'DestinationBlending' = __wrap(__DestinationBlending.ONE_MINUS_DST_COLOR)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.DST_COLOR
    DST_COLOR: 'DestinationBlending' = __wrap(__DestinationBlending.DST_COLOR)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.DST_ALPHA
    DST_ALPHA: 'DestinationBlending' = __wrap(__DestinationBlending.DST_ALPHA)

    # public static final dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.ONE
    ONE: 'DestinationBlending' = __wrap(__DestinationBlending.ONE)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DestinationBlending':
        """public static dev.ultreon.quantum.client.render.DestinationBlending dev.ultreon.quantum.client.render.DestinationBlending.valueOf(java.lang.String)"""
        return DestinationBlending.__wrap(__DestinationBlending.valueOf(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['DestinationBlending']:
        """public static dev.ultreon.quantum.client.render.DestinationBlending[] dev.ultreon.quantum.client.render.DestinationBlending.values()"""
        return List[DestinationBlending].__wrap(__DestinationBlending.values()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.ModelObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
try:
    from pyquantum.client.render import shader
except ImportError:
    shader = __import_once__("pyquantum.client.render.shader")

import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as __OpenShaderProvider
__OpenShaderProvider = __OpenShaderProvider
import dev.ultreon.quantum.client.render.ModelObject as __ModelObject
__ModelObject = __ModelObject
import dev.ultreon.quantum.client.util.RenderableArray as __RenderableArray
__RenderableArray = __RenderableArray
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.client import util
except ImportError:
    util = __import_once__("pyquantum.client.util")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModelObject():
    """dev.ultreon.quantum.client.render.ModelObject"""
 
    @staticmethod
    def __wrap(java_value: __ModelObject) -> 'ModelObject':
        return ModelObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelObject):
        """
        Dynamic initializer for ModelObject.
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
    def shaderProvider(self) -> 'shader.OpenShaderProvider':
        """public dev.ultreon.quantum.client.render.shader.OpenShaderProvider dev.ultreon.quantum.client.render.ModelObject.shaderProvider()"""
        return 'shader.OpenShaderProvider'.__wrap(super(ModelObject, self).shaderProvider())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.ModelObject.equals(java.lang.Object)"""
        return bool.__wrap(super(__ModelObject, self).equals(arg0))

    @overload
    def renderables(self) -> 'util.RenderableArray':
        """public dev.ultreon.quantum.client.util.RenderableArray dev.ultreon.quantum.client.render.ModelObject.renderables()"""
        return 'util.RenderableArray'.__wrap(super(ModelObject, self).renderables())

    @overload
    def __init__(self, arg0: 'OpenShaderProvider', arg1: 'ModelInstance', arg2: 'RenderableArray'):
        """public dev.ultreon.quantum.client.render.ModelObject(dev.ultreon.quantum.client.render.shader.OpenShaderProvider,com.badlogic.gdx.graphics.g3d.ModelInstance,dev.ultreon.quantum.client.util.RenderableArray)"""
        val = __ModelObject(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.ModelObject.dispose()"""
        super(ModelObject, self).dispose()

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.ModelObject.toString()"""
        return str.__wrap(super(ModelObject, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def model(self) -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.ModelObject.model()"""
        return 'g3d.ModelInstance'.__wrap(super(ModelObject, self).model())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.render.ModelObject.hashCode()"""
        return int.__wrap(super(ModelObject, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.render.Scene3D
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.render.Scene3D as __Scene3D
__Scene3D = __Scene3D
import java.lang.Long as __long
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.graphics.g3d.utils.MeshBuilder as __MeshBuilder
__MeshBuilder = __MeshBuilder
from builtins import int
 
class Scene3D():
    """dev.ultreon.quantum.client.render.Scene3D"""
 
    @staticmethod
    def __wrap(java_value: __Scene3D) -> 'Scene3D':
        return Scene3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scene3D):
        """
        Dynamic initializer for Scene3D.
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
 
    # public static final dev.ultreon.quantum.client.render.Scene3D dev.ultreon.quantum.client.render.Scene3D.BACKGROUND
    BACKGROUND: 'Scene3D' = __wrap(__Scene3D.BACKGROUND)

    # public static final dev.ultreon.quantum.client.render.Scene3D dev.ultreon.quantum.client.render.Scene3D.WORLD
    WORLD: 'Scene3D' = __wrap(__Scene3D.WORLD)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def create(self, arg0: 'Model') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model)"""
        return 'g3d.ModelInstance'.__wrap(super(__Scene3D, self).create(arg0))

    @overload
    def destroy(self, arg0: 'AnimationController') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Scene3D.destroy(com.badlogic.gdx.graphics.g3d.utils.AnimationController)"""
        return bool.__wrap(super(__Scene3D, self).destroy(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def add(self, arg0: 'QVModel'):
        """public void dev.ultreon.quantum.client.render.Scene3D.add(dev.ultreon.quantum.client.model.QVModel)"""
        super(__Scene3D, self).add(arg0)

    @overload
    def destroy(self, arg0: 'QVModel') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Scene3D.destroy(dev.ultreon.quantum.client.model.QVModel)"""
        return bool.__wrap(super(__Scene3D, self).destroy(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def destroy(self, arg0: 'ModelInstance') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Scene3D.destroy(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        return bool.__wrap(super(__Scene3D, self).destroy(arg0))

    @overload
    def finish(self, arg0: 'Array', arg1: 'Pool'):
        """public void dev.ultreon.quantum.client.render.Scene3D.finish(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__Scene3D, self).finish(arg0, arg1)

    @overload
    def activate(self, arg0: 'ModelInstance'):
        """public void dev.ultreon.quantum.client.render.Scene3D.activate(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        super(__Scene3D, self).activate(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'AnimationController'):
        """public void dev.ultreon.quantum.client.render.Scene3D.add(com.badlogic.gdx.graphics.g3d.utils.AnimationController)"""
        super(__Scene3D, self).add(arg0)

    @overload
    def add(self, arg0: 'ModelInstance'):
        """public void dev.ultreon.quantum.client.render.Scene3D.add(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        super(__Scene3D, self).add(arg0)

    @overload
    def meshBuilder(self) -> 'utils.MeshBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshBuilder dev.ultreon.quantum.client.render.Scene3D.meshBuilder()"""
        return 'utils.MeshBuilder'.__wrap(super(Scene3D, self).meshBuilder())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def deactivate(self, arg0: 'ModelInstance'):
        """public void dev.ultreon.quantum.client.render.Scene3D.deactivate(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        super(__Scene3D, self).deactivate(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def create(self, arg0: 'Model', arg1: 'Vector3') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Vector3)"""
        return 'g3d.ModelInstance'.__wrap(super(__Scene3D, self).create(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clear(self):
        """public void dev.ultreon.quantum.client.render.Scene3D.clear()"""
        super(Scene3D, self).clear()

    @overload
    def create(self, arg0: 'Model', arg1: 'Matrix4') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4)"""
        return 'g3d.ModelInstance'.__wrap(super(__Scene3D, self).create(arg0, arg1))

    @overload
    def create(self, arg0: 'Model', arg1: float, arg2: float, arg3: float) -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.render.Scene3D.create(com.badlogic.gdx.graphics.g3d.Model,float,float,float)"""
        return 'g3d.ModelInstance'.__wrap(super(__Scene3D, self).create(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.render.Scene3D.update(float)"""
        super(__Scene3D, self).update(__float.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.ShaderContext$ShaderMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
import dev.ultreon.quantum.client.render.ShaderContext as __ShaderContext_ShaderMode
__ShaderMode = __ShaderContext_ShaderMode.ShaderMode
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class ShaderMode():
    """dev.ultreon.quantum.client.render.ShaderContext.ShaderMode"""
 
    @staticmethod
    def __wrap(java_value: __ShaderMode) -> 'ShaderMode':
        return ShaderMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderMode):
        """
        Dynamic initializer for ShaderMode.
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
 
    # public static final dev.ultreon.quantum.client.render.ShaderContext$ShaderMode dev.ultreon.quantum.client.render.ShaderContext$ShaderMode.DEPTH
    DEPTH: 'ShaderMode' = __wrap(__ShaderMode.DEPTH)

    # public static final dev.ultreon.quantum.client.render.ShaderContext$ShaderMode dev.ultreon.quantum.client.render.ShaderContext$ShaderMode.DIFFUSE
    DIFFUSE: 'ShaderMode' = __wrap(__ShaderMode.DIFFUSE)


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

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def values() -> List['ShaderMode']:
        """public static dev.ultreon.quantum.client.render.ShaderContext$ShaderMode[] dev.ultreon.quantum.client.render.ShaderContext$ShaderMode.values()"""
        return List[ShaderMode].__wrap(__ShaderMode.values())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ShaderMode':
        """public static dev.ultreon.quantum.client.render.ShaderContext$ShaderMode dev.ultreon.quantum.client.render.ShaderContext$ShaderMode.valueOf(java.lang.String)"""
        return ShaderMode.__wrap(__ShaderMode.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.NormalBlockRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyquantum.client.render import meshing
except ImportError:
    meshing = __import_once__("pyquantum.client.render.meshing")

import dev.ultreon.quantum.client.render.NormalBlockRenderer as __NormalBlockRenderer
__NormalBlockRenderer = __NormalBlockRenderer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class NormalBlockRenderer():
    """dev.ultreon.quantum.client.render.NormalBlockRenderer"""
 
    @staticmethod
    def __wrap(java_value: __NormalBlockRenderer) -> 'NormalBlockRenderer':
        return NormalBlockRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NormalBlockRenderer):
        """
        Dynamic initializer for NormalBlockRenderer.
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
    def renderNorth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderNorth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__NormalBlockRenderer, self).renderNorth(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @staticmethod
    @overload
    def getV2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getV2(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getU(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getU(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.NormalBlockRenderer()"""
        val = __NormalBlockRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getV(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getV(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getV(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def renderWest(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderWest(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__NormalBlockRenderer, self).renderWest(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def renderTop(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderTop(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__NormalBlockRenderer, self).renderTop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getU2(arg0: 'TextureRegion') -> float:
        """public static float dev.ultreon.quantum.client.render.NormalBlockRenderer.getU2(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return float.__wrap(__NormalBlockRenderer.getU2(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.NormalBlockRenderer()"""
        val = __NormalBlockRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def renderBottom(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderBottom(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__NormalBlockRenderer, self).renderBottom(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

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
    def renderEast(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderEast(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__NormalBlockRenderer, self).renderEast(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @override
    @overload
    def renderSouth(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'LightLevelData', arg7: 'PerCornerLightData', arg8: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.NormalBlockRenderer.renderSouth(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__NormalBlockRenderer, self).renderSouth(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.Meshes3D
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.render.Meshes3D as __Meshes3D
__Meshes3D = __Meshes3D
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Meshes3D():
    """dev.ultreon.quantum.client.render.Meshes3D"""
 
    @staticmethod
    def __wrap(java_value: __Meshes3D) -> 'Meshes3D':
        return Meshes3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Meshes3D):
        """
        Dynamic initializer for Meshes3D.
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
 
    # public static final dev.ultreon.quantum.client.render.Meshes3D dev.ultreon.quantum.client.render.Meshes3D.INSTANCE
    INSTANCE: 'Meshes3D' = __wrap(__Meshes3D.INSTANCE)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def generateMesh(self, arg0: int, arg1: 'Consumer') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.generateMesh(long,java.util.function.Consumer<com.badlogic.gdx.graphics.g3d.utils.MeshBuilder>)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).generateMesh(__long.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createSphere(float,float,float,int,int)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).createSphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def generateMesh(self, arg0: 'VertexAttributes', arg1: 'Consumer') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.generateMesh(com.badlogic.gdx.graphics.VertexAttributes,java.util.function.Consumer<com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder>)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).generateMesh(arg0, arg1))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createCylinder(float,float,float,int)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).createCylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def createCube(self, arg0: float) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createCube(float)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).createCube(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def generateMesh(self, arg0: 'Function') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.generateMesh(java.util.function.Function<com.badlogic.gdx.graphics.g3d.utils.MeshBuilder, com.badlogic.gdx.graphics.Mesh>)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).generateMesh(arg0))

    @overload
    def add(self, arg0: 'Mesh'):
        """public void dev.ultreon.quantum.client.render.Meshes3D.add(com.badlogic.gdx.graphics.Mesh)"""
        super(__Meshes3D, self).add(arg0)

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.Meshes3D.dispose()"""
        super(Meshes3D, self).dispose()

    @overload
    def unloadMesh(self, arg0: 'Mesh') -> bool:
        """public boolean dev.ultreon.quantum.client.render.Meshes3D.unloadMesh(com.badlogic.gdx.graphics.Mesh)"""
        return bool.__wrap(super(__Meshes3D, self).unloadMesh(arg0))

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
    def reload(self):
        """public void dev.ultreon.quantum.client.render.Meshes3D.reload()"""
        super(Meshes3D, self).reload()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createCone(float,float,float,int)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).createCone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.Meshes3D.createBox(float,float,float)"""
        return 'graphics.Mesh'.__wrap(super(__Meshes3D, self).createBox(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))