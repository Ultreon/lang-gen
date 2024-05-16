from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch as _PolygonSpriteBatch
_PolygonSpriteBatch = _PolygonSpriteBatch
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

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
 
class PolygonSpriteBatch():
    """com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch"""
 
    @staticmethod
    def _wrap(java_value: _PolygonSpriteBatch) -> 'PolygonSpriteBatch':
        return PolygonSpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonSpriteBatch):
        """
        Dynamic initializer for PolygonSpriteBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonSpriteBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonSpriteBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.begin()"""
        super(PolygonSpriteBatch, self).begin()

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.enableBlending()"""
        super(PolygonSpriteBatch, self).enableBlending()

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setBlendFunction(int,int)"""
        super(_PolygonSpriteBatch, self).setBlendFunction(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getColor()"""
        return 'graphics.Color'._wrap(super(PolygonSpriteBatch, self).getColor())

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendSrcFunc()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendSrcFunc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _boolean.valueOf(arg14), _boolean.valueOf(arg15))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.flush()"""
        super(PolygonSpriteBatch, self).flush()

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
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getPackedColor()"""
        return float._wrap(super(PolygonSpriteBatch, self).getPackedColor())

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_PolygonSpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.disableBlending()"""
        super(PolygonSpriteBatch, self).disableBlending()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendSrcFuncAlpha()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendSrcFuncAlpha())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setColor(float,float,float,float)"""
        super(_PolygonSpriteBatch, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(_PolygonSpriteBatch, self).setBlendFunctionSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int,int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _PolygonSpriteBatch(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.dispose()"""
        super(PolygonSpriteBatch, self).dispose()

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.isDrawing()"""
        return bool._wrap(super(PolygonSpriteBatch, self).isDrawing())

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _PolygonSpriteBatch(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch()"""
        val = _PolygonSpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendDstFunc()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendDstFunc())

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'._wrap(super(PolygonSpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch()"""
        val = _PolygonSpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(_PolygonSpriteBatch, self).draw(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_PolygonSpriteBatch, self).setColor(arg0)

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendDstFuncAlpha()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendDstFuncAlpha())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int,short[],int,int)"""
        super(_PolygonSpriteBatch, self).draw(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.isBlendingEnabled()"""
        return bool._wrap(super(PolygonSpriteBatch, self).isBlendingEnabled())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int)"""
        val = _PolygonSpriteBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_PolygonSpriteBatch, self).setShader(arg0)

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setPackedColor(float)"""
        super(_PolygonSpriteBatch, self).setPackedColor(_float.valueOf(arg0))

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'._wrap(super(PolygonSpriteBatch, self).getShader())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.end()"""
        super(PolygonSpriteBatch, self).end()

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_PolygonSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float,float,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'._wrap(super(PolygonSpriteBatch, self).getProjectionMatrix())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch as _PolygonSpriteBatch
_PolygonSpriteBatch = _PolygonSpriteBatch
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

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
 
