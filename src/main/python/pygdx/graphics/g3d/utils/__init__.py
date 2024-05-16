from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController_AnimationListener
_AnimationListener = _AnimationController_AnimationListener.AnimationListener
from abc import abstractmethod, ABC
 
class AnimationListener():
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController.AnimationListener"""
 
    @staticmethod
    def _wrap(java_value: _AnimationListener) -> 'AnimationListener':
        return AnimationListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnimationListener):
        """
        Dynamic initializer for AnimationListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnimationListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnimationListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onLoop(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onLoop(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

    @abstractmethod
    def onEnd(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onEnd(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController_AnimationListener
_AnimationListener = _AnimationController_AnimationListener.AnimationListener
from abc import abstractmethod, ABC
 
class AnimationListener():
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController.AnimationListener"""
 
    @staticmethod
    def _wrap(java_value: _AnimationListener) -> 'AnimationListener':
        return AnimationListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnimationListener):
        """
        Dynamic initializer for AnimationListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnimationListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnimationListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onLoop(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onLoop(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

    @abstractmethod
    def onEnd(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onEnd(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureProvider
import com.badlogic.gdx.graphics.g3d.utils.TextureProvider as _TextureProvider
_TextureProvider = _TextureProvider
from abc import abstractmethod, ABC
 
class TextureProvider():
    """com.badlogic.gdx.graphics.g3d.utils.TextureProvider"""
 
    @staticmethod
    def _wrap(java_value: _TextureProvider) -> 'TextureProvider':
        return TextureProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureProvider):
        """
        Dynamic initializer for TextureProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def load(self, arg0: str):
        """public abstract com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.utils.TextureProvider.load(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.ShaderProvider
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
import com.badlogic.gdx.graphics.g3d.utils.ShaderProvider as _ShaderProvider
_ShaderProvider = _ShaderProvider
 
class ShaderProvider():
    """com.badlogic.gdx.graphics.g3d.utils.ShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProvider) -> 'ShaderProvider':
        return ShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProvider):
        """
        Dynamic initializer for ShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getShader(self, arg0: 'Renderable'):
        """public abstract com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.ShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.ShapeCache
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.ShapeCache as _ShapeCache
_ShapeCache = _ShapeCache
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as _MeshPartBuilder
_MeshPartBuilder = _MeshPartBuilder
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeCache():
    """com.badlogic.gdx.graphics.g3d.utils.ShapeCache"""
 
    @staticmethod
    def _wrap(java_value: _ShapeCache) -> 'ShapeCache':
        return ShapeCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeCache):
        """
        Dynamic initializer for ShapeCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def begin(self) -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ShapeCache.begin()"""
        return 'MeshPartBuilder'._wrap(super(ShapeCache, self).begin())

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.utils.ShapeCache.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_ShapeCache, self).getRenderables(arg0, arg1)

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
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.ShapeCache.end()"""
        super(ShapeCache, self).end()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.utils.ShapeCache.getMaterial()"""
        return 'g3d.Material'._wrap(super(ShapeCache, self).getMaterial())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.ShapeCache()"""
        val = _ShapeCache()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'VertexAttributes', arg3: int):
        """public com.badlogic.gdx.graphics.g3d.utils.ShapeCache(int,int,com.badlogic.gdx.graphics.VertexAttributes,int)"""
        val = _ShapeCache(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.ShapeCache.dispose()"""
        super(ShapeCache, self).dispose()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getWorldTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.ShapeCache.getWorldTransform()"""
        return 'math.Matrix4'._wrap(super(ShapeCache, self).getWorldTransform())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.ShapeCache()"""
        val = _ShapeCache()
        self.__wrapper = val

    @overload
    def begin(self, arg0: int) -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ShapeCache.begin(int)"""
        return 'MeshPartBuilder'._wrap(super(_ShapeCache, self).begin(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController as _BaseAnimationController_Transform
_Transform = _BaseAnimationController_Transform.Transform
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Transform():
    """com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController.Transform"""
 
    @staticmethod
    def _wrap(java_value: _Transform) -> 'Transform':
        return Transform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Transform):
        """
        Dynamic initializer for Transform.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Transform__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Transform__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def lerp(self, arg0: 'Transform', arg1: float) -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.lerp(com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform,float)"""
        return 'Transform'._wrap(super(_Transform, self).lerp(arg0, _float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Transform') -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.set(com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform)"""
        return 'Transform'._wrap(super(_Transform, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3') -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3)"""
        return 'Transform'._wrap(super(_Transform, self).set(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.toString()"""
        return str._wrap(super(Transform, self).toString())

    @overload
    def lerp(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3', arg3: float) -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.lerp(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3,float)"""
        return 'Transform'._wrap(super(_Transform, self).lerp(arg0, arg1, arg2, _float.valueOf(arg3)))

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
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform()"""
        val = _Transform()
        self.__wrapper = val

    @overload
    def toMatrix4(self, arg0: 'Matrix4') -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.toMatrix4(com.badlogic.gdx.math.Matrix4)"""
        return 'math.Matrix4'._wrap(super(_Transform, self).toMatrix4(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform()"""
        val = _Transform()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.reset()"""
        super(Transform, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def idt(self) -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.idt()"""
        return 'Transform'._wrap(super(Transform, self).idt())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.utils.TextureProvider as _TextureProvider_FileTextureProvider
_FileTextureProvider = _TextureProvider_FileTextureProvider.FileTextureProvider
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileTextureProvider():
    """com.badlogic.gdx.graphics.g3d.utils.TextureProvider.FileTextureProvider"""
 
    @staticmethod
    def _wrap(java_value: _FileTextureProvider) -> 'FileTextureProvider':
        return FileTextureProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileTextureProvider):
        """
        Dynamic initializer for FileTextureProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileTextureProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileTextureProvider__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider()"""
        val = _FileTextureProvider()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider()"""
        val = _FileTextureProvider()
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

    @overload
    def load(self, arg0: str) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider.load(java.lang.String)"""
        return 'graphics.Texture'._wrap(super(_FileTextureProvider, self).load(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: 'TextureWrap', arg3: 'TextureWrap', arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        val = _FileTextureProvider(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as _BaseShaderProvider
_BaseShaderProvider = _BaseShaderProvider
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseShaderProvider():
    """com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _BaseShaderProvider) -> 'BaseShaderProvider':
        return BaseShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseShaderProvider):
        """
        Dynamic initializer for BaseShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(BaseShaderProvider, self).dispose()

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
        """public com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider()"""
        val = _BaseShaderProvider()
        self.__wrapper = val

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_BaseShaderProvider, self).getShader(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider()"""
        val = _BaseShaderProvider()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder as _DefaultTextureBinder
_DefaultTextureBinder = _DefaultTextureBinder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultTextureBinder():
    """com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder"""
 
    @staticmethod
    def _wrap(java_value: _DefaultTextureBinder) -> 'DefaultTextureBinder':
        return DefaultTextureBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultTextureBinder):
        """
        Dynamic initializer for DefaultTextureBinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultTextureBinder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultTextureBinder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder(int)"""
        val = _DefaultTextureBinder(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def bind(self, arg0: 'TextureDescriptor') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.bind(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return int._wrap(super(_DefaultTextureBinder, self).bind(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getBindCount(self) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.getBindCount()"""
        return int._wrap(super(DefaultTextureBinder, self).getBindCount())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder(int,int)"""
        val = _DefaultTextureBinder(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.end()"""
        super(DefaultTextureBinder, self).end()

    @overload
    def bind(self, arg0: 'GLTexture') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.bind(com.badlogic.gdx.graphics.GLTexture)"""
        return int._wrap(super(_DefaultTextureBinder, self).bind(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def resetCounts(self):
        """public final void com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.resetCounts()"""
        super(DefaultTextureBinder, self).resetCounts()

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
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder(int,int,int)"""
        val = _DefaultTextureBinder(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getReuseCount(self) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.getReuseCount()"""
        return int._wrap(super(DefaultTextureBinder, self).getReuseCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.begin()"""
        super(DefaultTextureBinder, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.ModelBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder as _ModelBuilder
_ModelBuilder = _ModelBuilder
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.MeshPart as _MeshPart
_MeshPart = _MeshPart
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as _MeshPartBuilder
_MeshPartBuilder = _MeshPartBuilder
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.ModelBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ModelBuilder) -> 'ModelBuilder':
        return ModelBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelBuilder):
        """
        Dynamic initializer for ModelBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createCapsule(self, arg0: float, arg1: float, arg2: int, arg3: 'Material', arg4: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCapsule(float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCapsule(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @overload
    def createXYZCoordinates(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createXYZCoordinates(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createXYZCoordinates(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.begin()"""
        super(ModelBuilder, self).begin()

    @overload
    def part(self, arg0: str, arg1: int, arg2: 'VertexAttributes', arg3: 'Material') -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,int,com.badlogic.gdx.graphics.VertexAttributes,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'MeshPartBuilder'._wrap(super(_ModelBuilder, self).part(arg0, _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def node(self, arg0: str, arg1: 'Model') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.node(java.lang.String,com.badlogic.gdx.graphics.g3d.Model)"""
        return 'model.Node'._wrap(super(_ModelBuilder, self).node(arg0, arg1))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int, arg7: float, arg8: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8)))

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float, arg3: 'Material', arg4: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createBox(float,float,float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createBox(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: 'Material', arg7: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createSphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7)))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createSphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.ModelBuilder()"""
        val = _ModelBuilder()
        self.__wrapper = val

    @overload
    def createXYZCoordinates(self, arg0: float, arg1: 'Material', arg2: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createXYZCoordinates(float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createXYZCoordinates(_float.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int, arg6: float, arg7: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @overload
    def part(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: 'Material') -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'model.MeshPart'._wrap(super(_ModelBuilder, self).part(arg0, arg1, _int.valueOf(arg2), arg3))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @overload
    def end(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.end()"""
        return 'g3d.Model'._wrap(super(ModelBuilder, self).end())

    @overload
    def createLineGrid(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createLineGrid(int,int,float,float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createLineGrid(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def part(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: int, arg4: int, arg5: 'Material') -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,int,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'model.MeshPart'._wrap(super(_ModelBuilder, self).part(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int, arg7: float, arg8: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8)))

    @overload
    def node(self) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.node()"""
        return 'model.Node'._wrap(super(ModelBuilder, self).node())

    @overload
    def createRect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: int, arg16: 'Material', arg17: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createRect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createRect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _int.valueOf(arg15), arg16, _long.valueOf(arg17)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.ModelBuilder()"""
        val = _ModelBuilder()
        self.__wrapper = val

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: 'Material', arg7: int, arg8: float, arg9: float, arg10: float, arg11: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float,float,float)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createSphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11)))

    @overload
    def manage(self, arg0: 'Disposable'):
        """public void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.manage(com.badlogic.gdx.utils.Disposable)"""
        super(_ModelBuilder, self).manage(arg0)

    @overload
    def part(self, arg0: 'MeshPart', arg1: 'Material'):
        """public void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(com.badlogic.gdx.graphics.g3d.model.MeshPart,com.badlogic.gdx.graphics.g3d.Material)"""
        super(_ModelBuilder, self).part(arg0, arg1)

    @overload
    def createArrow(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Material', arg3: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createArrow(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createArrow(arg0, arg1, arg2, _long.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def createArrow(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int, arg10: 'Material', arg11: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createArrow(float,float,float,float,float,float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createArrow(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10, _long.valueOf(arg11)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createBox(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createBox(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @overload
    def createCapsule(self, arg0: float, arg1: float, arg2: int, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCapsule(float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCapsule(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int, arg7: float, arg8: float, arg9: float, arg10: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float,float,float)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createSphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10)))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int, arg6: float, arg7: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @overload
    def createRect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: 'Material', arg16: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createRect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createRect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), arg15, _long.valueOf(arg16)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def part(self, arg0: str, arg1: int, arg2: int, arg3: 'Material') -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,int,long,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'MeshPartBuilder'._wrap(super(_ModelBuilder, self).part(arg0, _int.valueOf(arg1), _long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def rebuildReferences(arg0: 'Model'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.rebuildReferences(com.badlogic.gdx.graphics.g3d.Model)"""
        _ModelBuilder.rebuildReferences(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'._wrap(super(_ModelBuilder, self).createCone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.MeshBuilder
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import com.badlogic.gdx.graphics.g3d.model.MeshPart as _MeshPart
_MeshPart = _MeshPart
import com.badlogic.gdx.graphics.g3d.utils.MeshBuilder as _MeshBuilder
_MeshBuilder = _MeshBuilder
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MeshBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.MeshBuilder"""
 
    @staticmethod
    def _wrap(java_value: _MeshBuilder) -> 'MeshBuilder':
        return MeshBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MeshBuilder):
        """
        Dynamic initializer for MeshBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MeshBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MeshBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, arg6)

    @override
    @overload
    def rect(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(_MeshBuilder, self).rect(arg0, arg1, arg2, arg3)

    @overload
    def vertex(self, arg0: 'VertexInfo') -> int:
        """public short com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.vertex(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        return int._wrap(super(_MeshBuilder, self).vertex(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def end(self) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.end()"""
        return 'graphics.Mesh'._wrap(super(MeshBuilder, self).end())

    @override
    @overload
    def addMesh(self, arg0: 'float', arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(float[],short[],int,int)"""
        super(_MeshBuilder, self).addMesh(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def begin(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(long,int)"""
        super(_MeshBuilder, self).begin(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ensureTriangles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureTriangles(int)"""
        super(_MeshBuilder, self).ensureTriangles(_int.valueOf(arg0))

    @override
    @overload
    def sphere(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(com.badlogic.gdx.math.Matrix4,float,float,float,int,int,float,float,float,float)"""
        super(_MeshBuilder, self).sphere(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13))

    @override
    @overload
    def line(self, arg0: 'Vector3', arg1: 'Color', arg2: 'Vector3', arg3: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color)"""
        super(_MeshBuilder, self).line(arg0, arg1, arg2, arg3)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, arg6, _float.valueOf(arg7), _float.valueOf(arg8))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_MeshBuilder, self).setColor(arg0)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: 'Vector3', arg6: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), arg5, arg6)

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short,short,short,short,short,short)"""
        super(_MeshBuilder, self).index(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _short.valueOf(arg7))

    @override
    @overload
    def line(self, arg0: 'VertexInfo', arg1: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(_MeshBuilder, self).line(arg0, arg1)

    @override
    @overload
    def isVertexTransformationEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.isVertexTransformationEnabled()"""
        return bool._wrap(super(MeshBuilder, self).isVertexTransformationEnabled())

    @override
    @overload
    def line(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(short,short)"""
        super(_MeshBuilder, self).line(_short.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(MeshBuilder, self).getAttributes())

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short,short,short,short)"""
        super(_MeshBuilder, self).index(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def begin(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(long)"""
        super(_MeshBuilder, self).begin(_long.valueOf(arg0))

    @override
    @overload
    def box(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: 'VertexInfo', arg6: 'VertexInfo', arg7: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(_MeshBuilder, self).box(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @override
    @overload
    def setUVRange(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setUVRange(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_MeshBuilder, self).setUVRange(arg0)

    @override
    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(float,float,float,float,float,float)"""
        super(_MeshBuilder, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15), _float.valueOf(arg16))

    @override
    @overload
    def setVertexTransformationEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setVertexTransformationEnabled(boolean)"""
        super(_MeshBuilder, self).setVertexTransformationEnabled(_boolean.valueOf(arg0))

    @overload
    def ensureRectangles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureRectangles(int)"""
        super(_MeshBuilder, self).ensureRectangles(_int.valueOf(arg0))

    @override
    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cone(float,float,float,int,float,float)"""
        super(_MeshBuilder, self).cone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def vertex(self, *arg0: float) -> int:
        """public short com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.vertex(float...)"""
        return int._wrap(super(_MeshBuilder, self).vertex(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def sphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(float,float,float,int,int)"""
        super(_MeshBuilder, self).sphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def createAttributes(arg0: int) -> 'graphics.VertexAttributes':
        """public static com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.createAttributes(long)"""
        return graphics.VertexAttributes._wrap(_MeshBuilder.createAttributes(_long.valueOf(arg0)))

    @override
    @overload
    def sphere(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(com.badlogic.gdx.math.Matrix4,float,float,float,int,int)"""
        super(_MeshBuilder, self).sphere(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def lastIndex(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.lastIndex()"""
        return int._wrap(super(MeshBuilder, self).lastIndex())

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short,short)"""
        super(_MeshBuilder, self).index(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3))

    @override
    @overload
    def patch(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: int, arg16: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.patch(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,int)"""
        super(_MeshBuilder, self).patch(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16))

    @overload
    def getVertices(self, arg0: 'float', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getVertices(float[],int)"""
        super(_MeshBuilder, self).getVertices(arg0, _int.valueOf(arg1))

    @override
    @overload
    def sphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(float,float,float,int,int,float,float,float,float)"""
        super(_MeshBuilder, self).sphere(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @override
    @overload
    def box(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(float,float,float)"""
        super(_MeshBuilder, self).box(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def triangle(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).triangle(arg0, arg1, arg2)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10))

    @override
    @overload
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cylinder(float,float,float,int,float,float,boolean)"""
        super(_MeshBuilder, self).cylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6))

    @override
    @overload
    def rect(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).rect(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5, _float.valueOf(arg6), _float.valueOf(arg7))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def begin(self, arg0: 'VertexAttributes', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(com.badlogic.gdx.graphics.VertexAttributes,int)"""
        super(_MeshBuilder, self).begin(arg0, _int.valueOf(arg1))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _float.valueOf(arg5), _float.valueOf(arg6))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10))

    @overload
    def part(self, arg0: str, arg1: int) -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.part(java.lang.String,int)"""
        return 'model.MeshPart'._wrap(super(_MeshBuilder, self).part(arg0, _int.valueOf(arg1)))

    @overload
    def getVertexTransform(self, arg0: 'Matrix4') -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getVertexTransform(com.badlogic.gdx.math.Matrix4)"""
        return 'math.Matrix4'._wrap(super(_MeshBuilder, self).getVertexTransform(arg0))

    @override
    @overload
    def ensureVertices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureVertices(int)"""
        super(_MeshBuilder, self).ensureVertices(_int.valueOf(arg0))

    @override
    @overload
    def box(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(com.badlogic.gdx.math.Matrix4)"""
        super(_MeshBuilder, self).box(arg0)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def addMesh(self, arg0: 'MeshPart'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        super(_MeshBuilder, self).addMesh(arg0)

    @override
    @overload
    def triangle(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(short,short,short)"""
        super(_MeshBuilder, self).triangle(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def addMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(_MeshBuilder, self).addMesh(arg0)

    @override
    @overload
    def patch(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.patch(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,int,int)"""
        super(_MeshBuilder, self).patch(arg0, arg1, arg2, arg3, _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def box(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).box(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @overload
    def part(self, arg0: str, arg1: int, arg2: 'MeshPart') -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.part(java.lang.String,int,com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        return 'model.MeshPart'._wrap(super(_MeshBuilder, self).part(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def triangle(self, arg0: 'Vector3', arg1: 'Color', arg2: 'Vector3', arg3: 'Color', arg4: 'Vector3', arg5: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color)"""
        super(_MeshBuilder, self).triangle(arg0, arg1, arg2, arg3, arg4, arg5)

    @override
    @overload
    def setUVRange(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setUVRange(float,float,float,float)"""
        super(_MeshBuilder, self).setUVRange(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).rect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14))

    @override
    @overload
    def addMesh(self, arg0: 'float', arg1: 'short'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(float[],short[])"""
        super(_MeshBuilder, self).addMesh(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getNumIndices()"""
        return int._wrap(super(MeshBuilder, self).getNumIndices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cylinder(float,float,float,int,float,float)"""
        super(_MeshBuilder, self).cylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14))

    @override
    @overload
    def ensureTriangleIndices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureTriangleIndices(int)"""
        super(_MeshBuilder, self).ensureTriangleIndices(_int.valueOf(arg0))

    @overload
    def ensureRectangles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureRectangles(int,int)"""
        super(_MeshBuilder, self).ensureRectangles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPrimitiveType(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getPrimitiveType()"""
        return int._wrap(super(MeshBuilder, self).getPrimitiveType())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshBuilder()"""
        val = _MeshBuilder()
        self.__wrapper = val

    @override
    @overload
    def index(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short)"""
        super(_MeshBuilder, self).index(_short.valueOf(arg0))

    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getNumVertices()"""
        return int._wrap(super(MeshBuilder, self).getNumVertices())

    @override
    @overload
    def triangle(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(_MeshBuilder, self).triangle(arg0, arg1, arg2)

    @override
    @overload
    def ensureRectangleIndices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureRectangleIndices(int)"""
        super(_MeshBuilder, self).ensureRectangleIndices(_int.valueOf(arg0))

    @overload
    def begin(self, arg0: 'VertexAttributes'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(com.badlogic.gdx.graphics.VertexAttributes)"""
        super(_MeshBuilder, self).begin(arg0)

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.clear()"""
        super(MeshBuilder, self).clear()

    @overload
    def getIndices(self, arg0: 'short', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getIndices(short[],int)"""
        super(_MeshBuilder, self).getIndices(arg0, _int.valueOf(arg1))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15))

    @override
    @overload
    def arrow(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.arrow(float,float,float,float,float,float,float,float,int)"""
        super(_MeshBuilder, self).arrow(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float, arg18: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15), _float.valueOf(arg16), _float.valueOf(arg17), _float.valueOf(arg18))

    @override
    @overload
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cylinder(float,float,float,int)"""
        super(_MeshBuilder, self).cylinder(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getFloatsPerVertex(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getFloatsPerVertex()"""
        return int._wrap(super(MeshBuilder, self).getFloatsPerVertex())

    @override
    @overload
    def rect(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(short,short,short,short)"""
        super(_MeshBuilder, self).rect(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4)

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setColor(float,float,float,float)"""
        super(_MeshBuilder, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def box(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(float,float,float,float,float,float)"""
        super(_MeshBuilder, self).box(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def ensureIndices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureIndices(int)"""
        super(_MeshBuilder, self).ensureIndices(_int.valueOf(arg0))

    @overload
    def ensureTriangles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureTriangles(int,int)"""
        super(_MeshBuilder, self).ensureTriangles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short)"""
        super(_MeshBuilder, self).index(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshBuilder()"""
        val = _MeshBuilder()
        self.__wrapper = val

    @override
    @overload
    def ensureCapacity(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureCapacity(int,int)"""
        super(_MeshBuilder, self).ensureCapacity(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def line(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).line(arg0, arg1)

    @override
    @overload
    def patch(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.patch(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int)"""
        super(_MeshBuilder, self).patch(arg0, arg1, arg2, arg3, arg4, _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def index(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short)"""
        super(_MeshBuilder, self).index(_short.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def addMesh(self, arg0: 'Mesh', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(com.badlogic.gdx.graphics.Mesh,int,int)"""
        super(_MeshBuilder, self).addMesh(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cone(float,float,float,int)"""
        super(_MeshBuilder, self).cone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def getMeshPart(self) -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getMeshPart()"""
        return 'model.MeshPart'._wrap(super(MeshBuilder, self).getMeshPart())

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_MeshBuilder, self).circle(_float.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def setVertexTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setVertexTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_MeshBuilder, self).setVertexTransform(arg0)

    @override
    @overload
    def capsule(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.capsule(float,float,int)"""
        super(_MeshBuilder, self).capsule(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def end(self, arg0: 'Mesh') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.end(com.badlogic.gdx.graphics.Mesh)"""
        return 'graphics.Mesh'._wrap(super(_MeshBuilder, self).end(arg0))

    @overload
    def vertex(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2') -> int:
        """public short com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.vertex(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        return int._wrap(super(_MeshBuilder, self).vertex(arg0, arg1, arg2, arg3)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

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
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter as _DefaultRenderableSorter
_DefaultRenderableSorter = _DefaultRenderableSorter
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultRenderableSorter():
    """com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter"""
 
    @staticmethod
    def _wrap(java_value: _DefaultRenderableSorter) -> 'DefaultRenderableSorter':
        return DefaultRenderableSorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultRenderableSorter):
        """
        Dynamic initializer for DefaultRenderableSorter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultRenderableSorter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultRenderableSorter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @override
    @overload
    def sort(self, arg0: 'Camera', arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter.sort(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_DefaultRenderableSorter, self).sort(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter()"""
        val = _DefaultRenderableSorter()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: 'Renderable', arg1: 'Renderable') -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter.compare(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return int._wrap(super(_DefaultRenderableSorter, self).compare(arg0, arg1))

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
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter()"""
        val = _DefaultRenderableSorter()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor as _TextureDescriptor
_TextureDescriptor = _TextureDescriptor
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureDescriptor():
    """com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor"""
 
    @staticmethod
    def _wrap(java_value: _TextureDescriptor) -> 'TextureDescriptor':
        return TextureDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureDescriptor):
        """
        Dynamic initializer for TextureDescriptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureDescriptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureDescriptor__wrapper":
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

    @overload
    def __init__(self, arg0: 'GLTexture', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: 'TextureWrap', arg4: 'TextureWrap'):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor(T,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        val = _TextureDescriptor(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def set(self, arg0: 'TextureDescriptor'):
        """public <V extends T> void com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.set(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<V>)"""
        super(_TextureDescriptor, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def compareTo(self, arg0: 'TextureDescriptor') -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.compareTo(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>)"""
        return int._wrap(super(_TextureDescriptor, self).compareTo(arg0))

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
    def set(self, arg0: 'GLTexture', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: 'TextureWrap', arg4: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.set(T,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_TextureDescriptor, self).set(arg0, arg1, arg2, arg3, arg4)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor()"""
        val = _TextureDescriptor()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.equals(java.lang.Object)"""
        return bool._wrap(super(_TextureDescriptor, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'GLTexture'):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor(T)"""
        val = _TextureDescriptor(arg0)
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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.hashCode()"""
        return int._wrap(super(TextureDescriptor, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor()"""
        val = _TextureDescriptor()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.utils.CameraInputController as _CameraInputController_CameraGestureListener
_CameraGestureListener = _CameraInputController_CameraGestureListener.CameraGestureListener
import java.lang.Float as _float
import com.badlogic.gdx.input.GestureDetector as _GestureDetector_GestureAdapter
_GestureAdapter = _GestureDetector_GestureAdapter.GestureAdapter
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CameraGestureListener():
    """com.badlogic.gdx.graphics.g3d.utils.CameraInputController.CameraGestureListener"""
 
    @staticmethod
    def _wrap(java_value: _CameraGestureListener) -> 'CameraGestureListener':
        return CameraGestureListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CameraGestureListener):
        """
        Dynamic initializer for CameraGestureListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CameraGestureListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CameraGestureListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def fling(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.fling(float,float,int)"""
        return bool._wrap(super(_CameraGestureListener, self).fling(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def panStop(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.panStop(float,float,int,int)"""
        return bool._wrap(super(_input.GestureDetector$GestureAdapter, self).panStop(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def pan(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.pan(float,float,float,float)"""
        return bool._wrap(super(_CameraGestureListener, self).pan(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def pinchStop(self):
        """public void com.badlogic.gdx.input.GestureDetector$GestureAdapter.pinchStop()"""
        super(input.GestureDetector$GestureAdapter, self).pinchStop()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def longPress(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.longPress(float,float)"""
        return bool._wrap(super(_CameraGestureListener, self).longPress(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def tap(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.tap(float,float,int,int)"""
        return bool._wrap(super(_CameraGestureListener, self).tap(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.touchDown(float,float,int,int)"""
        return bool._wrap(super(_CameraGestureListener, self).touchDown(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def zoom(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.zoom(float,float)"""
        return bool._wrap(super(_CameraGestureListener, self).zoom(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def pinch(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.pinch(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_CameraGestureListener, self).pinch(arg0, arg1, arg2, arg3))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.RenderableSorter
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.utils.RenderableSorter as _RenderableSorter
_RenderableSorter = _RenderableSorter
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

 
class RenderableSorter():
    """com.badlogic.gdx.graphics.g3d.utils.RenderableSorter"""
 
    @staticmethod
    def _wrap(java_value: _RenderableSorter) -> 'RenderableSorter':
        return RenderableSorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderableSorter):
        """
        Dynamic initializer for RenderableSorter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderableSorter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderableSorter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def sort(self, arg0: 'Camera', arg1: 'Array'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.RenderableSorter.sort(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider
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
import com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider as _DepthShaderProvider
_DepthShaderProvider = _DepthShaderProvider
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DepthShaderProvider():
    """com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _DepthShaderProvider) -> 'DepthShaderProvider':
        return DepthShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DepthShaderProvider):
        """
        Dynamic initializer for DepthShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DepthShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DepthShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(BaseShaderProvider, self).dispose()

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
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _DepthShaderProvider(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider()"""
        val = _DepthShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider(java.lang.String,java.lang.String)"""
        val = _DepthShaderProvider(arg0, arg1)
        self.__wrapper = val

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_BaseShaderProvider, self).getShader(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider()"""
        val = _DepthShaderProvider()
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
    def __init__(self, arg0: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        val = _DepthShaderProvider(arg0)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController
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

import com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController as _BaseAnimationController
_BaseAnimationController = _BaseAnimationController
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseAnimationController():
    """com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController"""
 
    @staticmethod
    def _wrap(java_value: _BaseAnimationController) -> 'BaseAnimationController':
        return BaseAnimationController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseAnimationController):
        """
        Dynamic initializer for BaseAnimationController.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseAnimationController__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseAnimationController__wrapper":
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
    def __init__(self, arg0: 'ModelInstance'):
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = _BaseAnimationController(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureBinder
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.utils.TextureBinder as _TextureBinder
_TextureBinder = _TextureBinder
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

 
class TextureBinder():
    """com.badlogic.gdx.graphics.g3d.utils.TextureBinder"""
 
    @staticmethod
    def _wrap(java_value: _TextureBinder) -> 'TextureBinder':
        return TextureBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureBinder):
        """
        Dynamic initializer for TextureBinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureBinder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureBinder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.TextureBinder.begin()"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.TextureBinder.end()"""
        pass

    @abstractmethod
    def bind(self, arg0: 'GLTexture'):
        """public abstract int com.badlogic.gdx.graphics.g3d.utils.TextureBinder.bind(com.badlogic.gdx.graphics.GLTexture)"""
        pass

    @abstractmethod
    def getReuseCount(self, ):
        """public abstract int com.badlogic.gdx.graphics.g3d.utils.TextureBinder.getReuseCount()"""
        pass

    @abstractmethod
    def getBindCount(self, ):
        """public abstract int com.badlogic.gdx.graphics.g3d.utils.TextureBinder.getBindCount()"""
        pass

    @abstractmethod
    def resetCounts(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.TextureBinder.resetCounts()"""
        pass

    @abstractmethod
    def bind(self, arg0: 'TextureDescriptor'):
        """public abstract int com.badlogic.gdx.graphics.g3d.utils.TextureBinder.bind(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController
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

import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController_AnimationDesc
_AnimationDesc = _AnimationController_AnimationDesc.AnimationDesc
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController
_AnimationController = _AnimationController
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnimationController():
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController"""
 
    @staticmethod
    def _wrap(java_value: _AnimationController) -> 'AnimationController':
        return AnimationController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnimationController):
        """
        Dynamic initializer for AnimationController.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnimationController__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnimationController__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def action(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.action(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).action(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).setAnimation(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ModelInstance'):
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = _AnimationController(arg0)
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
    def animate(self, arg0: str, arg1: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).animate(arg0, _float.valueOf(arg1)))

    @overload
    def queue(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.queue(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).queue(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @overload
    def setAnimation(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).setAnimation(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def action(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.action(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).action(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _float.valueOf(arg6)))

    @overload
    def animate(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).animate(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @overload
    def animate(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).animate(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _float.valueOf(arg6)))

    @overload
    def setAnimation(self, arg0: str) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).setAnimation(arg0))

    @overload
    def setAnimation(self, arg0: str, arg1: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).setAnimation(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def animate(self, arg0: str, arg1: int, arg2: 'AnimationListener', arg3: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).animate(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3)))

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).setAnimation(arg0, _int.valueOf(arg1), arg2))

    @overload
    def animate(self, arg0: str, arg1: 'AnimationListener', arg2: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).animate(arg0, arg1, _float.valueOf(arg2)))

    @overload
    def queue(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.queue(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).queue(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _float.valueOf(arg6)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.AnimationController.update(float)"""
        super(_AnimationController, self).update(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setAnimation(self, arg0: str, arg1: int) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,int)"""
        return 'AnimationDesc'._wrap(super(_AnimationController, self).setAnimation(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

from builtins import float
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as _MeshPartBuilder
_MeshPartBuilder = _MeshPartBuilder
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import int
 
class MeshPartBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder"""
 
    @staticmethod
    def _wrap(java_value: _MeshPartBuilder) -> 'MeshPartBuilder':
        return MeshPartBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MeshPartBuilder):
        """
        Dynamic initializer for MeshPartBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MeshPartBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MeshPartBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: bool):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.cylinder(float,float,float,int,float,float,boolean)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def triangle(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.triangle(short,short,short)"""
        pass

    @abstractmethod
    def triangle(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.triangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def sphere(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.sphere(com.badlogic.gdx.math.Matrix4,float,float,float,int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def sphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.sphere(float,float,float,int,int)"""
        pass

    @abstractmethod
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.line(float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: 'Vector3', arg6: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def ensureRectangleIndices(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ensureRectangleIndices(int)"""
        pass

    @abstractmethod
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.index(short,short,short,short)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def index(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.index(short,short,short)"""
        pass

    @abstractmethod
    def setUVRange(self, arg0: 'TextureRegion'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.setUVRange(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        pass

    @abstractmethod
    def setUVRange(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.setUVRange(float,float,float,float)"""
        pass

    @abstractmethod
    def setColor(self, arg0: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.setColor(com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def vertex(self, *arg0: float):
        """public abstract short com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.vertex(float...)"""
        pass

    @abstractmethod
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.setColor(float,float,float,float)"""
        pass

    @abstractmethod
    def getAttributes(self, ):
        """public abstract com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.getAttributes()"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float, arg18: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def rect(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.rect(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def index(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.index(short)"""
        pass

    @abstractmethod
    def triangle(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.triangle(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        pass

    @abstractmethod
    def ensureTriangleIndices(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ensureTriangleIndices(int)"""
        pass

    @abstractmethod
    def index(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.index(short,short)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def line(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def box(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.box(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.index(short,short,short,short,short,short)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def capsule(self, arg0: float, arg1: float, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.capsule(float,float,int)"""
        pass

    @abstractmethod
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.index(short,short,short,short,short,short,short,short)"""
        pass

    @abstractmethod
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.rect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def box(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.box(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def getPrimitiveType(self, ):
        """public abstract int com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.getPrimitiveType()"""
        pass

    @abstractmethod
    def getMeshPart(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.getMeshPart()"""
        pass

    @abstractmethod
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.cylinder(float,float,float,int)"""
        pass

    @abstractmethod
    def addMesh(self, arg0: 'MeshPart'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.addMesh(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        pass

    @abstractmethod
    def vertex(self, arg0: 'VertexInfo'):
        """public abstract short com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.vertex(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        pass

    @abstractmethod
    def addMesh(self, arg0: 'Mesh', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.addMesh(com.badlogic.gdx.graphics.Mesh,int,int)"""
        pass

    @abstractmethod
    def setVertexTransformationEnabled(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.setVertexTransformationEnabled(boolean)"""
        pass

    @abstractmethod
    def setVertexTransform(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.setVertexTransform(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def rect(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.rect(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: float, arg7: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        pass

    @abstractmethod
    def line(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.line(short,short)"""
        pass

    @abstractmethod
    def patch(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.patch(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int)"""
        pass

    @abstractmethod
    def patch(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: int, arg16: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.patch(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,int)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def addMesh(self, arg0: 'Mesh'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.addMesh(com.badlogic.gdx.graphics.Mesh)"""
        pass

    @abstractmethod
    def addMesh(self, arg0: 'float', arg1: 'short'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.addMesh(float[],short[])"""
        pass

    @abstractmethod
    def ensureCapacity(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ensureCapacity(int,int)"""
        pass

    @abstractmethod
    def arrow(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.arrow(float,float,float,float,float,float,float,float,int)"""
        pass

    @abstractmethod
    def box(self, arg0: float, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.box(float,float,float)"""
        pass

    @abstractmethod
    def patch(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.patch(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,int,int)"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        pass

    @abstractmethod
    def vertex(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2'):
        """public abstract short com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.vertex(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        pass

    @abstractmethod
    def triangle(self, arg0: 'Vector3', arg1: 'Color', arg2: 'Vector3', arg3: 'Color', arg4: 'Vector3', arg5: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.triangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.cylinder(float,float,float,int,float,float)"""
        pass

    @abstractmethod
    def line(self, arg0: 'VertexInfo', arg1: 'VertexInfo'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.line(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        pass

    @abstractmethod
    def rect(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.rect(short,short,short,short)"""
        pass

    @abstractmethod
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.cone(float,float,float,int)"""
        pass

    @abstractmethod
    def line(self, arg0: 'Vector3', arg1: 'Color', arg2: 'Vector3', arg3: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def ensureIndices(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ensureIndices(int)"""
        pass

    @abstractmethod
    def addMesh(self, arg0: 'float', arg1: 'short', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.addMesh(float[],short[],int,int)"""
        pass

    @abstractmethod
    def box(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.box(float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.cone(float,float,float,int,float,float)"""
        pass

    @abstractmethod
    def box(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: 'VertexInfo', arg6: 'VertexInfo', arg7: 'VertexInfo'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.box(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        pass

    @abstractmethod
    def isVertexTransformationEnabled(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.isVertexTransformationEnabled()"""
        pass

    @abstractmethod
    def sphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.sphere(float,float,float,int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def getVertexTransform(self, arg0: 'Matrix4'):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.getVertexTransform(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def ensureVertices(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ensureVertices(int)"""
        pass

    @abstractmethod
    def sphere(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.sphere(com.badlogic.gdx.math.Matrix4,float,float,float,int,int)"""
        pass

    @abstractmethod
    def lastIndex(self, ):
        """public abstract int com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.lastIndex()"""
        pass

    @abstractmethod
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.InputAdapter as _InputAdapter
_InputAdapter = _InputAdapter
import com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController as _FirstPersonCameraController
_FirstPersonCameraController = _FirstPersonCameraController
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FirstPersonCameraController():
    """com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController"""
 
    @staticmethod
    def _wrap(java_value: _FirstPersonCameraController) -> 'FirstPersonCameraController':
        return FirstPersonCameraController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FirstPersonCameraController):
        """
        Dynamic initializer for FirstPersonCameraController.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FirstPersonCameraController__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FirstPersonCameraController__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setVelocity(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.setVelocity(float)"""
        super(_FirstPersonCameraController, self).setVelocity(_float.valueOf(arg0))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.touchDragged(int,int,int)"""
        return bool._wrap(super(_FirstPersonCameraController, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def setDegreesPerPixel(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.setDegreesPerPixel(float)"""
        super(_FirstPersonCameraController, self).setDegreesPerPixel(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchDown(int,int,int,int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.update(float)"""
        super(_FirstPersonCameraController, self).update(_float.valueOf(arg0))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController(com.badlogic.gdx.graphics.Camera)"""
        val = _FirstPersonCameraController(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.keyUp(int)"""
        return bool._wrap(super(_FirstPersonCameraController, self).keyUp(_int.valueOf(arg0)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).keyTyped(_char.valueOf(arg0)))

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
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchUp(int,int,int,int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.keyDown(int)"""
        return bool._wrap(super(_FirstPersonCameraController, self).keyDown(_int.valueOf(arg0)))

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.update()"""
        super(FirstPersonCameraController, self).update()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as _AnimationController_AnimationDesc
_AnimationDesc = _AnimationController_AnimationDesc.AnimationDesc
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnimationDesc():
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController.AnimationDesc"""
 
    @staticmethod
    def _wrap(java_value: _AnimationDesc) -> 'AnimationDesc':
        return AnimationDesc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnimationDesc):
        """
        Dynamic initializer for AnimationDesc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnimationDesc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnimationDesc__wrapper":
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.RenderContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.RenderContext as _RenderContext
_RenderContext = _RenderContext
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderContext():
    """com.badlogic.gdx.graphics.g3d.utils.RenderContext"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setDepthTest(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setDepthTest(int)"""
        super(_RenderContext, self).setDepthTest(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setCullFace(int)"""
        super(_RenderContext, self).setCullFace(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.end()"""
        super(RenderContext, self).end()

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
    def setDepthTest(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setDepthTest(int,float,float)"""
        super(_RenderContext, self).setDepthTest(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setDepthMask(boolean)"""
        super(_RenderContext, self).setDepthMask(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TextureBinder'):
        """public com.badlogic.gdx.graphics.g3d.utils.RenderContext(com.badlogic.gdx.graphics.g3d.utils.TextureBinder)"""
        val = _RenderContext(arg0)
        self.__wrapper = val

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.begin()"""
        super(RenderContext, self).begin()

    @overload
    def setBlending(self, arg0: bool, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setBlending(boolean,int,int)"""
        super(_RenderContext, self).setBlending(_boolean.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.CameraInputController
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.input.GestureDetector as _GestureDetector
_GestureDetector = _GestureDetector
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.InputAdapter as _InputAdapter
_InputAdapter = _InputAdapter
import com.badlogic.gdx.graphics.g3d.utils.CameraInputController as _CameraInputController
_CameraInputController = _CameraInputController
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CameraInputController():
    """com.badlogic.gdx.graphics.g3d.utils.CameraInputController"""
 
    @staticmethod
    def _wrap(java_value: _CameraInputController) -> 'CameraInputController':
        return CameraInputController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CameraInputController):
        """
        Dynamic initializer for CameraInputController.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CameraInputController__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CameraInputController__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def zoom(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.zoom(float)"""
        return bool._wrap(super(_CameraInputController, self).zoom(_float.valueOf(arg0)))

    @overload
    def touchUp(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(float,float,int,int)"""
        return bool._wrap(super(_input.GestureDetector, self).touchUp(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def cancel(self):
        """public void com.badlogic.gdx.input.GestureDetector.cancel()"""
        super(input.GestureDetector, self).cancel()

    @override
    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.input.GestureDetector.invalidateTapSquare()"""
        super(input.GestureDetector, self).invalidateTapSquare()

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.keyDown(int)"""
        return bool._wrap(super(_CameraInputController, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.touchDragged(int,int,int)"""
        return bool._wrap(super(_CameraInputController, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isPanning(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isPanning()"""
        return bool._wrap(super(input.GestureDetector, self).isPanning())

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.touchUp(int,int,int,int)"""
        return bool._wrap(super(_CameraInputController, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.graphics.g3d.utils.CameraInputController(com.badlogic.gdx.graphics.Camera)"""
        val = _CameraInputController(arg0)
        self.__wrapper = val

    @override
    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapSquareSize(float)"""
        super(_input.GestureDetector, self).setTapSquareSize(_float.valueOf(arg0))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.keyUp(int)"""
        return bool._wrap(super(_CameraInputController, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setMaxFlingDelay(self, arg0: int):
        """public void com.badlogic.gdx.input.GestureDetector.setMaxFlingDelay(long)"""
        super(_input.GestureDetector, self).setMaxFlingDelay(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def touchDragged(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(float,float,int)"""
        return bool._wrap(super(_input.GestureDetector, self).touchDragged(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.input.GestureDetector.reset()"""
        super(input.GestureDetector, self).reset()

    @overload
    def setInvertedControls(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.CameraInputController.setInvertedControls(boolean)"""
        super(_CameraInputController, self).setInvertedControls(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_input.GestureDetector, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.scrolled(float,float)"""
        return bool._wrap(super(_CameraInputController, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isLongPressed(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed(float)"""
        return bool._wrap(super(_input.GestureDetector, self).isLongPressed(_float.valueOf(arg0)))

    @override
    @overload
    def setLongPressSeconds(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setLongPressSeconds(float)"""
        super(_input.GestureDetector, self).setLongPressSeconds(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.CameraInputController.update()"""
        super(CameraInputController, self).update()

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).keyTyped(_char.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.touchDown(int,int,int,int)"""
        return bool._wrap(super(_CameraInputController, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def isLongPressed(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed()"""
        return bool._wrap(super(input.GestureDetector, self).isLongPressed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapCountInterval(float)"""
        super(_input.GestureDetector, self).setTapCountInterval(_float.valueOf(arg0))

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(float,float,int,int)"""
        return bool._wrap(super(_input.GestureDetector, self).touchDown(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def setTapRectangleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapRectangleSize(float,float)"""
        super(_input.GestureDetector, self).setTapRectangleSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureProvider$AssetTextureProvider
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.TextureProvider as _TextureProvider_AssetTextureProvider
_AssetTextureProvider = _TextureProvider_AssetTextureProvider.AssetTextureProvider
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetTextureProvider():
    """com.badlogic.gdx.graphics.g3d.utils.TextureProvider.AssetTextureProvider"""
 
    @staticmethod
    def _wrap(java_value: _AssetTextureProvider) -> 'AssetTextureProvider':
        return AssetTextureProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetTextureProvider):
        """
        Dynamic initializer for AssetTextureProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetTextureProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetTextureProvider__wrapper":
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

    @overload
    def __init__(self, arg0: 'AssetManager'):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$AssetTextureProvider(com.badlogic.gdx.assets.AssetManager)"""
        val = _AssetTextureProvider(arg0)
        self.__wrapper = val

    @overload
    def load(self, arg0: str) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.utils.TextureProvider$AssetTextureProvider.load(java.lang.String)"""
        return 'graphics.Texture'._wrap(super(_AssetTextureProvider, self).load(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.Shader as _Shader
_Shader = _Shader
import com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider as _DefaultShaderProvider
_DefaultShaderProvider = _DefaultShaderProvider
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
 
class DefaultShaderProvider():
    """com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider"""
 
    @staticmethod
    def _wrap(java_value: _DefaultShaderProvider) -> 'DefaultShaderProvider':
        return DefaultShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultShaderProvider):
        """
        Dynamic initializer for DefaultShaderProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultShaderProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultShaderProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider()"""
        val = _DefaultShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(BaseShaderProvider, self).dispose()

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
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _DefaultShaderProvider(arg0, arg1)
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

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'._wrap(super(_BaseShaderProvider, self).getShader(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider()"""
        val = _DefaultShaderProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = _DefaultShaderProvider(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider(java.lang.String,java.lang.String)"""
        val = _DefaultShaderProvider(arg0, arg1)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as _MeshPartBuilder_VertexInfo
_VertexInfo = _MeshPartBuilder_VertexInfo.VertexInfo
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexInfo():
    """com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.VertexInfo"""
 
    @staticmethod
    def _wrap(java_value: _VertexInfo) -> 'VertexInfo':
        return VertexInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexInfo):
        """
        Dynamic initializer for VertexInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setUV(self, arg0: float, arg1: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setUV(float,float)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setUV(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setCol(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setCol(float,float,float,float)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setCol(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.reset()"""
        super(VertexInfo, self).reset()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo()"""
        val = _VertexInfo()
        self.__wrapper = val

    @overload
    def set(self, arg0: 'VertexInfo') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.set(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).set(arg0))

    @overload
    def setUV(self, arg0: 'Vector2') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setUV(com.badlogic.gdx.math.Vector2)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setUV(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).set(arg0, arg1, arg2, arg3))

    @overload
    def setNor(self, arg0: 'Vector3') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setNor(com.badlogic.gdx.math.Vector3)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setNor(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setNor(self, arg0: float, arg1: float, arg2: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setNor(float,float,float)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setNor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def lerp(self, arg0: 'VertexInfo', arg1: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.lerp(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,float)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).lerp(arg0, _float.valueOf(arg1)))

    @overload
    def setCol(self, arg0: 'Color') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setCol(com.badlogic.gdx.graphics.Color)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setCol(arg0))

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
    def setPos(self, arg0: 'Vector3') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setPos(com.badlogic.gdx.math.Vector3)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setPos(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo()"""
        val = _VertexInfo()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPos(self, arg0: float, arg1: float, arg2: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setPos(float,float,float)"""
        return 'VertexInfo'._wrap(super(_VertexInfo, self).setPos(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())