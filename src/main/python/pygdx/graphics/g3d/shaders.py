from __future__ import annotations
from overload import overload


 
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
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_LocalSetter
_LocalSetter = _BaseShader_LocalSetter.LocalSetter
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader_Setters_ACubemap
_ACubemap = _DefaultShader_Setters_ACubemap.Setters.ACubemap
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ACubemap():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters.ACubemap"""
 
    @staticmethod
    def _wrap(java_value: _ACubemap) -> 'ACubemap':
        return ACubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ACubemap):
        """
        Dynamic initializer for ACubemap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ACubemap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ACubemap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_ACubemap, self).set(arg0, _int.valueOf(arg1), arg2, arg3)

    @overload
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool._wrap(super(_LocalSetter, self).isGlobal(arg0, _int.valueOf(arg1)))

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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap(int,int)"""
        val = _ACubemap(_int.valueOf(arg0), _int.valueOf(arg1))
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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap
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
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_LocalSetter
_LocalSetter = _BaseShader_LocalSetter.LocalSetter
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader_Setters_ACubemap
_ACubemap = _DefaultShader_Setters_ACubemap.Setters.ACubemap
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ACubemap():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters.ACubemap"""
 
    @staticmethod
    def _wrap(java_value: _ACubemap) -> 'ACubemap':
        return ACubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ACubemap):
        """
        Dynamic initializer for ACubemap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ACubemap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ACubemap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_ACubemap, self).set(arg0, _int.valueOf(arg1), arg2, arg3)

    @overload
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool._wrap(super(_LocalSetter, self).isGlobal(arg0, _int.valueOf(arg1)))

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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap(int,int)"""
        val = _ACubemap(_int.valueOf(arg0), _int.valueOf(arg1))
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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform
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
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_Uniform
_Uniform = _BaseShader_Uniform.Uniform
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Uniform():
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Uniform"""
 
    @staticmethod
    def _wrap(java_value: _Uniform) -> 'Uniform':
        return Uniform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Uniform):
        """
        Dynamic initializer for Uniform.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Uniform__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Uniform__wrapper":
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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String)"""
        val = _Uniform(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long,long,long)"""
        val = _Uniform(arg0, _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long,long)"""
        val = _Uniform(arg0, _long.valueOf(arg1), _long.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def validate(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform.validate(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_Uniform, self).validate(arg0, _int.valueOf(arg1), arg2))

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
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long)"""
        val = _Uniform(arg0, _long.valueOf(arg1))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_LocalSetter
