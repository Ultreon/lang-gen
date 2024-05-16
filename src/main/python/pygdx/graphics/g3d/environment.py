from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight as __DirectionalShadowLight
__DirectionalShadowLight = __DirectionalShadowLight
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.environment.DirectionalLight as __DirectionalLight
__DirectionalLight = __DirectionalLight
import com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor as __TextureDescriptor
__TextureDescriptor = __TextureDescriptor
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
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
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as __BaseLight
__BaseLight = __BaseLight
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class DirectionalShadowLight(__DirectionalLight, DirectionalLight, __ShadowMap, ShadowMap, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight"""
 
    @staticmethod
    def __wrap(java_value: __DirectionalShadowLight) -> 'DirectionalShadowLight':
        return DirectionalShadowLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectionalShadowLight):
        """
        Dynamic initializer for DirectionalShadowLight.
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
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(DirectionalShadowLight, self).getFrameBuffer())

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin()"""
        super(DirectionalShadowLight, self).begin()

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getCamera()"""
        return 'graphics.Camera'.__wrap(super(DirectionalShadowLight, self).getCamera())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.end()"""
        super(DirectionalShadowLight, self).end()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def update(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.update(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__DirectionalShadowLight, self).update(arg0, arg1)

    @overload
    def begin(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__DirectionalShadowLight, self).begin(arg0, arg1)

    @overload
    def equals(self, arg0: 'DirectionalLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return bool.__wrap(super(__DirectionalLight, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'DirectionalLight') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0))

    @override
    @overload
    def getDepthMap(self) -> 'utils.TextureDescriptor':
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getDepthMap()"""
        return 'utils.TextureDescriptor'.__wrap(super(DirectionalShadowLight, self).getDepthMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(arg0))

    @overload
    def setDirection(self, arg0: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).setDirection(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight(int,int,float,float,float,float)"""
        val = __DirectionalShadowLight(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).setDirection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0, arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.dispose()"""
        super(DirectionalShadowLight, self).dispose()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

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
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin(com.badlogic.gdx.graphics.Camera)"""
        super(__DirectionalShadowLight, self).begin(arg0)

    @override
    @overload
    def getProjViewTrans(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getProjViewTrans()"""
        return 'math.Matrix4'.__wrap(super(DirectionalShadowLight, self).getProjViewTrans())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(java.lang.Object)"""
        return bool.__wrap(super(__DirectionalLight, self).equals(arg0))

    @overload
    def update(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.update(com.badlogic.gdx.graphics.Camera)"""
        super(__DirectionalShadowLight, self).update(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight as __DirectionalShadowLight
__DirectionalShadowLight = __DirectionalShadowLight
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.environment.DirectionalLight as __DirectionalLight
__DirectionalLight = __DirectionalLight
import com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor as __TextureDescriptor
__TextureDescriptor = __TextureDescriptor
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
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
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as __BaseLight
__BaseLight = __BaseLight
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class DirectionalShadowLight(__DirectionalLight, DirectionalLight, __ShadowMap, ShadowMap, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight"""
 
    @staticmethod
    def __wrap(java_value: __DirectionalShadowLight) -> 'DirectionalShadowLight':
        return DirectionalShadowLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectionalShadowLight):
        """
        Dynamic initializer for DirectionalShadowLight.
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
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(DirectionalShadowLight, self).getFrameBuffer())

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin()"""
        super(DirectionalShadowLight, self).begin()

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getCamera()"""
        return 'graphics.Camera'.__wrap(super(DirectionalShadowLight, self).getCamera())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.end()"""
        super(DirectionalShadowLight, self).end()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def update(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.update(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__DirectionalShadowLight, self).update(arg0, arg1)

    @overload
    def begin(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__DirectionalShadowLight, self).begin(arg0, arg1)

    @overload
    def equals(self, arg0: 'DirectionalLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return bool.__wrap(super(__DirectionalLight, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'DirectionalLight') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0))

    @override
    @overload
    def getDepthMap(self) -> 'utils.TextureDescriptor':
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getDepthMap()"""
        return 'utils.TextureDescriptor'.__wrap(super(DirectionalShadowLight, self).getDepthMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(arg0))

    @overload
    def setDirection(self, arg0: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).setDirection(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight(int,int,float,float,float,float)"""
        val = __DirectionalShadowLight(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).setDirection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0, arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.dispose()"""
        super(DirectionalShadowLight, self).dispose()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

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
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin(com.badlogic.gdx.graphics.Camera)"""
        super(__DirectionalShadowLight, self).begin(arg0)

    @override
    @overload
    def getProjViewTrans(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getProjViewTrans()"""
        return 'math.Matrix4'.__wrap(super(DirectionalShadowLight, self).getProjViewTrans())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(java.lang.Object)"""
        return bool.__wrap(super(__DirectionalLight, self).equals(arg0))

    @overload
    def update(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.update(com.badlogic.gdx.graphics.Camera)"""
        super(__DirectionalShadowLight, self).update(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap as __AmbientCubemap
__AmbientCubemap = __AmbientCubemap
from builtins import float
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class AmbientCubemap():
    """com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap"""
 
    @staticmethod
    def __wrap(java_value: __AmbientCubemap) -> 'AmbientCubemap':
        return AmbientCubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AmbientCubemap):
        """
        Dynamic initializer for AmbientCubemap.
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
    def add(self, arg0: float, arg1: float, arg2: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(float,float,float)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(float,float,float,float,float,float)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(float,float,float)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'AmbientCubemap') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).set(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap()"""
        val = __AmbientCubemap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Color', arg1: 'Vector3', arg2: 'Vector3') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def clamp(self) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.clamp()"""
        return 'AmbientCubemap'.__wrap(super(AmbientCubemap, self).clamp())

    @overload
    def add(self, arg0: 'Color') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap()"""
        val = __AmbientCubemap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def clear(self) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.clear()"""
        return 'AmbientCubemap'.__wrap(super(AmbientCubemap, self).clear())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.toString()"""
        return str.__wrap(super(AmbientCubemap, self).toString())

    @overload
    def add(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def add(self, arg0: 'Color', arg1: 'Vector3', arg2: 'Vector3', arg3: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(arg0, arg1, arg2, __float.valueOf(arg3)))

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
    def set(self, arg0: 'Color') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(com.badlogic.gdx.graphics.Color)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).set(arg0))

    @overload
    def add(self, arg0: 'Color', arg1: 'Vector3') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).add(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColor(self, arg0: 'Color', arg1: int) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.getColor(com.badlogic.gdx.graphics.Color,int)"""
        return 'graphics.Color'.__wrap(super(__AmbientCubemap, self).getColor(arg0, __int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'float') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(float[])"""
        return 'AmbientCubemap'.__wrap(super(__AmbientCubemap, self).set(arg0))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap(float[])"""
        val = __AmbientCubemap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'AmbientCubemap'):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap(com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap)"""
        val = __AmbientCubemap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.SpotLight
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.environment.SpotLight as __SpotLight
__SpotLight = __SpotLight
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as __BaseLight
__BaseLight = __BaseLight
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
 
class SpotLight(__BaseLight, BaseLight):
    """com.badlogic.gdx.graphics.g3d.environment.SpotLight"""
 
    @staticmethod
    def __wrap(java_value: __SpotLight) -> 'SpotLight':
        return SpotLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpotLight):
        """
        Dynamic initializer for SpotLight.
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
    def setDirection(self, arg0: 'Vector3') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setDirection(arg0))

    @overload
    def setTarget(self, arg0: 'Vector3') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setTarget(com.badlogic.gdx.math.Vector3)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setTarget(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setDirection(float,float,float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setDirection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.SpotLight.equals(java.lang.Object)"""
        return bool.__wrap(super(__SpotLight, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setPosition(float,float,float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float, arg7: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(float,float,float,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float,float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3, arg4, __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

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
    def setCutoffAngle(self, arg0: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setCutoffAngle(float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setCutoffAngle(__float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(float,float,float,float,float,float,float,float,float,float,float,float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11)))

    @overload
    def setPosition(self, arg0: 'Vector3') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setPosition(com.badlogic.gdx.math.Vector3)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setPosition(arg0))

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(com.badlogic.gdx.graphics.Color,float,float,float,float,float,float,float,float,float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).set(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setExponent(self, arg0: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setExponent(float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setExponent(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'SpotLight') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: 'SpotLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.SpotLight.equals(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return bool.__wrap(super(__SpotLight, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight()"""
        val = __SpotLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3', arg2: 'Vector3', arg3: float, arg4: float, arg5: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float,float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).set(arg0, arg1, arg2, __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def setIntensity(self, arg0: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setIntensity(float)"""
        return 'SpotLight'.__wrap(super(__SpotLight, self).setIntensity(__float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight()"""
        val = __SpotLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.ShadowMap
import com.badlogic.gdx.graphics.g3d.environment.ShadowMap as __ShadowMap
__ShadowMap = __ShadowMap
from abc import abstractmethod, ABC
 
class ShadowMap(ABC):
    """com.badlogic.gdx.graphics.g3d.environment.ShadowMap"""
 
    @staticmethod
    def __wrap(java_value: __ShadowMap) -> 'ShadowMap':
        return ShadowMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShadowMap):
        """
        Dynamic initializer for ShadowMap.
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
    def getProjViewTrans(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.environment.ShadowMap.getProjViewTrans()"""
        pass

    @abstractmethod
    def getDepthMap(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor com.badlogic.gdx.graphics.g3d.environment.ShadowMap.getDepthMap()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.BaseLight
from pyquantum_helper import import_once as __import_once__
from builtins import str
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
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as __BaseLight
__BaseLight = __BaseLight
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class BaseLight(ABC):
    """com.badlogic.gdx.graphics.g3d.environment.BaseLight"""
 
    @staticmethod
    def __wrap(java_value: __BaseLight) -> 'BaseLight':
        return BaseLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseLight):
        """
        Dynamic initializer for BaseLight.
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
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.BaseLight()"""
        val = __BaseLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.BaseLight()"""
        val = __BaseLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.DirectionalLight
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.environment.DirectionalLight as __DirectionalLight
__DirectionalLight = __DirectionalLight
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as __BaseLight
__BaseLight = __BaseLight
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
 
class DirectionalLight(__BaseLight, BaseLight):
    """com.badlogic.gdx.graphics.g3d.environment.DirectionalLight"""
 
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).setDirection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,float,float,float)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

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
    def equals(self, arg0: 'DirectionalLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return bool.__wrap(super(__DirectionalLight, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight()"""
        val = __DirectionalLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(java.lang.Object)"""
        return bool.__wrap(super(__DirectionalLight, self).equals(arg0))

    @overload
    def set(self, arg0: 'DirectionalLight') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).set(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setDirection(self, arg0: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'.__wrap(super(__DirectionalLight, self).setDirection(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight()"""
        val = __DirectionalLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics as __SphericalHarmonics
__SphericalHarmonics = __SphericalHarmonics
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
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class SphericalHarmonics():
    """com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics"""
 
    @staticmethod
    def __wrap(java_value: __SphericalHarmonics) -> 'SphericalHarmonics':
        return SphericalHarmonics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SphericalHarmonics):
        """
        Dynamic initializer for SphericalHarmonics.
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
    def set(self, arg0: 'Color') -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(com.badlogic.gdx.graphics.Color)"""
        return 'SphericalHarmonics'.__wrap(super(__SphericalHarmonics, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics()"""
        val = __SphericalHarmonics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics(float[])"""
        val = __SphericalHarmonics(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics()"""
        val = __SphericalHarmonics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(float,float,float)"""
        return 'SphericalHarmonics'.__wrap(super(__SphericalHarmonics, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'float') -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(float[])"""
        return 'SphericalHarmonics'.__wrap(super(__SphericalHarmonics, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: 'AmbientCubemap') -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap)"""
        return 'SphericalHarmonics'.__wrap(super(__SphericalHarmonics, self).set(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.PointLight
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.environment.PointLight as __PointLight
__PointLight = __PointLight
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as __BaseLight
__BaseLight = __BaseLight
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
 
class PointLight(__BaseLight, BaseLight):
    """com.badlogic.gdx.graphics.g3d.environment.PointLight"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight()"""
        val = __PointLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: 'PointLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.PointLight.equals(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return bool.__wrap(super(__PointLight, self).equals(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float, arg4: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(com.badlogic.gdx.graphics.Color,float,float,float,float)"""
        return 'PointLight'.__wrap(super(__PointLight, self).set(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.PointLight.equals(java.lang.Object)"""
        return bool.__wrap(super(__PointLight, self).equals(arg0))

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3', arg2: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,float)"""
        return 'PointLight'.__wrap(super(__PointLight, self).set(arg0, arg1, __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'PointLight') -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return 'PointLight'.__wrap(super(__PointLight, self).set(arg0))

    @overload
    def setIntensity(self, arg0: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.setIntensity(float)"""
        return 'PointLight'.__wrap(super(__PointLight, self).setIntensity(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3', arg4: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(float,float,float,com.badlogic.gdx.math.Vector3,float)"""
        return 'PointLight'.__wrap(super(__PointLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight()"""
        val = __PointLight()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(float,float,float,float,float,float,float)"""
        return 'PointLight'.__wrap(super(__PointLight, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6)))

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
    def setPosition(self, arg0: 'Vector3') -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.setPosition(com.badlogic.gdx.math.Vector3)"""
        return 'PointLight'.__wrap(super(__PointLight, self).setPosition(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.setPosition(float,float,float)"""
        return 'PointLight'.__wrap(super(__PointLight, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'.__wrap(super(__BaseLight, self).setColor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()