class PolygonSpriteBatch():
    """com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch"""
 
    @staticmethod
    def _wrap(java_value: _PolygonSpriteBatch) -> 'PolygonSpriteBatch':
        return PolygonSpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonSpriteBatch):
        """
        Dynamic initializer for PolygonSpriteBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonSpriteBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonSpriteBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.begin()"""
        super(PolygonSpriteBatch, self).begin()

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.enableBlending()"""
        super(PolygonSpriteBatch, self).enableBlending()

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setBlendFunction(int,int)"""
        super(_PolygonSpriteBatch, self).setBlendFunction(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getColor()"""
        return 'graphics.Color'._wrap(super(PolygonSpriteBatch, self).getColor())

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendSrcFunc()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendSrcFunc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _boolean.valueOf(arg14), _boolean.valueOf(arg15))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.flush()"""
        super(PolygonSpriteBatch, self).flush()

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
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getPackedColor()"""
        return float._wrap(super(PolygonSpriteBatch, self).getPackedColor())

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_PolygonSpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.disableBlending()"""
        super(PolygonSpriteBatch, self).disableBlending()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendSrcFuncAlpha()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendSrcFuncAlpha())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setColor(float,float,float,float)"""
        super(_PolygonSpriteBatch, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(_PolygonSpriteBatch, self).setBlendFunctionSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int,int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _PolygonSpriteBatch(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.dispose()"""
        super(PolygonSpriteBatch, self).dispose()

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.isDrawing()"""
        return bool._wrap(super(PolygonSpriteBatch, self).isDrawing())

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _PolygonSpriteBatch(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch()"""
        val = _PolygonSpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendDstFunc()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendDstFunc())

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'._wrap(super(PolygonSpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch()"""
        val = _PolygonSpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(_PolygonSpriteBatch, self).draw(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_PolygonSpriteBatch, self).setColor(arg0)

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendDstFuncAlpha()"""
        return int._wrap(super(PolygonSpriteBatch, self).getBlendDstFuncAlpha())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int,short[],int,int)"""
        super(_PolygonSpriteBatch, self).draw(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.isBlendingEnabled()"""
        return bool._wrap(super(PolygonSpriteBatch, self).isBlendingEnabled())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int)"""
        val = _PolygonSpriteBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_PolygonSpriteBatch, self).setShader(arg0)

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setPackedColor(float)"""
        super(_PolygonSpriteBatch, self).setPackedColor(_float.valueOf(arg0))

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'._wrap(super(PolygonSpriteBatch, self).getShader())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.end()"""
        super(PolygonSpriteBatch, self).end()

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_PolygonSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float,float,float,float,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(_PolygonSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'._wrap(super(PolygonSpriteBatch, self).getProjectionMatrix())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_AtlasSprite
_AtlasSprite = _TextureAtlas_AtlasSprite.AtlasSprite
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_AtlasRegion
_AtlasRegion = _TextureAtlas_AtlasRegion.AtlasRegion
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g2d.Sprite as _Sprite
_Sprite = _Sprite
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtlasSprite():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.AtlasSprite"""
 
    @staticmethod
    def _wrap(java_value: _AtlasSprite) -> 'AtlasSprite':
        return AtlasSprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtlasSprite):
        """
        Dynamic initializer for AtlasSprite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtlasSprite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtlasSprite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getOriginX()"""
        return float._wrap(super(AtlasSprite, self).getOriginX())

    @override
    @overload
    def rotate90(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.rotate90(boolean)"""
        super(_AtlasSprite, self).rotate90(_boolean.valueOf(arg0))

    @override
    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setAlpha(float)"""
        super(_Sprite, self).setAlpha(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_Sprite, self).draw(arg0)

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(_TextureRegion, self).setRegionY(_int.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(_TextureRegion, self).setRegion(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

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
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate(float)"""
        super(_Sprite, self).rotate(_float.valueOf(arg0))

    @override
    @overload
    def setCenterX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterX(float)"""
        super(_Sprite, self).setCenterX(_float.valueOf(arg0))

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scroll(float,float)"""
        super(_Sprite, self).scroll(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'._wrap(super(TextureRegion, self).getTexture())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setCenterY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterY(float)"""
        super(_Sprite, self).setCenterY(_float.valueOf(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getX()"""
        return float._wrap(super(AtlasSprite, self).getX())

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int._wrap(super(TextureRegion, self).getRegionX())

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getWidth()"""
        return float._wrap(super(AtlasSprite, self).getWidth())

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float._wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int._wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getRotation()"""
        return float._wrap(super(Sprite, self).getRotation())

    @overload
    def getWidthRatio(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getWidthRatio()"""
        return float._wrap(super(AtlasSprite, self).getWidthRatio())

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getY()"""
        return float._wrap(super(AtlasSprite, self).getY())

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(_TextureRegion, self).setRegionX(_int.valueOf(arg0))

    @overload
    def getHeightRatio(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getHeightRatio()"""
        return float._wrap(super(AtlasSprite, self).getHeightRatio())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.toString()"""
        return str._wrap(super(AtlasSprite, self).toString())

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int._wrap(super(TextureRegion, self).getRegionWidth())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(_TextureRegion, self).setRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPackedColor(float)"""
        super(_Sprite, self).setPackedColor(_float.valueOf(arg0))

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.flip(boolean,boolean)"""
        super(_AtlasSprite, self).flip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.Sprite.getBoundingRectangle()"""
        return 'math.Rectangle'._wrap(super(Sprite, self).getBoundingRectangle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'AtlasSprite'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite(com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite)"""
        val = _AtlasSprite(arg0)
        self.__wrapper = val

    @override
    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateY(float)"""
        super(_Sprite, self).translateY(_float.valueOf(arg0))

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU(float)"""
        super(_Sprite, self).setU(_float.valueOf(arg0))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float._wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float)"""
        super(_Sprite, self).setScale(_float.valueOf(arg0))

    @overload
    def getAtlasRegion(self) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getAtlasRegion()"""
        return 'AtlasRegion'._wrap(super(AtlasSprite, self).getAtlasRegion())

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getHeight()"""
        return float._wrap(super(AtlasSprite, self).getHeight())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Sprite, self).setColor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool._wrap(super(TextureRegion, self).isFlipY())

    @override
    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translate(float,float)"""
        super(_Sprite, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU2(float)"""
        super(_Sprite, self).setU2(_float.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setPosition(float,float)"""
        super(_AtlasSprite, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateX(float)"""
        super(_Sprite, self).translateX(_float.valueOf(arg0))

    @override
    @overload
    def setCenter(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenter(float,float)"""
        super(_Sprite, self).setCenter(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.set(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(_Sprite, self).set(arg0)

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRegion(float,float,float,float)"""
        super(_Sprite, self).setRegion(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float._wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float,float)"""
        super(_Sprite, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setOriginCenter(self):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setOriginCenter()"""
        super(AtlasSprite, self).setOriginCenter()

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_Sprite, self).draw(arg0, _float.valueOf(arg1))

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleX()"""
        return float._wrap(super(Sprite, self).getScaleX())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRotation(float)"""
        super(_Sprite, self).setRotation(_float.valueOf(arg0))

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float._wrap(super(TextureRegion, self).getV2())

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scale(float)"""
        super(_Sprite, self).scale(_float.valueOf(arg0))

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(_TextureRegion, self).setRegionWidth(_int.valueOf(arg0))

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int._wrap(super(TextureRegion, self).getRegionHeight())

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setSize(float,float)"""
        super(_AtlasSprite, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setOrigin(float,float)"""
        super(_AtlasSprite, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setFlip(boolean,boolean)"""
        super(_Sprite, self).setFlip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setBounds(float,float,float,float)"""
        super(_AtlasSprite, self).setBounds(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(float,float,float,float)"""
        super(_Sprite, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setX(float)"""
        super(_AtlasSprite, self).setX(_float.valueOf(arg0))

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]]._wrap(_TextureRegion.split(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setY(float)"""
        super(_AtlasSprite, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV(float)"""
        super(_Sprite, self).setV(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Sprite.getColor()"""
        return 'graphics.Color'._wrap(super(Sprite, self).getColor())

    @overload
    def __init__(self, arg0: 'AtlasRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite(com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion)"""
        val = _AtlasSprite(arg0)
        self.__wrapper = val

    @override
    @overload
    def setOriginBasedPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginBasedPosition(float,float)"""
        super(_Sprite, self).setOriginBasedPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']]._wrap(super(_TextureRegion, self).split(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool._wrap(super(TextureRegion, self).isFlipX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.Sprite.getVertices()"""
        return List[float]._wrap(super(Sprite, self).getVertices())

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV2(float)"""
        super(_Sprite, self).setV2(_float.valueOf(arg0))

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getOriginY()"""
        return float._wrap(super(AtlasSprite, self).getOriginY())

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleY()"""
        return float._wrap(super(Sprite, self).getScaleY())

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(_TextureRegion, self).setRegionHeight(_int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.ObjectSet as _ObjectSet
_ObjectSet = _ObjectSet
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_AtlasRegion
_AtlasRegion = _TextureAtlas_AtlasRegion.AtlasRegion
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g2d.Sprite as _Sprite
_Sprite = _Sprite
import com.badlogic.gdx.graphics.g2d.NinePatch as _NinePatch
_NinePatch = _NinePatch
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureAtlas():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlas) -> 'TextureAtlas':
        return TextureAtlas(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlas):
        """
        Dynamic initializer for TextureAtlas.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlas__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlas__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createSprites(self, arg0: str) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprites(java.lang.String)"""
        return 'utils.Array'._wrap(super(_TextureAtlas, self).createSprites(arg0))

    @overload
    def createSprite(self, arg0: str) -> 'Sprite':
        """public com.badlogic.gdx.graphics.g2d.Sprite com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprite(java.lang.String)"""
        return 'Sprite'._wrap(super(_TextureAtlas, self).createSprite(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def findRegion(self, arg0: str) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.findRegion(java.lang.String)"""
        return 'AtlasRegion'._wrap(super(_TextureAtlas, self).findRegion(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _TextureAtlas(arg0, _boolean.valueOf(arg1))
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
    def findRegion(self, arg0: str, arg1: int) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.findRegion(java.lang.String,int)"""
        return 'AtlasRegion'._wrap(super(_TextureAtlas, self).findRegion(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle)"""
        val = _TextureAtlas(arg0)
        self.__wrapper = val

    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion> com.badlogic.gdx.graphics.g2d.TextureAtlas.getRegions()"""
        return 'utils.Array'._wrap(super(TextureAtlas, self).getRegions())

    @overload
    def createSprites(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprites()"""
        return 'utils.Array'._wrap(super(TextureAtlas, self).createSprites())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _TextureAtlas(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def load(self, arg0: 'TextureAtlasData'):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas.load(com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData)"""
        super(_TextureAtlas, self).load(arg0)

    @overload
    def createSprite(self, arg0: str, arg1: int) -> 'Sprite':
        """public com.badlogic.gdx.graphics.g2d.Sprite com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprite(java.lang.String,int)"""
        return 'Sprite'._wrap(super(_TextureAtlas, self).createSprite(arg0, _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas.dispose()"""
        super(TextureAtlas, self).dispose()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _TextureAtlas(arg0, arg1)
        self.__wrapper = val

    @overload
    def getTextures(self) -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g2d.TextureAtlas.getTextures()"""
        return 'utils.ObjectSet'._wrap(super(TextureAtlas, self).getTextures())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas()"""
        val = _TextureAtlas()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas()"""
        val = _TextureAtlas()
        self.__wrapper = val

    @overload
    def addRegion(self, arg0: str, arg1: 'TextureRegion') -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.addRegion(java.lang.String,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'AtlasRegion'._wrap(super(_TextureAtlas, self).addRegion(arg0, arg1))

    @overload
    def findRegions(self, arg0: str) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion> com.badlogic.gdx.graphics.g2d.TextureAtlas.findRegions(java.lang.String)"""
        return 'utils.Array'._wrap(super(_TextureAtlas, self).findRegions(arg0))

    @overload
    def createPatch(self, arg0: str) -> 'NinePatch':
        """public com.badlogic.gdx.graphics.g2d.NinePatch com.badlogic.gdx.graphics.g2d.TextureAtlas.createPatch(java.lang.String)"""
        return 'NinePatch'._wrap(super(_TextureAtlas, self).createPatch(arg0))

    @overload
    def addRegion(self, arg0: str, arg1: 'Texture', arg2: int, arg3: int, arg4: int, arg5: int) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.addRegion(java.lang.String,com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        return 'AtlasRegion'._wrap(super(_TextureAtlas, self).addRegion(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(java.lang.String)"""
        val = _TextureAtlas(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TextureAtlasData'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData)"""
        val = _TextureAtlas(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_TextureAtlasData_Page
_Page = _TextureAtlas_TextureAtlasData_Page.TextureAtlasData.Page
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Page():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.TextureAtlasData.Page"""
 
    @staticmethod
    def _wrap(java_value: _Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Page):
        """
        Dynamic initializer for Page.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Page__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Page__wrapper":
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
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page()"""
        val = _Page()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page()"""
        val = _Page()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.SpriteBatch
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g2d.SpriteBatch as _SpriteBatch
_SpriteBatch = _SpriteBatch
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

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
 
class SpriteBatch():
    """com.badlogic.gdx.graphics.g2d.SpriteBatch"""
 
    @staticmethod
    def _wrap(java_value: _SpriteBatch) -> 'SpriteBatch':
        return SpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpriteBatch):
        """
        Dynamic initializer for SpriteBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpriteBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpriteBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _boolean.valueOf(arg14), _boolean.valueOf(arg15))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(float,float,float,float)"""
        super(_SpriteBatch, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.SpriteBatch.getPackedColor()"""
        return float._wrap(super(SpriteBatch, self).getPackedColor())

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(_SpriteBatch, self).setBlendFunctionSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

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
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setPackedColor(float)"""
        super(_SpriteBatch, self).setPackedColor(_float.valueOf(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.end()"""
        super(SpriteBatch, self).end()

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.disableBlending()"""
        super(SpriteBatch, self).disableBlending()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_SpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFunc()"""
        return int._wrap(super(SpriteBatch, self).getBlendDstFunc())

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_SpriteBatch, self).setShader(arg0)

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFunc()"""
        return int._wrap(super(SpriteBatch, self).getBlendSrcFunc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'._wrap(super(SpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.flush()"""
        super(SpriteBatch, self).flush()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_SpriteBatch, self).setColor(arg0)

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFuncAlpha()"""
        return int._wrap(super(SpriteBatch, self).getBlendDstFuncAlpha())

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFuncAlpha()"""
        return int._wrap(super(SpriteBatch, self).getBlendSrcFuncAlpha())

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.enableBlending()"""
        super(SpriteBatch, self).enableBlending()

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _SpriteBatch(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(_SpriteBatch, self).draw(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.SpriteBatch.getColor()"""
        return 'graphics.Color'._wrap(super(SpriteBatch, self).getColor())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch()"""
        val = _SpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunction(int,int)"""
        super(_SpriteBatch, self).setBlendFunction(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch()"""
        val = _SpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_SpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isDrawing()"""
        return bool._wrap(super(SpriteBatch, self).isDrawing())

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'._wrap(super(SpriteBatch, self).getShader())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch(int)"""
        val = _SpriteBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.begin()"""
        super(SpriteBatch, self).begin()

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_SpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.dispose()"""
        super(SpriteBatch, self).dispose()

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'._wrap(super(SpriteBatch, self).getProjectionMatrix())

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isBlendingEnabled()"""
        return bool._wrap(super(SpriteBatch, self).isBlendingEnabled())

    @staticmethod
    @overload
    def createDefaultShader() -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.createDefaultShader()"""
        return glutils.ShaderProgram._wrap(_SpriteBatch.createDefaultShader()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker
_PixmapPacker = _PixmapPacker
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_Page
_Page = _PixmapPacker_Page.Page
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
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
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapPacker():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker"""
 
    @staticmethod
    def _wrap(java_value: _PixmapPacker) -> 'PixmapPacker':
        return PixmapPacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapPacker):
        """
        Dynamic initializer for PixmapPacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapPacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapPacker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setTransparentColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setTransparentColor(com.badlogic.gdx.graphics.Color)"""
        super(_PixmapPacker, self).setTransparentColor(arg0)

    @overload
    def setPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPageWidth(int)"""
        super(_PixmapPacker, self).setPageWidth(_int.valueOf(arg0))

    @overload
    def getPackToTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PixmapPacker.getPackToTexture()"""
        return bool._wrap(super(PixmapPacker, self).getPackToTexture())

    @overload
    def getTransparentColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PixmapPacker.getTransparentColor()"""
        return 'graphics.Color'._wrap(super(PixmapPacker, self).getTransparentColor())

    @overload
    def updateTextureAtlas(self, arg0: 'TextureAtlas', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: bool, arg4: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updateTextureAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean,boolean)"""
        super(_PixmapPacker, self).updateTextureAtlas(arg0, arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPageFormat(self, arg0: 'Format'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPageFormat(com.badlogic.gdx.graphics.Pixmap$Format)"""
        super(_PixmapPacker, self).setPageFormat(arg0)

    @overload
    def sort(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        super(_PixmapPacker, self).sort(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPageHeight(int)"""
        super(_PixmapPacker, self).setPageHeight(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getPages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.PixmapPacker$Page> com.badlogic.gdx.graphics.g2d.PixmapPacker.getPages()"""
        return 'utils.Array'._wrap(super(PixmapPacker, self).getPages())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format', arg3: int, arg4: bool):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker(int,int,com.badlogic.gdx.graphics.Pixmap$Format,int,boolean)"""
        val = _PixmapPacker(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @overload
    def getPageIndex(self, arg0: str) -> int:
        """public synchronized int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageIndex(java.lang.String)"""
        return int._wrap(super(_PixmapPacker, self).getPageIndex(arg0))

    @overload
    def setDuplicateBorder(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setDuplicateBorder(boolean)"""
        super(_PixmapPacker, self).setDuplicateBorder(_boolean.valueOf(arg0))

    @overload
    def getDuplicateBorder(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PixmapPacker.getDuplicateBorder()"""
        return bool._wrap(super(PixmapPacker, self).getDuplicateBorder())

    @overload
    def getPageHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageHeight()"""
        return int._wrap(super(PixmapPacker, self).getPageHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getPageWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageWidth()"""
        return int._wrap(super(PixmapPacker, self).getPageWidth())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format', arg3: int, arg4: bool, arg5: bool, arg6: bool, arg7: 'PackStrategy'):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker(int,int,com.badlogic.gdx.graphics.Pixmap$Format,int,boolean,boolean,boolean,com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy)"""
        val = _PixmapPacker(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5), _boolean.valueOf(arg6), arg7)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format', arg3: int, arg4: bool, arg5: 'PackStrategy'):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker(int,int,com.badlogic.gdx.graphics.Pixmap$Format,int,boolean,com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy)"""
        val = _PixmapPacker(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _boolean.valueOf(arg4), arg5)
        self.__wrapper = val

    @overload
    def pack(self, arg0: 'Pixmap') -> 'math.Rectangle':
        """public synchronized com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PixmapPacker.pack(com.badlogic.gdx.graphics.Pixmap)"""
        return 'math.Rectangle'._wrap(super(_PixmapPacker, self).pack(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def updateTextureAtlas(self, arg0: 'TextureAtlas', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updateTextureAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_PixmapPacker, self).updateTextureAtlas(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @overload
    def setPackToTexture(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPackToTexture(boolean)"""
        super(_PixmapPacker, self).setPackToTexture(_boolean.valueOf(arg0))

    @overload
    def setPadding(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPadding(int)"""
        super(_PixmapPacker, self).setPadding(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.dispose()"""
        super(PixmapPacker, self).dispose()

    @overload
    def getPageFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(PixmapPacker, self).getPageFormat())

    @overload
    def getPage(self, arg0: str) -> 'Page':
        """public synchronized com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker.getPage(java.lang.String)"""
        return 'Page'._wrap(super(_PixmapPacker, self).getPage(arg0))

    @overload
    def generateTextureAtlas(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool) -> 'TextureAtlas':
        """public synchronized com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.graphics.g2d.PixmapPacker.generateTextureAtlas(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        return 'TextureAtlas'._wrap(super(_PixmapPacker, self).generateTextureAtlas(arg0, arg1, _boolean.valueOf(arg2)))

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
    def pack(self, arg0: str, arg1: 'Pixmap') -> 'math.Rectangle':
        """public synchronized com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PixmapPacker.pack(java.lang.String,com.badlogic.gdx.graphics.Pixmap)"""
        return 'math.Rectangle'._wrap(super(_PixmapPacker, self).pack(arg0, arg1))

    @overload
    def updatePageTextures(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updatePageTextures(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_PixmapPacker, self).updatePageTextures(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def getPadding(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPadding()"""
        return int._wrap(super(PixmapPacker, self).getPadding())

    @overload
    def updateTextureRegions(self, arg0: 'Array', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updateTextureRegions(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion>,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_PixmapPacker, self).updateTextureRegions(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @overload
    def getRect(self, arg0: str) -> 'math.Rectangle':
        """public synchronized com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PixmapPacker.getRect(java.lang.String)"""
        return 'math.Rectangle'._wrap(super(_PixmapPacker, self).getRect(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite as _RepeatablePolygonSprite
_RepeatablePolygonSprite = _RepeatablePolygonSprite
import java.lang.Float as _float
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
 
class RepeatablePolygonSprite():
    """com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite"""
 
    @staticmethod
    def _wrap(java_value: _RepeatablePolygonSprite) -> 'RepeatablePolygonSprite':
        return RepeatablePolygonSprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RepeatablePolygonSprite):
        """
        Dynamic initializer for RepeatablePolygonSprite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RepeatablePolygonSprite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RepeatablePolygonSprite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_RepeatablePolygonSprite, self).setColor(arg0)

    @overload
    def setPolygon(self, arg0: 'TextureRegion', arg1: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setPolygon(com.badlogic.gdx.graphics.g2d.TextureRegion,float[])"""
        super(_RepeatablePolygonSprite, self).setPolygon(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite()"""
        val = _RepeatablePolygonSprite()
        self.__wrapper = val

    @overload
    def setPolygon(self, arg0: 'TextureRegion', arg1: 'float', arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setPolygon(com.badlogic.gdx.graphics.g2d.TextureRegion,float[],float)"""
        super(_RepeatablePolygonSprite, self).setPolygon(arg0, arg1, _float.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def draw(self, arg0: 'PolygonSpriteBatch'):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.draw(com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch)"""
        super(_RepeatablePolygonSprite, self).draw(arg0)

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
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setPosition(float,float)"""
        super(_RepeatablePolygonSprite, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite()"""
        val = _RepeatablePolygonSprite()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode
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
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpriteMode
_SpriteMode = _ParticleEmitter_SpriteMode.SpriteMode
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpriteMode():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpriteMode"""
 
    @staticmethod
    def _wrap(java_value: _SpriteMode) -> 'SpriteMode':
        return SpriteMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpriteMode):
        """
        Dynamic initializer for SpriteMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpriteMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpriteMode__wrapper":
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
    def valueOf(arg0: str) -> 'SpriteMode':
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode.valueOf(java.lang.String)"""
        return SpriteMode._wrap(_SpriteMode.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['SpriteMode']:
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode.values()"""
        return List[SpriteMode]._wrap(_SpriteMode.values())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpawnShape
_SpawnShape = _ParticleEmitter_SpawnShape.SpawnShape
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
 
class SpawnShape():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpawnShape"""
 
    @staticmethod
    def _wrap(java_value: _SpawnShape) -> 'SpawnShape':
        return SpawnShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpawnShape):
        """
        Dynamic initializer for SpawnShape.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpawnShape__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpawnShape__wrapper":
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
    def valueOf(arg0: str) -> 'SpawnShape':
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape.valueOf(java.lang.String)"""
        return SpawnShape._wrap(_SpawnShape.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['SpawnShape']:
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape.values()"""
        return List[SpawnShape]._wrap(_SpawnShape.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_Page
_Page = _PixmapPacker_Page.Page
import java.lang.String as _string
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_GuillotineStrategy
_GuillotineStrategy = _PixmapPacker_GuillotineStrategy.GuillotineStrategy
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
 
class GuillotineStrategy():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.GuillotineStrategy"""
 
    @staticmethod
    def _wrap(java_value: _GuillotineStrategy) -> 'GuillotineStrategy':
        return GuillotineStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GuillotineStrategy):
        """
        Dynamic initializer for GuillotineStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GuillotineStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GuillotineStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def sort(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        super(_GuillotineStrategy, self).sort(arg0)

    @overload
    def pack(self, arg0: 'PixmapPacker', arg1: str, arg2: 'Rectangle') -> 'Page':
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy.pack(com.badlogic.gdx.graphics.g2d.PixmapPacker,java.lang.String,com.badlogic.gdx.math.Rectangle)"""
        return 'Page'._wrap(super(_GuillotineStrategy, self).pack(arg0, arg1, arg2))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy()"""
        val = _GuillotineStrategy()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy()"""
        val = _GuillotineStrategy()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.io.BufferedReader as BufferedReader
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_RangedNumericValue
_RangedNumericValue = _ParticleEmitter_RangedNumericValue.RangedNumericValue
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ScaledNumericValue
_ScaledNumericValue = _ParticleEmitter_ScaledNumericValue.ScaledNumericValue
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaledNumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.ScaledNumericValue"""
 
    @staticmethod
    def _wrap(java_value: _ScaledNumericValue) -> 'ScaledNumericValue':
        return ScaledNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaledNumericValue):
        """
        Dynamic initializer for ScaledNumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaledNumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaledNumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue()"""
        val = _ScaledNumericValue()
        self.__wrapper = val

    @overload
    def newHighValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.newHighValue()"""
        return float._wrap(super(ScaledNumericValue, self).newHighValue())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def set(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(_ScaledNumericValue, self).set(arg0)

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getTimeline()"""
        return List[float]._wrap(super(ScaledNumericValue, self).getTimeline())

    @overload
    def getScaling(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScaling()"""
        return List[float]._wrap(super(ScaledNumericValue, self).getScaling())

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getScale(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScale(float)"""
        return float._wrap(super(_ScaledNumericValue, self).getScale(_float.valueOf(arg0)))

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setTimeline(float[])"""
        super(_ScaledNumericValue, self).setTimeline(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMin()"""
        return float._wrap(super(RangedNumericValue, self).getLowMin())

    @overload
    def getHighMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMin()"""
        return float._wrap(super(ScaledNumericValue, self).getHighMin())

    @overload
    def setHighMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMax(float)"""
        super(_ScaledNumericValue, self).setHighMax(_float.valueOf(arg0))

    @override
    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.newLowValue()"""
        return float._wrap(super(RangedNumericValue, self).newLowValue())

    @overload
    def getHighMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMax()"""
        return float._wrap(super(ScaledNumericValue, self).getHighMax())

    @override
    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMax(float)"""
        super(_RangedNumericValue, self).setLowMax(_float.valueOf(arg0))

    @overload
    def setHighMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMin(float)"""
        super(_ScaledNumericValue, self).setHighMin(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue()"""
        val = _ScaledNumericValue()
        self.__wrapper = val

    @override
    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(_ScaledNumericValue, self).save(arg0)

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.scale(float)"""
        super(_ScaledNumericValue, self).scale(_float.valueOf(arg0))

    @override
    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMin(float)"""
        super(_RangedNumericValue, self).setLowMin(_float.valueOf(arg0))

    @overload
    def setRelative(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setRelative(boolean)"""
        super(_ScaledNumericValue, self).setRelative(_boolean.valueOf(arg0))

    @overload
    def set(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(_ScaledNumericValue, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(_ScaledNumericValue, self).load(arg0)

    @overload
    def isRelative(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.isRelative()"""
        return bool._wrap(super(ScaledNumericValue, self).isRelative())

    @overload
    def setHigh(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float,float)"""
        super(_ScaledNumericValue, self).setHigh(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float,float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_ScaledNumericValue, self).load(arg0)

    @overload
    def setHigh(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float)"""
        super(_ScaledNumericValue, self).setHigh(_float.valueOf(arg0))

    @override
    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMax()"""
        return float._wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setScaling(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setScaling(float[])"""
        super(_ScaledNumericValue, self).setScaling(arg0)

    @override
    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(_RangedNumericValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$Particle
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_Particle
_Particle = _ParticleEmitter_Particle.Particle
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g2d.Sprite as _Sprite
_Sprite = _Sprite
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Particle():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.Particle"""
 
    @staticmethod
    def _wrap(java_value: _Particle) -> 'Particle':
        return Particle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Particle):
        """
        Dynamic initializer for Particle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Particle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Particle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setSize(float,float)"""
        super(_Sprite, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setAlpha(float)"""
        super(_Sprite, self).setAlpha(_float.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setBounds(float,float,float,float)"""
        super(_Sprite, self).setBounds(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginY()"""
        return float._wrap(super(Sprite, self).getOriginY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_Sprite, self).draw(arg0)

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(_TextureRegion, self).setRegionY(_int.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(_TextureRegion, self).setRegion(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setOriginCenter(self):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginCenter()"""
        super(Sprite, self).setOriginCenter()

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
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate(float)"""
        super(_Sprite, self).rotate(_float.valueOf(arg0))

    @override
    @overload
    def setCenterX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterX(float)"""
        super(_Sprite, self).setCenterX(_float.valueOf(arg0))

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scroll(float,float)"""
        super(_Sprite, self).scroll(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'._wrap(super(TextureRegion, self).getTexture())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setCenterY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterY(float)"""
        super(_Sprite, self).setCenterY(_float.valueOf(arg0))

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int._wrap(super(TextureRegion, self).getRegionX())

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float._wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int._wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getRotation()"""
        return float._wrap(super(Sprite, self).getRotation())

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.flip(boolean,boolean)"""
        super(_Sprite, self).flip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(_TextureRegion, self).setRegionX(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int._wrap(super(TextureRegion, self).getRegionWidth())

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getHeight()"""
        return float._wrap(super(Sprite, self).getHeight())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(_TextureRegion, self).setRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPackedColor(float)"""
        super(_Sprite, self).setPackedColor(_float.valueOf(arg0))

    @override
    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.Sprite.getBoundingRectangle()"""
        return 'math.Rectangle'._wrap(super(Sprite, self).getBoundingRectangle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setX(float)"""
        super(_Sprite, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateY(float)"""
        super(_Sprite, self).translateY(_float.valueOf(arg0))

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU(float)"""
        super(_Sprite, self).setU(_float.valueOf(arg0))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float._wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float)"""
        super(_Sprite, self).setScale(_float.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Sprite, self).setColor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getX()"""
        return float._wrap(super(Sprite, self).getX())

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool._wrap(super(TextureRegion, self).isFlipY())

    @override
    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translate(float,float)"""
        super(_Sprite, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU2(float)"""
        super(_Sprite, self).setU2(_float.valueOf(arg0))

    @override
    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateX(float)"""
        super(_Sprite, self).translateX(_float.valueOf(arg0))

    @override
    @overload
    def setCenter(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenter(float,float)"""
        super(_Sprite, self).setCenter(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.set(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(_Sprite, self).set(arg0)

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRegion(float,float,float,float)"""
        super(_Sprite, self).setRegion(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float._wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float,float)"""
        super(_Sprite, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_Sprite, self).draw(arg0, _float.valueOf(arg1))

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleX()"""
        return float._wrap(super(Sprite, self).getScaleX())

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getY()"""
        return float._wrap(super(Sprite, self).getY())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRotation(float)"""
        super(_Sprite, self).setRotation(_float.valueOf(arg0))

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float._wrap(super(TextureRegion, self).getV2())

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scale(float)"""
        super(_Sprite, self).scale(_float.valueOf(arg0))

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(_TextureRegion, self).setRegionWidth(_int.valueOf(arg0))

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int._wrap(super(TextureRegion, self).getRegionHeight())

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOrigin(float,float)"""
        super(_Sprite, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def rotate90(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate90(boolean)"""
        super(_Sprite, self).rotate90(_boolean.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setFlip(boolean,boolean)"""
        super(_Sprite, self).setFlip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(float,float,float,float)"""
        super(_Sprite, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]]._wrap(_TextureRegion.split(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setY(float)"""
        super(_Sprite, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV(float)"""
        super(_Sprite, self).setV(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Sprite.getColor()"""
        return 'graphics.Color'._wrap(super(Sprite, self).getColor())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPosition(float,float)"""
        super(_Sprite, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setOriginBasedPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginBasedPosition(float,float)"""
        super(_Sprite, self).setOriginBasedPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Sprite'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$Particle(com.badlogic.gdx.graphics.g2d.Sprite)"""
        val = _Particle(arg0)
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getWidth()"""
        return float._wrap(super(Sprite, self).getWidth())

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']]._wrap(super(_TextureRegion, self).split(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool._wrap(super(TextureRegion, self).isFlipX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.Sprite.getVertices()"""
        return List[float]._wrap(super(Sprite, self).getVertices())

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginX()"""
        return float._wrap(super(Sprite, self).getOriginX())

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV2(float)"""
        super(_Sprite, self).setV2(_float.valueOf(arg0))

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleY()"""
        return float._wrap(super(Sprite, self).getScaleY())

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(_TextureRegion, self).setRegionHeight(_int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Character as _char
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont_Glyph
_Glyph = _BitmapFont_Glyph.Glyph
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont_BitmapFontData
_BitmapFontData = _BitmapFont_BitmapFontData.BitmapFontData
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitmapFontData():
    """com.badlogic.gdx.graphics.g2d.BitmapFont.BitmapFontData"""
 
    @staticmethod
    def _wrap(java_value: _BitmapFontData) -> 'BitmapFontData':
        return BitmapFontData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitmapFontData):
        """
        Dynamic initializer for BitmapFontData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitmapFontData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitmapFontData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setScale(float,float)"""
        super(_BitmapFontData, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getImagePaths(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getImagePaths()"""
        return List[str]._wrap(super(BitmapFontData, self).getImagePaths())

    @overload
    def getFirstGlyph(self) -> 'Glyph':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getFirstGlyph()"""
        return 'Glyph'._wrap(super(BitmapFontData, self).getFirstGlyph())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _BitmapFontData(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.scale(float)"""
        super(_BitmapFontData, self).scale(_float.valueOf(arg0))

    @overload
    def getGlyphs(self, arg0: 'GlyphRun', arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'Glyph'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getGlyphs(com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun,java.lang.CharSequence,int,int,com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph)"""
        super(_BitmapFontData, self).getGlyphs(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def isWhitespace(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.isWhitespace(char)"""
        return bool._wrap(super(_BitmapFontData, self).isWhitespace(_char.valueOf(arg0)))

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setScale(float)"""
        super(_BitmapFontData, self).setScale(_float.valueOf(arg0))

    @overload
    def load(self, arg0: 'FileHandle', arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.load(com.badlogic.gdx.files.FileHandle,boolean)"""
        super(_BitmapFontData, self).load(arg0, _boolean.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getFontFile(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getFontFile()"""
        return 'files.FileHandle'._wrap(super(BitmapFontData, self).getFontFile())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getGlyph(self, arg0: str) -> 'Glyph':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getGlyph(char)"""
        return 'Glyph'._wrap(super(_BitmapFontData, self).getGlyph(_char.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData()"""
        val = _BitmapFontData()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData()"""
        val = _BitmapFontData()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getWrapIndex(self, arg0: 'Array', arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getWrapIndex(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph>,int)"""
        return int._wrap(super(_BitmapFontData, self).getWrapIndex(arg0, _int.valueOf(arg1)))

    @overload
    def hasGlyph(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.hasGlyph(char)"""
        return bool._wrap(super(_BitmapFontData, self).hasGlyph(_char.valueOf(arg0)))

    @overload
    def setGlyph(self, arg0: int, arg1: 'Glyph'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setGlyph(int,com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph)"""
        super(_BitmapFontData, self).setGlyph(_int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.toString()"""
        return str._wrap(super(BitmapFontData, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isBreakChar(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.isBreakChar(char)"""
        return bool._wrap(super(_BitmapFontData, self).isBreakChar(_char.valueOf(arg0)))

    @overload
    def setLineHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setLineHeight(float)"""
        super(_BitmapFontData, self).setLineHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getImagePath(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getImagePath(int)"""
        return str._wrap(super(_BitmapFontData, self).getImagePath(_int.valueOf(arg0)))

    @overload
    def setGlyphRegion(self, arg0: 'Glyph', arg1: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setGlyphRegion(com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_BitmapFontData, self).setGlyphRegion(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.NinePatch
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.NinePatch as _NinePatch
_NinePatch = _NinePatch
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NinePatch():
    """com.badlogic.gdx.graphics.g2d.NinePatch"""
 
    @staticmethod
    def _wrap(java_value: _NinePatch) -> 'NinePatch':
        return NinePatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NinePatch):
        """
        Dynamic initializer for NinePatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NinePatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NinePatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.Color)"""
        val = _NinePatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_NinePatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def setMiddleWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setMiddleWidth(float)"""
        super(_NinePatch, self).setMiddleWidth(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = _NinePatch(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'NinePatch', arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.NinePatch,com.badlogic.gdx.graphics.Color)"""
        val = _NinePatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def setPadRight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadRight(float)"""
        super(_NinePatch, self).setPadRight(_float.valueOf(arg0))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_NinePatch, self).setColor(arg0)

    @overload
    def getTotalWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getTotalWidth()"""
        return float._wrap(super(NinePatch, self).getTotalWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getMiddleWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getMiddleWidth()"""
        return float._wrap(super(NinePatch, self).getMiddleWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getLeftWidth()"""
        return float._wrap(super(NinePatch, self).getLeftWidth())

    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getBottomHeight()"""
        return float._wrap(super(NinePatch, self).getBottomHeight())

    @overload
    def setMiddleHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setMiddleHeight(float)"""
        super(_NinePatch, self).setMiddleHeight(_float.valueOf(arg0))

    @overload
    def setPadTop(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadTop(float)"""
        super(_NinePatch, self).setPadTop(_float.valueOf(arg0))

    @overload
    def getPadRight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadRight()"""
        return float._wrap(super(NinePatch, self).getPadRight())

    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getRightWidth()"""
        return float._wrap(super(NinePatch, self).getRightWidth())

    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getTopHeight()"""
        return float._wrap(super(NinePatch, self).getTopHeight())

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.NinePatch.getTexture()"""
        return 'graphics.Texture'._wrap(super(NinePatch, self).getTexture())

    @overload
    def getTotalHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getTotalHeight()"""
        return float._wrap(super(NinePatch, self).getTotalHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, *arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        val = _NinePatch(arg0)
        self.__wrapper = val

    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setBottomHeight(float)"""
        super(_NinePatch, self).setBottomHeight(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.Texture)"""
        val = _NinePatch(arg0)
        self.__wrapper = val

    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setLeftWidth(float)"""
        super(_NinePatch, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPadLeft(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadLeft()"""
        return float._wrap(super(NinePatch, self).getPadLeft())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _NinePatch(arg0)
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(_NinePatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'NinePatch'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.NinePatch)"""
        val = _NinePatch(arg0)
        self.__wrapper = val

    @overload
    def setPadLeft(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadLeft(float)"""
        super(_NinePatch, self).setPadLeft(_float.valueOf(arg0))

    @overload
    def getPadBottom(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadBottom()"""
        return float._wrap(super(NinePatch, self).getPadBottom())

    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setRightWidth(float)"""
        super(_NinePatch, self).setRightWidth(_float.valueOf(arg0))

    @overload
    def setPadBottom(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadBottom(float)"""
        super(_NinePatch, self).setPadBottom(_float.valueOf(arg0))

    @overload
    def scale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.scale(float,float)"""
        super(_NinePatch, self).scale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getPadTop(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadTop()"""
        return float._wrap(super(NinePatch, self).getPadTop())

    @overload
    def getMiddleHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getMiddleHeight()"""
        return float._wrap(super(NinePatch, self).getMiddleHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadding(float,float,float,float)"""
        super(_NinePatch, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        val = _NinePatch(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Texture', arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.Texture,com.badlogic.gdx.graphics.Color)"""
        val = _NinePatch(arg0, arg1)
        self.__wrapper = val

    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setTopHeight(float)"""
        super(_NinePatch, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.NinePatch.getColor()"""
        return 'graphics.Color'._wrap(super(NinePatch, self).getColor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEffectPool
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.ParticleEffectPool as _ParticleEffectPool
_ParticleEffectPool = _ParticleEffectPool
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffectPool():
    """com.badlogic.gdx.graphics.g2d.ParticleEffectPool"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffectPool) -> 'ParticleEffectPool':
        return ParticleEffectPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffectPool):
        """
        Dynamic initializer for ParticleEffectPool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffectPool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffectPool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ParticleEffect', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffectPool(com.badlogic.gdx.graphics.g2d.ParticleEffect,int,int)"""
        val = _ParticleEffectPool(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int._wrap(super(utils.Pool, self).getFree())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(_utils.Pool, self).fill(_int.valueOf(arg0))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def obtain(self) -> object:
        """public T com.badlogic.gdx.utils.Pool.obtain()"""
        return object._wrap(super(utils.Pool, self).obtain())

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Pool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_utils.Pool, self).freeAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def free(self, arg0: 'PooledEffect'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffectPool.free(com.badlogic.gdx.graphics.g2d.ParticleEffectPool$PooledEffect)"""
        super(_ParticleEffectPool, self).free(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter
_ParticleEmitter = _ParticleEmitter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEffect as _ParticleEffect
_ParticleEffect = _ParticleEffect
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.String as _string
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffect():
    """com.badlogic.gdx.graphics.g2d.ParticleEffect"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffect) -> 'ParticleEffect':
        return ParticleEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffect):
        """
        Dynamic initializer for ParticleEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def findEmitter(self, arg0: str) -> 'ParticleEmitter':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter com.badlogic.gdx.graphics.g2d.ParticleEffect.findEmitter(java.lang.String)"""
        return 'ParticleEmitter'._wrap(super(_ParticleEffect, self).findEmitter(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect()"""
        val = _ParticleEffect()
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_ParticleEffect, self).draw(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.dispose()"""
        super(ParticleEffect, self).dispose()

    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.preAllocateParticles()"""
        super(ParticleEffect, self).preAllocateParticles()

    @overload
    def reset(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset(boolean)"""
        super(_ParticleEffect, self).reset(_boolean.valueOf(arg0))

    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(_ParticleEffect, self).load(arg0, arg1)

    @overload
    def setEmittersCleanUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setEmittersCleanUpBlendFunction(boolean)"""
        super(_ParticleEffect, self).setEmittersCleanUpBlendFunction(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.allowCompletion()"""
        super(ParticleEffect, self).allowCompletion()

    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.flipY()"""
        super(ParticleEffect, self).flipY()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset()"""
        super(ParticleEffect, self).reset()

    @overload
    def loadEmitters(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitters(com.badlogic.gdx.files.FileHandle)"""
        super(_ParticleEffect, self).loadEmitters(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def scaleEffect(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float)"""
        super(_ParticleEffect, self).scaleEffect(_float.valueOf(arg0))

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEffect.getBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(ParticleEffect, self).getBoundingBox())

    @overload
    def load(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        super(_ParticleEffect, self).load(arg0, arg1)

    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.save(java.io.Writer) throws java.io.IOException"""
        super(_ParticleEffect, self).save(arg0)

    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(_ParticleEffect, self).loadEmitterImages(arg0)

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.start()"""
        super(ParticleEffect, self).start()

    @overload
    def setDuration(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setDuration(int)"""
        super(_ParticleEffect, self).setDuration(_int.valueOf(arg0))

    @overload
    def getEmitters(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.ParticleEmitter> com.badlogic.gdx.graphics.g2d.ParticleEffect.getEmitters()"""
        return 'utils.Array'._wrap(super(ParticleEffect, self).getEmitters())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setPosition(float,float)"""
        super(_ParticleEffect, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setFlip(boolean,boolean)"""
        super(_ParticleEffect, self).setFlip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.update(float)"""
        super(_ParticleEffect, self).update(_float.valueOf(arg0))

    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas', arg1: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(_ParticleEffect, self).loadEmitterImages(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def scaleEffect(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float)"""
        super(_ParticleEffect, self).scaleEffect(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def loadEmitterImages(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.files.FileHandle)"""
        super(_ParticleEffect, self).loadEmitterImages(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect()"""
        val = _ParticleEffect()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas', arg2: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(_ParticleEffect, self).load(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEffect.isComplete()"""
        return bool._wrap(super(ParticleEffect, self).isComplete())

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_ParticleEffect, self).draw(arg0, _float.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ParticleEffect'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect(com.badlogic.gdx.graphics.g2d.ParticleEffect)"""
        val = _ParticleEffect(arg0)
        self.__wrapper = val

    @overload
    def scaleEffect(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float,float)"""
        super(_ParticleEffect, self).scaleEffect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.String as _string
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpriteMode
_SpriteMode = _ParticleEmitter_SpriteMode.SpriteMode
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_RangedNumericValue
_RangedNumericValue = _ParticleEmitter_RangedNumericValue.RangedNumericValue
import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpawnShapeValue
_SpawnShapeValue = _ParticleEmitter_SpawnShapeValue.SpawnShapeValue
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ScaledNumericValue
_ScaledNumericValue = _ParticleEmitter_ScaledNumericValue.ScaledNumericValue
from builtins import str
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter
_ParticleEmitter = _ParticleEmitter
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.io.BufferedReader as BufferedReader
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_GradientColorValue
_GradientColorValue = _ParticleEmitter_GradientColorValue.GradientColorValue
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEmitter():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEmitter) -> 'ParticleEmitter':
        return ParticleEmitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEmitter):
        """
        Dynamic initializer for ParticleEmitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEmitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEmitter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def cleansUpBlendFunction(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.cleansUpBlendFunction()"""
        return bool._wrap(super(ParticleEmitter, self).cleansUpBlendFunction())

    @overload
    def isAdditive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAdditive()"""
        return bool._wrap(super(ParticleEmitter, self).isAdditive())

    @overload
    def setSprites(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSprites(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite>)"""
        super(_ParticleEmitter, self).setSprites(arg0)

    @overload
    def getTint(self) -> 'GradientColorValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTint()"""
        return 'GradientColorValue'._wrap(super(ParticleEmitter, self).getTint())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getXScale(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXScale()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getXScale())

    @overload
    def getDuration(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDuration()"""
        return 'RangedNumericValue'._wrap(super(ParticleEmitter, self).getDuration())

    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getSpawnWidth())

    @overload
    def scaleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float,float)"""
        super(_ParticleEmitter, self).scaleSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.save(java.io.Writer) throws java.io.IOException"""
        super(_ParticleEmitter, self).save(arg0)

    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMinParticleCount()"""
        return int._wrap(super(ParticleEmitter, self).getMinParticleCount())

    @overload
    def isAttached(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAttached()"""
        return bool._wrap(super(ParticleEmitter, self).isAttached())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getActiveCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getActiveCount()"""
        return int._wrap(super(ParticleEmitter, self).getActiveCount())

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_ParticleEmitter, self).draw(arg0)

    @overload
    def getXOffsetValue(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXOffsetValue()"""
        return 'RangedNumericValue'._wrap(super(ParticleEmitter, self).getXOffsetValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isPremultipliedAlpha(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isPremultipliedAlpha()"""
        return bool._wrap(super(ParticleEmitter, self).isPremultipliedAlpha())

    @overload
    def getSprites(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSprites()"""
        return 'utils.Array'._wrap(super(ParticleEmitter, self).getSprites())

    @overload
    def getLifeOffset(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLifeOffset()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getLifeOffset())

    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMaxParticleCount(int)"""
        super(_ParticleEmitter, self).setMaxParticleCount(_int.valueOf(arg0))

    @overload
    def getYOffsetValue(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYOffsetValue()"""
        return 'RangedNumericValue'._wrap(super(ParticleEmitter, self).getYOffsetValue())

    @overload
    def getTransparency(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTransparency()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getTransparency())

    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.flipY()"""
        super(ParticleEmitter, self).flipY()

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEmitter.getBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(ParticleEmitter, self).getBoundingBox())

    @overload
    def setAdditive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAdditive(boolean)"""
        super(_ParticleEmitter, self).setAdditive(_boolean.valueOf(arg0))

    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getPercentComplete()"""
        return float._wrap(super(ParticleEmitter, self).getPercentComplete())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.update(float)"""
        super(_ParticleEmitter, self).update(_float.valueOf(arg0))

    @overload
    def getEmission(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getEmission()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getEmission())

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setName(java.lang.String)"""
        super(_ParticleEmitter, self).setName(arg0)

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPosition(float,float)"""
        super(_ParticleEmitter, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ParticleEmitter'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        val = _ParticleEmitter(arg0)
        self.__wrapper = val

    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getSpawnHeight())

    @overload
    def getLife(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLife()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getLife())

    @overload
    def matchXSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchXSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(_ParticleEmitter, self).matchXSize(arg0)

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isComplete()"""
        return bool._wrap(super(ParticleEmitter, self).isComplete())

    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isContinuous()"""
        return bool._wrap(super(ParticleEmitter, self).isContinuous())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isBehind(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isBehind()"""
        return bool._wrap(super(ParticleEmitter, self).isBehind())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getY()"""
        return float._wrap(super(ParticleEmitter, self).getY())

    @overload
    def getSpriteMode(self) -> 'SpriteMode':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpriteMode()"""
        return 'SpriteMode'._wrap(super(ParticleEmitter, self).getSpriteMode())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def isAligned(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAligned()"""
        return bool._wrap(super(ParticleEmitter, self).isAligned())

    @overload
    def setSpriteMode(self, arg0: 'SpriteMode'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSpriteMode(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode)"""
        super(_ParticleEmitter, self).setSpriteMode(arg0)

    @overload
    def getSpawnShape(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnShape()"""
        return 'SpawnShapeValue'._wrap(super(ParticleEmitter, self).getSpawnShape())

    @overload
    def getDelay(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDelay()"""
        return 'RangedNumericValue'._wrap(super(ParticleEmitter, self).getDelay())

    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setFlip(boolean,boolean)"""
        super(_ParticleEmitter, self).setFlip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.allowCompletion()"""
        super(ParticleEmitter, self).allowCompletion()

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getX()"""
        return float._wrap(super(ParticleEmitter, self).getX())

    @overload
    def matchYSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchYSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(_ParticleEmitter, self).matchYSize(arg0)

    @overload
    def __init__(self, arg0: 'BufferedReader'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter(java.io.BufferedReader) throws java.io.IOException"""
        val = _ParticleEmitter(arg0)
        self.__wrapper = val

    @overload
    def setAttached(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAttached(boolean)"""
        super(_ParticleEmitter, self).setAttached(_boolean.valueOf(arg0))

    @overload
    def matchSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(_ParticleEmitter, self).matchSize(arg0)

    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.preAllocateParticles()"""
        super(ParticleEmitter, self).preAllocateParticles()

    @overload
    def getWind(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getWind()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getWind())

    @overload
    def scaleMotion(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleMotion(float)"""
        super(_ParticleEmitter, self).scaleMotion(_float.valueOf(arg0))

    @overload
    def setBehind(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setBehind(boolean)"""
        super(_ParticleEmitter, self).setBehind(_boolean.valueOf(arg0))

    @overload
    def setImagePaths(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setImagePaths(com.badlogic.gdx.utils.Array<java.lang.String>)"""
        super(_ParticleEmitter, self).setImagePaths(arg0)

    @overload
    def getImagePaths(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getImagePaths()"""
        return 'utils.Array'._wrap(super(ParticleEmitter, self).getImagePaths())

    @overload
    def setCleansUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setCleansUpBlendFunction(boolean)"""
        super(_ParticleEmitter, self).setCleansUpBlendFunction(_boolean.valueOf(arg0))

    @overload
    def scaleSize(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float)"""
        super(_ParticleEmitter, self).scaleSize(_float.valueOf(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.reset()"""
        super(ParticleEmitter, self).reset()

    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_ParticleEmitter, self).load(arg0)

    @overload
    def addParticles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticles(int)"""
        super(_ParticleEmitter, self).addParticles(_int.valueOf(arg0))

    @overload
    def setAligned(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAligned(boolean)"""
        super(_ParticleEmitter, self).setAligned(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter()"""
        val = _ParticleEmitter()
        self.__wrapper = val

    @overload
    def getYScale(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYScale()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getYScale())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.ParticleEmitter.getName()"""
        return str._wrap(super(ParticleEmitter, self).getName())

    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMaxParticleCount()"""
        return int._wrap(super(ParticleEmitter, self).getMaxParticleCount())

    @overload
    def getGravity(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getGravity()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getGravity())

    @overload
    def getRotation(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getRotation()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getRotation())

    @overload
    def setPremultipliedAlpha(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPremultipliedAlpha(boolean)"""
        super(_ParticleEmitter, self).setPremultipliedAlpha(_boolean.valueOf(arg0))

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.start()"""
        super(ParticleEmitter, self).start()

    @overload
    def matchMotion(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchMotion(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(_ParticleEmitter, self).matchMotion(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addParticle(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticle()"""
        super(ParticleEmitter, self).addParticle()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter()"""
        val = _ParticleEmitter()
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_ParticleEmitter, self).draw(arg0, _float.valueOf(arg1))

    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setContinuous(boolean)"""
        super(_ParticleEmitter, self).setContinuous(_boolean.valueOf(arg0))

    @overload
    def getVelocity(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getVelocity()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getVelocity())

    @overload
    def getAngle(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getAngle()"""
        return 'ScaledNumericValue'._wrap(super(ParticleEmitter, self).getAngle())

    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMinParticleCount(int)"""
        super(_ParticleEmitter, self).setMinParticleCount(_int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.io.BufferedReader as BufferedReader
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.ParticleValue"""
 
    @staticmethod
    def _wrap(java_value: _ParticleValue) -> 'ParticleValue':
        return ParticleValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleValue):
        """
        Dynamic initializer for ParticleValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_ParticleValue, self).load(arg0)

    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.save(java.io.Writer) throws java.io.IOException"""
        super(_ParticleValue, self).save(arg0)

    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

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
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue()"""
        val = _ParticleValue()
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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue()"""
        val = _ParticleValue()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonRegion
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import com.badlogic.gdx.graphics.g2d.PolygonRegion as _PolygonRegion
_PolygonRegion = _PolygonRegion
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolygonRegion():
    """com.badlogic.gdx.graphics.g2d.PolygonRegion"""
 
    @staticmethod
    def _wrap(java_value: _PolygonRegion) -> 'PolygonRegion':
        return PolygonRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonRegion):
        """
        Dynamic initializer for PolygonRegion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonRegion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonRegion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTextureCoords(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.PolygonRegion.getTextureCoords()"""
        return List[float]._wrap(super(PolygonRegion, self).getTextureCoords())

    @overload
    def getRegion(self) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.PolygonRegion.getRegion()"""
        return 'TextureRegion'._wrap(super(PolygonRegion, self).getRegion())

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
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.PolygonRegion.getVertices()"""
        return List[float]._wrap(super(PolygonRegion, self).getVertices())

    @overload
    def getTriangles(self) -> List[int]:
        """public short[] com.badlogic.gdx.graphics.g2d.PolygonRegion.getTriangles()"""
        return List[int]._wrap(super(PolygonRegion, self).getTriangles())

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: 'float', arg2: 'short'):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,float[],short[])"""
        val = _PolygonRegion(arg0, arg1, arg2)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonBatch
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
import com.badlogic.gdx.graphics.g2d.PolygonBatch as _PolygonBatch
_PolygonBatch = _PolygonBatch
from builtins import float
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
from builtins import int
 
class PolygonBatch():
    """com.badlogic.gdx.graphics.g2d.PolygonBatch"""
 
    @staticmethod
    def _wrap(java_value: _PolygonBatch) -> 'PolygonBatch':
        return PolygonBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonBatch):
        """
        Dynamic initializer for PolygonBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def enableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.enableBlending()"""
        pass

    @abstractmethod
    def setColor(self, arg0: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        pass

    @abstractmethod
    def getTransformMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getTransformMatrix()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.begin()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        pass

    @abstractmethod
    def getShader(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.Batch.getShader()"""
        pass

    @abstractmethod
    def getBlendDstFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFunc()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float)"""
        pass

    @abstractmethod
    def getColor(self, ):
        """public abstract com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Batch.getColor()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        pass

    @abstractmethod
    def getProjectionMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getProjectionMatrix()"""
        pass

    @abstractmethod
    def isDrawing(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isDrawing()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float)"""
        pass

    @abstractmethod
    def getBlendSrcFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFuncAlpha()"""
        pass

    @abstractmethod
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunctionSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(float,float,float,float)"""
        pass

    @abstractmethod
    def setPackedColor(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setPackedColor(float)"""
        pass

    @abstractmethod
    def getBlendSrcFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFunc()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int,short[],int,int)"""
        pass

    @abstractmethod
    def disableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.disableBlending()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def setShader(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.flush()"""
        pass

    @abstractmethod
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        pass

    @abstractmethod
    def isBlendingEnabled(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isBlendingEnabled()"""
        pass

    @abstractmethod
    def setBlendFunction(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunction(int,int)"""
        pass

    @abstractmethod
    def getBlendDstFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFuncAlpha()"""
        pass

    @abstractmethod
    def getPackedColor(self, ):
        """public abstract float com.badlogic.gdx.graphics.g2d.Batch.getPackedColor()"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.end()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.SpriteCache
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.g2d.SpriteCache as _SpriteCache
_SpriteCache = _SpriteCache
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
 
class SpriteCache():
    """com.badlogic.gdx.graphics.g2d.SpriteCache"""
 
    @staticmethod
    def _wrap(java_value: _SpriteCache) -> 'SpriteCache':
        return SpriteCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpriteCache):
        """
        Dynamic initializer for SpriteCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpriteCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpriteCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(_SpriteCache, self).add(arg0)

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache(int,boolean)"""
        val = _SpriteCache(_int.valueOf(arg0), _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache()"""
        val = _SpriteCache()
        self.__wrapper = val

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setColor(float,float,float,float)"""
        super(_SpriteCache, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_SpriteCache, self).setTransformMatrix(arg0)

    @overload
    def getCustomShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteCache.getCustomShader()"""
        return 'glutils.ShaderProgram'._wrap(super(SpriteCache, self).getCustomShader())

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache(int,com.badlogic.gdx.graphics.glutils.ShaderProgram,boolean)"""
        val = _SpriteCache(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.dispose()"""
        super(SpriteCache, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def draw(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.draw(int)"""
        super(_SpriteCache, self).draw(_int.valueOf(arg0))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.begin()"""
        super(SpriteCache, self).begin()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.SpriteCache.getColor()"""
        return 'graphics.Color'._wrap(super(SpriteCache, self).getColor())

    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_SpriteCache, self).setProjectionMatrix(arg0)

    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteCache.getTransformMatrix()"""
        return 'math.Matrix4'._wrap(super(SpriteCache, self).getTransformMatrix())

    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteCache.getProjectionMatrix()"""
        return 'math.Matrix4'._wrap(super(SpriteCache, self).getProjectionMatrix())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _boolean.valueOf(arg10))

    @overload
    def beginCache(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.beginCache(int)"""
        super(_SpriteCache, self).beginCache(_int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache()"""
        val = _SpriteCache()
        self.__wrapper = val

    @overload
    def beginCache(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.beginCache()"""
        super(SpriteCache, self).beginCache()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.clear()"""
        super(SpriteCache, self).clear()

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _boolean.valueOf(arg14), _boolean.valueOf(arg15))

    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.SpriteCache.getPackedColor()"""
        return float._wrap(super(SpriteCache, self).getPackedColor())

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_SpriteCache, self).setColor(arg0)

    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteCache.isDrawing()"""
        return bool._wrap(super(SpriteCache, self).isDrawing())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def endCache(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteCache.endCache()"""
        return int._wrap(super(SpriteCache, self).endCache())

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,int,int,float,float,float,float,float)"""
        super(_SpriteCache, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_SpriteCache, self).setShader(arg0)

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.end()"""
        super(SpriteCache, self).end()

    @overload
    def draw(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.draw(int,int,int)"""
        super(_SpriteCache, self).draw(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setPackedColor(float)"""
        super(_SpriteCache, self).setPackedColor(_float.valueOf(arg0))

    @overload
    def add(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(_SpriteCache, self).add(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEffectPool$PooledEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter
_ParticleEmitter = _ParticleEmitter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEffectPool as _ParticleEffectPool_PooledEffect
_PooledEffect = _ParticleEffectPool_PooledEffect.PooledEffect
import com.badlogic.gdx.graphics.g2d.ParticleEffect as _ParticleEffect
_ParticleEffect = _ParticleEffect
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.String as _string
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PooledEffect():
    """com.badlogic.gdx.graphics.g2d.ParticleEffectPool.PooledEffect"""
 
    @staticmethod
    def _wrap(java_value: _PooledEffect) -> 'PooledEffect':
        return PooledEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PooledEffect):
        """
        Dynamic initializer for PooledEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PooledEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PooledEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setPosition(float,float)"""
        super(_ParticleEffect, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def findEmitter(self, arg0: str) -> 'ParticleEmitter':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter com.badlogic.gdx.graphics.g2d.ParticleEffect.findEmitter(java.lang.String)"""
        return 'ParticleEmitter'._wrap(super(_ParticleEffect, self).findEmitter(arg0))

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.start()"""
        super(ParticleEffect, self).start()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.dispose()"""
        super(ParticleEffect, self).dispose()

    @override
    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.flipY()"""
        super(ParticleEffect, self).flipY()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas', arg2: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(_ParticleEffect, self).load(arg0, arg1, arg2)

    @override
    @overload
    def loadEmitters(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitters(com.badlogic.gdx.files.FileHandle)"""
        super(_ParticleEffect, self).loadEmitters(arg0)

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
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_ParticleEffect, self).draw(arg0)

    @override
    @overload
    def scaleEffect(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float,float)"""
        super(_ParticleEffect, self).scaleEffect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def setEmittersCleanUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setEmittersCleanUpBlendFunction(boolean)"""
        super(_ParticleEffect, self).setEmittersCleanUpBlendFunction(_boolean.valueOf(arg0))

    @override
    @overload
    def scaleEffect(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float)"""
        super(_ParticleEffect, self).scaleEffect(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.save(java.io.Writer) throws java.io.IOException"""
        super(_ParticleEffect, self).save(arg0)

    @override
    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(_ParticleEffect, self).load(arg0, arg1)

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setFlip(boolean,boolean)"""
        super(_ParticleEffect, self).setFlip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.allowCompletion()"""
        super(ParticleEffect, self).allowCompletion()

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.update(float)"""
        super(_ParticleEffect, self).update(_float.valueOf(arg0))

    @override
    @overload
    def reset(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset(boolean)"""
        super(_ParticleEffect, self).reset(_boolean.valueOf(arg0))

    @override
    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas', arg1: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(_ParticleEffect, self).loadEmitterImages(arg0, arg1)

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

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEffect.isComplete()"""
        return bool._wrap(super(ParticleEffect, self).isComplete())

    @override
    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(_ParticleEffect, self).loadEmitterImages(arg0)

    @overload
    def free(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffectPool$PooledEffect.free()"""
        super(PooledEffect, self).free()

    @override
    @overload
    def load(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        super(_ParticleEffect, self).load(arg0, arg1)

    @override
    @overload
    def getEmitters(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.ParticleEmitter> com.badlogic.gdx.graphics.g2d.ParticleEffect.getEmitters()"""
        return 'utils.Array'._wrap(super(ParticleEffect, self).getEmitters())

    @override
    @overload
    def scaleEffect(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float)"""
        super(_ParticleEffect, self).scaleEffect(_float.valueOf(arg0))

    @override
    @overload
    def setDuration(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setDuration(int)"""
        super(_ParticleEffect, self).setDuration(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_ParticleEffect, self).draw(arg0, _float.valueOf(arg1))

    @override
    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEffect.getBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(ParticleEffect, self).getBoundingBox())

    @override
    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.preAllocateParticles()"""
        super(ParticleEffect, self).preAllocateParticles()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset()"""
        super(ParticleEffect, self).reset()

    @override
    @overload
    def loadEmitterImages(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.files.FileHandle)"""
        super(_ParticleEffect, self).loadEmitterImages(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFont
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.BitmapFontCache as _BitmapFontCache
_BitmapFontCache = _BitmapFontCache
import com.badlogic.gdx.graphics.g2d.GlyphLayout as _GlyphLayout
_GlyphLayout = _GlyphLayout
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont_BitmapFontData
_BitmapFontData = _BitmapFont_BitmapFontData.BitmapFontData
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont
_BitmapFont = _BitmapFont
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitmapFont():
    """com.badlogic.gdx.graphics.g2d.BitmapFont"""
 
    @staticmethod
    def _wrap(java_value: _BitmapFont) -> 'BitmapFont':
        return BitmapFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitmapFont):
        """
        Dynamic initializer for BitmapFont.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitmapFont__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitmapFont__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion> com.badlogic.gdx.graphics.g2d.BitmapFont.getRegions()"""
        return 'utils.Array'._wrap(super(BitmapFont, self).getRegions())

    @overload
    def getRegion(self, arg0: int) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion(int)"""
        return 'TextureRegion'._wrap(super(_BitmapFont, self).getRegion(_int.valueOf(arg0)))

    @overload
    def getData(self) -> 'BitmapFontData':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData com.badlogic.gdx.graphics.g2d.BitmapFont.getData()"""
        return 'BitmapFontData'._wrap(super(BitmapFont, self).getData())

    @overload
    def isFlipped(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.isFlipped()"""
        return bool._wrap(super(BitmapFont, self).isFlipped())

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle)"""
        val = _BitmapFont(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setFixedWidthGlyphs(self, arg0: 'CharSequence'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setFixedWidthGlyphs(java.lang.CharSequence)"""
        super(_BitmapFont, self).setFixedWidthGlyphs(arg0)

    @overload
    def setOwnsTexture(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setOwnsTexture(boolean)"""
        super(_BitmapFont, self).setOwnsTexture(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont()"""
        val = _BitmapFont()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setUseIntegerPositions(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setUseIntegerPositions(boolean)"""
        super(_BitmapFont, self).setUseIntegerPositions(_boolean.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: float, arg5: int, arg6: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _boolean.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.BitmapFont.getCache()"""
        return 'BitmapFontCache'._wrap(super(BitmapFont, self).getCache())

    @overload
    def getCapHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getCapHeight()"""
        return float._wrap(super(BitmapFont, self).getCapHeight())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(float,float,float,float)"""
        super(_BitmapFont, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(boolean)"""
        val = _BitmapFont(_boolean.valueOf(arg0))
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool, arg9: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _boolean.valueOf(arg8), arg9))

    @overload
    def draw(self, arg0: 'Batch', arg1: 'GlyphLayout', arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getRegion(self) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion()"""
        return 'TextureRegion'._wrap(super(BitmapFont, self).getRegion())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleY()"""
        return float._wrap(super(BitmapFont, self).getScaleY())

    @overload
    def getDescent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getDescent()"""
        return float._wrap(super(BitmapFont, self).getDescent())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont()"""
        val = _BitmapFont()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _BitmapFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_BitmapFont, self).setColor(arg0)

    @overload
    def getLineHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getLineHeight()"""
        return float._wrap(super(BitmapFont, self).getLineHeight())

    @overload
    def usesIntegerPositions(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.usesIntegerPositions()"""
        return bool._wrap(super(BitmapFont, self).usesIntegerPositions())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = _BitmapFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean,boolean)"""
        val = _BitmapFont(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _BitmapFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def ownsTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.ownsTexture()"""
        return bool._wrap(super(BitmapFont, self).ownsTexture())

    @overload
    def getXHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getXHeight()"""
        return float._wrap(super(BitmapFont, self).getXHeight())

    @overload
    def getSpaceXadvance(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getSpaceXadvance()"""
        return float._wrap(super(BitmapFont, self).getSpaceXadvance())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.dispose()"""
        super(BitmapFont, self).dispose()

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont.toString()"""
        return str._wrap(super(BitmapFont, self).toString())

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'Array', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion>,boolean)"""
        val = _BitmapFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = _BitmapFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleX()"""
        return float._wrap(super(BitmapFont, self).getScaleX())

    @overload
    def getAscent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getAscent()"""
        return float._wrap(super(BitmapFont, self).getAscent())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _boolean.valueOf(arg8)))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.BitmapFont.getColor()"""
        return 'graphics.Color'._wrap(super(BitmapFont, self).getColor())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _BitmapFont(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def newFontCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.BitmapFont.newFontCache()"""
        return 'BitmapFontCache'._wrap(super(BitmapFont, self).newFontCache()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_AtlasRegion
_AtlasRegion = _TextureAtlas_AtlasRegion.AtlasRegion
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtlasRegion():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.AtlasRegion"""
 
    @staticmethod
    def _wrap(java_value: _AtlasRegion) -> 'AtlasRegion':
        return AtlasRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtlasRegion):
        """
        Dynamic initializer for AtlasRegion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtlasRegion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtlasRegion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool._wrap(super(TextureRegion, self).isFlipY())

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU(float)"""
        super(_TextureRegion, self).setU(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float._wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(_TextureRegion, self).setRegionY(_int.valueOf(arg0))

    @overload
    def findValue(self, arg0: str) -> List[int]:
        """public int[] com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.findValue(java.lang.String)"""
        return List[int]._wrap(super(_AtlasRegion, self).findValue(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(_TextureRegion, self).setRegion(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU2(float)"""
        super(_TextureRegion, self).setU2(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _AtlasRegion(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.toString()"""
        return str._wrap(super(AtlasRegion, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float._wrap(super(TextureRegion, self).getV2())

    @overload
    def getRotatedPackedWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.getRotatedPackedWidth()"""
        return float._wrap(super(AtlasRegion, self).getRotatedPackedWidth())

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV2(float)"""
        super(_TextureRegion, self).setV2(_float.valueOf(arg0))

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(_TextureRegion, self).setRegionWidth(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int._wrap(super(TextureRegion, self).getRegionHeight())

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.flip(boolean,boolean)"""
        super(_AtlasRegion, self).flip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setRegion(arg0)

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = _AtlasRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'._wrap(super(TextureRegion, self).getTexture())

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV(float)"""
        super(_TextureRegion, self).setV(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getRotatedPackedHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.getRotatedPackedHeight()"""
        return float._wrap(super(AtlasRegion, self).getRotatedPackedHeight())

    @overload
    def __init__(self, arg0: 'AtlasRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion(com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion)"""
        val = _AtlasRegion(arg0)
        self.__wrapper = val

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int._wrap(super(TextureRegion, self).getRegionX())

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]]._wrap(_TextureRegion.split(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.scroll(float,float)"""
        super(_TextureRegion, self).scroll(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float._wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int._wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(_TextureRegion, self).setRegionX(_int.valueOf(arg0))

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int._wrap(super(TextureRegion, self).getRegionWidth())

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']]._wrap(super(_TextureRegion, self).split(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(_TextureRegion, self).setRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool._wrap(super(TextureRegion, self).isFlipX())

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
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float._wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(float,float,float,float)"""
        super(_TextureRegion, self).setRegion(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(_TextureRegion, self).setRegionHeight(_int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.io.BufferedReader as BufferedReader
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_GradientColorValue
_GradientColorValue = _ParticleEmitter_GradientColorValue.GradientColorValue
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GradientColorValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.GradientColorValue"""
 
    @staticmethod
    def _wrap(java_value: _GradientColorValue) -> 'GradientColorValue':
        return GradientColorValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GradientColorValue):
        """
        Dynamic initializer for GradientColorValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GradientColorValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GradientColorValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getColor(self, arg0: float) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getColor(float)"""
        return List[float]._wrap(super(_GradientColorValue, self).getColor(_float.valueOf(arg0)))

    @overload
    def setColors(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.setColors(float[])"""
        super(_GradientColorValue, self).setColors(arg0)

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.save(java.io.Writer) throws java.io.IOException"""
        super(_GradientColorValue, self).save(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue()"""
        val = _GradientColorValue()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'GradientColorValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue)"""
        super(_GradientColorValue, self).load(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue()"""
        val = _GradientColorValue()
        self.__wrapper = val

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

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
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getTimeline()"""
        return List[float]._wrap(super(GradientColorValue, self).getTimeline())

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_GradientColorValue, self).load(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.setTimeline(float[])"""
        super(_GradientColorValue, self).setTimeline(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColors(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getColors()"""
        return List[float]._wrap(super(GradientColorValue, self).getColors())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.GlyphLayout
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g2d.GlyphLayout as _GlyphLayout
_GlyphLayout = _GlyphLayout
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
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
 
class GlyphLayout():
    """com.badlogic.gdx.graphics.g2d.GlyphLayout"""
 
    @staticmethod
    def _wrap(java_value: _GlyphLayout) -> 'GlyphLayout':
        return GlyphLayout(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GlyphLayout):
        """
        Dynamic initializer for GlyphLayout.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GlyphLayout__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GlyphLayout__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'Color', arg5: float, arg6: int, arg7: bool, arg8: str):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,int,int,com.badlogic.gdx.graphics.Color,float,int,boolean,java.lang.String)"""
        val = _GlyphLayout(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4, _float.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7), arg8)
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
    def setText(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: 'Color', arg3: float, arg4: int, arg5: bool):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.setText(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,com.badlogic.gdx.graphics.Color,float,int,boolean)"""
        super(_GlyphLayout, self).setText(arg0, arg1, arg2, _float.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5))

    @overload
    def setText(self, arg0: 'BitmapFont', arg1: 'CharSequence'):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.setText(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence)"""
        super(_GlyphLayout, self).setText(arg0, arg1)

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: 'Color', arg3: float, arg4: int, arg5: bool):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,com.badlogic.gdx.graphics.Color,float,int,boolean)"""
        val = _GlyphLayout(arg0, arg1, arg2, _float.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'CharSequence'):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence)"""
        val = _GlyphLayout(arg0, arg1)
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout()"""
        val = _GlyphLayout()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.GlyphLayout.toString()"""
        return str._wrap(super(GlyphLayout, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setText(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'Color', arg5: float, arg6: int, arg7: bool, arg8: str):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.setText(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,int,int,com.badlogic.gdx.graphics.Color,float,int,boolean,java.lang.String)"""
        super(_GlyphLayout, self).setText(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4, _float.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7), arg8)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout()"""
        val = _GlyphLayout()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.reset()"""
        super(GlyphLayout, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFontCache
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.BitmapFontCache as _BitmapFontCache
_BitmapFontCache = _BitmapFontCache
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g2d.GlyphLayout as _GlyphLayout
_GlyphLayout = _GlyphLayout
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
from typing import List
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont
_BitmapFont = _BitmapFont
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
 
class BitmapFontCache():
    """com.badlogic.gdx.graphics.g2d.BitmapFontCache"""
 
    @staticmethod
    def _wrap(java_value: _BitmapFontCache) -> 'BitmapFontCache':
        return BitmapFontCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitmapFontCache):
        """
        Dynamic initializer for BitmapFontCache.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitmapFontCache__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitmapFontCache__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setColors(self, arg0: 'Color', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(com.badlogic.gdx.graphics.Color,int,int)"""
        super(_BitmapFontCache, self).setColors(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def draw(self, arg0: 'Batch', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.draw(com.badlogic.gdx.graphics.g2d.Batch,int,int)"""
        super(_BitmapFontCache, self).draw(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_BitmapFontCache, self).setColor(arg0)

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).setText(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_BitmapFontCache, self).draw(arg0, _float.valueOf(arg1))

    @overload
    def getFont(self) -> 'BitmapFont':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont com.badlogic.gdx.graphics.g2d.BitmapFontCache.getFont()"""
        return 'BitmapFont'._wrap(super(BitmapFontCache, self).getFont())

    @overload
    def usesIntegerPositions(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFontCache.usesIntegerPositions()"""
        return bool._wrap(super(BitmapFontCache, self).usesIntegerPositions())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getVertexCount(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.g2d.BitmapFontCache.getVertexCount(int)"""
        return int._wrap(super(_BitmapFontCache, self).getVertexCount(_int.valueOf(arg0)))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.clear()"""
        super(BitmapFontCache, self).clear()

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).addText(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setColors(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(com.badlogic.gdx.graphics.Color)"""
        super(_BitmapFontCache, self).setColors(arg0)

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.BitmapFontCache.getVertices()"""
        return List[float]._wrap(super(BitmapFontCache, self).getVertices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColors(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(float,float,float,float)"""
        super(_BitmapFontCache, self).setColors(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'BitmapFont'):
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache(com.badlogic.gdx.graphics.g2d.BitmapFont)"""
        val = _BitmapFontCache(arg0)
        self.__wrapper = val

    @overload
    def setUseIntegerPositions(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setUseIntegerPositions(boolean)"""
        super(_BitmapFontCache, self).setUseIntegerPositions(_boolean.valueOf(arg0))

    @overload
    def tint(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.tint(com.badlogic.gdx.graphics.Color)"""
        super(_BitmapFontCache, self).tint(arg0)

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_BitmapFontCache, self).draw(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setPosition(float,float)"""
        super(_BitmapFontCache, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool, arg8: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).setText(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7), arg8))

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: float, arg4: int, arg5: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).setText(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5)))

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).addText(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache(com.badlogic.gdx.graphics.g2d.BitmapFont,boolean)"""
        val = _BitmapFontCache(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setColors(self, arg0: float, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(float,int,int)"""
        super(_BitmapFontCache, self).setColors(_float.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColor(float,float,float,float)"""
        super(_BitmapFontCache, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setAlphas(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setAlphas(float)"""
        super(_BitmapFontCache, self).setAlphas(_float.valueOf(arg0))

    @overload
    def setText(self, arg0: 'GlyphLayout', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(_BitmapFontCache, self).setText(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: float, arg4: int, arg5: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).addText(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5)))

    @overload
    def addText(self, arg0: 'GlyphLayout', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(_BitmapFontCache, self).addText(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFontCache.getY()"""
        return float._wrap(super(BitmapFontCache, self).getY())

    @overload
    def getVertices(self, arg0: int) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.BitmapFontCache.getVertices(int)"""
        return List[float]._wrap(super(_BitmapFontCache, self).getVertices(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.translate(float,float)"""
        super(_BitmapFontCache, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.BitmapFontCache.getColor()"""
        return 'graphics.Color'._wrap(super(BitmapFontCache, self).getColor())

    @overload
    def getLayouts(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.GlyphLayout> com.badlogic.gdx.graphics.g2d.BitmapFontCache.getLayouts()"""
        return 'utils.Array'._wrap(super(BitmapFontCache, self).getLayouts())

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).setText(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7)))

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool, arg8: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'._wrap(super(_BitmapFontCache, self).addText(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7), arg8))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFontCache.getX()"""
        return float._wrap(super(BitmapFontCache, self).getX())

    @overload
    def setColors(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(float)"""
        super(_BitmapFontCache, self).setColors(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.GlyphLayout as _GlyphLayout_GlyphRun
_GlyphRun = _GlyphLayout_GlyphRun.GlyphRun
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GlyphRun():
    """com.badlogic.gdx.graphics.g2d.GlyphLayout.GlyphRun"""
 
    @staticmethod
    def _wrap(java_value: _GlyphRun) -> 'GlyphRun':
        return GlyphRun(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GlyphRun):
        """
        Dynamic initializer for GlyphRun.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GlyphRun__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GlyphRun__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun.reset()"""
        super(GlyphRun, self).reset()

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
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun()"""
        val = _GlyphRun()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun()"""
        val = _GlyphRun()
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
        """public java.lang.String com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun.toString()"""
        return str._wrap(super(GlyphRun, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_TextureAtlasData
_TextureAtlasData = _TextureAtlas_TextureAtlasData.TextureAtlasData
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureAtlasData():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.TextureAtlasData"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlasData) -> 'TextureAtlasData':
        return TextureAtlasData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlasData):
        """
        Dynamic initializer for TextureAtlasData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlasData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlasData__wrapper":
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
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData()"""
        val = _TextureAtlasData()
        self.__wrapper = val

    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region> com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData.getRegions()"""
        return 'utils.Array'._wrap(super(TextureAtlasData, self).getRegions())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _TextureAtlasData(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

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
    def load(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        super(_TextureAtlasData, self).load(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData()"""
        val = _TextureAtlasData()
        self.__wrapper = val

    @overload
    def getPages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page> com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData.getPages()"""
        return 'utils.Array'._wrap(super(TextureAtlasData, self).getPages())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas_TextureAtlasData_Region
_Region = _TextureAtlas_TextureAtlasData_Region.TextureAtlasData.Region
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Region():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.TextureAtlasData.Region"""
 
    @staticmethod
    def _wrap(java_value: _Region) -> 'Region':
        return Region(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Region):
        """
        Dynamic initializer for Region.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Region__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Region__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region()"""
        val = _Region()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region()"""
        val = _Region()
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
    def findValue(self, arg0: str) -> List[int]:
        """public int[] com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region.findValue(java.lang.String)"""
        return List[int]._wrap(super(_Region, self).findValue(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide
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
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpawnEllipseSide
_SpawnEllipseSide = _ParticleEmitter_SpawnEllipseSide.SpawnEllipseSide
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpawnEllipseSide():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpawnEllipseSide"""
 
    @staticmethod
    def _wrap(java_value: _SpawnEllipseSide) -> 'SpawnEllipseSide':
        return SpawnEllipseSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpawnEllipseSide):
        """
        Dynamic initializer for SpawnEllipseSide.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpawnEllipseSide__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpawnEllipseSide__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['SpawnEllipseSide']:
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide.values()"""
        return List[SpawnEllipseSide]._wrap(_SpawnEllipseSide.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SpawnEllipseSide':
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide.valueOf(java.lang.String)"""
        return SpawnEllipseSide._wrap(_SpawnEllipseSide.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$PixmapPackerRectangle
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_PixmapPackerRectangle
_PixmapPackerRectangle = _PixmapPacker_PixmapPackerRectangle.PixmapPackerRectangle
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapPackerRectangle():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.PixmapPackerRectangle"""
 
    @staticmethod
    def _wrap(java_value: _PixmapPackerRectangle) -> 'PixmapPackerRectangle':
        return PixmapPackerRectangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapPackerRectangle):
        """
        Dynamic initializer for PixmapPackerRectangle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapPackerRectangle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapPackerRectangle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def contains(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(super(_math.Rectangle, self).contains(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Rectangle.hashCode()"""
        return int._wrap(super(math.Rectangle, self).hashCode())

    @overload
    def setSize(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setSize(_float.valueOf(arg0)))

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getWidth()"""
        return float._wrap(super(math.Rectangle, self).getWidth())

    @overload
    def setPosition(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(com.badlogic.gdx.math.Vector2)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setPosition(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def merge(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).merge(arg0))

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getHeight()"""
        return float._wrap(super(math.Rectangle, self).getHeight())

    @overload
    def fromString(self, arg0: str) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fromString(java.lang.String)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).fromString(arg0))

    @overload
    def setCenter(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(com.badlogic.gdx.math.Vector2)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setCenter(arg0))

    @overload
    def setWidth(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setWidth(float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setWidth(_float.valueOf(arg0)))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(float,float)"""
        return bool._wrap(super(_math.Rectangle, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setSize(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float,float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def merge(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2[])"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).merge(arg0))

    @overload
    def setHeight(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setHeight(float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setHeight(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def contains(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Circle)"""
        return bool._wrap(super(_math.Rectangle, self).contains(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def perimeter(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.perimeter()"""
        return float._wrap(super(math.Rectangle, self).perimeter())

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getX()"""
        return float._wrap(super(math.Rectangle, self).getX())

    @overload
    def getPosition(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getPosition(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Rectangle, self).getPosition(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(float,float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setCenter(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(float,float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setCenter(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Rectangle.toString()"""
        return str._wrap(super(math.Rectangle, self).toString())

    @overload
    def overlaps(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.overlaps(com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(super(_math.Rectangle, self).overlaps(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(float,float,float,float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Rectangle, self).contains(arg0))

    @overload
    def getCenter(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getCenter(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Rectangle, self).getCenter(arg0))

    @overload
    def set(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).set(arg0))

    @overload
    def merge(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).merge(arg0))

    @overload
    def setX(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setX(float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setX(_float.valueOf(arg0)))

    @override
    @overload
    def getAspectRatio(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getAspectRatio()"""
        return float._wrap(super(math.Rectangle, self).getAspectRatio())

    @overload
    def merge(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(float,float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).merge(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getSize(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getSize(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Rectangle, self).getSize(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getY()"""
        return float._wrap(super(math.Rectangle, self).getY())

    @overload
    def setY(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setY(float)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).setY(_float.valueOf(arg0)))

    @overload
    def fitOutside(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitOutside(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).fitOutside(arg0))

    @overload
    def fitInside(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitInside(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'._wrap(super(_math.Rectangle, self).fitInside(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.area()"""
        return float._wrap(super(math.Rectangle, self).area())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.equals(java.lang.Object)"""
        return bool._wrap(super(_math.Rectangle, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.CpuSpriteBatch
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.CpuSpriteBatch as _CpuSpriteBatch
_CpuSpriteBatch = _CpuSpriteBatch
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g2d.SpriteBatch as _SpriteBatch
_SpriteBatch = _SpriteBatch
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

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
 
class CpuSpriteBatch():
    """com.badlogic.gdx.graphics.g2d.CpuSpriteBatch"""
 
    @staticmethod
    def _wrap(java_value: _CpuSpriteBatch) -> 'CpuSpriteBatch':
        return CpuSpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CpuSpriteBatch):
        """
        Dynamic initializer for CpuSpriteBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CpuSpriteBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CpuSpriteBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_CpuSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(float,float,float,float)"""
        super(_SpriteBatch, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch()"""
        val = _CpuSpriteBatch()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.SpriteBatch.getPackedColor()"""
        return float._wrap(super(SpriteBatch, self).getPackedColor())

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(_SpriteBatch, self).setBlendFunctionSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

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
    def setTransformMatrix(self, arg0: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Affine2)"""
        super(_CpuSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setPackedColor(float)"""
        super(_SpriteBatch, self).setPackedColor(_float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.end()"""
        super(SpriteBatch, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.disableBlending()"""
        super(SpriteBatch, self).disableBlending()

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_SpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFunc()"""
        return int._wrap(super(SpriteBatch, self).getBlendDstFunc())

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_SpriteBatch, self).setShader(arg0)

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFunc()"""
        return int._wrap(super(SpriteBatch, self).getBlendSrcFunc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def flushAndSyncTransformMatrix(self):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.flushAndSyncTransformMatrix()"""
        super(CpuSpriteBatch, self).flushAndSyncTransformMatrix()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.flush()"""
        super(SpriteBatch, self).flush()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_SpriteBatch, self).setColor(arg0)

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'._wrap(super(CpuSpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFuncAlpha()"""
        return int._wrap(super(SpriteBatch, self).getBlendDstFuncAlpha())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _boolean.valueOf(arg10))

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFuncAlpha()"""
        return int._wrap(super(SpriteBatch, self).getBlendSrcFuncAlpha())

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _CpuSpriteBatch(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.enableBlending()"""
        super(SpriteBatch, self).enableBlending()

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.SpriteBatch.getColor()"""
        return 'graphics.Color'._wrap(super(SpriteBatch, self).getColor())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch()"""
        val = _CpuSpriteBatch()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch(int)"""
        val = _CpuSpriteBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunction(int,int)"""
        super(_SpriteBatch, self).setBlendFunction(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(_CpuSpriteBatch, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _boolean.valueOf(arg14), _boolean.valueOf(arg15))

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isDrawing()"""
        return bool._wrap(super(SpriteBatch, self).isDrawing())

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'._wrap(super(SpriteBatch, self).getShader())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.begin()"""
        super(SpriteBatch, self).begin()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.dispose()"""
        super(SpriteBatch, self).dispose()

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'._wrap(super(SpriteBatch, self).getProjectionMatrix())

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isBlendingEnabled()"""
        return bool._wrap(super(SpriteBatch, self).isBlendingEnabled())

    @staticmethod
    @overload
    def createDefaultShader() -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.createDefaultShader()"""
        return glutils.ShaderProgram._wrap(_SpriteBatch.createDefaultShader())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(_CpuSpriteBatch, self).draw(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_Page
_Page = _PixmapPacker_Page.Page
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_SkylineStrategy
_SkylineStrategy = _PixmapPacker_SkylineStrategy.SkylineStrategy
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkylineStrategy():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.SkylineStrategy"""
 
    @staticmethod
    def _wrap(java_value: _SkylineStrategy) -> 'SkylineStrategy':
        return SkylineStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkylineStrategy):
        """
        Dynamic initializer for SkylineStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkylineStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkylineStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def sort(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        super(_SkylineStrategy, self).sort(arg0)

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy()"""
        val = _SkylineStrategy()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def pack(self, arg0: 'PixmapPacker', arg1: str, arg2: 'Rectangle') -> 'Page':
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy.pack(com.badlogic.gdx.graphics.g2d.PixmapPacker,java.lang.String,com.badlogic.gdx.math.Rectangle)"""
        return 'Page'._wrap(super(_SkylineStrategy, self).pack(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy()"""
        val = _SkylineStrategy()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpawnShape
_SpawnShape = _ParticleEmitter_SpawnShape.SpawnShape
import java.lang.String as _String
_String = _String
import java.io.BufferedReader as BufferedReader
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpawnEllipseSide
_SpawnEllipseSide = _ParticleEmitter_SpawnEllipseSide.SpawnEllipseSide
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_SpawnShapeValue
_SpawnShapeValue = _ParticleEmitter_SpawnShapeValue.SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpawnShapeValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _SpawnShapeValue) -> 'SpawnShapeValue':
        return SpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpawnShapeValue):
        """
        Dynamic initializer for SpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setShape(self, arg0: 'SpawnShape'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.setShape(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape)"""
        super(_SpawnShapeValue, self).setShape(arg0)

    @overload
    def setSide(self, arg0: 'SpawnEllipseSide'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.setSide(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide)"""
        super(_SpawnShapeValue, self).setSide(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

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
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue()"""
        val = _SpawnShapeValue()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.isEdges()"""
        return bool._wrap(super(SpawnShapeValue, self).isEdges())

    @overload
    def getSide(self) -> 'SpawnEllipseSide':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.getSide()"""
        return 'SpawnEllipseSide'._wrap(super(SpawnShapeValue, self).getSide())

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.setEdges(boolean)"""
        super(_SpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getShape(self) -> 'SpawnShape':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.getShape()"""
        return 'SpawnShape'._wrap(super(SpawnShapeValue, self).getShape())

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.save(java.io.Writer) throws java.io.IOException"""
        super(_SpawnShapeValue, self).save(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_SpawnShapeValue, self).load(arg0)

    @overload
    def load(self, arg0: 'SpawnShapeValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue)"""
        super(_SpawnShapeValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue()"""
        val = _SpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont_Glyph
_Glyph = _BitmapFont_Glyph.Glyph
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Glyph():
    """com.badlogic.gdx.graphics.g2d.BitmapFont.Glyph"""
 
    @staticmethod
    def _wrap(java_value: _Glyph) -> 'Glyph':
        return Glyph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Glyph):
        """
        Dynamic initializer for Glyph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Glyph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Glyph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph()"""
        val = _Glyph()
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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getKerning(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph.getKerning(char)"""
        return int._wrap(super(_Glyph, self).getKerning(_char.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph.toString()"""
        return str._wrap(super(Glyph, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph()"""
        val = _Glyph()
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
    def setKerning(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph.setKerning(int,int)"""
        super(_Glyph, self).setKerning(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.PixmapPackerIO as _PixmapPackerIO_SaveParameters
_SaveParameters = _PixmapPackerIO_SaveParameters.SaveParameters
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SaveParameters():
    """com.badlogic.gdx.graphics.g2d.PixmapPackerIO.SaveParameters"""
 
    @staticmethod
    def _wrap(java_value: _SaveParameters) -> 'SaveParameters':
        return SaveParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SaveParameters):
        """
        Dynamic initializer for SaveParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SaveParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SaveParameters__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters()"""
        val = _SaveParameters()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters()"""
        val = _SaveParameters()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_PackStrategy
_PackStrategy = _PixmapPacker_PackStrategy.PackStrategy
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

 
class PackStrategy():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.PackStrategy"""
 
    @staticmethod
    def _wrap(java_value: _PackStrategy) -> 'PackStrategy':
        return PackStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PackStrategy):
        """
        Dynamic initializer for PackStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PackStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PackStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def sort(self, arg0: 'Array'):
        """public abstract void com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        pass

    @abstractmethod
    def pack(self, arg0: 'PixmapPacker', arg1: str, arg2: 'Rectangle'):
        """public abstract com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy.pack(com.badlogic.gdx.graphics.g2d.PixmapPacker,java.lang.String,com.badlogic.gdx.math.Rectangle)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonSprite
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.PolygonSprite as _PolygonSprite
_PolygonSprite = _PolygonSprite
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g2d.PolygonRegion as _PolygonRegion
_PolygonRegion = _PolygonRegion
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
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
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolygonSprite():
    """com.badlogic.gdx.graphics.g2d.PolygonSprite"""
 
    @staticmethod
    def _wrap(java_value: _PolygonSprite) -> 'PolygonSprite':
        return PolygonSprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonSprite):
        """
        Dynamic initializer for PolygonSprite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonSprite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonSprite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.translate(float,float)"""
        super(_PolygonSprite, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getRegion(self) -> 'PolygonRegion':
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion com.badlogic.gdx.graphics.g2d.PolygonSprite.getRegion()"""
        return 'PolygonRegion'._wrap(super(PolygonSprite, self).getRegion())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getY()"""
        return float._wrap(super(PolygonSprite, self).getY())

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getRotation()"""
        return float._wrap(super(PolygonSprite, self).getRotation())

    @overload
    def __init__(self, arg0: 'PolygonSprite'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSprite(com.badlogic.gdx.graphics.g2d.PolygonSprite)"""
        val = _PolygonSprite(arg0)
        self.__wrapper = val

    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.translateX(float)"""
        super(_PolygonSprite, self).translateX(_float.valueOf(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSprite.getColor()"""
        return 'graphics.Color'._wrap(super(PolygonSprite, self).getColor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.rotate(float)"""
        super(_PolygonSprite, self).rotate(_float.valueOf(arg0))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setY(float)"""
        super(_PolygonSprite, self).setY(_float.valueOf(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getWidth()"""
        return float._wrap(super(PolygonSprite, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'PolygonSprite'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.set(com.badlogic.gdx.graphics.g2d.PolygonSprite)"""
        super(_PolygonSprite, self).set(arg0)

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setScale(float)"""
        super(_PolygonSprite, self).setScale(_float.valueOf(arg0))

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setBounds(float,float,float,float)"""
        super(_PolygonSprite, self).setBounds(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setColor(float,float,float,float)"""
        super(_PolygonSprite, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def draw(self, arg0: 'PolygonSpriteBatch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.draw(com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch,float)"""
        super(_PolygonSprite, self).draw(arg0, _float.valueOf(arg1))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getOriginX()"""
        return float._wrap(super(PolygonSprite, self).getOriginX())

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.PolygonSprite.getVertices()"""
        return List[float]._wrap(super(PolygonSprite, self).getVertices())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getX()"""
        return float._wrap(super(PolygonSprite, self).getX())

    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.translateY(float)"""
        super(_PolygonSprite, self).translateY(_float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'PolygonSpriteBatch'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.draw(com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch)"""
        super(_PolygonSprite, self).draw(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'PolygonRegion'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSprite(com.badlogic.gdx.graphics.g2d.PolygonRegion)"""
        val = _PolygonSprite(arg0)
        self.__wrapper = val

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setPosition(float,float)"""
        super(_PolygonSprite, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PolygonSprite.getBoundingRectangle()"""
        return 'math.Rectangle'._wrap(super(PolygonSprite, self).getBoundingRectangle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setSize(float,float)"""
        super(_PolygonSprite, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setOrigin(float,float)"""
        super(_PolygonSprite, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getPackedColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSprite.getPackedColor()"""
        return 'graphics.Color'._wrap(super(PolygonSprite, self).getPackedColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_PolygonSprite, self).setColor(arg0)

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.scale(float)"""
        super(_PolygonSprite, self).scale(_float.valueOf(arg0))

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setRotation(float)"""
        super(_PolygonSprite, self).setRotation(_float.valueOf(arg0))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setX(float)"""
        super(_PolygonSprite, self).setX(_float.valueOf(arg0))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getHeight()"""
        return float._wrap(super(PolygonSprite, self).getHeight())

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getScaleX()"""
        return float._wrap(super(PolygonSprite, self).getScaleX())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getScaleY()"""
        return float._wrap(super(PolygonSprite, self).getScaleY())

    @overload
    def setRegion(self, arg0: 'PolygonRegion'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setRegion(com.badlogic.gdx.graphics.g2d.PolygonRegion)"""
        super(_PolygonSprite, self).setRegion(arg0)

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
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setScale(float,float)"""
        super(_PolygonSprite, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getOriginY()"""
        return float._wrap(super(PolygonSprite, self).getOriginY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_NumericValue
_NumericValue = _ParticleEmitter_NumericValue.NumericValue
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.io.BufferedReader as BufferedReader
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.NumericValue"""
 
    @staticmethod
    def _wrap(java_value: _NumericValue) -> 'NumericValue':
        return NumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumericValue):
        """
        Dynamic initializer for NumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue()"""
        val = _NumericValue()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'NumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue)"""
        super(_NumericValue, self).load(arg0)

    @overload
    def setValue(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.setValue(float)"""
        super(_NumericValue, self).setValue(_float.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(_NumericValue, self).save(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.getValue()"""
        return float._wrap(super(NumericValue, self).getValue())

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
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue()"""
        val = _NumericValue()
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
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_NumericValue, self).load(arg0)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_IndependentScaledNumericValue
_IndependentScaledNumericValue = _ParticleEmitter_IndependentScaledNumericValue.IndependentScaledNumericValue
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.io.BufferedReader as BufferedReader
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_RangedNumericValue
_RangedNumericValue = _ParticleEmitter_RangedNumericValue.RangedNumericValue
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ScaledNumericValue
_ScaledNumericValue = _ParticleEmitter_ScaledNumericValue.ScaledNumericValue
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndependentScaledNumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.IndependentScaledNumericValue"""
 
    @staticmethod
    def _wrap(java_value: _IndependentScaledNumericValue) -> 'IndependentScaledNumericValue':
        return IndependentScaledNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndependentScaledNumericValue):
        """
        Dynamic initializer for IndependentScaledNumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndependentScaledNumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndependentScaledNumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'IndependentScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue)"""
        super(_IndependentScaledNumericValue, self).set(arg0)

    @override
    @overload
    def getHighMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMin()"""
        return float._wrap(super(ScaledNumericValue, self).getHighMin())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(_IndependentScaledNumericValue, self).save(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def setIndependent(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.setIndependent(boolean)"""
        super(_IndependentScaledNumericValue, self).setIndependent(_boolean.valueOf(arg0))

    @override
    @overload
    def setRelative(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setRelative(boolean)"""
        super(_ScaledNumericValue, self).setRelative(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setScaling(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setScaling(float[])"""
        super(_ScaledNumericValue, self).setScaling(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @overload
    def load(self, arg0: 'IndependentScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue)"""
        super(_IndependentScaledNumericValue, self).load(arg0)

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getScale(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScale(float)"""
        return float._wrap(super(_ScaledNumericValue, self).getScale(_float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMin()"""
        return float._wrap(super(RangedNumericValue, self).getLowMin())

    @override
    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setTimeline(float[])"""
        super(_ScaledNumericValue, self).setTimeline(arg0)

    @override
    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.newLowValue()"""
        return float._wrap(super(RangedNumericValue, self).newLowValue())

    @override
    @overload
    def load(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(_ScaledNumericValue, self).load(arg0)

    @override
    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMax(float)"""
        super(_RangedNumericValue, self).setLowMax(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_IndependentScaledNumericValue, self).load(arg0)

    @override
    @overload
    def getHighMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMax()"""
        return float._wrap(super(ScaledNumericValue, self).getHighMax())

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.scale(float)"""
        super(_ScaledNumericValue, self).scale(_float.valueOf(arg0))

    @override
    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMin(float)"""
        super(_RangedNumericValue, self).setLowMin(_float.valueOf(arg0))

    @override
    @overload
    def newHighValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.newHighValue()"""
        return float._wrap(super(ScaledNumericValue, self).newHighValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def set(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(_IndependentScaledNumericValue, self).set(arg0)

    @override
    @overload
    def setHigh(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float)"""
        super(_ScaledNumericValue, self).setHigh(_float.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue()"""
        val = _IndependentScaledNumericValue()
        self.__wrapper = val

    @override
    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float,float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def isRelative(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.isRelative()"""
        return bool._wrap(super(ScaledNumericValue, self).isRelative())

    @override
    @overload
    def setHighMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMin(float)"""
        super(_ScaledNumericValue, self).setHighMin(_float.valueOf(arg0))

    @override
    @overload
    def setHighMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMax(float)"""
        super(_ScaledNumericValue, self).setHighMax(_float.valueOf(arg0))

    @overload
    def isIndependent(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.isIndependent()"""
        return bool._wrap(super(IndependentScaledNumericValue, self).isIndependent())

    @override
    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMax()"""
        return float._wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(_IndependentScaledNumericValue, self).set(arg0)

    @override
    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getTimeline()"""
        return List[float]._wrap(super(ScaledNumericValue, self).getTimeline())

    @override
    @overload
    def setHigh(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float,float)"""
        super(_ScaledNumericValue, self).setHigh(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(_RangedNumericValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue()"""
        val = _IndependentScaledNumericValue()
        self.__wrapper = val

    @override
    @overload
    def getScaling(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScaling()"""
        return List[float]._wrap(super(ScaledNumericValue, self).getScaling())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.io.BufferedReader as BufferedReader
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_ParticleValue
_ParticleValue = _ParticleEmitter_ParticleValue.ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as _ParticleEmitter_RangedNumericValue
_RangedNumericValue = _ParticleEmitter_RangedNumericValue.RangedNumericValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RangedNumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.RangedNumericValue"""
 
    @staticmethod
    def _wrap(java_value: _RangedNumericValue) -> 'RangedNumericValue':
        return RangedNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RangedNumericValue):
        """
        Dynamic initializer for RangedNumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RangedNumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RangedNumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(_RangedNumericValue, self).load(arg0)

    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMin(float)"""
        super(_RangedNumericValue, self).setLowMin(_float.valueOf(arg0))

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(_ParticleValue, self).setAlwaysActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(_RangedNumericValue, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue()"""
        val = _RangedNumericValue()
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(_RangedNumericValue, self).save(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue()"""
        val = _RangedNumericValue()
        self.__wrapper = val

    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float,float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMin()"""
        return float._wrap(super(RangedNumericValue, self).getLowMin())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.scale(float)"""
        super(_RangedNumericValue, self).scale(_float.valueOf(arg0))

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool._wrap(super(ParticleValue, self).isAlwaysActive())

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
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(_RangedNumericValue, self).load(arg0)

    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMax(float)"""
        super(_RangedNumericValue, self).setLowMax(_float.valueOf(arg0))

    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.newLowValue()"""
        return float._wrap(super(RangedNumericValue, self).newLowValue())

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
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMax()"""
        return float._wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.DistanceFieldFont
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.BitmapFontCache as _BitmapFontCache
_BitmapFontCache = _BitmapFontCache
import com.badlogic.gdx.graphics.g2d.GlyphLayout as _GlyphLayout
_GlyphLayout = _GlyphLayout
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.g2d.DistanceFieldFont as _DistanceFieldFont
_DistanceFieldFont = _DistanceFieldFont
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont_BitmapFontData
_BitmapFontData = _BitmapFont_BitmapFontData.BitmapFontData
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont
_BitmapFont = _BitmapFont
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistanceFieldFont():
    """com.badlogic.gdx.graphics.g2d.DistanceFieldFont"""
 
    @staticmethod
    def _wrap(java_value: _DistanceFieldFont) -> 'DistanceFieldFont':
        return DistanceFieldFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistanceFieldFont):
        """
        Dynamic initializer for DistanceFieldFont.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistanceFieldFont__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistanceFieldFont__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDistanceFieldSmoothing(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.DistanceFieldFont.getDistanceFieldSmoothing()"""
        return float._wrap(super(DistanceFieldFont, self).getDistanceFieldSmoothing())

    @override
    @overload
    def getCapHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getCapHeight()"""
        return float._wrap(super(BitmapFont, self).getCapHeight())

    @override
    @overload
    def getCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.BitmapFont.getCache()"""
        return 'BitmapFontCache'._wrap(super(BitmapFont, self).getCache())

    @overload
    def getRegion(self, arg0: int) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion(int)"""
        return 'TextureRegion'._wrap(super(_BitmapFont, self).getRegion(_int.valueOf(arg0)))

    @override
    @overload
    def getAscent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getAscent()"""
        return float._wrap(super(BitmapFont, self).getAscent())

    @override
    @overload
    def setFixedWidthGlyphs(self, arg0: 'CharSequence'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setFixedWidthGlyphs(java.lang.CharSequence)"""
        super(_BitmapFont, self).setFixedWidthGlyphs(arg0)

    @override
    @overload
    def getLineHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getLineHeight()"""
        return float._wrap(super(BitmapFont, self).getLineHeight())

    @override
    @overload
    def setUseIntegerPositions(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setUseIntegerPositions(boolean)"""
        super(_BitmapFont, self).setUseIntegerPositions(_boolean.valueOf(arg0))

    @override
    @overload
    def newFontCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.DistanceFieldFont.newFontCache()"""
        return 'BitmapFontCache'._wrap(super(DistanceFieldFont, self).newFontCache())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean,boolean)"""
        val = _DistanceFieldFont(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.BitmapFont.getColor()"""
        return 'graphics.Color'._wrap(super(BitmapFont, self).getColor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setOwnsTexture(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setOwnsTexture(boolean)"""
        super(_BitmapFont, self).setOwnsTexture(_boolean.valueOf(arg0))

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_BitmapFont, self).setColor(arg0)

    @overload
    def setDistanceFieldSmoothing(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.DistanceFieldFont.setDistanceFieldSmoothing(float)"""
        super(_DistanceFieldFont, self).setDistanceFieldSmoothing(_float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: float, arg5: int, arg6: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _boolean.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _DistanceFieldFont(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getData(self) -> 'BitmapFontData':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData com.badlogic.gdx.graphics.g2d.BitmapFont.getData()"""
        return 'BitmapFontData'._wrap(super(BitmapFont, self).getData())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _DistanceFieldFont(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getSpaceXadvance(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getSpaceXadvance()"""
        return float._wrap(super(BitmapFont, self).getSpaceXadvance())

    @staticmethod
    @overload
    def createDistanceFieldShader() -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.DistanceFieldFont.createDistanceFieldShader()"""
        return glutils.ShaderProgram._wrap(_DistanceFieldFont.createDistanceFieldShader())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(float,float,float,float)"""
        super(_BitmapFont, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isFlipped(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.isFlipped()"""
        return bool._wrap(super(BitmapFont, self).isFlipped())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: 'GlyphLayout', arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool, arg9: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _boolean.valueOf(arg8), arg9))

    @override
    @overload
    def usesIntegerPositions(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.usesIntegerPositions()"""
        return bool._wrap(super(BitmapFont, self).usesIntegerPositions())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _DistanceFieldFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = _DistanceFieldFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion> com.badlogic.gdx.graphics.g2d.BitmapFont.getRegions()"""
        return 'utils.Array'._wrap(super(BitmapFont, self).getRegions())

    @override
    @overload
    def getRegion(self) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion()"""
        return 'TextureRegion'._wrap(super(BitmapFont, self).getRegion())

    @override
    @overload
    def ownsTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.ownsTexture()"""
        return bool._wrap(super(BitmapFont, self).ownsTexture())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.dispose()"""
        super(BitmapFont, self).dispose()

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def getXHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getXHeight()"""
        return float._wrap(super(BitmapFont, self).getXHeight())

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleX()"""
        return float._wrap(super(BitmapFont, self).getScaleX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont.toString()"""
        return str._wrap(super(BitmapFont, self).toString())

    @override
    @overload
    def getDescent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getDescent()"""
        return float._wrap(super(BitmapFont, self).getDescent())

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'Array', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion>,boolean)"""
        val = _DistanceFieldFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = _DistanceFieldFont(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle)"""
        val = _DistanceFieldFont(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'._wrap(super(_BitmapFont, self).draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _boolean.valueOf(arg8)))

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleY()"""
        return float._wrap(super(BitmapFont, self).getScaleY()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureRegion
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
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
 
class TextureRegion():
    """com.badlogic.gdx.graphics.g2d.TextureRegion"""
 
    @staticmethod
    def _wrap(java_value: _TextureRegion) -> 'TextureRegion':
        return TextureRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureRegion):
        """
        Dynamic initializer for TextureRegion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureRegion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureRegion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(_TextureRegion, self).setRegionY(_int.valueOf(arg0))

    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(_TextureRegion, self).setRegionHeight(_int.valueOf(arg0))

    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV2(float)"""
        super(_TextureRegion, self).setV2(_float.valueOf(arg0))

    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool._wrap(super(TextureRegion, self).isFlipX())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion()"""
        val = _TextureRegion()
        self.__wrapper = val

    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int._wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float._wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(float,float,float,float)"""
        super(_TextureRegion, self).setRegion(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int._wrap(super(TextureRegion, self).getRegionX())

    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool._wrap(super(TextureRegion, self).isFlipY())

    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float._wrap(super(TextureRegion, self).getU2())

    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU(float)"""
        super(_TextureRegion, self).setU(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        val = _TextureRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float._wrap(super(TextureRegion, self).getV2())

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = _TextureRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(_TextureRegion, self).setRegionX(_int.valueOf(arg0))

    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(_TextureRegion, self).setRegionWidth(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        val = _TextureRegion(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))
        self.__wrapper = val

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]]._wrap(_TextureRegion.split(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.flip(boolean,boolean)"""
        super(_TextureRegion, self).flip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU2(float)"""
        super(_TextureRegion, self).setU2(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV(float)"""
        super(_TextureRegion, self).setV(_float.valueOf(arg0))

    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setTexture(arg0)

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture)"""
        val = _TextureRegion(arg0)
        self.__wrapper = val

    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int._wrap(super(TextureRegion, self).getRegionHeight())

    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int._wrap(super(TextureRegion, self).getRegionWidth())

    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float._wrap(super(TextureRegion, self).getV())

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']]._wrap(super(_TextureRegion, self).split(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _TextureRegion(arg0)
        self.__wrapper = val

    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.scroll(float,float)"""
        super(_TextureRegion, self).scroll(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'._wrap(super(TextureRegion, self).getTexture())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion()"""
        val = _TextureRegion()
        self.__wrapper = val

    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegion, self).setRegion(arg0)

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture,int,int)"""
        val = _TextureRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(_TextureRegion, self).setRegion(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(_TextureRegion, self).setRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonRegionLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.PolygonRegionLoader as _PolygonRegionLoader
_PolygonRegionLoader = _PolygonRegionLoader
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import com.badlogic.gdx.graphics.g2d.PolygonRegion as _PolygonRegion
_PolygonRegion = _PolygonRegion
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolygonRegionLoader():
    """com.badlogic.gdx.graphics.g2d.PolygonRegionLoader"""
 
    @staticmethod
    def _wrap(java_value: _PolygonRegionLoader) -> 'PolygonRegionLoader':
        return PolygonRegionLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonRegionLoader):
        """
        Dynamic initializer for PolygonRegionLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonRegionLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonRegionLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'PolygonRegionParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters)"""
        return 'utils.Array'._wrap(super(_PolygonRegionLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _PolygonRegionLoader(arg0)
        self.__wrapper = val

    @overload
    def load(self, arg0: 'TextureRegion', arg1: 'FileHandle') -> 'PolygonRegion':
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.load(com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.files.FileHandle)"""
        return 'PolygonRegion'._wrap(super(_PolygonRegionLoader, self).load(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader()"""
        val = _PolygonRegionLoader()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader()"""
        val = _PolygonRegionLoader()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'PolygonRegionParameters') -> 'PolygonRegion':
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters)"""
        return 'PolygonRegion'._wrap(super(_PolygonRegionLoader, self).load(arg0, arg1, arg2, arg3))

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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Animation
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.Animation as _Animation
_Animation = _Animation
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g2d.Animation as _Animation_PlayMode
_PlayMode = _Animation_PlayMode.PlayMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Animation():
    """com.badlogic.gdx.graphics.g2d.Animation"""
 
    @staticmethod
    def _wrap(java_value: _Animation) -> 'Animation':
        return Animation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Animation):
        """
        Dynamic initializer for Animation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Animation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Animation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAnimationDuration(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Animation.getAnimationDuration()"""
        return float._wrap(super(Animation, self).getAnimationDuration())

    @overload
    def getKeyFrame(self, arg0: float, arg1: bool) -> object:
        """public T com.badlogic.gdx.graphics.g2d.Animation.getKeyFrame(float,boolean)"""
        return object._wrap(super(_Animation, self).getKeyFrame(_float.valueOf(arg0), _boolean.valueOf(arg1)))

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
    def getKeyFrame(self, arg0: float) -> object:
        """public T com.badlogic.gdx.graphics.g2d.Animation.getKeyFrame(float)"""
        return object._wrap(super(_Animation, self).getKeyFrame(_float.valueOf(arg0)))

    @overload
    def setFrameDuration(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Animation.setFrameDuration(float)"""
        super(_Animation, self).setFrameDuration(_float.valueOf(arg0))

    @overload
    def isAnimationFinished(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.Animation.isAnimationFinished(float)"""
        return bool._wrap(super(_Animation, self).isAnimationFinished(_float.valueOf(arg0)))

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
    def getKeyFrameIndex(self, arg0: float) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Animation.getKeyFrameIndex(float)"""
        return int._wrap(super(_Animation, self).getKeyFrameIndex(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: 'Array'):
        """public com.badlogic.gdx.graphics.g2d.Animation(float,com.badlogic.gdx.utils.Array<? extends T>)"""
        val = _Animation(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: 'Array', arg2: 'PlayMode'):
        """public com.badlogic.gdx.graphics.g2d.Animation(float,com.badlogic.gdx.utils.Array<? extends T>,com.badlogic.gdx.graphics.g2d.Animation$PlayMode)"""
        val = _Animation(_float.valueOf(arg0), arg1, arg2)
        self.__wrapper = val

    @overload
    def getKeyFrames(self) -> List[object]:
        """public T[] com.badlogic.gdx.graphics.g2d.Animation.getKeyFrames()"""
        return List[object]._wrap(super(Animation, self).getKeyFrames())

    @overload
    def setPlayMode(self, arg0: 'PlayMode'):
        """public void com.badlogic.gdx.graphics.g2d.Animation.setPlayMode(com.badlogic.gdx.graphics.g2d.Animation$PlayMode)"""
        super(_Animation, self).setPlayMode(arg0)

    @overload
    def getPlayMode(self) -> 'PlayMode':
        """public com.badlogic.gdx.graphics.g2d.Animation$PlayMode com.badlogic.gdx.graphics.g2d.Animation.getPlayMode()"""
        return 'PlayMode'._wrap(super(Animation, self).getPlayMode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, *arg1: object):
        """public com.badlogic.gdx.graphics.g2d.Animation(float,T...)"""
        val = _Animation(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def getFrameDuration(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Animation.getFrameDuration()"""
        return float._wrap(super(Animation, self).getFrameDuration())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$Page
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g2d.PixmapPacker as _PixmapPacker_Page
_Page = _PixmapPacker_Page.Page
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.utils.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Page():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.Page"""
 
    @staticmethod
    def _wrap(java_value: _Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Page):
        """
        Dynamic initializer for Page.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Page__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Page__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.getTexture()"""
        return 'graphics.Texture'._wrap(super(Page, self).getTexture())

    @overload
    def getRects(self) -> 'utils.OrderedMap':
        """public com.badlogic.gdx.utils.OrderedMap<java.lang.String, com.badlogic.gdx.graphics.g2d.PixmapPacker$PixmapPackerRectangle> com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.getRects()"""
        return 'utils.OrderedMap'._wrap(super(Page, self).getRects())

    @overload
    def getPixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.getPixmap()"""
        return 'graphics.Pixmap'._wrap(super(Page, self).getPixmap())

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

    @overload
    def updateTexture(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.updateTexture(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        return bool._wrap(super(_Page, self).updateTexture(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'PixmapPacker'):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$Page(com.badlogic.gdx.graphics.g2d.PixmapPacker)"""
        val = _Page(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Sprite
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g2d.Sprite as _Sprite
_Sprite = _Sprite
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Sprite():
    """com.badlogic.gdx.graphics.g2d.Sprite"""
 
    @staticmethod
    def _wrap(java_value: _Sprite) -> 'Sprite':
        return Sprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Sprite):
        """
        Dynamic initializer for Sprite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Sprite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Sprite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setTexture(arg0)

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float)"""
        super(_Sprite, self).setScale(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scale(float)"""
        super(_Sprite, self).scale(_float.valueOf(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleX()"""
        return float._wrap(super(Sprite, self).getScaleX())

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(_TextureRegion, self).setRegionY(_int.valueOf(arg0))

    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateX(float)"""
        super(_Sprite, self).translateX(_float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(_TextureRegion, self).setRegion(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getWidth()"""
        return float._wrap(super(Sprite, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setOriginCenter(self):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginCenter()"""
        super(Sprite, self).setOriginCenter()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.Sprite.getBoundingRectangle()"""
        return 'math.Rectangle'._wrap(super(Sprite, self).getBoundingRectangle())

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginY()"""
        return float._wrap(super(Sprite, self).getOriginY())

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scroll(float,float)"""
        super(_Sprite, self).scroll(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'._wrap(super(TextureRegion, self).getTexture())

    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPackedColor(float)"""
        super(_Sprite, self).setPackedColor(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setAlpha(float)"""
        super(_Sprite, self).setAlpha(_float.valueOf(arg0))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginX()"""
        return float._wrap(super(Sprite, self).getOriginX())

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.Texture,int,int)"""
        val = _Sprite(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int._wrap(super(TextureRegion, self).getRegionX())

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setBounds(float,float,float,float)"""
        super(_Sprite, self).setBounds(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getX()"""
        return float._wrap(super(Sprite, self).getX())

    @overload
    def setCenterX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterX(float)"""
        super(_Sprite, self).setCenterX(_float.valueOf(arg0))

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float._wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int._wrap(super(TextureRegion, self).getRegionY())

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.Texture)"""
        val = _Sprite(arg0)
        self.__wrapper = val

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setX(float)"""
        super(_Sprite, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.flip(boolean,boolean)"""
        super(_Sprite, self).flip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(_TextureRegion, self).setRegionX(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleY()"""
        return float._wrap(super(Sprite, self).getScaleY())

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int._wrap(super(TextureRegion, self).getRegionWidth())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _Sprite(arg0)
        self.__wrapper = val

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(_TextureRegion, self).setRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        val = _Sprite(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getY()"""
        return float._wrap(super(Sprite, self).getY())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.Sprite()"""
        val = _Sprite()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(float,float,float,float)"""
        super(_Sprite, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU(float)"""
        super(_Sprite, self).setU(_float.valueOf(arg0))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float._wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setOriginBasedPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginBasedPosition(float,float)"""
        super(_Sprite, self).setOriginBasedPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool._wrap(super(TextureRegion, self).isFlipY())

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU2(float)"""
        super(_Sprite, self).setU2(_float.valueOf(arg0))

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.Sprite.getVertices()"""
        return List[float]._wrap(super(Sprite, self).getVertices())

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRegion(float,float,float,float)"""
        super(_Sprite, self).setRegion(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getRotation()"""
        return float._wrap(super(Sprite, self).getRotation())

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float._wrap(super(TextureRegion, self).getU())

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translate(float,float)"""
        super(_Sprite, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_Sprite, self).draw(arg0, _float.valueOf(arg1))

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPosition(float,float)"""
        super(_Sprite, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float._wrap(super(TextureRegion, self).getV2())

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(_TextureRegion, self).setRegionWidth(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = _Sprite(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setY(float)"""
        super(_Sprite, self).setY(_float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(_Sprite, self).draw(arg0)

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int._wrap(super(TextureRegion, self).getRegionHeight())

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(_TextureRegion, self).setRegion(arg0)

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOrigin(float,float)"""
        super(_Sprite, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def set(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.set(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(_Sprite, self).set(arg0)

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate(float)"""
        super(_Sprite, self).rotate(_float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegion, self).setRegion(arg0)

    @overload
    def rotate90(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate90(boolean)"""
        super(_Sprite, self).rotate90(_boolean.valueOf(arg0))

    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setFlip(boolean,boolean)"""
        super(_Sprite, self).setFlip(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Sprite'):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.g2d.Sprite)"""
        val = _Sprite(arg0)
        self.__wrapper = val

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRotation(float)"""
        super(_Sprite, self).setRotation(_float.valueOf(arg0))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Sprite, self).setColor(arg0)

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]]._wrap(_TextureRegion.split(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Sprite.getColor()"""
        return 'graphics.Color'._wrap(super(Sprite, self).getColor())

    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateY(float)"""
        super(_Sprite, self).translateY(_float.valueOf(arg0))

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV(float)"""
        super(_Sprite, self).setV(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.Sprite()"""
        val = _Sprite()
        self.__wrapper = val

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getHeight()"""
        return float._wrap(super(Sprite, self).getHeight())

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float,float)"""
        super(_Sprite, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setCenterY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterY(float)"""
        super(_Sprite, self).setCenterY(_float.valueOf(arg0))

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']]._wrap(super(_TextureRegion, self).split(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setSize(float,float)"""
        super(_Sprite, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool._wrap(super(TextureRegion, self).isFlipX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setCenter(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenter(float,float)"""
        super(_Sprite, self).setCenter(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV2(float)"""
        super(_Sprite, self).setV2(_float.valueOf(arg0))

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(_TextureRegion, self).setRegionHeight(_int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPackerIO
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import com.badlogic.gdx.graphics.g2d.PixmapPackerIO as _PixmapPackerIO
_PixmapPackerIO = _PixmapPackerIO
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapPackerIO():
    """com.badlogic.gdx.graphics.g2d.PixmapPackerIO"""
 
    @staticmethod
    def _wrap(java_value: _PixmapPackerIO) -> 'PixmapPackerIO':
        return PixmapPackerIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapPackerIO):
        """
        Dynamic initializer for PixmapPackerIO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapPackerIO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapPackerIO__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def save(self, arg0: 'FileHandle', arg1: 'PixmapPacker'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPackerIO.save(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PixmapPacker) throws java.io.IOException"""
        super(_PixmapPackerIO, self).save(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO()"""
        val = _PixmapPackerIO()
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
    def save(self, arg0: 'FileHandle', arg1: 'PixmapPacker', arg2: 'SaveParameters'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPackerIO.save(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PixmapPacker,com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters) throws java.io.IOException"""
        super(_PixmapPackerIO, self).save(arg0, arg1, arg2)

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
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO()"""
        val = _PixmapPackerIO()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Animation$PlayMode
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
import com.badlogic.gdx.graphics.g2d.Animation as _Animation_PlayMode
_PlayMode = _Animation_PlayMode.PlayMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayMode():
    """com.badlogic.gdx.graphics.g2d.Animation.PlayMode"""
 
    @staticmethod
    def _wrap(java_value: _PlayMode) -> 'PlayMode':
        return PlayMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayMode):
        """
        Dynamic initializer for PlayMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayMode__wrapper":
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
    def values() -> List['PlayMode']:
        """public static com.badlogic.gdx.graphics.g2d.Animation$PlayMode[] com.badlogic.gdx.graphics.g2d.Animation$PlayMode.values()"""
        return List[PlayMode]._wrap(_PlayMode.values())

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
    def valueOf(arg0: str) -> 'PlayMode':
        """public static com.badlogic.gdx.graphics.g2d.Animation$PlayMode com.badlogic.gdx.graphics.g2d.Animation$PlayMode.valueOf(java.lang.String)"""
        return PlayMode._wrap(_PlayMode.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters
import com.badlogic.gdx.graphics.g2d.PolygonRegionLoader as _PolygonRegionLoader_PolygonRegionParameters
_PolygonRegionParameters = _PolygonRegionLoader_PolygonRegionParameters.PolygonRegionParameters
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolygonRegionParameters():
    """com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.PolygonRegionParameters"""
 
    @staticmethod
    def _wrap(java_value: _PolygonRegionParameters) -> 'PolygonRegionParameters':
        return PolygonRegionParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonRegionParameters):
        """
        Dynamic initializer for PolygonRegionParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonRegionParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonRegionParameters__wrapper":
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
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters()"""
        val = _PolygonRegionParameters()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters()"""
        val = _PolygonRegionParameters()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat
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
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g2d.PixmapPackerIO as _PixmapPackerIO_ImageFormat
_ImageFormat = _PixmapPackerIO_ImageFormat.ImageFormat
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImageFormat():
    """com.badlogic.gdx.graphics.g2d.PixmapPackerIO.ImageFormat"""
 
    @staticmethod
    def _wrap(java_value: _ImageFormat) -> 'ImageFormat':
        return ImageFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImageFormat):
        """
        Dynamic initializer for ImageFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImageFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImageFormat__wrapper":
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

    @overload
    def getExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat.getExtension()"""
        return str._wrap(super(ImageFormat, self).getExtension())

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
    def values() -> List['ImageFormat']:
        """public static com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat[] com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat.values()"""
        return List[ImageFormat]._wrap(_ImageFormat.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ImageFormat':
        """public static com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat.valueOf(java.lang.String)"""
        return ImageFormat._wrap(_ImageFormat.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Batch
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
from builtins import float
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class Batch():
    """com.badlogic.gdx.graphics.g2d.Batch"""
 
    @staticmethod
    def _wrap(java_value: _Batch) -> 'Batch':
        return Batch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Batch):
        """
        Dynamic initializer for Batch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Batch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Batch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def enableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.enableBlending()"""
        pass

    @abstractmethod
    def setColor(self, arg0: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        pass

    @abstractmethod
    def getTransformMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getTransformMatrix()"""
        pass

    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.begin()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        pass

    @abstractmethod
    def getShader(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.Batch.getShader()"""
        pass

    @abstractmethod
    def getBlendDstFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFunc()"""
        pass

    @abstractmethod
    def getColor(self, ):
        """public abstract com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Batch.getColor()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        pass

    @abstractmethod
    def getProjectionMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getProjectionMatrix()"""
        pass

    @abstractmethod
    def isDrawing(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isDrawing()"""
        pass

    @abstractmethod
    def getBlendSrcFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFuncAlpha()"""
        pass

    @abstractmethod
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunctionSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(float,float,float,float)"""
        pass

    @abstractmethod
    def setPackedColor(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setPackedColor(float)"""
        pass

    @abstractmethod
    def getBlendSrcFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFunc()"""
        pass

    @abstractmethod
    def disableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.disableBlending()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def setShader(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.flush()"""
        pass

    @abstractmethod
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        pass

    @abstractmethod
    def isBlendingEnabled(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isBlendingEnabled()"""
        pass

    @abstractmethod
    def setBlendFunction(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunction(int,int)"""
        pass

    @abstractmethod
    def getBlendDstFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFuncAlpha()"""
        pass

    @abstractmethod
    def getPackedColor(self, ):
        """public abstract float com.badlogic.gdx.graphics.g2d.Batch.getPackedColor()"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.end()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Gdx2DPixmap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import com.badlogic.gdx.graphics.g2d.Gdx2DPixmap as _Gdx2DPixmap
_Gdx2DPixmap = _Gdx2DPixmap
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Gdx2DPixmap():
    """com.badlogic.gdx.graphics.g2d.Gdx2DPixmap"""
 
    @staticmethod
    def _wrap(java_value: _Gdx2DPixmap) -> 'Gdx2DPixmap':
        return Gdx2DPixmap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Gdx2DPixmap):
        """
        Dynamic initializer for Gdx2DPixmap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Gdx2DPixmap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Gdx2DPixmap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def fillTriangle(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.fillTriangle(int,int,int,int,int,int,int)"""
        super(_Gdx2DPixmap, self).fillTriangle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def getFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getFormat()"""
        return int._wrap(super(Gdx2DPixmap, self).getFormat())

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getWidth()"""
        return int._wrap(super(Gdx2DPixmap, self).getWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setScale(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.setScale(int)"""
        super(_Gdx2DPixmap, self).setScale(_int.valueOf(arg0))

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getHeight()"""
        return int._wrap(super(Gdx2DPixmap, self).getHeight())

    @overload
    def drawCircle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawCircle(int,int,int,int)"""
        super(_Gdx2DPixmap, self).drawCircle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setBlend(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.setBlend(int)"""
        super(_Gdx2DPixmap, self).setBlend(_int.valueOf(arg0))

    @overload
    def drawRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawRect(int,int,int,int,int)"""
        super(_Gdx2DPixmap, self).drawRect(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def fillRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.fillRect(int,int,int,int,int)"""
        super(_Gdx2DPixmap, self).fillRect(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(java.nio.ByteBuffer,int,int,int) throws java.io.IOException"""
        val = _Gdx2DPixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def newPixmap(arg0: 'InputStream', arg1: int) -> 'Gdx2DPixmap':
        """public static com.badlogic.gdx.graphics.g2d.Gdx2DPixmap com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.newPixmap(java.io.InputStream,int)"""
        return Gdx2DPixmap._wrap(_Gdx2DPixmap.newPixmap(arg0, _int.valueOf(arg1)))

    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getGLType()"""
        return int._wrap(super(Gdx2DPixmap, self).getGLType())

    @overload
    def drawPixmap(self, arg0: 'Gdx2DPixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawPixmap(com.badlogic.gdx.graphics.g2d.Gdx2DPixmap,int,int,int,int,int,int,int,int)"""
        super(_Gdx2DPixmap, self).drawPixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @overload
    def drawLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawLine(int,int,int,int,int)"""
        super(_Gdx2DPixmap, self).drawLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.clear(int)"""
        super(_Gdx2DPixmap, self).clear(_int.valueOf(arg0))

    @overload
    def getGLFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getGLFormat()"""
        return int._wrap(super(Gdx2DPixmap, self).getGLFormat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer', arg1: 'long'):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(java.nio.ByteBuffer,long[])"""
        val = _Gdx2DPixmap(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(int,int,int) throws com.badlogic.gdx.utils.GdxRuntimeException"""
        val = _Gdx2DPixmap(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getPixels(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getPixels()"""
        return 'ByteBuffer'._wrap(super(Gdx2DPixmap, self).getPixels())

    @overload
    def drawPixmap(self, arg0: 'Gdx2DPixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawPixmap(com.badlogic.gdx.graphics.g2d.Gdx2DPixmap,int,int,int,int,int,int)"""
        super(_Gdx2DPixmap, self).drawPixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @staticmethod
    @overload
    def newPixmap(arg0: int, arg1: int, arg2: int) -> 'Gdx2DPixmap':
        """public static com.badlogic.gdx.graphics.g2d.Gdx2DPixmap com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.newPixmap(int,int,int)"""
        return Gdx2DPixmap._wrap(_Gdx2DPixmap.newPixmap(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toGlType(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.toGlType(int)"""
        return int._wrap(_Gdx2DPixmap.toGlType(_int.valueOf(arg0)))

    @overload
    def setPixel(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.setPixel(int,int,int)"""
        super(_Gdx2DPixmap, self).setPixel(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(byte[],int,int,int) throws java.io.IOException"""
        val = _Gdx2DPixmap(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @staticmethod
    @overload
    def toGlFormat(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.toGlFormat(int)"""
        return int._wrap(_Gdx2DPixmap.toGlFormat(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def fillCircle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.fillCircle(int,int,int,int)"""
        super(_Gdx2DPixmap, self).fillCircle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getFormatString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getFormatString()"""
        return str._wrap(super(Gdx2DPixmap, self).getFormatString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.dispose()"""
        super(Gdx2DPixmap, self).dispose()

    @staticmethod
    @overload
    def getFailureReason() -> str:
        """public static native java.lang.String com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getFailureReason()"""
        return str._wrap(_Gdx2DPixmap.getFailureReason())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getGLInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getGLInternalFormat()"""
        return int._wrap(super(Gdx2DPixmap, self).getGLInternalFormat())

    @overload
    def getPixel(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getPixel(int,int)"""
        return int._wrap(super(_Gdx2DPixmap, self).getPixel(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'InputStream', arg1: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(java.io.InputStream,int) throws java.io.IOException"""
        val = _Gdx2DPixmap(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())