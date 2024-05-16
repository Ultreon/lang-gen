from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_Uniform
__Uniform = __BaseShader_Uniform.Uniform
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Uniform(__Validator, Validator):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Uniform"""
 
    @staticmethod
    def __wrap(java_value: __Uniform) -> 'Uniform':
        return Uniform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Uniform):
        """
        Dynamic initializer for Uniform.
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
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long,long,long)"""
        val = __Uniform(arg0, __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def validate(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform.validate(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool.__wrap(super(__Uniform, self).validate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long)"""
        val = __Uniform(arg0, __long.valueOf(arg1))
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
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long,long)"""
        val = __Uniform(arg0, __long.valueOf(arg1), __long.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String)"""
        val = __Uniform(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_Uniform
__Uniform = __BaseShader_Uniform.Uniform
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Uniform(__Validator, Validator):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Uniform"""
 
    @staticmethod
    def __wrap(java_value: __Uniform) -> 'Uniform':
        return Uniform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Uniform):
        """
        Dynamic initializer for Uniform.
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
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long,long,long)"""
        val = __Uniform(arg0, __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def validate(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform.validate(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool.__wrap(super(__Uniform, self).validate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long)"""
        val = __Uniform(arg0, __long.valueOf(arg1))
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
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String,long,long)"""
        val = __Uniform(arg0, __long.valueOf(arg1), __long.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform(java.lang.String)"""
        val = __Uniform(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_Setter
__Setter = __BaseShader_Setter.Setter
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_GlobalSetter
__GlobalSetter = __BaseShader_GlobalSetter.GlobalSetter
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
 
class GlobalSetter(ABC, __Setter, Setter):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.GlobalSetter"""
 
    @staticmethod
    def __wrap(java_value: __GlobalSetter) -> 'GlobalSetter':
        return GlobalSetter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GlobalSetter):
        """
        Dynamic initializer for GlobalSetter.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter()"""
        val = __GlobalSetter()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter()"""
        val = __GlobalSetter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$GlobalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool.__wrap(super(__GlobalSetter, self).isGlobal(arg0, __int.valueOf(arg1)))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader
__BaseShader = __BaseShader
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class BaseShader(ABC, graphics.__Shader, g3d.Shader):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader"""
 
    @staticmethod
    def __wrap(java_value: __BaseShader) -> 'BaseShader':
        return BaseShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseShader):
        """
        Dynamic initializer for BaseShader.
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
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int.__wrap(super(__BaseShader, self).getUniformID(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader()"""
        val = __BaseShader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @abstractmethod
    def canRender(self, arg0: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.Shader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int.__wrap(super(__BaseShader, self).loc(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int.__wrap(super(__BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.end()"""
        super(BaseShader, self).end()

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(__BaseShader, self).begin(arg0, arg1)

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str.__wrap(super(__BaseShader, self).getUniformAlias(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__BaseShader, self).render(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def compareTo(self, arg0: 'Shader'):
        """public abstract int com.badlogic.gdx.graphics.g3d.Shader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        pass

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(__BaseShader, self).render(arg0, arg1)

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.dispose()"""
        super(BaseShader, self).dispose()

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1, arg2))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int.__wrap(super(__BaseShader, self).register(arg0))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool.__wrap(super(__BaseShader, self).has(__int.valueOf(arg0)))

    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__BaseShader, self).init(arg0, arg1)

    @abstractmethod
    def init(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.init()"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader()"""
        val = __BaseShader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$Bones
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader_Setters_Bones
__Bones = __DefaultShader_Setters_Bones.Setters.Bones
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_LocalSetter
__LocalSetter = __BaseShader_LocalSetter.LocalSetter
from builtins import bool
from builtins import int
 
class Bones(__LocalSetter, LocalSetter):
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters.Bones"""
 
    @staticmethod
    def __wrap(java_value: __Bones) -> 'Bones':
        return Bones(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bones):
        """
        Dynamic initializer for Bones.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$Bones.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(__Bones, self).set(arg0, __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$Bones(int)"""
        val = __Bones(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool.__wrap(super(__LocalSetter, self).isGlobal(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DepthShader as __DepthShader_Config
__Config = __DepthShader_Config.Config
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Config(__Config, Config):
    """com.badlogic.gdx.graphics.g3d.shaders.DepthShader.Config"""
 
    @staticmethod
    def __wrap(java_value: __Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Config):
        """
        Dynamic initializer for Config.
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
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config(java.lang.String,java.lang.String)"""
        val = __Config(arg0, arg1)
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_Validator
__Validator = __BaseShader_Validator.Validator
from abc import abstractmethod, ABC
 
class Validator(ABC):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Validator"""
 
    @staticmethod
    def __wrap(java_value: __Validator) -> 'Validator':
        return Validator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Validator):
        """
        Dynamic initializer for Validator.
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
    def validate(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator.validate(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader
__DefaultShader = __DefaultShader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader
__BaseShader = __BaseShader
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class DefaultShader(__BaseShader, BaseShader):
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader"""
 
    @staticmethod
    def __wrap(java_value: __DefaultShader) -> 'DefaultShader':
        return DefaultShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultShader):
        """
        Dynamic initializer for DefaultShader.
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
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultDepthFunc()"""
        return int.__wrap(super(DefaultShader, self).getDefaultDepthFunc())

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(__DefaultShader, self).begin(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool.__wrap(super(__DefaultShader, self).equals(arg0))

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__BaseShader, self).init(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = __DefaultShader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __DefaultShader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = __DefaultShader(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = __DefaultShader(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(__DefaultShader, self).render(arg0, arg1)

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int.__wrap(super(__BaseShader, self).loc(__int.valueOf(arg0)))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int.__wrap(super(__BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool.__wrap(super(__DefaultShader, self).equals(arg0))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.init()"""
        super(DefaultShader, self).init()

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str.__wrap(super(__BaseShader, self).getUniformAlias(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__BaseShader, self).render(arg0)

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultFragmentShader()"""
        return str.__wrap(__DefaultShader.getDefaultFragmentShader())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.dispose()"""
        super(DefaultShader, self).dispose()

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int.__wrap(super(__BaseShader, self).register(arg0))

    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultDepthFunc(int)"""
        super(__DefaultShader, self).setDefaultDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool.__wrap(super(__DefaultShader, self).canRender(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str.__wrap(__DefaultShader.createPrefix(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int.__wrap(super(__DefaultShader, self).compareTo(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.end()"""
        super(DefaultShader, self).end()

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int.__wrap(super(__BaseShader, self).getUniformID(arg0))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config,java.lang.String)"""
        val = __DefaultShader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultCullFace()"""
        return int.__wrap(super(DefaultShader, self).getDefaultCullFace())

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultVertexShader()"""
        return str.__wrap(__DefaultShader.getDefaultVertexShader())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1, arg2))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool.__wrap(super(__BaseShader, self).has(__int.valueOf(arg0)))

    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultCullFace(int)"""
        super(__DefaultShader, self).setDefaultCullFace(__int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_Setter
__Setter = __BaseShader_Setter.Setter
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from abc import abstractmethod, ABC
 
class Setter(ABC):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.Setter"""
 
    @staticmethod
    def __wrap(java_value: __Setter) -> 'Setter':
        return Setter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Setter):
        """
        Dynamic initializer for Setter.
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
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public abstract void com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        pass

    @abstractmethod
    def isGlobal(self, arg0: 'BaseShader', arg1: int):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Inputs
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader_Inputs
__Inputs = __DefaultShader_Inputs.Inputs
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Inputs():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Inputs"""
 
    @staticmethod
    def __wrap(java_value: __Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Inputs):
        """
        Dynamic initializer for Inputs.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Inputs()"""
        val = __Inputs()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Inputs()"""
        val = __Inputs()
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader_Config
__Config = __DefaultShader_Config.Config
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Config():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Config"""
 
    @staticmethod
    def __wrap(java_value: __Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Config):
        """
        Dynamic initializer for Config.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config(java.lang.String,java.lang.String)"""
        val = __Config(arg0, arg1)
        self.__dict__ = val.__dict__
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
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader_Setters_ACubemap
__ACubemap = __DefaultShader_Setters_ACubemap.Setters.ACubemap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_LocalSetter
__LocalSetter = __BaseShader_LocalSetter.LocalSetter
from builtins import bool
from builtins import int
 
class ACubemap(__LocalSetter, LocalSetter):
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters.ACubemap"""
 
    @staticmethod
    def __wrap(java_value: __ACubemap) -> 'ACubemap':
        return ACubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ACubemap):
        """
        Dynamic initializer for ACubemap.
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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap(int,int)"""
        val = __ACubemap(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool.__wrap(super(__LocalSetter, self).isGlobal(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters$ACubemap.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(__ACubemap, self).set(arg0, __int.valueOf(arg1), arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DepthShader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DepthShader as __DepthShader
__DepthShader = __DepthShader
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader
__DefaultShader = __DefaultShader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader
__BaseShader = __BaseShader
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class DepthShader(__DefaultShader, DefaultShader):
    """com.badlogic.gdx.graphics.g3d.shaders.DepthShader"""
 
    @staticmethod
    def __wrap(java_value: __DepthShader) -> 'DepthShader':
        return DepthShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DepthShader):
        """
        Dynamic initializer for DepthShader.
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
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(__DepthShader, self).begin(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(java.lang.Object)"""
        return bool.__wrap(super(__DefaultShader, self).equals(arg0))

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__BaseShader, self).init(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int.__wrap(super(__BaseShader, self).loc(__int.valueOf(arg0)))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int.__wrap(super(__BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DepthShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool.__wrap(super(__DepthShader, self).canRender(arg0))

    @override
    @overload
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultDepthFunc()"""
        return int.__wrap(super(DefaultShader, self).getDefaultDepthFunc())

    @overload
    def equals(self, arg0: 'DefaultShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.equals(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader)"""
        return bool.__wrap(super(__DefaultShader, self).equals(arg0))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.init()"""
        super(DefaultShader, self).init()

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str.__wrap(super(__BaseShader, self).getUniformAlias(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__BaseShader, self).render(arg0)

    @override
    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultCullFace(int)"""
        super(__DefaultShader, self).setDefaultCullFace(__int.valueOf(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = __DepthShader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        val = __DepthShader(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config,java.lang.String)"""
        val = __DepthShader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.dispose()"""
        super(DefaultShader, self).dispose()

    @override
    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.setDefaultDepthFunc(int)"""
        super(__DefaultShader, self).setDefaultDepthFunc(__int.valueOf(arg0))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int.__wrap(super(__BaseShader, self).register(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        return str.__wrap(__DefaultShader.createPrefix(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int.__wrap(super(__DefaultShader, self).compareTo(arg0))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int.__wrap(super(__BaseShader, self).getUniformID(arg0))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @override
    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.getDefaultCullFace()"""
        return int.__wrap(super(DefaultShader, self).getDefaultCullFace())

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __DepthShader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(__DepthShader, self).render(arg0, arg1)

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.getDefaultFragmentShader()"""
        return str.__wrap(__DepthShader.getDefaultFragmentShader())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__BaseShader, self).register(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public com.badlogic.gdx.graphics.g3d.shaders.DepthShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = __DepthShader(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.shaders.DepthShader.end()"""
        super(DepthShader, self).end()

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.getDefaultVertexShader()"""
        return str.__wrap(__DepthShader.getDefaultVertexShader())

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.shaders.DepthShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        return str.__wrap(__DepthShader.createPrefix(arg0, arg1))

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool.__wrap(super(__BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool.__wrap(super(__BaseShader, self).has(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_Setter
__Setter = __BaseShader_Setter.Setter
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader_LocalSetter
__LocalSetter = __BaseShader_LocalSetter.LocalSetter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LocalSetter(ABC, __Setter, Setter):
    """com.badlogic.gdx.graphics.g3d.shaders.BaseShader.LocalSetter"""
 
    @staticmethod
    def __wrap(java_value: __LocalSetter) -> 'LocalSetter':
        return LocalSetter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LocalSetter):
        """
        Dynamic initializer for LocalSetter.
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
    def isGlobal(self, arg0: 'BaseShader', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter.isGlobal(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int)"""
        return bool.__wrap(super(__LocalSetter, self).isGlobal(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter()"""
        val = __LocalSetter()
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

    @abstractmethod
    def set(self, arg0: 'BaseShader', arg1: int, arg2: 'Renderable', arg3: 'Attributes'):
        """public abstract void com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter.set(com.badlogic.gdx.graphics.g3d.shaders.BaseShader,int,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.BaseShader$LocalSetter()"""
        val = __LocalSetter()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g3d.shaders.DefaultShader as __DefaultShader_Setters
__Setters = __DefaultShader_Setters.Setters
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Setters():
    """com.badlogic.gdx.graphics.g3d.shaders.DefaultShader.Setters"""
 
    @staticmethod
    def __wrap(java_value: __Setters) -> 'Setters':
        return Setters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Setters):
        """
        Dynamic initializer for Setters.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters()"""
        val = __Setters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Setters()"""
        val = __Setters()
        self.__dict__ = val.__dict__
        self.__wrapper = val