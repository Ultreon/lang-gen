from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import box2dLight.RayHandler as __RayHandler
__RayHandler = __RayHandler
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
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
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
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
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import int
 
class RayHandler(pygdx.__Disposable, utils.Disposable):
    """box2dLight.RayHandler"""
 
    @staticmethod
    def __wrap(java_value: __RayHandler) -> 'RayHandler':
        return RayHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RayHandler):
        """
        Dynamic initializer for RayHandler.
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
    def pointAtLight(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.RayHandler.pointAtLight(float,float)"""
        return bool.__wrap(super(__RayHandler, self).pointAtLight(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def useDefaultViewport(self):
        """public void box2dLight.RayHandler.useDefaultViewport()"""
        super(RayHandler, self).useDefaultViewport()

    @overload
    def prepareRender(self):
        """public void box2dLight.RayHandler.prepareRender()"""
        super(RayHandler, self).prepareRender()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCulling(self, arg0: bool):
        """public void box2dLight.RayHandler.setCulling(boolean)"""
        super(__RayHandler, self).setCulling(__boolean.valueOf(arg0))

    @overload
    def setCombinedMatrix(self, arg0: 'Matrix4'):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__RayHandler, self).setCombinedMatrix(arg0)

    @overload
    def setCombinedMatrix(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__RayHandler, self).setCombinedMatrix(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def useCustomViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void box2dLight.RayHandler.useCustomViewport(int,int,int,int)"""
        super(__RayHandler, self).useCustomViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAmbientLight(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.RayHandler.setAmbientLight(float,float,float,float)"""
        super(__RayHandler, self).setAmbientLight(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setAmbientLight(self, arg0: 'Color'):
        """public void box2dLight.RayHandler.setAmbientLight(com.badlogic.gdx.graphics.Color)"""
        super(__RayHandler, self).setAmbientLight(arg0)

    @staticmethod
    @overload
    def setGammaCorrection(arg0: bool):
        """public static void box2dLight.RayHandler.setGammaCorrection(boolean)"""
        __RayHandler.setGammaCorrection(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def render(self):
        """public void box2dLight.RayHandler.render()"""
        super(RayHandler, self).render()

    @staticmethod
    @overload
    def getGammaCorrection() -> bool:
        """public static boolean box2dLight.RayHandler.getGammaCorrection()"""
        return bool.__wrap(__RayHandler.getGammaCorrection())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.RayHandler.dispose()"""
        super(RayHandler, self).dispose()

    @staticmethod
    @overload
    def useDiffuseLight(arg0: bool):
        """public static void box2dLight.RayHandler.useDiffuseLight(boolean)"""
        __RayHandler.useDiffuseLight(__boolean.valueOf(arg0))

    @overload
    def setAmbientLight(self, arg0: float):
        """public void box2dLight.RayHandler.setAmbientLight(float)"""
        super(__RayHandler, self).setAmbientLight(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLightShader(self, arg0: 'ShaderProgram'):
        """public void box2dLight.RayHandler.setLightShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__RayHandler, self).setLightShader(arg0)

    @overload
    def setBlurNum(self, arg0: int):
        """public void box2dLight.RayHandler.setBlurNum(int)"""
        super(__RayHandler, self).setBlurNum(__int.valueOf(arg0))

    @overload
    def pointAtShadow(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.RayHandler.pointAtShadow(float,float)"""
        return bool.__wrap(super(__RayHandler, self).pointAtShadow(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def resizeFBO(self, arg0: int, arg1: int):
        """public void box2dLight.RayHandler.resizeFBO(int,int)"""
        super(__RayHandler, self).resizeFBO(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeAll(self):
        """public void box2dLight.RayHandler.removeAll()"""
        super(RayHandler, self).removeAll()

    @overload
    def setWorld(self, arg0: 'World'):
        """public void box2dLight.RayHandler.setWorld(com.badlogic.gdx.physics.box2d.World)"""
        super(__RayHandler, self).setWorld(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setLightMapRendering(self, arg0: bool):
        """public void box2dLight.RayHandler.setLightMapRendering(boolean)"""
        super(__RayHandler, self).setLightMapRendering(__boolean.valueOf(arg0))

    @overload
    def renderOnly(self):
        """public void box2dLight.RayHandler.renderOnly()"""
        super(RayHandler, self).renderOnly()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'World'):
        """public box2dLight.RayHandler(com.badlogic.gdx.physics.box2d.World)"""
        val = __RayHandler(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def update(self):
        """public void box2dLight.RayHandler.update()"""
        super(RayHandler, self).update()

    @overload
    def setCombinedMatrix(self, arg0: 'OrthographicCamera'):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__RayHandler, self).setCombinedMatrix(arg0)

    @overload
    def setShadows(self, arg0: bool):
        """public void box2dLight.RayHandler.setShadows(boolean)"""
        super(__RayHandler, self).setShadows(__boolean.valueOf(arg0))

    @overload
    def updateAndRender(self):
        """public void box2dLight.RayHandler.updateAndRender()"""
        super(RayHandler, self).updateAndRender()

    @overload
    def getLightMapBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer box2dLight.RayHandler.getLightMapBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RayHandler, self).getLightMapBuffer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'World', arg1: int, arg2: int):
        """public box2dLight.RayHandler(com.badlogic.gdx.physics.box2d.World,int,int)"""
        val = __RayHandler(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setBlur(self, arg0: bool):
        """public void box2dLight.RayHandler.setBlur(boolean)"""
        super(__RayHandler, self).setBlur(__boolean.valueOf(arg0))

    @overload
    def getLightMapTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture box2dLight.RayHandler.getLightMapTexture()"""
        return 'graphics.Texture'.__wrap(super(RayHandler, self).getLightMapTexture())

 
 
 
# CLASS: box2dLight.RayHandler
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import box2dLight.RayHandler as __RayHandler
__RayHandler = __RayHandler
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
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
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
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
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import int
 
class RayHandler(pygdx.__Disposable, utils.Disposable):
    """box2dLight.RayHandler"""
 
    @staticmethod
    def __wrap(java_value: __RayHandler) -> 'RayHandler':
        return RayHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RayHandler):
        """
        Dynamic initializer for RayHandler.
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
    def pointAtLight(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.RayHandler.pointAtLight(float,float)"""
        return bool.__wrap(super(__RayHandler, self).pointAtLight(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def useDefaultViewport(self):
        """public void box2dLight.RayHandler.useDefaultViewport()"""
        super(RayHandler, self).useDefaultViewport()

    @overload
    def prepareRender(self):
        """public void box2dLight.RayHandler.prepareRender()"""
        super(RayHandler, self).prepareRender()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCulling(self, arg0: bool):
        """public void box2dLight.RayHandler.setCulling(boolean)"""
        super(__RayHandler, self).setCulling(__boolean.valueOf(arg0))

    @overload
    def setCombinedMatrix(self, arg0: 'Matrix4'):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__RayHandler, self).setCombinedMatrix(arg0)

    @overload
    def setCombinedMatrix(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__RayHandler, self).setCombinedMatrix(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def useCustomViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void box2dLight.RayHandler.useCustomViewport(int,int,int,int)"""
        super(__RayHandler, self).useCustomViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAmbientLight(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.RayHandler.setAmbientLight(float,float,float,float)"""
        super(__RayHandler, self).setAmbientLight(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setAmbientLight(self, arg0: 'Color'):
        """public void box2dLight.RayHandler.setAmbientLight(com.badlogic.gdx.graphics.Color)"""
        super(__RayHandler, self).setAmbientLight(arg0)

    @staticmethod
    @overload
    def setGammaCorrection(arg0: bool):
        """public static void box2dLight.RayHandler.setGammaCorrection(boolean)"""
        __RayHandler.setGammaCorrection(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def render(self):
        """public void box2dLight.RayHandler.render()"""
        super(RayHandler, self).render()

    @staticmethod
    @overload
    def getGammaCorrection() -> bool:
        """public static boolean box2dLight.RayHandler.getGammaCorrection()"""
        return bool.__wrap(__RayHandler.getGammaCorrection())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.RayHandler.dispose()"""
        super(RayHandler, self).dispose()

    @staticmethod
    @overload
    def useDiffuseLight(arg0: bool):
        """public static void box2dLight.RayHandler.useDiffuseLight(boolean)"""
        __RayHandler.useDiffuseLight(__boolean.valueOf(arg0))

    @overload
    def setAmbientLight(self, arg0: float):
        """public void box2dLight.RayHandler.setAmbientLight(float)"""
        super(__RayHandler, self).setAmbientLight(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLightShader(self, arg0: 'ShaderProgram'):
        """public void box2dLight.RayHandler.setLightShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__RayHandler, self).setLightShader(arg0)

    @overload
    def setBlurNum(self, arg0: int):
        """public void box2dLight.RayHandler.setBlurNum(int)"""
        super(__RayHandler, self).setBlurNum(__int.valueOf(arg0))

    @overload
    def pointAtShadow(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.RayHandler.pointAtShadow(float,float)"""
        return bool.__wrap(super(__RayHandler, self).pointAtShadow(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def resizeFBO(self, arg0: int, arg1: int):
        """public void box2dLight.RayHandler.resizeFBO(int,int)"""
        super(__RayHandler, self).resizeFBO(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeAll(self):
        """public void box2dLight.RayHandler.removeAll()"""
        super(RayHandler, self).removeAll()

    @overload
    def setWorld(self, arg0: 'World'):
        """public void box2dLight.RayHandler.setWorld(com.badlogic.gdx.physics.box2d.World)"""
        super(__RayHandler, self).setWorld(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setLightMapRendering(self, arg0: bool):
        """public void box2dLight.RayHandler.setLightMapRendering(boolean)"""
        super(__RayHandler, self).setLightMapRendering(__boolean.valueOf(arg0))

    @overload
    def renderOnly(self):
        """public void box2dLight.RayHandler.renderOnly()"""
        super(RayHandler, self).renderOnly()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'World'):
        """public box2dLight.RayHandler(com.badlogic.gdx.physics.box2d.World)"""
        val = __RayHandler(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def update(self):
        """public void box2dLight.RayHandler.update()"""
        super(RayHandler, self).update()

    @overload
    def setCombinedMatrix(self, arg0: 'OrthographicCamera'):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__RayHandler, self).setCombinedMatrix(arg0)

    @overload
    def setShadows(self, arg0: bool):
        """public void box2dLight.RayHandler.setShadows(boolean)"""
        super(__RayHandler, self).setShadows(__boolean.valueOf(arg0))

    @overload
    def updateAndRender(self):
        """public void box2dLight.RayHandler.updateAndRender()"""
        super(RayHandler, self).updateAndRender()

    @overload
    def getLightMapBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer box2dLight.RayHandler.getLightMapBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RayHandler, self).getLightMapBuffer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'World', arg1: int, arg2: int):
        """public box2dLight.RayHandler(com.badlogic.gdx.physics.box2d.World,int,int)"""
        val = __RayHandler(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setBlur(self, arg0: bool):
        """public void box2dLight.RayHandler.setBlur(boolean)"""
        super(__RayHandler, self).setBlur(__boolean.valueOf(arg0))

    @overload
    def getLightMapTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture box2dLight.RayHandler.getLightMapTexture()"""
        return 'graphics.Texture'.__wrap(super(RayHandler, self).getLightMapTexture())

 
 
 
# CLASS: box2dLight.RayHandler 
 
 
# CLASS: box2dLight.ConeLight
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
from builtins import type
import box2dLight.RayHandler as RayHandler
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
import java.lang.Short as __short
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import box2dLight.PositionalLight as __PositionalLight
__PositionalLight = __PositionalLight
import box2dLight.Light as __Light
__Light = __Light
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import box2dLight.ConeLight as __ConeLight
__ConeLight = __ConeLight
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ConeLight(__PositionalLight, PositionalLight):
    """box2dLight.ConeLight"""
 
    @staticmethod
    def __wrap(java_value: __ConeLight) -> 'ConeLight':
        return ConeLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConeLight):
        """
        Dynamic initializer for ConeLight.
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
    def getX(self) -> float:
        """public float box2dLight.PositionalLight.getX()"""
        return float.__wrap(super(PositionalLight, self).getX())

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float)"""
        super(__PositionalLight, self).attachToBody(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(__Light, self).setIgnoreAttachedBody(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        __Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.PositionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__PositionalLight, self).setPosition(arg0)

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(__Light, self).setXray(__boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool.__wrap(super(Light, self).isSoft())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(__Light, self).setStaticLight(__boolean.valueOf(arg0))

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(__Light, self).setSoftnessLength(__float.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        __Light.setGlobalContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float.__wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(__Light, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(__Light, self).setActive(__boolean.valueOf(arg0))

    @overload
    def update(self):
        """public void box2dLight.ConeLight.update()"""
        super(ConeLight, self).update()

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.ConeLight.setDirection(float)"""
        super(__ConeLight, self).setDirection(__float.valueOf(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.PositionalLight.getY()"""
        return float.__wrap(super(PositionalLight, self).getY())

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(__Light, self).setSoft(__boolean.valueOf(arg0))

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float.__wrap(super(Light, self).getDistance())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int.__wrap(super(Light, self).getRayNum())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float, arg3: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float,float)"""
        super(__PositionalLight, self).attachToBody(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(__Light, self).remove(__boolean.valueOf(arg0))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool.__wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def getConeDegree(self) -> float:
        """public float box2dLight.ConeLight.getConeDegree()"""
        return float.__wrap(super(ConeLight, self).getConeDegree())

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.PositionalLight.contains(float,float)"""
        return bool.__wrap(super(__PositionalLight, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.PositionalLight.getPosition()"""
        return 'math.Vector2'.__wrap(super(PositionalLight, self).getPosition())

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(__Light, self).setContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.PositionalLight.setPosition(float,float)"""
        super(__PositionalLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float.__wrap(super(Light, self).getDirection())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool.__wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(__Light, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool.__wrap(super(Light, self).isXray())

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__PositionalLight, self).attachToBody(arg0)

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.PositionalLight.getBody()"""
        return 'box2d.Body'.__wrap(super(PositionalLight, self).getBody())

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
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Light, self).setContactFilter(arg0)

    @overload
    def setConeDegree(self, arg0: float):
        """public void box2dLight.ConeLight.setConeDegree(float)"""
        super(__ConeLight, self).setConeDegree(__float.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Light, self).setColor(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public box2dLight.ConeLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float,float,float,float)"""
        val = __ConeLight(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'.__wrap(super(Light, self).getColor())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool.__wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.ConeLight.setDistance(float)"""
        super(__ConeLight, self).setDistance(__float.valueOf(arg0)) 
 
 
# CLASS: box2dLight.DirectionalLight
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import box2dLight.RayHandler as RayHandler
import box2dLight.DirectionalLight as __DirectionalLight
__DirectionalLight = __DirectionalLight
import box2dLight.Light as __Light
__Light = __Light
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class DirectionalLight(__Light, Light):
    """box2dLight.DirectionalLight"""
 
    @staticmethod
    def __wrap(java_value: __DirectionalLight) -> 'DirectionalLight':
        return DirectionalLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectionalLight):
        """
        Dynamic initializer for DirectionalLight.
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
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.DirectionalLight.setDistance(float)"""
        super(__DirectionalLight, self).setDistance(__float.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        __Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.DirectionalLight.setPosition(float,float)"""
        super(__DirectionalLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.DirectionalLight.getBody()"""
        return 'box2d.Body'.__wrap(super(DirectionalLight, self).getBody())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.DirectionalLight.setIgnoreAttachedBody(boolean)"""
        super(__DirectionalLight, self).setIgnoreAttachedBody(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float):
        """public box2dLight.DirectionalLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float)"""
        val = __DirectionalLight(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(__Light, self).setXray(__boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool.__wrap(super(Light, self).isSoft())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(__Light, self).setContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(__Light, self).setStaticLight(__boolean.valueOf(arg0))

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(__Light, self).setSoftnessLength(__float.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        __Light.setGlobalContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float.__wrap(super(Light, self).getDirection())

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float.__wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.DirectionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__DirectionalLight, self).attachToBody(arg0)

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool.__wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(__Light, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(__Light, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(__Light, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool.__wrap(super(Light, self).isXray())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.DirectionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__DirectionalLight, self).setPosition(arg0)

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.DirectionalLight.contains(float,float)"""
        return bool.__wrap(super(__DirectionalLight, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.DirectionalLight.getX()"""
        return float.__wrap(super(DirectionalLight, self).getX())

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'.__wrap(super(Light, self).getPosition())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.DirectionalLight.setDirection(float)"""
        super(__DirectionalLight, self).setDirection(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.DirectionalLight.getY()"""
        return float.__wrap(super(DirectionalLight, self).getY())

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Light, self).setContactFilter(arg0)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Light, self).setColor(arg0)

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(__Light, self).setSoft(__boolean.valueOf(arg0))

    @overload
    def setIgnoreBody(self, arg0: 'Body'):
        """public void box2dLight.DirectionalLight.setIgnoreBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__DirectionalLight, self).setIgnoreBody(arg0)

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float.__wrap(super(Light, self).getDistance())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int.__wrap(super(Light, self).getRayNum())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'.__wrap(super(Light, self).getColor())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool.__wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.DirectionalLight.getIgnoreAttachedBody()"""
        return bool.__wrap(super(DirectionalLight, self).getIgnoreAttachedBody())

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(__Light, self).remove(__boolean.valueOf(arg0)) 
 
 
# CLASS: box2dLight.PointLight
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import box2dLight.PointLight as __PointLight
__PointLight = __PointLight
import java.lang.Boolean as __boolean
from builtins import type
import box2dLight.RayHandler as RayHandler
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
import java.lang.Short as __short
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import box2dLight.PositionalLight as __PositionalLight
__PositionalLight = __PositionalLight
import box2dLight.Light as __Light
__Light = __Light
import java.lang.Long as __long
import java.lang.Float as __float
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
 
class PointLight(__PositionalLight, PositionalLight):
    """box2dLight.PointLight"""
 
    @staticmethod
    def __wrap(java_value: __PointLight) -> 'PointLight':
        return PointLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointLight):
        """
        Dynamic initializer for PointLight.
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
    def __init__(self, arg0: 'RayHandler', arg1: int):
        """public box2dLight.PointLight(box2dLight.RayHandler,int)"""
        val = __PointLight(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.PositionalLight.getX()"""
        return float.__wrap(super(PositionalLight, self).getX())

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float)"""
        super(__PositionalLight, self).attachToBody(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(__Light, self).setIgnoreAttachedBody(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        __Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.PositionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__PositionalLight, self).setPosition(arg0)

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(__Light, self).setXray(__boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool.__wrap(super(Light, self).isSoft())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(__Light, self).setStaticLight(__boolean.valueOf(arg0))

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(__Light, self).setSoftnessLength(__float.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        __Light.setGlobalContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float.__wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.PointLight.setDirection(float)"""
        super(__PointLight, self).setDirection(__float.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(__Light, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(__Light, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.PointLight.setDistance(float)"""
        super(__PointLight, self).setDistance(__float.valueOf(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.PositionalLight.getY()"""
        return float.__wrap(super(PositionalLight, self).getY())

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(__Light, self).setSoft(__boolean.valueOf(arg0))

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float.__wrap(super(Light, self).getDistance())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int.__wrap(super(Light, self).getRayNum())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float, arg3: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float,float)"""
        super(__PositionalLight, self).attachToBody(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(__Light, self).remove(__boolean.valueOf(arg0))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool.__wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.PositionalLight.contains(float,float)"""
        return bool.__wrap(super(__PositionalLight, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.PositionalLight.getPosition()"""
        return 'math.Vector2'.__wrap(super(PositionalLight, self).getPosition())

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(__Light, self).setContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.PositionalLight.setPosition(float,float)"""
        super(__PositionalLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float.__wrap(super(Light, self).getDirection())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool.__wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(__Light, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool.__wrap(super(Light, self).isXray())

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__PositionalLight, self).attachToBody(arg0)

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.PositionalLight.getBody()"""
        return 'box2d.Body'.__wrap(super(PositionalLight, self).getBody())

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
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Light, self).setContactFilter(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float, arg5: float):
        """public box2dLight.PointLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float,float)"""
        val = __PointLight(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Light, self).setColor(arg0)

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'.__wrap(super(Light, self).getColor())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool.__wrap(super(Light, self).isStaticLight())

    @overload
    def update(self):
        """public void box2dLight.PointLight.update()"""
        super(PointLight, self).update() 
 
 
# CLASS: box2dLight.PositionalLight
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
from builtins import type
from abc import abstractmethod, ABC
import box2dLight.RayHandler as RayHandler
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
import java.lang.Short as __short
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import box2dLight.PositionalLight as __PositionalLight
__PositionalLight = __PositionalLight
import box2dLight.Light as __Light
__Light = __Light
import java.lang.Long as __long
import java.lang.Float as __float
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
 
class PositionalLight(ABC, __Light, Light):
    """box2dLight.PositionalLight"""
 
    @staticmethod
    def __wrap(java_value: __PositionalLight) -> 'PositionalLight':
        return PositionalLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PositionalLight):
        """
        Dynamic initializer for PositionalLight.
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
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.PositionalLight.getX()"""
        return float.__wrap(super(PositionalLight, self).getX())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(__Light, self).setIgnoreAttachedBody(__boolean.valueOf(arg0))

    @abstractmethod
    def setDistance(self, arg0: float):
        """public abstract void box2dLight.Light.setDistance(float)"""
        pass

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        __Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.PositionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__PositionalLight, self).setPosition(arg0)

    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float)"""
        super(__PositionalLight, self).attachToBody(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(__Light, self).setXray(__boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool.__wrap(super(Light, self).isSoft())

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float, arg5: float, arg6: float):
        """public box2dLight.PositionalLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float,float,float)"""
        val = __PositionalLight(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.PositionalLight.contains(float,float)"""
        return bool.__wrap(super(__PositionalLight, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.PositionalLight.getPosition()"""
        return 'math.Vector2'.__wrap(super(PositionalLight, self).getPosition())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(__Light, self).setContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(__Light, self).setStaticLight(__boolean.valueOf(arg0))

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(__Light, self).setSoftnessLength(__float.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        __Light.setGlobalContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.PositionalLight.setPosition(float,float)"""
        super(__PositionalLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float, arg3: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float,float)"""
        super(__PositionalLight, self).attachToBody(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float.__wrap(super(Light, self).getDirection())

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float.__wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool.__wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(__Light, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(__Light, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(__Light, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool.__wrap(super(Light, self).isXray())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__PositionalLight, self).attachToBody(arg0)

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.PositionalLight.getBody()"""
        return 'box2d.Body'.__wrap(super(PositionalLight, self).getBody())

    @abstractmethod
    def setDirection(self, arg0: float):
        """public abstract void box2dLight.Light.setDirection(float)"""
        pass

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
    def getY(self) -> float:
        """public float box2dLight.PositionalLight.getY()"""
        return float.__wrap(super(PositionalLight, self).getY())

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Light, self).setContactFilter(arg0)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Light, self).setColor(arg0)

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(__Light, self).setSoft(__boolean.valueOf(arg0))

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float.__wrap(super(Light, self).getDistance())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int.__wrap(super(Light, self).getRayNum())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'.__wrap(super(Light, self).getColor())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool.__wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(__Light, self).remove(__boolean.valueOf(arg0))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool.__wrap(super(Light, self).getIgnoreAttachedBody()) 
 
 
# CLASS: box2dLight.ChainLight
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
from builtins import type
import box2dLight.RayHandler as RayHandler
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
import java.lang.Short as __short
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import box2dLight.Light as __Light
__Light = __Light
import java.lang.Long as __long
import java.lang.Float as __float
import box2dLight.ChainLight as __ChainLight
__ChainLight = __ChainLight
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ChainLight(__Light, Light):
    """box2dLight.ChainLight"""
 
    @staticmethod
    def __wrap(java_value: __ChainLight) -> 'ChainLight':
        return ChainLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChainLight):
        """
        Dynamic initializer for ChainLight.
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
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.ChainLight.getBody()"""
        return 'box2d.Body'.__wrap(super(ChainLight, self).getBody())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(__Light, self).setIgnoreAttachedBody(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        __Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.ChainLight.getX()"""
        return float.__wrap(super(ChainLight, self).getX())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.ChainLight.setPosition(float,float)"""
        super(__ChainLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(__Light, self).setXray(__boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool.__wrap(super(Light, self).isSoft())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(__Light, self).setStaticLight(__boolean.valueOf(arg0))

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(__Light, self).setSoftnessLength(__float.valueOf(arg0))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        __Light.setGlobalContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float.__wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(__Light, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def update(self):
        """public void box2dLight.ChainLight.update()"""
        super(ChainLight, self).update()

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(__Light, self).setActive(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: int):
        """public box2dLight.ChainLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,int)"""
        val = __ChainLight(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: int, arg5: 'float'):
        """public box2dLight.ChainLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,int,float[])"""
        val = __ChainLight(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3), __int.valueOf(arg4), arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.ChainLight.setDistance(float)"""
        super(__ChainLight, self).setDistance(__float.valueOf(arg0))

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(__Light, self).setSoft(__boolean.valueOf(arg0))

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float.__wrap(super(Light, self).getDistance())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int.__wrap(super(Light, self).getRayNum())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def attachToBody(self, arg0: 'Body', arg1: float):
        """public void box2dLight.ChainLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float)"""
        super(__ChainLight, self).attachToBody(arg0, __float.valueOf(arg1))

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(__Light, self).remove(__boolean.valueOf(arg0))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool.__wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def debugRender(self, arg0: 'ShapeRenderer'):
        """public void box2dLight.ChainLight.debugRender(com.badlogic.gdx.graphics.glutils.ShapeRenderer)"""
        super(__ChainLight, self).debugRender(arg0)

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def updateChain(self):
        """public void box2dLight.ChainLight.updateChain()"""
        super(ChainLight, self).updateChain()

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.ChainLight.contains(float,float)"""
        return bool.__wrap(super(__ChainLight, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.ChainLight.setDirection(float)"""
        super(__ChainLight, self).setDirection(__float.valueOf(arg0))

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(__Light, self).setContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float.__wrap(super(Light, self).getDirection())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool.__wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(__Light, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.ChainLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__ChainLight, self).attachToBody(arg0)

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool.__wrap(super(Light, self).isXray())

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'.__wrap(super(Light, self).getPosition())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def render(self):
        """public void box2dLight.ChainLight.render()"""
        super(ChainLight, self).render()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Light, self).setContactFilter(arg0)

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.ChainLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__ChainLight, self).setPosition(arg0)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Light, self).setColor(arg0)

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'.__wrap(super(Light, self).getColor())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool.__wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.ChainLight.getY()"""
        return float.__wrap(super(ChainLight, self).getY()) 
 
 
# CLASS: box2dLight.Light
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import box2dLight.RayHandler as RayHandler
import box2dLight.Light as __Light
__Light = __Light
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Light(ABC, pygdx.__Disposable, utils.Disposable):
    """box2dLight.Light"""
 
    @staticmethod
    def __wrap(java_value: __Light) -> 'Light':
        return Light(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Light):
        """
        Dynamic initializer for Light.
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
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(__Light, self).remove(__boolean.valueOf(arg0))

    @abstractmethod
    def getY(self, ):
        """public abstract float box2dLight.Light.getY()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool.__wrap(super(Light, self).isXray())

    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool.__wrap(super(Light, self).getIgnoreAttachedBody())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'.__wrap(super(Light, self).getColor())

    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float.__wrap(super(Light, self).getSoftShadowLength())

    @abstractmethod
    def setDistance(self, arg0: float):
        """public abstract void box2dLight.Light.setDistance(float)"""
        pass

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        __Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool.__wrap(super(Light, self).isStaticLight())

    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(__Light, self).setIgnoreAttachedBody(__boolean.valueOf(arg0))

    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool.__wrap(super(Light, self).isActive())

    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float.__wrap(super(Light, self).getDirection())

    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int.__wrap(super(Light, self).getRayNum())

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'.__wrap(super(Light, self).getPosition())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        __Light.setGlobalContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(__Light, self).setActive(__boolean.valueOf(arg0))

    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float.__wrap(super(Light, self).getDistance())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def getBody(self, ):
        """public abstract com.badlogic.gdx.physics.box2d.Body box2dLight.Light.getBody()"""
        pass

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @abstractmethod
    def setPosition(self, arg0: float, arg1: float):
        """public abstract void box2dLight.Light.setPosition(float,float)"""
        pass

    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(__Light, self).setSoftnessLength(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @abstractmethod
    def setPosition(self, arg0: 'Vector2'):
        """public abstract void box2dLight.Light.setPosition(com.badlogic.gdx.math.Vector2)"""
        pass

    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Light, self).setContactFilter(arg0)

    @abstractmethod
    def setDirection(self, arg0: float):
        """public abstract void box2dLight.Light.setDirection(float)"""
        pass

    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(__Light, self).setStaticLight(__boolean.valueOf(arg0))

    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(__Light, self).setXray(__boolean.valueOf(arg0))

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
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float):
        """public box2dLight.Light(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float)"""
        val = __Light(arg0, __int.valueOf(arg1), arg2, __float.valueOf(arg3), __float.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(__Light, self).setContactFilter(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @abstractmethod
    def attachToBody(self, arg0: 'Body'):
        """public abstract void box2dLight.Light.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        pass

    @abstractmethod
    def getX(self, ):
        """public abstract float box2dLight.Light.getX()"""
        pass

    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool.__wrap(super(Light, self).isSoft())

    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(__Light, self).add(arg0)

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(__Light, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Light, self).setColor(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(__Light, self).setSoft(__boolean.valueOf(arg0))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.Light.contains(float,float)"""
        return bool.__wrap(super(__Light, self).contains(__float.valueOf(arg0), __float.valueOf(arg1))) 
 
 
# CLASS: box2dLight.Spinor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import box2dLight.Spinor as Spinor
from builtins import float
import box2dLight.Spinor as __Spinor
__Spinor = __Spinor
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
from builtins import int
 
class Spinor():
    """box2dLight.Spinor"""
 
    @staticmethod
    def __wrap(java_value: __Spinor) -> 'Spinor':
        return Spinor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Spinor):
        """
        Dynamic initializer for Spinor.
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
    def set(self, arg0: float, arg1: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.set(float,float)"""
        return 'Spinor'.__wrap(super(__Spinor, self).set(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def lerp(self, arg0: 'Spinor', arg1: float, arg2: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.lerp(box2dLight.Spinor,float,box2dLight.Spinor)"""
        return 'Spinor'.__wrap(super(__Spinor, self).lerp(arg0, __float.valueOf(arg1), arg2))

    @overload
    def add(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.add(float)"""
        return 'Spinor'.__wrap(super(__Spinor, self).add(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.add(box2dLight.Spinor)"""
        return 'Spinor'.__wrap(super(__Spinor, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Spinor'):
        """public box2dLight.Spinor(box2dLight.Spinor)"""
        val = __Spinor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def nor(self) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.nor()"""
        return 'Spinor'.__wrap(super(Spinor, self).nor())

    @overload
    def angle(self) -> float:
        """public float box2dLight.Spinor.angle()"""
        return float.__wrap(super(Spinor, self).angle())

    @overload
    def slerp(self, arg0: 'Spinor', arg1: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.slerp(box2dLight.Spinor,float)"""
        return 'Spinor'.__wrap(super(__Spinor, self).slerp(arg0, __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String box2dLight.Spinor.toString()"""
        return str.__wrap(super(Spinor, self).toString())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public box2dLight.Spinor(float,float)"""
        val = __Spinor(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.set(float)"""
        return 'Spinor'.__wrap(super(__Spinor, self).set(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.set(box2dLight.Spinor)"""
        return 'Spinor'.__wrap(super(__Spinor, self).set(arg0))

    @overload
    def __init__(self, arg0: float):
        """public box2dLight.Spinor(float)"""
        val = __Spinor(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def invert(self) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.invert()"""
        return 'Spinor'.__wrap(super(Spinor, self).invert())

    @overload
    def __init__(self, ):
        """public box2dLight.Spinor()"""
        val = __Spinor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def len(self) -> float:
        """public float box2dLight.Spinor.len()"""
        return float.__wrap(super(Spinor, self).len())

    @overload
    def sub(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.sub(box2dLight.Spinor)"""
        return 'Spinor'.__wrap(super(__Spinor, self).sub(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def len2(self) -> float:
        """public float box2dLight.Spinor.len2()"""
        return float.__wrap(super(Spinor, self).len2())

    @overload
    def sub(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.sub(float)"""
        return 'Spinor'.__wrap(super(__Spinor, self).sub(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def scale(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.scale(float)"""
        return 'Spinor'.__wrap(super(__Spinor, self).scale(__float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public box2dLight.Spinor()"""
        val = __Spinor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mul(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.mul(box2dLight.Spinor)"""
        return 'Spinor'.__wrap(super(__Spinor, self).mul(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: box2dLight.BlendFunc
from builtins import str
import box2dLight.BlendFunc as __BlendFunc
__BlendFunc = __BlendFunc
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
 
class BlendFunc():
    """box2dLight.BlendFunc"""
 
    @staticmethod
    def __wrap(java_value: __BlendFunc) -> 'BlendFunc':
        return BlendFunc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlendFunc):
        """
        Dynamic initializer for BlendFunc.
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
    def apply(self):
        """public void box2dLight.BlendFunc.apply()"""
        super(BlendFunc, self).apply()

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
    def set(self, arg0: int, arg1: int):
        """public void box2dLight.BlendFunc.set(int,int)"""
        super(__BlendFunc, self).set(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def reset(self):
        """public void box2dLight.BlendFunc.reset()"""
        super(BlendFunc, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public box2dLight.BlendFunc(int,int)"""
        val = __BlendFunc(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))