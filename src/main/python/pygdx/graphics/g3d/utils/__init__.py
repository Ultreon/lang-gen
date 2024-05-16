from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController_AnimationListener
__AnimationListener = __AnimationController_AnimationListener.AnimationListener
 
class AnimationListener(ABC):
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController.AnimationListener"""
 
    @staticmethod
    def __wrap(java_value: __AnimationListener) -> 'AnimationListener':
        return AnimationListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnimationListener):
        """
        Dynamic initializer for AnimationListener.
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
    def onLoop(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onLoop(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

    @abstractmethod
    def onEnd(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onEnd(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController_AnimationListener
__AnimationListener = __AnimationController_AnimationListener.AnimationListener
 
class AnimationListener(ABC):
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController.AnimationListener"""
 
    @staticmethod
    def __wrap(java_value: __AnimationListener) -> 'AnimationListener':
        return AnimationListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnimationListener):
        """
        Dynamic initializer for AnimationListener.
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
    def onLoop(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onLoop(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

    @abstractmethod
    def onEnd(self, arg0: 'AnimationDesc'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener.onEnd(com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureProvider
import com.badlogic.gdx.graphics.g3d.utils.TextureProvider as __TextureProvider
__TextureProvider = __TextureProvider
from abc import abstractmethod, ABC
 
class TextureProvider(ABC):
    """com.badlogic.gdx.graphics.g3d.utils.TextureProvider"""
 
    @staticmethod
    def __wrap(java_value: __TextureProvider) -> 'TextureProvider':
        return TextureProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureProvider):
        """
        Dynamic initializer for TextureProvider.
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
    def load(self, arg0: str):
        """public abstract com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.utils.TextureProvider.load(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.ShaderProvider
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.utils.ShaderProvider as __ShaderProvider
__ShaderProvider = __ShaderProvider
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class ShaderProvider(ABC, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.g3d.utils.ShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __ShaderProvider) -> 'ShaderProvider':
        return ShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderProvider):
        """
        Dynamic initializer for ShaderProvider.
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
    def getShader(self, arg0: 'Renderable'):
        """public abstract com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.ShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter as __DefaultRenderableSorter
__DefaultRenderableSorter = __DefaultRenderableSorter
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class DefaultRenderableSorter(__RenderableSorter, RenderableSorter, __Comparator, Comparator):
    """com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter"""
 
    @staticmethod
    def __wrap(java_value: __DefaultRenderableSorter) -> 'DefaultRenderableSorter':
        return DefaultRenderableSorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultRenderableSorter):
        """
        Dynamic initializer for DefaultRenderableSorter.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter()"""
        val = __DefaultRenderableSorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compare(self, arg0: 'Renderable', arg1: 'Renderable') -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter.compare(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return int.__wrap(super(__DefaultRenderableSorter, self).compare(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter()"""
        val = __DefaultRenderableSorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sort(self, arg0: 'Camera', arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.utils.DefaultRenderableSorter.sort(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__DefaultRenderableSorter, self).sort(arg0, arg1)

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.MeshBuilder
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Short as __short
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.utils.MeshBuilder as __MeshBuilder
__MeshBuilder = __MeshBuilder
import com.badlogic.gdx.graphics.g3d.model.MeshPart as __MeshPart
__MeshPart = __MeshPart
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class MeshBuilder(__MeshPartBuilder, MeshPartBuilder):
    """com.badlogic.gdx.graphics.g3d.utils.MeshBuilder"""
 
    @staticmethod
    def __wrap(java_value: __MeshBuilder) -> 'MeshBuilder':
        return MeshBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MeshBuilder):
        """
        Dynamic initializer for MeshBuilder.
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
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __float.valueOf(arg5), __float.valueOf(arg6))

    @override
    @overload
    def ensureRectangleIndices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureRectangleIndices(int)"""
        super(__MeshBuilder, self).ensureRectangleIndices(__int.valueOf(arg0))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13))

    @override
    @overload
    def box(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(com.badlogic.gdx.math.Matrix4)"""
        super(__MeshBuilder, self).box(arg0)

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def vertex(self, arg0: 'VertexInfo') -> int:
        """public short com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.vertex(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        return int.__wrap(super(__MeshBuilder, self).vertex(arg0))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15), __float.valueOf(arg16))

    @override
    @overload
    def box(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(float,float,float)"""
        super(__MeshBuilder, self).box(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def capsule(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.capsule(float,float,int)"""
        super(__MeshBuilder, self).capsule(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4)

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short,short)"""
        super(__MeshBuilder, self).index(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3))

    @override
    @overload
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cylinder(float,float,float,int)"""
        super(__MeshBuilder, self).cylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def sphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(float,float,float,int,int,float,float,float,float)"""
        super(__MeshBuilder, self).sphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @overload
    def vertex(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2') -> int:
        """public short com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.vertex(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        return int.__wrap(super(__MeshBuilder, self).vertex(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshBuilder()"""
        val = __MeshBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def patch(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: int, arg16: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.patch(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,int)"""
        super(__MeshBuilder, self).patch(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16))

    @override
    @overload
    def setUVRange(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setUVRange(float,float,float,float)"""
        super(__MeshBuilder, self).setUVRange(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def ensureRectangles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureRectangles(int)"""
        super(__MeshBuilder, self).ensureRectangles(__int.valueOf(arg0))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, arg6, __float.valueOf(arg7), __float.valueOf(arg8))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cone(float,float,float,int,float,float)"""
        super(__MeshBuilder, self).cone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def line(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).line(arg0, arg1)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14))

    @override
    @overload
    def rect(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).rect(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def rect(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(__MeshBuilder, self).rect(arg0, arg1, arg2, arg3)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float, arg18: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15), __float.valueOf(arg16), __float.valueOf(arg17), __float.valueOf(arg18))

    @overload
    def part(self, arg0: str, arg1: int, arg2: 'MeshPart') -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.part(java.lang.String,int,com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        return 'model.MeshPart'.__wrap(super(__MeshBuilder, self).part(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def ensureIndices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureIndices(int)"""
        super(__MeshBuilder, self).ensureIndices(__int.valueOf(arg0))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, arg6)

    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getNumIndices()"""
        return int.__wrap(super(MeshBuilder, self).getNumIndices())

    @overload
    def ensureRectangles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureRectangles(int,int)"""
        super(__MeshBuilder, self).ensureRectangles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def line(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(short,short)"""
        super(__MeshBuilder, self).line(__short.valueOf(arg0), __short.valueOf(arg1))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: 'Vector3', arg6: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), arg5, arg6)

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @override
    @overload
    def addMesh(self, arg0: 'float', arg1: 'short'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(float[],short[])"""
        super(__MeshBuilder, self).addMesh(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def vertex(self, *arg0: float) -> int:
        """public short com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.vertex(float...)"""
        return int.__wrap(super(__MeshBuilder, self).vertex(arg0))

    @overload
    def begin(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(long)"""
        super(__MeshBuilder, self).begin(__long.valueOf(arg0))

    @override
    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).rect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14))

    @override
    @overload
    def ensureTriangleIndices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureTriangleIndices(int)"""
        super(__MeshBuilder, self).ensureTriangleIndices(__int.valueOf(arg0))

    @override
    @overload
    def line(self, arg0: 'Vector3', arg1: 'Color', arg2: 'Vector3', arg3: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color)"""
        super(__MeshBuilder, self).line(arg0, arg1, arg2, arg3)

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @overload
    def begin(self, arg0: 'VertexAttributes', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(com.badlogic.gdx.graphics.VertexAttributes,int)"""
        super(__MeshBuilder, self).begin(arg0, __int.valueOf(arg1))

    @override
    @overload
    def ensureCapacity(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureCapacity(int,int)"""
        super(__MeshBuilder, self).ensureCapacity(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getIndices(self, arg0: 'short', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getIndices(short[],int)"""
        super(__MeshBuilder, self).getIndices(arg0, __int.valueOf(arg1))

    @override
    @overload
    def setVertexTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setVertexTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__MeshBuilder, self).setVertexTransform(arg0)

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setColor(float,float,float,float)"""
        super(__MeshBuilder, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setUVRange(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setUVRange(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__MeshBuilder, self).setUVRange(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def begin(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(long,int)"""
        super(__MeshBuilder, self).begin(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def sphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(float,float,float,int,int)"""
        super(__MeshBuilder, self).sphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cone(float,float,float,int)"""
        super(__MeshBuilder, self).cone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @override
    @overload
    def addMesh(self, arg0: 'Mesh', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(com.badlogic.gdx.graphics.Mesh,int,int)"""
        super(__MeshBuilder, self).addMesh(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def ensureTriangles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureTriangles(int,int)"""
        super(__MeshBuilder, self).ensureTriangles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshBuilder()"""
        val = __MeshBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getVertexTransform(self, arg0: 'Matrix4') -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getVertexTransform(com.badlogic.gdx.math.Matrix4)"""
        return 'math.Matrix4'.__wrap(super(__MeshBuilder, self).getVertexTransform(arg0))

    @override
    @overload
    def box(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(float,float,float,float,float,float)"""
        super(__MeshBuilder, self).box(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getMeshPart(self) -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getMeshPart()"""
        return 'model.MeshPart'.__wrap(super(MeshBuilder, self).getMeshPart())

    @override
    @overload
    def triangle(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(short,short,short)"""
        super(__MeshBuilder, self).triangle(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(MeshBuilder, self).getAttributes())

    @override
    @overload
    def ensureVertices(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureVertices(int)"""
        super(__MeshBuilder, self).ensureVertices(__int.valueOf(arg0))

    @override
    @overload
    def index(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short)"""
        super(__MeshBuilder, self).index(__short.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def end(self, arg0: 'Mesh') -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.end(com.badlogic.gdx.graphics.Mesh)"""
        return 'graphics.Mesh'.__wrap(super(__MeshBuilder, self).end(arg0))

    @override
    @overload
    def addMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(__MeshBuilder, self).addMesh(arg0)

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @overload
    def part(self, arg0: str, arg1: int) -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.part(java.lang.String,int)"""
        return 'model.MeshPart'.__wrap(super(__MeshBuilder, self).part(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5, __float.valueOf(arg6), __float.valueOf(arg7))

    @override
    @overload
    def getPrimitiveType(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getPrimitiveType()"""
        return int.__wrap(super(MeshBuilder, self).getPrimitiveType())

    @override
    @overload
    def triangle(self, arg0: 'Vector3', arg1: 'Color', arg2: 'Vector3', arg3: 'Color', arg4: 'Vector3', arg5: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color)"""
        super(__MeshBuilder, self).triangle(arg0, arg1, arg2, arg3, arg4, arg5)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def triangle(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(__MeshBuilder, self).triangle(arg0, arg1, arg2)

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5)

    @staticmethod
    @overload
    def createAttributes(arg0: int) -> 'graphics.VertexAttributes':
        """public static com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.createAttributes(long)"""
        return graphics.VertexAttributes.__wrap(__MeshBuilder.createAttributes(__long.valueOf(arg0)))

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short,short,short,short,short,short)"""
        super(__MeshBuilder, self).index(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __short.valueOf(arg7))

    @override
    @overload
    def triangle(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.triangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).triangle(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def sphere(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(com.badlogic.gdx.math.Matrix4,float,float,float,int,int)"""
        super(__MeshBuilder, self).sphere(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def circle(self, arg0: float, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.circle(float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).circle(__float.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15))

    @override
    @overload
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cylinder(float,float,float,int,float,float)"""
        super(__MeshBuilder, self).cylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def addMesh(self, arg0: 'MeshPart'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        super(__MeshBuilder, self).addMesh(arg0)

    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getNumVertices()"""
        return int.__wrap(super(MeshBuilder, self).getNumVertices())

    @overload
    def end(self) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.end()"""
        return 'graphics.Mesh'.__wrap(super(MeshBuilder, self).end())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.clear()"""
        super(MeshBuilder, self).clear()

    @override
    @overload
    def addMesh(self, arg0: 'float', arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.addMesh(float[],short[],int,int)"""
        super(__MeshBuilder, self).addMesh(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def patch(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.patch(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,int,int)"""
        super(__MeshBuilder, self).patch(arg0, arg1, arg2, arg3, __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short)"""
        super(__MeshBuilder, self).index(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @overload
    def begin(self, arg0: 'VertexAttributes'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.begin(com.badlogic.gdx.graphics.VertexAttributes)"""
        super(__MeshBuilder, self).begin(arg0)

    @override
    @overload
    def cylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.cylinder(float,float,float,int,float,float,boolean)"""
        super(__MeshBuilder, self).cylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __boolean.valueOf(arg6))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,int,float,float,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10))

    @overload
    def ensureTriangles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ensureTriangles(int)"""
        super(__MeshBuilder, self).ensureTriangles(__int.valueOf(arg0))

    @overload
    def getVertices(self, arg0: 'float', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getVertices(float[],int)"""
        super(__MeshBuilder, self).getVertices(arg0, __int.valueOf(arg1))

    @override
    @overload
    def box(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: 'VertexInfo', arg6: 'VertexInfo', arg7: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(__MeshBuilder, self).box(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @override
    @overload
    def lastIndex(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.lastIndex()"""
        return int.__wrap(super(MeshBuilder, self).lastIndex())

    @override
    @overload
    def isVertexTransformationEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.isVertexTransformationEnabled()"""
        return bool.__wrap(super(MeshBuilder, self).isVertexTransformationEnabled())

    @override
    @overload
    def setVertexTransformationEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setVertexTransformationEnabled(boolean)"""
        super(__MeshBuilder, self).setVertexTransformationEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def arrow(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.arrow(float,float,float,float,float,float,float,float,int)"""
        super(__MeshBuilder, self).arrow(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def rect(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.rect(short,short,short,short)"""
        super(__MeshBuilder, self).rect(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3))

    @overload
    def getFloatsPerVertex(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.getFloatsPerVertex()"""
        return int.__wrap(super(MeshBuilder, self).getFloatsPerVertex())

    @override
    @overload
    def index(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short,short,short,short,short,short)"""
        super(__MeshBuilder, self).index(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(float,float,float,float,float,float)"""
        super(__MeshBuilder, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__MeshBuilder, self).setColor(arg0)

    @override
    @overload
    def index(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.index(short)"""
        super(__MeshBuilder, self).index(__short.valueOf(arg0))

    @override
    @overload
    def patch(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.patch(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int)"""
        super(__MeshBuilder, self).patch(arg0, arg1, arg2, arg3, arg4, __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def box(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.box(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__MeshBuilder, self).box(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @override
    @overload
    def line(self, arg0: 'VertexInfo', arg1: 'VertexInfo'):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.line(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        super(__MeshBuilder, self).line(arg0, arg1)

    @override
    @overload
    def sphere(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.sphere(com.badlogic.gdx.math.Matrix4,float,float,float,int,int,float,float,float,float)"""
        super(__MeshBuilder, self).sphere(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshBuilder.ellipse(float,float,float,float,int,float,float,float,float,float,float)"""
        super(__MeshBuilder, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider
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
import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BaseShaderProvider(ABC, __ShaderProvider, ShaderProvider):
    """com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __BaseShaderProvider) -> 'BaseShaderProvider':
        return BaseShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseShaderProvider):
        """
        Dynamic initializer for BaseShaderProvider.
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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(BaseShaderProvider, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider()"""
        val = __BaseShaderProvider()
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
        """public com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider()"""
        val = __BaseShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__BaseShaderProvider, self).getShader(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.ModelBuilder
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.model.MeshPart as __MeshPart
__MeshPart = __MeshPart
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as __MeshPartBuilder
__MeshPartBuilder = __MeshPartBuilder
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder as __ModelBuilder
__ModelBuilder = __ModelBuilder
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
from builtins import int
 
class ModelBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.ModelBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ModelBuilder) -> 'ModelBuilder':
        return ModelBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelBuilder):
        """
        Dynamic initializer for ModelBuilder.
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
    def part(self, arg0: str, arg1: int, arg2: 'VertexAttributes', arg3: 'Material') -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,int,com.badlogic.gdx.graphics.VertexAttributes,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'MeshPartBuilder'.__wrap(super(__ModelBuilder, self).part(arg0, __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createBox(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createBox(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @overload
    def createXYZCoordinates(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createXYZCoordinates(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createXYZCoordinates(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @overload
    def createCapsule(self, arg0: float, arg1: float, arg2: int, arg3: 'Material', arg4: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCapsule(float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCapsule(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.ModelBuilder()"""
        val = __ModelBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int, arg7: float, arg8: float, arg9: float, arg10: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float,float,float)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createSphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10)))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: 'Material', arg7: int, arg8: float, arg9: float, arg10: float, arg11: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float,float,float)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createSphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11)))

    @overload
    def createArrow(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Material', arg3: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createArrow(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createArrow(arg0, arg1, arg2, __long.valueOf(arg3)))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.begin()"""
        super(ModelBuilder, self).begin()

    @overload
    def part(self, arg0: str, arg1: int, arg2: int, arg3: 'Material') -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,int,long,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'MeshPartBuilder'.__wrap(super(__ModelBuilder, self).part(arg0, __int.valueOf(arg1), __long.valueOf(arg2), arg3))

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @overload
    def part(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: 'Material') -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'model.MeshPart'.__wrap(super(__ModelBuilder, self).part(arg0, arg1, __int.valueOf(arg2), arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def end(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.end()"""
        return 'g3d.Model'.__wrap(super(ModelBuilder, self).end())

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int, arg7: float, arg8: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8)))

    @overload
    def manage(self, arg0: 'Disposable'):
        """public void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.manage(com.badlogic.gdx.utils.Disposable)"""
        super(__ModelBuilder, self).manage(arg0)

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: 'Material', arg7: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createSphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7)))

    @overload
    def node(self) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.node()"""
        return 'model.Node'.__wrap(super(ModelBuilder, self).node())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createXYZCoordinates(self, arg0: float, arg1: 'Material', arg2: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createXYZCoordinates(float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createXYZCoordinates(__float.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def createRect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: int, arg16: 'Material', arg17: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createRect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createRect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __int.valueOf(arg15), arg16, __long.valueOf(arg17)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.ModelBuilder()"""
        val = __ModelBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createLineGrid(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createLineGrid(int,int,float,float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createLineGrid(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @overload
    def createRect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: 'Material', arg16: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createRect(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createRect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), arg15, __long.valueOf(arg16)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def createBox(self, arg0: float, arg1: float, arg2: float, arg3: 'Material', arg4: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createBox(float,float,float,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createBox(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @overload
    def createSphere(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createSphere(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createSphere(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int, arg6: float, arg7: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

    @overload
    def part(self, arg0: 'MeshPart', arg1: 'Material'):
        """public void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(com.badlogic.gdx.graphics.g3d.model.MeshPart,com.badlogic.gdx.graphics.g3d.Material)"""
        super(__ModelBuilder, self).part(arg0, arg1)

    @overload
    def createArrow(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int, arg10: 'Material', arg11: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createArrow(float,float,float,float,float,float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createArrow(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10, __long.valueOf(arg11)))

    @overload
    def part(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: int, arg4: int, arg5: 'Material') -> 'model.MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.part(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,int,int,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'model.MeshPart'.__wrap(super(__ModelBuilder, self).part(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @overload
    def node(self, arg0: str, arg1: 'Model') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.node(java.lang.String,com.badlogic.gdx.graphics.g3d.Model)"""
        return 'model.Node'.__wrap(super(__ModelBuilder, self).node(arg0, arg1))

    @overload
    def createCone(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int, arg7: float, arg8: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCone(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Material', arg6: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @overload
    def createCapsule(self, arg0: float, arg1: float, arg2: int, arg3: int, arg4: 'Material', arg5: int) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCapsule(float,float,int,int,com.badlogic.gdx.graphics.g3d.Material,long)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCapsule(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def rebuildReferences(arg0: 'Model'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.rebuildReferences(com.badlogic.gdx.graphics.g3d.Model)"""
        __ModelBuilder.rebuildReferences(arg0)

    @overload
    def createCylinder(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: 'Material', arg5: int, arg6: float, arg7: float) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.utils.ModelBuilder.createCylinder(float,float,float,int,com.badlogic.gdx.graphics.g3d.Material,long,float,float)"""
        return 'g3d.Model'.__wrap(super(__ModelBuilder, self).createCylinder(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.RenderableSorter
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.utils.RenderableSorter as __RenderableSorter
__RenderableSorter = __RenderableSorter
 
class RenderableSorter(ABC):
    """com.badlogic.gdx.graphics.g3d.utils.RenderableSorter"""
 
    @staticmethod
    def __wrap(java_value: __RenderableSorter) -> 'RenderableSorter':
        return RenderableSorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderableSorter):
        """
        Dynamic initializer for RenderableSorter.
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
    def sort(self, arg0: 'Camera', arg1: 'Array'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.RenderableSorter.sort(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.ShapeCache
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.graphics.g3d.utils.ShapeCache as __ShapeCache
__ShapeCache = __ShapeCache
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as __MeshPartBuilder
__MeshPartBuilder = __MeshPartBuilder
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ShapeCache(pygdx.__Disposable, utils.Disposable, graphics.__RenderableProvider, g3d.RenderableProvider):
    """com.badlogic.gdx.graphics.g3d.utils.ShapeCache"""
 
    @staticmethod
    def __wrap(java_value: __ShapeCache) -> 'ShapeCache':
        return ShapeCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShapeCache):
        """
        Dynamic initializer for ShapeCache.
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
        """public com.badlogic.gdx.graphics.g3d.utils.ShapeCache()"""
        val = __ShapeCache()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getWorldTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.ShapeCache.getWorldTransform()"""
        return 'math.Matrix4'.__wrap(super(ShapeCache, self).getWorldTransform())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.utils.ShapeCache.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__ShapeCache, self).getRenderables(arg0, arg1)

    @overload
    def begin(self, arg0: int) -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ShapeCache.begin(int)"""
        return 'MeshPartBuilder'.__wrap(super(__ShapeCache, self).begin(__int.valueOf(arg0)))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.ShapeCache.end()"""
        super(ShapeCache, self).end()

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
        """public com.badlogic.gdx.graphics.g3d.utils.ShapeCache()"""
        val = __ShapeCache()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def begin(self) -> 'MeshPartBuilder':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder com.badlogic.gdx.graphics.g3d.utils.ShapeCache.begin()"""
        return 'MeshPartBuilder'.__wrap(super(ShapeCache, self).begin())

    @overload
    def getMaterial(self) -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.utils.ShapeCache.getMaterial()"""
        return 'g3d.Material'.__wrap(super(ShapeCache, self).getMaterial())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.ShapeCache.dispose()"""
        super(ShapeCache, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'VertexAttributes', arg3: int):
        """public com.badlogic.gdx.graphics.g3d.utils.ShapeCache(int,int,com.badlogic.gdx.graphics.VertexAttributes,int)"""
        val = __ShapeCache(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor as __TextureDescriptor
__TextureDescriptor = __TextureDescriptor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class TextureDescriptor(__Comparable, Comparable):
    """com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor"""
 
    @staticmethod
    def __wrap(java_value: __TextureDescriptor) -> 'TextureDescriptor':
        return TextureDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureDescriptor):
        """
        Dynamic initializer for TextureDescriptor.
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
    def set(self, arg0: 'GLTexture', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: 'TextureWrap', arg4: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.set(T,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__TextureDescriptor, self).set(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.equals(java.lang.Object)"""
        return bool.__wrap(super(__TextureDescriptor, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor()"""
        val = __TextureDescriptor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'GLTexture', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: 'TextureWrap', arg4: 'TextureWrap'):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor(T,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        val = __TextureDescriptor(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'TextureDescriptor') -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.compareTo(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>)"""
        return int.__wrap(super(__TextureDescriptor, self).compareTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'TextureDescriptor'):
        """public <V extends T> void com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.set(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<V>)"""
        super(__TextureDescriptor, self).set(arg0)

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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor.hashCode()"""
        return int.__wrap(super(TextureDescriptor, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'GLTexture'):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor(T)"""
        val = __TextureDescriptor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor()"""
        val = __TextureDescriptor()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureProvider$AssetTextureProvider
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.utils.TextureProvider as __TextureProvider_AssetTextureProvider
__AssetTextureProvider = __TextureProvider_AssetTextureProvider.AssetTextureProvider
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class AssetTextureProvider(__TextureProvider, TextureProvider):
    """com.badlogic.gdx.graphics.g3d.utils.TextureProvider.AssetTextureProvider"""
 
    @staticmethod
    def __wrap(java_value: __AssetTextureProvider) -> 'AssetTextureProvider':
        return AssetTextureProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetTextureProvider):
        """
        Dynamic initializer for AssetTextureProvider.
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
    def load(self, arg0: str) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.utils.TextureProvider$AssetTextureProvider.load(java.lang.String)"""
        return 'graphics.Texture'.__wrap(super(__AssetTextureProvider, self).load(arg0))

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
        val = __AssetTextureProvider(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.utils.TextureProvider as __TextureProvider_FileTextureProvider
__FileTextureProvider = __TextureProvider_FileTextureProvider.FileTextureProvider
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FileTextureProvider(__TextureProvider, TextureProvider):
    """com.badlogic.gdx.graphics.g3d.utils.TextureProvider.FileTextureProvider"""
 
    @staticmethod
    def __wrap(java_value: __FileTextureProvider) -> 'FileTextureProvider':
        return FileTextureProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileTextureProvider):
        """
        Dynamic initializer for FileTextureProvider.
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
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider()"""
        val = __FileTextureProvider()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider()"""
        val = __FileTextureProvider()
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

    @overload
    def load(self, arg0: str) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider.load(java.lang.String)"""
        return 'graphics.Texture'.__wrap(super(__FileTextureProvider, self).load(arg0))

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
    def __init__(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: 'TextureWrap', arg3: 'TextureWrap', arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.utils.TextureProvider$FileTextureProvider(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        val = __FileTextureProvider(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder as __DefaultTextureBinder
__DefaultTextureBinder = __DefaultTextureBinder
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class DefaultTextureBinder(__TextureBinder, TextureBinder):
    """com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder"""
 
    @staticmethod
    def __wrap(java_value: __DefaultTextureBinder) -> 'DefaultTextureBinder':
        return DefaultTextureBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultTextureBinder):
        """
        Dynamic initializer for DefaultTextureBinder.
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
    def bind(self, arg0: 'GLTexture') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.bind(com.badlogic.gdx.graphics.GLTexture)"""
        return int.__wrap(super(__DefaultTextureBinder, self).bind(arg0))

    @override
    @overload
    def getBindCount(self) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.getBindCount()"""
        return int.__wrap(super(DefaultTextureBinder, self).getBindCount())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getReuseCount(self) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.getReuseCount()"""
        return int.__wrap(super(DefaultTextureBinder, self).getReuseCount())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder(int,int,int)"""
        val = __DefaultTextureBinder(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder(int)"""
        val = __DefaultTextureBinder(__int.valueOf(arg0))
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
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.end()"""
        super(DefaultTextureBinder, self).end()

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder(int,int)"""
        val = __DefaultTextureBinder(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def bind(self, arg0: 'TextureDescriptor') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.bind(com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return int.__wrap(super(__DefaultTextureBinder, self).bind(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.DefaultTextureBinder.begin()"""
        super(DefaultTextureBinder, self).begin() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.TextureBinder
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.utils.TextureBinder as __TextureBinder
__TextureBinder = __TextureBinder
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

 
class TextureBinder(ABC):
    """com.badlogic.gdx.graphics.g3d.utils.TextureBinder"""
 
    @staticmethod
    def __wrap(java_value: __TextureBinder) -> 'TextureBinder':
        return TextureBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureBinder):
        """
        Dynamic initializer for TextureBinder.
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController as __BaseAnimationController_Transform
__Transform = __BaseAnimationController_Transform.Transform
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
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
from builtins import int
 
class Transform(pygdx.__Pool_Poolable, utils.Pool$Poolable):
    """com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController.Transform"""
 
    @staticmethod
    def __wrap(java_value: __Transform) -> 'Transform':
        return Transform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Transform):
        """
        Dynamic initializer for Transform.
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.toString()"""
        return str.__wrap(super(Transform, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def toMatrix4(self, arg0: 'Matrix4') -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.toMatrix4(com.badlogic.gdx.math.Matrix4)"""
        return 'math.Matrix4'.__wrap(super(__Transform, self).toMatrix4(arg0))

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

    @overload
    def set(self, arg0: 'Transform') -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.set(com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform)"""
        return 'Transform'.__wrap(super(__Transform, self).set(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform()"""
        val = __Transform()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform()"""
        val = __Transform()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def lerp(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3', arg3: float) -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.lerp(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3,float)"""
        return 'Transform'.__wrap(super(__Transform, self).lerp(arg0, arg1, arg2, __float.valueOf(arg3)))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.reset()"""
        super(Transform, self).reset()

    @overload
    def idt(self) -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.idt()"""
        return 'Transform'.__wrap(super(Transform, self).idt())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def lerp(self, arg0: 'Transform', arg1: float) -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.lerp(com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform,float)"""
        return 'Transform'.__wrap(super(__Transform, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3') -> 'Transform':
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController$Transform.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3)"""
        return 'Transform'.__wrap(super(__Transform, self).set(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.CameraInputController as __CameraInputController_CameraGestureListener
__CameraGestureListener = __CameraInputController_CameraGestureListener.CameraGestureListener
import com.badlogic.gdx.input.GestureDetector as __GestureDetector_GestureAdapter
__GestureAdapter = __GestureDetector_GestureAdapter.GestureAdapter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class CameraGestureListener(pygdx.__GestureDetector_GestureAdapter, input.GestureDetector$GestureAdapter):
    """com.badlogic.gdx.graphics.g3d.utils.CameraInputController.CameraGestureListener"""
 
    @staticmethod
    def __wrap(java_value: __CameraGestureListener) -> 'CameraGestureListener':
        return CameraGestureListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CameraGestureListener):
        """
        Dynamic initializer for CameraGestureListener.
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
    def pinch(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.pinch(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__CameraGestureListener, self).pinch(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def zoom(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.zoom(float,float)"""
        return bool.__wrap(super(__CameraGestureListener, self).zoom(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def fling(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.fling(float,float,int)"""
        return bool.__wrap(super(__CameraGestureListener, self).fling(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def pan(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.pan(float,float,float,float)"""
        return bool.__wrap(super(__CameraGestureListener, self).pan(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def tap(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.tap(float,float,int,int)"""
        return bool.__wrap(super(__CameraGestureListener, self).tap(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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

    @overload
    def panStop(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.panStop(float,float,int,int)"""
        return bool.__wrap(super(__input.GestureDetector$GestureAdapter, self).panStop(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def longPress(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.longPress(float,float)"""
        return bool.__wrap(super(__CameraGestureListener, self).longPress(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController$CameraGestureListener.touchDown(float,float,int,int)"""
        return bool.__wrap(super(__CameraGestureListener, self).touchDown(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider
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

import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider as __DepthShaderProvider
__DepthShaderProvider = __DepthShaderProvider
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class DepthShaderProvider(__BaseShaderProvider, BaseShaderProvider):
    """com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __DepthShaderProvider) -> 'DepthShaderProvider':
        return DepthShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DepthShaderProvider):
        """
        Dynamic initializer for DepthShaderProvider.
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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(BaseShaderProvider, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DepthShader$Config)"""
        val = __DepthShaderProvider(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider(java.lang.String,java.lang.String)"""
        val = __DepthShaderProvider(arg0, arg1)
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
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __DepthShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__BaseShaderProvider, self).getShader(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider()"""
        val = __DepthShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.DepthShaderProvider()"""
        val = __DepthShaderProvider()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController as __BaseAnimationController
__BaseAnimationController = __BaseAnimationController
from builtins import int
 
class BaseAnimationController():
    """com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController"""
 
    @staticmethod
    def __wrap(java_value: __BaseAnimationController) -> 'BaseAnimationController':
        return BaseAnimationController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseAnimationController):
        """
        Dynamic initializer for BaseAnimationController.
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
    def __init__(self, arg0: 'ModelInstance'):
        """public com.badlogic.gdx.graphics.g3d.utils.BaseAnimationController(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = __BaseAnimationController(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController
__AnimationController = __AnimationController
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController_AnimationDesc
__AnimationDesc = __AnimationController_AnimationDesc.AnimationDesc
from builtins import bool
from builtins import int
 
class AnimationController(__BaseAnimationController, BaseAnimationController):
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController"""
 
    @staticmethod
    def __wrap(java_value: __AnimationController) -> 'AnimationController':
        return AnimationController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnimationController):
        """
        Dynamic initializer for AnimationController.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).setAnimation(arg0, __int.valueOf(arg1), arg2))

    @overload
    def queue(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.queue(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).queue(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def animate(self, arg0: str, arg1: 'AnimationListener', arg2: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).animate(arg0, arg1, __float.valueOf(arg2)))

    @overload
    def setAnimation(self, arg0: str) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).setAnimation(arg0))

    @overload
    def action(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.action(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).action(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __float.valueOf(arg6)))

    @overload
    def setAnimation(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).setAnimation(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def animate(self, arg0: str, arg1: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).animate(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ModelInstance'):
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = __AnimationController(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setAnimation(self, arg0: str, arg1: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).setAnimation(arg0, arg1))

    @overload
    def setAnimation(self, arg0: str, arg1: int) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,int)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).setAnimation(arg0, __int.valueOf(arg1)))

    @overload
    def animate(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).animate(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __float.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def animate(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).animate(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def action(self, arg0: str, arg1: int, arg2: float, arg3: 'AnimationListener', arg4: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.action(java.lang.String,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).action(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.AnimationController.update(float)"""
        super(__AnimationController, self).update(__float.valueOf(arg0))

    @overload
    def setAnimation(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener') -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.setAnimation(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).setAnimation(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5))

    @overload
    def queue(self, arg0: str, arg1: float, arg2: float, arg3: int, arg4: float, arg5: 'AnimationListener', arg6: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.queue(java.lang.String,float,float,int,float,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).queue(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __float.valueOf(arg6)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def animate(self, arg0: str, arg1: int, arg2: 'AnimationListener', arg3: float) -> 'AnimationDesc':
        """public com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc com.badlogic.gdx.graphics.g3d.utils.AnimationController.animate(java.lang.String,int,com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationListener,float)"""
        return 'AnimationDesc'.__wrap(super(__AnimationController, self).animate(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3))) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as __MeshPartBuilder
__MeshPartBuilder = __MeshPartBuilder
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

from builtins import float
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class MeshPartBuilder(ABC):
    """com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder"""
 
    @staticmethod
    def __wrap(java_value: __MeshPartBuilder) -> 'MeshPartBuilder':
        return MeshPartBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MeshPartBuilder):
        """
        Dynamic initializer for MeshPartBuilder.
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
    def circle(self, arg0: float, arg1: int, arg2: 'Vector3', arg3: 'Vector3', arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.circle(float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        pass

    @abstractmethod
    def rect(self, arg0: 'VertexInfo', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo'):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.rect(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
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
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.cone(float,float,float,int)"""
        pass

    @abstractmethod
    def rect(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.rect(short,short,short,short)"""
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.AnimationController$AnimationDesc
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
import com.badlogic.gdx.graphics.g3d.utils.AnimationController as __AnimationController_AnimationDesc
__AnimationDesc = __AnimationController_AnimationDesc.AnimationDesc
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AnimationDesc():
    """com.badlogic.gdx.graphics.g3d.utils.AnimationController.AnimationDesc"""
 
    @staticmethod
    def __wrap(java_value: __AnimationDesc) -> 'AnimationDesc':
        return AnimationDesc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnimationDesc):
        """
        Dynamic initializer for AnimationDesc.
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.RenderContext
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
import com.badlogic.gdx.graphics.g3d.utils.RenderContext as __RenderContext
__RenderContext = __RenderContext
from builtins import int
 
class RenderContext():
    """com.badlogic.gdx.graphics.g3d.utils.RenderContext"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setBlending(self, arg0: bool, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setBlending(boolean,int,int)"""
        super(__RenderContext, self).setBlending(__boolean.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDepthTest(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setDepthTest(int)"""
        super(__RenderContext, self).setDepthTest(__int.valueOf(arg0))

    @overload
    def setDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setDepthMask(boolean)"""
        super(__RenderContext, self).setDepthMask(__boolean.valueOf(arg0))

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

    @overload
    def __init__(self, arg0: 'TextureBinder'):
        """public com.badlogic.gdx.graphics.g3d.utils.RenderContext(com.badlogic.gdx.graphics.g3d.utils.TextureBinder)"""
        val = __RenderContext(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.end()"""
        super(RenderContext, self).end()

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
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.begin()"""
        super(RenderContext, self).begin()

    @overload
    def setDepthTest(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setDepthTest(int,float,float)"""
        super(__RenderContext, self).setDepthTest(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.utils.RenderContext.setCullFace(int)"""
        super(__RenderContext, self).setCullFace(__int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.CameraInputController
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.CameraInputController as __CameraInputController
__CameraInputController = __CameraInputController
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.InputAdapter as __InputAdapter
__InputAdapter = __InputAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.input.GestureDetector as __GestureDetector
__GestureDetector = __GestureDetector
from builtins import int
 
class CameraInputController(pygdx.__GestureDetector, input.GestureDetector):
    """com.badlogic.gdx.graphics.g3d.utils.CameraInputController"""
 
    @staticmethod
    def __wrap(java_value: __CameraInputController) -> 'CameraInputController':
        return CameraInputController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CameraInputController):
        """
        Dynamic initializer for CameraInputController.
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
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__CameraInputController, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def setInvertedControls(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.utils.CameraInputController.setInvertedControls(boolean)"""
        super(__CameraInputController, self).setInvertedControls(__boolean.valueOf(arg0))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.keyDown(int)"""
        return bool.__wrap(super(__CameraInputController, self).keyDown(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def touchDragged(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(float,float,int)"""
        return bool.__wrap(super(__input.GestureDetector, self).touchDragged(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__input.GestureDetector, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__CameraInputController, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(float,float,int,int)"""
        return bool.__wrap(super(__input.GestureDetector, self).touchDown(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxFlingDelay(self, arg0: int):
        """public void com.badlogic.gdx.input.GestureDetector.setMaxFlingDelay(long)"""
        super(__input.GestureDetector, self).setMaxFlingDelay(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.input.GestureDetector.reset()"""
        super(input.GestureDetector, self).reset()

    @override
    @overload
    def isLongPressed(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed()"""
        return bool.__wrap(super(input.GestureDetector, self).isLongPressed())

    @overload
    def zoom(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.zoom(float)"""
        return bool.__wrap(super(__CameraInputController, self).zoom(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isPanning(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isPanning()"""
        return bool.__wrap(super(input.GestureDetector, self).isPanning())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.scrolled(float,float)"""
        return bool.__wrap(super(__CameraInputController, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.keyUp(int)"""
        return bool.__wrap(super(__CameraInputController, self).keyUp(__int.valueOf(arg0)))

    @override
    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapCountInterval(float)"""
        super(__input.GestureDetector, self).setTapCountInterval(__float.valueOf(arg0))

    @overload
    def isLongPressed(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed(float)"""
        return bool.__wrap(super(__input.GestureDetector, self).isLongPressed(__float.valueOf(arg0)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.CameraInputController.touchDragged(int,int,int)"""
        return bool.__wrap(super(__CameraInputController, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapSquareSize(float)"""
        super(__input.GestureDetector, self).setTapSquareSize(__float.valueOf(arg0))

    @override
    @overload
    def setTapRectangleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapRectangleSize(float,float)"""
        super(__input.GestureDetector, self).setTapRectangleSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.CameraInputController.update()"""
        super(CameraInputController, self).update()

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
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setLongPressSeconds(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setLongPressSeconds(float)"""
        super(__input.GestureDetector, self).setLongPressSeconds(__float.valueOf(arg0))

    @overload
    def touchUp(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(float,float,int,int)"""
        return bool.__wrap(super(__input.GestureDetector, self).touchUp(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.graphics.g3d.utils.CameraInputController(com.badlogic.gdx.graphics.Camera)"""
        val = __CameraInputController(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider as __BaseShaderProvider
__BaseShaderProvider = __BaseShaderProvider
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider as __DefaultShaderProvider
__DefaultShaderProvider = __DefaultShaderProvider
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
 
class DefaultShaderProvider(__BaseShaderProvider, BaseShaderProvider):
    """com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider"""
 
    @staticmethod
    def __wrap(java_value: __DefaultShaderProvider) -> 'DefaultShaderProvider':
        return DefaultShaderProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultShaderProvider):
        """
        Dynamic initializer for DefaultShaderProvider.
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
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider(java.lang.String,java.lang.String)"""
        val = __DefaultShaderProvider(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider(com.badlogic.gdx.graphics.g3d.shaders.DefaultShader$Config)"""
        val = __DefaultShaderProvider(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.dispose()"""
        super(BaseShaderProvider, self).dispose()

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
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __DefaultShaderProvider(arg0, arg1)
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider()"""
        val = __DefaultShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getShader(self, arg0: 'Renderable') -> 'g3d.Shader':
        """public com.badlogic.gdx.graphics.g3d.Shader com.badlogic.gdx.graphics.g3d.utils.BaseShaderProvider.getShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Shader'.__wrap(super(__BaseShaderProvider, self).getShader(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.DefaultShaderProvider()"""
        val = __DefaultShaderProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as __MeshPartBuilder_VertexInfo
__VertexInfo = __MeshPartBuilder_VertexInfo.VertexInfo
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class VertexInfo(pygdx.__Pool_Poolable, utils.Pool$Poolable):
    """com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.VertexInfo"""
 
    @staticmethod
    def __wrap(java_value: __VertexInfo) -> 'VertexInfo':
        return VertexInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexInfo):
        """
        Dynamic initializer for VertexInfo.
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
    def setCol(self, arg0: 'Color') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setCol(com.badlogic.gdx.graphics.Color)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setCol(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: 'VertexInfo') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.set(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).set(arg0))

    @overload
    def lerp(self, arg0: 'VertexInfo', arg1: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.lerp(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,float)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def setCol(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setCol(float,float,float,float)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setCol(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo()"""
        val = __VertexInfo()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.reset()"""
        super(VertexInfo, self).reset()

    @overload
    def setUV(self, arg0: float, arg1: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setUV(float,float)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setUV(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPos(self, arg0: float, arg1: float, arg2: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setPos(float,float,float)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setPos(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo()"""
        val = __VertexInfo()
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

    @overload
    def setNor(self, arg0: float, arg1: float, arg2: float) -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setNor(float,float,float)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setNor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).set(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setNor(self, arg0: 'Vector3') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setNor(com.badlogic.gdx.math.Vector3)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setNor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setUV(self, arg0: 'Vector2') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setUV(com.badlogic.gdx.math.Vector2)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setUV(arg0))

    @overload
    def setPos(self, arg0: 'Vector3') -> 'VertexInfo':
        """public com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.setPos(com.badlogic.gdx.math.Vector3)"""
        return 'VertexInfo'.__wrap(super(__VertexInfo, self).setPos(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.InputAdapter as __InputAdapter
__InputAdapter = __InputAdapter
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController as __FirstPersonCameraController
__FirstPersonCameraController = __FirstPersonCameraController
from builtins import int
 
class FirstPersonCameraController(pygdx.__InputAdapter, pygdx.InputAdapter):
    """com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController"""
 
    @staticmethod
    def __wrap(java_value: __FirstPersonCameraController) -> 'FirstPersonCameraController':
        return FirstPersonCameraController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FirstPersonCameraController):
        """
        Dynamic initializer for FirstPersonCameraController.
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
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.keyUp(int)"""
        return bool.__wrap(super(__FirstPersonCameraController, self).keyUp(__int.valueOf(arg0)))

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
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.touchDragged(int,int,int)"""
        return bool.__wrap(super(__FirstPersonCameraController, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDegreesPerPixel(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.setDegreesPerPixel(float)"""
        super(__FirstPersonCameraController, self).setDegreesPerPixel(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController(com.badlogic.gdx.graphics.Camera)"""
        val = __FirstPersonCameraController(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setVelocity(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.setVelocity(float)"""
        super(__FirstPersonCameraController, self).setVelocity(__float.valueOf(arg0))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.keyDown(int)"""
        return bool.__wrap(super(__FirstPersonCameraController, self).keyDown(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.update(float)"""
        super(__FirstPersonCameraController, self).update(__float.valueOf(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.FirstPersonCameraController.update()"""
        super(FirstPersonCameraController, self).update()