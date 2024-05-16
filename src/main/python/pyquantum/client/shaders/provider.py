from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as __BaseShaderProvider
__BaseShaderProvider = __BaseShaderProvider
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider as __SkyboxShaderProvider
__SkyboxShaderProvider = __SkyboxShaderProvider
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = __import_once__("pygdx.graphics.g3d.shaders")

import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class SkyboxShaderProvider(g3d.__DefaultShaderProvider, utils.DefaultShaderProvider, render.__OpenShaderProvider, shader.OpenShaderProvider):
    """dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __SkyboxShaderProvider) -> 'SkyboxShaderProvider':
        return SkyboxShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SkyboxShaderProvider):
        """
        Dynamic initializer for SkyboxShaderProvider.
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

    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__SkyboxShaderProvider, self).createShader(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(java.lang.String,java.lang.String)"""
        val = __SkyboxShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = __SkyboxShaderProvider(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__utils.BaseShaderProvider, self).getShader(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __SkyboxShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = __SkyboxShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = __SkyboxShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as __BaseShaderProvider
__BaseShaderProvider = __BaseShaderProvider
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider as __SkyboxShaderProvider
__SkyboxShaderProvider = __SkyboxShaderProvider
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = __import_once__("pygdx.graphics.g3d.shaders")

import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class SkyboxShaderProvider(g3d.__DefaultShaderProvider, utils.DefaultShaderProvider, render.__OpenShaderProvider, shader.OpenShaderProvider):
    """dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __SkyboxShaderProvider) -> 'SkyboxShaderProvider':
        return SkyboxShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SkyboxShaderProvider):
        """
        Dynamic initializer for SkyboxShaderProvider.
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

    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__SkyboxShaderProvider, self).createShader(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(java.lang.String,java.lang.String)"""
        val = __SkyboxShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = __SkyboxShaderProvider(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__utils.BaseShaderProvider, self).getShader(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __SkyboxShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = __SkyboxShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider()"""
        val = __SkyboxShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.SkyboxShaderProvider 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider as __ModelViewShaderProvider
__ModelViewShaderProvider = __ModelViewShaderProvider
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as __BaseShaderProvider
__BaseShaderProvider = __BaseShaderProvider
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
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = __import_once__("pygdx.graphics.g3d.shaders")

import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class ModelViewShaderProvider(g3d.__DefaultShaderProvider, utils.DefaultShaderProvider, render.__OpenShaderProvider, shader.OpenShaderProvider):
    """dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __ModelViewShaderProvider) -> 'ModelViewShaderProvider':
        return ModelViewShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelViewShaderProvider):
        """
        Dynamic initializer for ModelViewShaderProvider.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = __ModelViewShaderProvider(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider(java.lang.String,java.lang.String)"""
        val = __ModelViewShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider()"""
        val = __ModelViewShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__ModelViewShaderProvider, self).createShader(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __ModelViewShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__utils.BaseShaderProvider, self).getShader(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.ModelViewShaderProvider()"""
        val = __ModelViewShaderProvider()
        self.__dict__ = val.__dict__
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
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as __BaseShaderProvider
__BaseShaderProvider = __BaseShaderProvider
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
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = __import_once__("pygdx.graphics.g3d.shaders")

import dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider as __WorldShaderProvider
__WorldShaderProvider = __WorldShaderProvider
import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class WorldShaderProvider(g3d.__DefaultShaderProvider, utils.DefaultShaderProvider, render.__OpenShaderProvider, shader.OpenShaderProvider):
    """dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __WorldShaderProvider) -> 'WorldShaderProvider':
        return WorldShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldShaderProvider):
        """
        Dynamic initializer for WorldShaderProvider.
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

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider(java.lang.String,java.lang.String)"""
        val = __WorldShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider()"""
        val = __WorldShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider()"""
        val = __WorldShaderProvider()
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

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__utils.BaseShaderProvider, self).getShader(arg0))

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
    def createShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider.createShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__WorldShaderProvider, self).createShader(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(utils.BaseShaderProvider, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __WorldShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.shaders.provider.WorldShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = __WorldShaderProvider(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val