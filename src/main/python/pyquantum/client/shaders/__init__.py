from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.shaders.SkyboxShader as _SkyboxShader_Inputs
_Inputs = _SkyboxShader_Inputs.Inputs
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inputs():
    """dev.ultreon.quantum.client.shaders.SkyboxShader.Inputs"""
 
    @staticmethod
    def _wrap(java_value: _Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Inputs):
        """
        Dynamic initializer for Inputs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Inputs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Inputs__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.SkyboxShader$Inputs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.shaders.SkyboxShader as _SkyboxShader_Inputs
_Inputs = _SkyboxShader_Inputs.Inputs
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inputs():
    """dev.ultreon.quantum.client.shaders.SkyboxShader.Inputs"""
 
    @staticmethod
    def _wrap(java_value: _Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Inputs):
        """
        Dynamic initializer for Inputs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Inputs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Inputs__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.SkyboxShader$Inputs 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.ModelViewShader$Inputs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.shaders.ModelViewShader as _ModelViewShader_Inputs
_Inputs = _ModelViewShader_Inputs.Inputs
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inputs():
    """dev.ultreon.quantum.client.shaders.ModelViewShader.Inputs"""
 
    @staticmethod
    def _wrap(java_value: _Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Inputs):
        """
        Dynamic initializer for Inputs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Inputs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Inputs__wrapper":
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.shaders.ShaderProviderFactory
import dev.ultreon.quantum.client.shaders.ShaderProviderFactory as _ShaderProviderFactory
_ShaderProviderFactory = _ShaderProviderFactory
from abc import abstractmethod, ABC
 
class ShaderProviderFactory():
    """dev.ultreon.quantum.client.shaders.ShaderProviderFactory"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProviderFactory) -> 'ShaderProviderFactory':
        return ShaderProviderFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProviderFactory):
        """
        Dynamic initializer for ShaderProviderFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProviderFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProviderFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, ):
        """public abstract T dev.ultreon.quantum.client.shaders.ShaderProviderFactory.create()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.ModelViewShader$Setters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.shaders.ModelViewShader as _ModelViewShader_Setters
_Setters = _ModelViewShader_Setters.Setters
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Setters():
    """dev.ultreon.quantum.client.shaders.ModelViewShader.Setters"""
 
    @staticmethod
    def _wrap(java_value: _Setters) -> 'Setters':
        return Setters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Setters):
        """
        Dynamic initializer for Setters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Setters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Setters__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader$Setters()"""
        val = _Setters()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader$Setters()"""
        val = _Setters()
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
 
 
# CLASS: dev.ultreon.quantum.client.shaders.WorldShader$Setters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.shaders.WorldShader as _WorldShader_Setters
_Setters = _WorldShader_Setters.Setters
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Setters():
    """dev.ultreon.quantum.client.shaders.WorldShader.Setters"""
 
    @staticmethod
    def _wrap(java_value: _Setters) -> 'Setters':
        return Setters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Setters):
        """
        Dynamic initializer for Setters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Setters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Setters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.WorldShader$Setters()"""
        val = _Setters()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.WorldShader$Setters()"""
        val = _Setters()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.shaders.ModelViewShader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.shaders.ModelViewShader as _ModelViewShader
