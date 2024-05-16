from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder as __FrustumShapeBuilder
__FrustumShapeBuilder = __FrustumShapeBuilder
import java.lang.Long as __long
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class FrustumShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __FrustumShapeBuilder) -> 'FrustumShapeBuilder':
        return FrustumShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrustumShapeBuilder):
        """
        Dynamic initializer for FrustumShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Camera', arg2: 'Color', arg3: 'Color', arg4: 'Color', arg5: 'Color', arg6: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        __FrustumShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Frustum', arg2: 'Color', arg3: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Frustum,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        __FrustumShapeBuilder.build(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Camera'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.Camera)"""
        __FrustumShapeBuilder.build(arg0, arg1)

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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder()"""
        val = __FrustumShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder()"""
        val = __FrustumShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder as __FrustumShapeBuilder
__FrustumShapeBuilder = __FrustumShapeBuilder
import java.lang.Long as __long
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class FrustumShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __FrustumShapeBuilder) -> 'FrustumShapeBuilder':
        return FrustumShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrustumShapeBuilder):
        """
        Dynamic initializer for FrustumShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Camera', arg2: 'Color', arg3: 'Color', arg4: 'Color', arg5: 'Color', arg6: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        __FrustumShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Frustum', arg2: 'Color', arg3: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Frustum,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        __FrustumShapeBuilder.build(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Camera'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.Camera)"""
        __FrustumShapeBuilder.build(arg0, arg1)

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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder()"""
        val = __FrustumShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder()"""
        val = __FrustumShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder as __ArrowShapeBuilder
__ArrowShapeBuilder = __ArrowShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ArrowShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ArrowShapeBuilder) -> 'ArrowShapeBuilder':
        return ArrowShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrowShapeBuilder):
        """
        Dynamic initializer for ArrowShapeBuilder.
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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder()"""
        val = __ArrowShapeBuilder()
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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder()"""
        val = __ArrowShapeBuilder()
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,float,float,float,float,int)"""
        __ArrowShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder as __RenderableShapeBuilder
__RenderableShapeBuilder = __RenderableShapeBuilder
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

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
 
class RenderableShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __RenderableShapeBuilder) -> 'RenderableShapeBuilder':
        return RenderableShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderableShapeBuilder):
        """
        Dynamic initializer for RenderableShapeBuilder.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder()"""
        val = __RenderableShapeBuilder()
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

    @staticmethod
    @overload
    def buildNormals(arg0: 'MeshPartBuilder', arg1: 'RenderableProvider', arg2: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder.buildNormals(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.RenderableProvider,float)"""
        __RenderableShapeBuilder.buildNormals(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def buildNormals(arg0: 'MeshPartBuilder', arg1: 'Renderable', arg2: float, arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder.buildNormals(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.Renderable,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        __RenderableShapeBuilder.buildNormals(arg0, arg1, __float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def buildNormals(arg0: 'MeshPartBuilder', arg1: 'RenderableProvider', arg2: float, arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder.buildNormals(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.RenderableProvider,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        __RenderableShapeBuilder.buildNormals(arg0, arg1, __float.valueOf(arg2), arg3, arg4, arg5)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder()"""
        val = __RenderableShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder as __SphereShapeBuilder
__SphereShapeBuilder = __SphereShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class SphereShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __SphereShapeBuilder) -> 'SphereShapeBuilder':
        return SphereShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SphereShapeBuilder):
        """
        Dynamic initializer for SphereShapeBuilder.
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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder()"""
        val = __SphereShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,int,float,float,float,float)"""
        __SphereShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Matrix4', arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: float, arg8: float, arg9: float, arg10: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Matrix4,float,float,float,int,int,float,float,float,float)"""
        __SphereShapeBuilder.build(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,int)"""
        __SphereShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Matrix4', arg2: float, arg3: float, arg4: float, arg5: int, arg6: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Matrix4,float,float,float,int,int)"""
        __SphereShapeBuilder.build(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder()"""
        val = __SphereShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder as __CylinderShapeBuilder
__CylinderShapeBuilder = __CylinderShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class CylinderShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __CylinderShapeBuilder) -> 'CylinderShapeBuilder':
        return CylinderShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CylinderShapeBuilder):
        """
        Dynamic initializer for CylinderShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: bool):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float,boolean)"""
        __CylinderShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __boolean.valueOf(arg7))

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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder()"""
        val = __CylinderShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float)"""
        __CylinderShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int)"""
        __CylinderShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder()"""
        val = __CylinderShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

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
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder as __BoxShapeBuilder
__BoxShapeBuilder = __BoxShapeBuilder
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class BoxShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __BoxShapeBuilder) -> 'BoxShapeBuilder':
        return BoxShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoxShapeBuilder):
        """
        Dynamic initializer for BoxShapeBuilder.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder()"""
        val = __BoxShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,float,float)"""
        __BoxShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: 'VertexInfo', arg6: 'VertexInfo', arg7: 'VertexInfo', arg8: 'VertexInfo'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        __BoxShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3', arg8: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        __BoxShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Matrix4'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Matrix4)"""
        __BoxShapeBuilder.build(arg0, arg1)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'BoundingBox'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.collision.BoundingBox)"""
        __BoxShapeBuilder.build(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder()"""
        val = __BoxShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float)"""
        __BoxShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder as __PatchShapeBuilder
__PatchShapeBuilder = __PatchShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class PatchShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __PatchShapeBuilder) -> 'PatchShapeBuilder':
        return PatchShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PatchShapeBuilder):
        """
        Dynamic initializer for PatchShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: int, arg17: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,int)"""
        __PatchShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15), __int.valueOf(arg16), __int.valueOf(arg17))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder()"""
        val = __PatchShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: int, arg7: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int)"""
        __PatchShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, __int.valueOf(arg6), __int.valueOf(arg7))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: int, arg6: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,int,int)"""
        __PatchShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, __int.valueOf(arg5), __int.valueOf(arg6))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder()"""
        val = __PatchShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder
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
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder as __BaseShapeBuilder
__BaseShapeBuilder = __BaseShapeBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BaseShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __BaseShapeBuilder) -> 'BaseShapeBuilder':
        return BaseShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseShapeBuilder):
        """
        Dynamic initializer for BaseShapeBuilder.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder()"""
        val = __BaseShapeBuilder()
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder()"""
        val = __BaseShapeBuilder()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder as __EllipseShapeBuilder
__EllipseShapeBuilder = __EllipseShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class EllipseShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __EllipseShapeBuilder) -> 'EllipseShapeBuilder':
        return EllipseShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EllipseShapeBuilder):
        """
        Dynamic initializer for EllipseShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __float.valueOf(arg5), __float.valueOf(arg6))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder()"""
        val = __EllipseShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3', arg6: float, arg7: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __float.valueOf(arg6), __float.valueOf(arg7))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float, arg18: float, arg19: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15), __float.valueOf(arg16), __float.valueOf(arg17), __float.valueOf(arg18), __float.valueOf(arg19))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'Vector3', arg7: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder()"""
        val = __EllipseShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: float, arg8: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, arg6, __float.valueOf(arg7), __float.valueOf(arg8))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, arg6)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15), __float.valueOf(arg16), __float.valueOf(arg17))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3', arg8: float, arg9: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7, __float.valueOf(arg8), __float.valueOf(arg9))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        __EllipseShapeBuilder.build(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __float.valueOf(arg11), __float.valueOf(arg12), __float.valueOf(arg13), __float.valueOf(arg14), __float.valueOf(arg15), __float.valueOf(arg16))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder as __CapsuleShapeBuilder
__CapsuleShapeBuilder = __CapsuleShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class CapsuleShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __CapsuleShapeBuilder) -> 'CapsuleShapeBuilder':
        return CapsuleShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CapsuleShapeBuilder):
        """
        Dynamic initializer for CapsuleShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int)"""
        __CapsuleShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder()"""
        val = __CapsuleShapeBuilder()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder()"""
        val = __CapsuleShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder as __ConeShapeBuilder
__ConeShapeBuilder = __ConeShapeBuilder
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ConeShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ConeShapeBuilder) -> 'ConeShapeBuilder':
        return ConeShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConeShapeBuilder):
        """
        Dynamic initializer for ConeShapeBuilder.
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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int)"""
        __ConeShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder()"""
        val = __ConeShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float)"""
        __ConeShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))

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
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder()"""
        val = __ConeShapeBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: bool):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float,boolean)"""
        __ConeShapeBuilder.build(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __boolean.valueOf(arg7))

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