_LocalSetter = _BaseShader_LocalSetter.LocalSetter
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_Setter
_Setter = _BaseShader_Setter.Setter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LocalSetter():
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.LocalSetter"""
 
    @staticmethod
    def _wrap(java_value: _LocalSetter) -> 'LocalSetter':
        return LocalSetter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LocalSetter):
        """
        Dynamic initializer for LocalSetter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LocalSetter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LocalSetter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool._wrap(super(_LocalSetter, self).isGlobal(arg0, _int.valueOf(arg1)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter()"""
        val = _LocalSetter()
        self.__wrapper = val

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

    @abstractmethod
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public abstract void com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter()"""
        val = _LocalSetter()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader
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
from abc import abstractmethod, ABC
import java.lang.Float as _float
import java.lang.String as _string
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
 
class BaseShader():
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader"""
 
    @staticmethod
    def _wrap(java_value: _BaseShader) -> 'BaseShader':
        return BaseShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseShader):
        """
        Dynamic initializer for BaseShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader()"""
        val = _BaseShader()
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @abstractmethod
    def canRender(self, arg0: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.Shader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_BaseShader, self).render(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader()"""
        val = _BaseShader()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.end()"""
        super(BaseShader, self).end()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_BaseShader, self).render(arg0)

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_BaseShader, self).has(_int.valueOf(arg0)))

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_BaseShader, self).begin(arg0, arg1)

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def compareTo(self, arg0: 'Shader'):
        """public abstract int com.badlogic.gdx.graphics.g3d.Shader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        pass

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int._wrap(super(_BaseShader, self).getUniformID(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.dispose()"""
        super(BaseShader, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str._wrap(super(_BaseShader, self).getUniformAlias(_int.valueOf(arg0)))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int._wrap(super(_BaseShader, self).loc(_int.valueOf(arg0)))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_BaseShader, self).register(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def init(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.init()"""
        pass

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_BaseShader, self).register(arg0))

    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_BaseShader, self).init(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DepthShader as _DepthShader_Config
_Config = _DepthShader_Config.Config
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Config():
    """com.badlogic.gdx.graphics.g3d.shaders.DepthShader.Config"""
 
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
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config(java.lang.String,java.lang.String)"""
        val = _Config(arg0, arg1)
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config()"""
        val = _Config()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config()"""
        val = _Config()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$Bones
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
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_LocalSetter
_LocalSetter = _BaseShader_LocalSetter.LocalSetter
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader_Setters_Bones
_Bones = _DefaultShader_Setters_Bones.Setters.Bones
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bones():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters.Bones"""
 
    @staticmethod
    def _wrap(java_value: _Bones) -> 'Bones':
        return Bones(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bones):
        """
        Dynamic initializer for Bones.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bones__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bones__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool._wrap(super(_LocalSetter, self).isGlobal(arg0, _int.valueOf(arg1)))

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
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$Bones.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_Bones, self).set(arg0, _int.valueOf(arg1), arg2, arg3)

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$Bones(int)"""
        val = _Bones(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_Validator
_Validator = _BaseShader_Validator.Validator
from abc import abstractmethod, ABC
 
class Validator():
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Validator"""
 
    @staticmethod
    def _wrap(java_value: _Validator) -> 'Validator':
        return Validator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Validator):
        """
        Dynamic initializer for Validator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Validator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Validator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def validate(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator.validate(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader
_DefaultShader = _DefaultShader
import java.lang.Object as _object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
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
 
class DefaultShader():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader"""
 
    @staticmethod
    def _wrap(java_value: _DefaultShader) -> 'DefaultShader':
        return DefaultShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultShader):
        """
        Dynamic initializer for DefaultShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_DefaultShader, self).begin(arg0, arg1)

    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultCullFace()"""
        return int._wrap(super(DefaultShader, self).getDefaultCullFace())

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _DefaultShader(arg0, arg1)
        self.__wrapper = val

    @overload
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultDepthFunc()"""
        return int._wrap(super(DefaultShader, self).getDefaultDepthFunc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

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
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _DefaultShader(arg0)
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.init()"""
        super(DefaultShader, self).init()

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_BaseShader, self).has(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_DefaultShader, self).compareTo(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _DefaultShader(arg0, arg1, arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str._wrap(_DefaultShader.createPrefix(arg0, arg1))

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str._wrap(super(_BaseShader, self).getUniformAlias(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool._wrap(super(_DefaultShader, self).equals(arg0))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.dispose()"""
        super(DefaultShader, self).dispose()

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultFragmentShader()"""
        return str._wrap(_DefaultShader.getDefaultFragmentShader())

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String)"""
        val = _DefaultShader(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.end()"""
        super(DefaultShader, self).end()

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultCullFace(int)"""
        super(_DefaultShader, self).setDefaultCullFace(_int.valueOf(arg0))

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultVertexShader()"""
        return str._wrap(_DefaultShader.getDefaultVertexShader())

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = _DefaultShader(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_DefaultShader, self).render(arg0, arg1)

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_BaseShader, self).init(arg0, arg1)

    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultDepthFunc(int)"""
        super(_DefaultShader, self).setDefaultDepthFunc(_int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_BaseShader, self).render(arg0)

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int._wrap(super(_BaseShader, self).getUniformID(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool._wrap(super(_DefaultShader, self).equals(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int._wrap(super(_BaseShader, self).loc(_int.valueOf(arg0)))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_BaseShader, self).register(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_DefaultShader, self).canRender(arg0))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_BaseShader, self).register(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_Setter
_Setter = _BaseShader_Setter.Setter
from abc import abstractmethod, ABC
 
class Setter():
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Setter"""
 
    @staticmethod
    def _wrap(java_value: _Setter) -> 'Setter':
        return Setter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Setter):
        """
        Dynamic initializer for Setter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Setter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Setter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public abstract void com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        pass

    @abstractmethod
    def isGlobal(self, arg0: 'BaseShader', arg1: int):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Inputs
from builtins import str
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader_Inputs
_Inputs = _DefaultShader_Inputs.Inputs
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inputs():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Inputs"""
 
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Inputs()"""
        val = _Inputs()
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Inputs()"""
        val = _Inputs()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_GlobalSetter
_GlobalSetter = _BaseShader_GlobalSetter.GlobalSetter
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader_Setter
_Setter = _BaseShader_Setter.Setter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GlobalSetter():
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.GlobalSetter"""
 
    @staticmethod
    def _wrap(java_value: _GlobalSetter) -> 'GlobalSetter':
        return GlobalSetter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GlobalSetter):
        """
        Dynamic initializer for GlobalSetter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GlobalSetter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GlobalSetter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter()"""
        val = _GlobalSetter()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter()"""
        val = _GlobalSetter()
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
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool._wrap(super(_GlobalSetter, self).isGlobal(arg0, _int.valueOf(arg1)))

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

    @abstractmethod
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public abstract void com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        pass

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader_Config
_Config = _DefaultShader_Config.Config
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Config():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Config"""
 
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
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config()"""
        val = _Config()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config(java.lang.String,java.lang.String)"""
        val = _Config(arg0, arg1)
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config()"""
        val = _Config()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DepthShader
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.shaders.DepthShader as _DepthShader
_DepthShader = _DepthShader
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
import java.lang.Float as _float
import java.lang.String as _string
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
 
class DepthShader():
    """com.badlogic.gdx.graphics.g3d.shaders.DepthShader"""
 
    @staticmethod
    def _wrap(java_value: _DepthShader) -> 'DepthShader':
        return DepthShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DepthShader):
        """
        Dynamic initializer for DepthShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DepthShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DepthShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_DepthShader, self).render(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _DepthShader(arg0)
        self.__wrapper = val

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DepthShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_DepthShader, self).canRender(arg0))

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
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.init()"""
        super(DefaultShader, self).init()

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_BaseShader, self).has(_int.valueOf(arg0)))

    @override
    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultCullFace()"""
        return int._wrap(super(DefaultShader, self).getDefaultCullFace())

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_DefaultShader, self).compareTo(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str._wrap(_DefaultShader.createPrefix(arg0, arg1))

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str._wrap(super(_BaseShader, self).getUniformAlias(_int.valueOf(arg0)))

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_DepthShader, self).begin(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool._wrap(super(_DefaultShader, self).equals(arg0))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = _DepthShader(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1, arg2))

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

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.dispose()"""
        super(DefaultShader, self).dispose()

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        val = _DepthShader(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.getDefaultFragmentShader()"""
        return str._wrap(_DepthShader.getDefaultFragmentShader())

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_BaseShader, self).init(arg0, arg1)

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_BaseShader, self).render(arg0)

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _DepthShader(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config,java.lang.String)"""
        val = _DepthShader(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int._wrap(super(_BaseShader, self).getUniformID(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool._wrap(super(_DefaultShader, self).equals(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int._wrap(super(_BaseShader, self).loc(_int.valueOf(arg0)))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_BaseShader, self).register(arg0))

    @override
    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultCullFace(int)"""
        super(_DefaultShader, self).setDefaultCullFace(_int.valueOf(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultDepthFunc()"""
        return int._wrap(super(DefaultShader, self).getDefaultDepthFunc())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.end()"""
        super(DepthShader, self).end()

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_BaseShader, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_BaseShader, self).register(arg0))

    @override
    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultDepthFunc(int)"""
        super(_DefaultShader, self).setDefaultDepthFunc(_int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters
from builtins import str
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as _DefaultShader_Setters
_Setters = _DefaultShader_Setters.Setters
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Setters():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters"""
 
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters()"""
        val = _Setters()
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
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters()"""
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