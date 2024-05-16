from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider as _SkyboxShaderProvider
_SkyboxShaderProvider = _SkyboxShaderProvider
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
import java.lang.String as _string
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkyboxShaderProvider():
    """dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _SkyboxShaderProvider) -> 'SkyboxShaderProvider':
        return SkyboxShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkyboxShaderProvider):
        """
        Dynamic initializer for SkyboxShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkyboxShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkyboxShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_SkyboxShaderProvider, self).createShader(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = _SkyboxShaderProvider()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = _SkyboxShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _SkyboxShaderProvider(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(java.lang.String,java.lang.String)"""
        val = _SkyboxShaderProvider(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _SkyboxShaderProvider(arg0)
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

 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider as _SkyboxShaderProvider
_SkyboxShaderProvider = _SkyboxShaderProvider
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
import java.lang.String as _string
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkyboxShaderProvider():
    """dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _SkyboxShaderProvider) -> 'SkyboxShaderProvider':
        return SkyboxShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkyboxShaderProvider):
        """
        Dynamic initializer for SkyboxShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkyboxShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkyboxShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_SkyboxShaderProvider, self).createShader(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = _SkyboxShaderProvider()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = _SkyboxShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _SkyboxShaderProvider(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(java.lang.String,java.lang.String)"""
        val = _SkyboxShaderProvider(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _SkyboxShaderProvider(arg0)
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

 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider
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
import dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider as _ModelViewShaderProvider
_ModelViewShaderProvider = _ModelViewShaderProvider
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelViewShaderProvider():
    """dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _ModelViewShaderProvider) -> 'ModelViewShaderProvider':
        return ModelViewShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelViewShaderProvider):
        """
        Dynamic initializer for ModelViewShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelViewShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelViewShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider(java.lang.String,java.lang.String)"""
        val = _ModelViewShaderProvider(arg0, arg1)
        self.__wrapper = val

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
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _ModelViewShaderProvider(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider()"""
        val = _ModelViewShaderProvider()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _ModelViewShaderProvider(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_ModelViewShaderProvider, self).createShader(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider()"""
        val = _ModelViewShaderProvider()
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
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider
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
import dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider as _WorldShaderProvider
_WorldShaderProvider = _WorldShaderProvider
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldShaderProvider():
    """dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _WorldShaderProvider) -> 'WorldShaderProvider':
        return WorldShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldShaderProvider):
        """
        Dynamic initializer for WorldShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _WorldShaderProvider(arg0)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider(java.lang.String,java.lang.String)"""
        val = _WorldShaderProvider(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_WorldShaderProvider, self).createShader(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _WorldShaderProvider(arg0, arg1)
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider()"""
        val = _WorldShaderProvider()
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

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider()"""
        val = _WorldShaderProvider()
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