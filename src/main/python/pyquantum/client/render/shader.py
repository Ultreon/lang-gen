from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider as _Pass1ShaderProvider
_Pass1ShaderProvider = _Pass1ShaderProvider
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pass1ShaderProvider():
    """dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _Pass1ShaderProvider) -> 'Pass1ShaderProvider':
        return Pass1ShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pass1ShaderProvider):
        """
        Dynamic initializer for Pass1ShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pass1ShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pass1ShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_Pass1ShaderProvider, self).createShader(arg0))

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_utils.BaseShaderProvider, self).getShader(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider()"""
        val = _Pass1ShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider()"""
        val = _Pass1ShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider
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
import dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider as _Pass1ShaderProvider
_Pass1ShaderProvider = _Pass1ShaderProvider
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pass1ShaderProvider():
    """dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _Pass1ShaderProvider) -> 'Pass1ShaderProvider':
        return Pass1ShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pass1ShaderProvider):
        """
        Dynamic initializer for Pass1ShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pass1ShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pass1ShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_Pass1ShaderProvider, self).createShader(arg0))

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_utils.BaseShaderProvider, self).getShader(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider()"""
        val = _Pass1ShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider()"""
        val = _Pass1ShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.Pass1ShaderProvider 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.Pass1Shader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.render.shader.Pass1Shader as _Pass1Shader_Config
_Config = _Pass1Shader_Config.Config
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Config():
    """dev.ultreon.quantum.client.render.shader.Pass1Shader.Config"""
 
    @staticmethod
    def _wrap(java_value: _Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Config):
        """
        Dynamic initializer for Config.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Config__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Config__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.shader.Pass1Shader$Config()"""
        val = _Config()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.shader.Pass1Shader$Config()"""
        val = _Config()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.MRTShaderProvider
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
import dev.ultreon.quantum.client.render.shader.MRTShaderProvider as _MRTShaderProvider
_MRTShaderProvider = _MRTShaderProvider
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MRTShaderProvider():
    """dev.ultreon.quantum.client.render.shader.MRTShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _MRTShaderProvider) -> 'MRTShaderProvider':
        return MRTShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MRTShaderProvider):
        """
        Dynamic initializer for MRTShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MRTShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MRTShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.render.shader.MRTShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_MRTShaderProvider, self).createShader(arg0))

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_utils.BaseShaderProvider, self).getShader(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.render.shader.MRTShaderProvider()"""
        val = _MRTShaderProvider()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.shader.MRTShaderProvider()"""
        val = _MRTShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.MRTShader
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
import dev.ultreon.quantum.client.render.shader.MRTShader as _MRTShader
_MRTShader = _MRTShader
import java.lang.Integer as _int
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
 
class MRTShader():
    """dev.ultreon.quantum.client.render.shader.MRTShader"""
 
    @staticmethod
    def _wrap(java_value: _MRTShader) -> 'MRTShader':
        return MRTShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MRTShader):
        """
        Dynamic initializer for MRTShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MRTShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MRTShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void dev.ultreon.quantum.client.render.shader.MRTShader.end()"""
        super(MRTShader, self).end()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.shader.MRTShader.dispose()"""
        super(MRTShader, self).dispose()

    @override
    @overload
    def init(self):
        """public void dev.ultreon.quantum.client.render.shader.MRTShader.init()"""
        super(MRTShader, self).init()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.render.shader.MRTShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _MRTShader(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void dev.ultreon.quantum.client.render.shader.MRTShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_MRTShader, self).begin(arg0, arg1)

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
    def render(self, arg0: 'Renderable'):
        """public void dev.ultreon.quantum.client.render.shader.MRTShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_MRTShader, self).render(arg0)

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean dev.ultreon.quantum.client.render.shader.MRTShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_MRTShader, self).canRender(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int dev.ultreon.quantum.client.render.shader.MRTShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_MRTShader, self).compareTo(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.Pass1Shader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.shaders.DepthShader as _DepthShader
_DepthShader = _DepthShader
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader
_DefaultShader = _DefaultShader
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.shader.Pass1Shader as _Pass1Shader
_Pass1Shader = _Pass1Shader
import java.lang.Float as _float
import java.lang.String as _string
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader
_BaseShader = _BaseShader
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

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
 
class Pass1Shader():
    """dev.ultreon.quantum.client.render.shader.Pass1Shader"""
 
    @staticmethod
    def _wrap(java_value: _Pass1Shader) -> 'Pass1Shader':
        return Pass1Shader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pass1Shader):
        """
        Dynamic initializer for Pass1Shader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pass1Shader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pass1Shader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.end()"""
        super(shaders.DepthShader, self).end()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int._wrap(super(_shaders.BaseShader, self).loc(_int.valueOf(arg0)))

    @override
    @overload
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultDepthFunc()"""
        return int._wrap(super(shaders.DefaultShader, self).getDefaultDepthFunc())

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        return str._wrap(_DepthShader.createPrefix(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1, arg2))

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str._wrap(_DefaultShader.createPrefix(arg0, arg1))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.init()"""
        super(shaders.DefaultShader, self).init()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.getDefaultVertexShader()"""
        return str._wrap(_DepthShader.getDefaultVertexShader())

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_shaders.BaseShader, self).has(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public dev.ultreon.quantum.client.render.shader.Pass1Shader(com.badlogic.gdx.graphics.g3d.Renderable,dev.ultreon.quantum.client.render.shader.Pass1Shader$Config)"""
        val = _Pass1Shader(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultCullFace()"""
        return int._wrap(super(shaders.DefaultShader, self).getDefaultCullFace())

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.dispose()"""
        super(shaders.DefaultShader, self).dispose()

    @override
    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultCullFace(int)"""
        super(_shaders.DefaultShader, self).setDefaultCullFace(_int.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_shaders.BaseShader, self).init(arg0, arg1)

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool._wrap(super(_shaders.DefaultShader, self).equals(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool._wrap(super(_shaders.DefaultShader, self).equals(arg0))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_shaders.DefaultShader, self).compareTo(arg0))

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void dev.ultreon.quantum.client.render.shader.Pass1Shader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_Pass1Shader, self).begin(arg0, arg1)

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.getDefaultFragmentShader()"""
        return str._wrap(_DepthShader.getDefaultFragmentShader())

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_shaders.DepthShader, self).render(arg0, arg1)

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_shaders.BaseShader, self).render(arg0)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int._wrap(super(_shaders.BaseShader, self).getUniformID(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultDepthFunc(int)"""
        super(_shaders.DefaultShader, self).setDefaultDepthFunc(_int.valueOf(arg0))

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str._wrap(super(_shaders.BaseShader, self).getUniformAlias(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DepthShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_shaders.DepthShader, self).canRender(arg0))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.Shaders
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.render.shader.Shaders as _Shaders
_Shaders = _Shaders
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Shaders():
    """dev.ultreon.quantum.client.render.shader.Shaders"""
 
    @staticmethod
    def _wrap(java_value: _Shaders) -> 'Shaders':
        return Shaders(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shaders):
        """
        Dynamic initializer for Shaders.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shaders__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shaders__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.render.shader.Shaders.init()"""
            _Shaders.init()

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
    def checkShaderCompilation(arg0: 'ShaderProgram', arg1: str):
        """public static void dev.ultreon.quantum.client.render.shader.Shaders.checkShaderCompilation(com.badlogic.gdx.graphics.glutils.ShaderProgram,java.lang.String)"""
        _Shaders.checkShaderCompilation(arg0, arg1)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.shader.Shaders()"""
        val = _Shaders()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.shader.Shaders()"""
        val = _Shaders()
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
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.OpenShaderProvider
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.render.shader.OpenShaderProvider as _OpenShaderProvider
_OpenShaderProvider = _OpenShaderProvider
from abc import abstractmethod, ABC
 
class OpenShaderProvider():
    """dev.ultreon.quantum.client.render.shader.OpenShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _OpenShaderProvider) -> 'OpenShaderProvider':
        return OpenShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OpenShaderProvider):
        """
        Dynamic initializer for OpenShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OpenShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OpenShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def createShader(self, arg0: 'Renderable'):
        """public abstract com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.render.shader.OpenShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.shader.GameShaderProvider
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
import dev.ultreon.quantum.client.render.shader.GameShaderProvider as _GameShaderProvider
_GameShaderProvider = _GameShaderProvider
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameShaderProvider():
    """dev.ultreon.quantum.client.render.shader.GameShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _GameShaderProvider) -> 'GameShaderProvider':
        return GameShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameShaderProvider):
        """
        Dynamic initializer for GameShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameShaderProvider__wrapper":
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
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_utils.BaseShaderProvider, self).getShader(arg0))

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

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.render.shader.GameShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        val = _GameShaderProvider(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())