_ModelViewShader = _ModelViewShader
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

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelViewShader():
    """dev.ultreon.quantum.client.shaders.ModelViewShader"""
 
    @staticmethod
    def _wrap(java_value: _ModelViewShader) -> 'ModelViewShader':
        return ModelViewShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelViewShader):
        """
        Dynamic initializer for ModelViewShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelViewShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelViewShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_shaders.DefaultShader, self).canRender(arg0))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def setVersion(arg0: str):
        """public static void dev.ultreon.quantum.client.shaders.ModelViewShader.setVersion(java.lang.String)"""
        _ModelViewShader.setVersion(arg0)

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _ModelViewShader(arg0, arg1, arg2)
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
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.end()"""
        super(shaders.DefaultShader, self).end()

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1, arg2))

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
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_shaders.DefaultShader, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_shaders.BaseShader, self).has(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultFragmentShader()"""
        return str._wrap(_DefaultShader.getDefaultFragmentShader())

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

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

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultVertexShader()"""
        return str._wrap(_DefaultShader.getDefaultVertexShader())

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool._wrap(super(_shaders.DefaultShader, self).equals(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool._wrap(super(_shaders.DefaultShader, self).equals(arg0))

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String dev.ultreon.quantum.client.shaders.ModelViewShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str._wrap(_ModelViewShader.createPrefix(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_shaders.DefaultShader, self).compareTo(arg0))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String)"""
        val = _ModelViewShader(arg0, arg1, arg2)
        self.__wrapper = val

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
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _ModelViewShader(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _ModelViewShader(arg0, arg1)
        self.__wrapper = val

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

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_shaders.DefaultShader, self).begin(arg0, arg1)

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

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public dev.ultreon.quantum.client.shaders.ModelViewShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = _ModelViewShader(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1)) 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.SkyboxShader
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
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader
_DefaultShader = _DefaultShader
from builtins import type
import dev.ultreon.quantum.client.shaders.SkyboxShader as _SkyboxShader
_SkyboxShader = _SkyboxShader
import java.lang.String as _String
_String = _String
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

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkyboxShader():
    """dev.ultreon.quantum.client.shaders.SkyboxShader"""
 
    @staticmethod
    def _wrap(java_value: _SkyboxShader) -> 'SkyboxShader':
        return SkyboxShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkyboxShader):
        """
        Dynamic initializer for SkyboxShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkyboxShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkyboxShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_shaders.DefaultShader, self).canRender(arg0))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _SkyboxShader(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.end()"""
        super(shaders.DefaultShader, self).end()

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = _SkyboxShader(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1, arg2))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.init()"""
        super(shaders.DefaultShader, self).init()

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String)"""
        val = _SkyboxShader(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_shaders.DefaultShader, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_shaders.BaseShader, self).has(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultFragmentShader()"""
        return str._wrap(_DefaultShader.getDefaultFragmentShader())

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

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

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultVertexShader()"""
        return str._wrap(_DefaultShader.getDefaultVertexShader())

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

    @staticmethod
    @overload
    def setVersion(arg0: str):
        """public static void dev.ultreon.quantum.client.shaders.SkyboxShader.setVersion(java.lang.String)"""
        _SkyboxShader.setVersion(arg0)

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

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_shaders.DefaultShader, self).begin(arg0, arg1)

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
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _SkyboxShader(arg0, arg1)
        self.__wrapper = val

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str._wrap(super(_shaders.BaseShader, self).getUniformAlias(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _SkyboxShader(arg0, arg1, arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String dev.ultreon.quantum.client.shaders.SkyboxShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str._wrap(_SkyboxShader.createPrefix(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1)) 
 
 
# CLASS: dev.ultreon.quantum.client.shaders.WorldShader$Inputs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.shaders.WorldShader as _WorldShader_Inputs
_Inputs = _WorldShader_Inputs.Inputs
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inputs():
    """dev.ultreon.quantum.client.shaders.WorldShader.Inputs"""
 
    @staticmethod
    def _wrap(java_value: _Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Inputs):
        """
        Dynamic initializer for Inputs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Inputs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Inputs__wrapper":
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
        """public dev.ultreon.quantum.client.shaders.WorldShader$Inputs()"""
        val = _Inputs()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.WorldShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.shaders.SkyboxShader$Setters
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.shaders.SkyboxShader as _SkyboxShader_Setters
_Setters = _SkyboxShader_Setters.Setters
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_Setter
_Setter = _BaseShader_Setter.Setter
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Setters():
    """dev.ultreon.quantum.client.shaders.SkyboxShader.Setters"""
 
    @staticmethod
    def _wrap(java_value: _Setters) -> 'Setters':
        return Setters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Setters):
        """
        Dynamic initializer for Setters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Setters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Setters__wrapper":
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader$Setters()"""
        val = _Setters()
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: 'Function') -> 'shaders.BaseShader$Setter':
        """public static com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter dev.ultreon.quantum.client.shaders.SkyboxShader$Setters.create(java.util.function.Function<dev.ultreon.quantum.client.world.WorldRenderer, com.badlogic.gdx.graphics.Color>)"""
        return shaders.BaseShader$Setter._wrap(_Setters.create(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.shaders.SkyboxShader$Setters()"""
        val = _Setters()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.shaders.WorldShader
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
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader
_DefaultShader = _DefaultShader
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.shaders.WorldShader as _WorldShader
_WorldShader = _WorldShader
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

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldShader():
    """dev.ultreon.quantum.client.shaders.WorldShader"""
 
    @staticmethod
    def _wrap(java_value: _WorldShader) -> 'WorldShader':
        return WorldShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldShader):
        """
        Dynamic initializer for WorldShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_shaders.DefaultShader, self).canRender(arg0))

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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.end()"""
        super(shaders.DefaultShader, self).end()

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1, arg2))

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
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_shaders.DefaultShader, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_shaders.BaseShader, self).has(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultFragmentShader()"""
        return str._wrap(_DefaultShader.getDefaultFragmentShader())

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

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

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String dev.ultreon.quantum.client.shaders.WorldShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str._wrap(_WorldShader.createPrefix(arg0, arg1))

    @staticmethod
    @overload
    def setVersion(arg0: str):
        """public static void dev.ultreon.quantum.client.shaders.WorldShader.setVersion(java.lang.String)"""
        _WorldShader.setVersion(arg0)

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
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.shaders.WorldShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _WorldShader(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void dev.ultreon.quantum.client.shaders.WorldShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_WorldShader, self).render(arg0)

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_shaders.BaseShader, self).init(arg0, arg1)

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultVertexShader()"""
        return str._wrap(_DefaultShader.getDefaultVertexShader())

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool._wrap(super(_shaders.DefaultShader, self).equals(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool._wrap(super(_shaders.DefaultShader, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public dev.ultreon.quantum.client.shaders.WorldShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = _WorldShader(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_shaders.DefaultShader, self).compareTo(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public dev.ultreon.quantum.client.shaders.WorldShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String)"""
        val = _WorldShader(arg0, arg1, arg2)
        self.__wrapper = val

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

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_shaders.DefaultShader, self).begin(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public dev.ultreon.quantum.client.shaders.WorldShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _WorldShader(arg0, arg1, arg2)
        self.__wrapper = val

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
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public dev.ultreon.quantum.client.shaders.WorldShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _WorldShader(arg0, arg1)
        self.__wrapper = val